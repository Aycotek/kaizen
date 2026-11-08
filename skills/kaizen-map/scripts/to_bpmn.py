"""Turn a simple process description (JSON) into a BPMN 2.0 file with diagram layout.

The output opens in bpmn.io, Camunda Modeler, Signavio and most BPMN tools.

    python to_bpmn.py process.json              -> process.bpmn
    python to_bpmn.py process.json out.bpmn

Input format (see example.json):
{
  "name": "Customer quote",
  "lanes": ["Sales", "Engineering", "Customer"],
  "steps": [
    {"id": "start", "type": "start", "name": "Request received", "lane": "Sales", "next": ["qualify"]},
    {"id": "qualify", "name": "Qualify request", "lane": "Sales", "next": ["ok"]},
    {"id": "ok", "type": "gateway", "name": "Complete?", "lane": "Sales",
     "next": [{"to": "price", "label": "yes"}, {"to": "ask", "label": "no"}]},
    {"id": "end", "type": "end", "name": "Quote sent", "lane": "Sales"}
  ]
}
type: start | end | task (default) | gateway. "next" lists ids, or {"to", "label"} for gateway branches.
Optional on any task: "waste": "short note" (exported as documentation).
Standard library only.
"""
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

TYPES = {"start": "startEvent", "end": "endEvent", "task": "task", "gateway": "exclusiveGateway"}
SIZE = {"start": (36, 36), "end": (36, 36), "task": (110, 70), "gateway": (50, 50)}
COL_W, LANE_H, LANE_HEADER, POOL_HEADER, MARGIN = 160, 130, 30, 30, 40


def load(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    steps = {s["id"]: dict(s, type=s.get("type", "task")) for s in data["steps"]}
    lanes = data.get("lanes") or sorted({s.get("lane", "Process") for s in steps.values()})
    errors = []
    for s in steps.values():
        if s["type"] not in TYPES:
            errors.append(f"step {s['id']}: unknown type {s['type']}")
        if s.get("lane", lanes[0]) not in lanes:
            errors.append(f"step {s['id']}: lane {s.get('lane')} is not in lanes")
        s["next"] = [n if isinstance(n, dict) else {"to": n} for n in s.get("next", [])]
        for n in s["next"]:
            if n["to"] not in steps:
                errors.append(f"step {s['id']}: next {n['to']} does not exist")
    if not any(s["type"] == "start" for s in steps.values()):
        errors.append("no start step")
    if errors:
        sys.exit("Invalid process:\n- " + "\n- ".join(errors))
    return data.get("name", "Process"), lanes, steps


def columns(steps):
    """Column = longest path from a start step, ignoring loops (back edges)."""
    col, order = {}, []
    starts = [i for i, s in steps.items() if s["type"] == "start"]
    for st in starts:
        col[st] = 0
    # Iterative DFS to find back edges, then longest path on the remaining DAG.
    state, back = {}, set()
    for st in starts:
        stack = [(st, iter(steps[st]["next"]))]
        state[st] = 1
        while stack:
            node, it = stack[-1]
            nxt = next(it, None)
            if nxt is None:
                state[node] = 2
                order.append(node)
                stack.pop()
                continue
            t = nxt["to"]
            if state.get(t) == 1:
                back.add((node, t))
            elif t not in state:
                state[t] = 1
                stack.append((t, iter(steps[t]["next"])))
    for node in reversed(order):  # topological order
        for n in steps[node]["next"]:
            if (node, n["to"]) not in back:
                col[n["to"]] = max(col.get(n["to"], 0), col.get(node, 0) + 1)
    for i in steps:  # unreachable steps go to the end
        col.setdefault(i, max(col.values(), default=0) + 1)
    return col


def layout(lanes, steps):
    col = columns(steps)
    lane_y = {l: MARGIN + i * LANE_H for i, l in enumerate(lanes)}
    # Two steps in the same lane and column: shift the later one down a little.
    used, pos = {}, {}
    for i, s in steps.items():
        lane = s.get("lane", lanes[0])
        key = (lane, col[i])
        k = used.get(key, 0)
        used[key] = k + 1
        w, h = SIZE[s["type"]]
        cx = MARGIN + POOL_HEADER + LANE_HEADER + 40 + col[i] * COL_W + 55
        cy = lane_y[lane] + LANE_H / 2 + k * 18
        pos[i] = (cx - w / 2, cy - h / 2, w, h)
    width = MARGIN + POOL_HEADER + LANE_HEADER + 80 + (max(col.values()) + 1) * COL_W
    return pos, lane_y, width


def waypoints(a, b, from_gateway=False):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    sx, sy = ax + aw, ay + ah / 2
    tx, ty = bx, by + bh / 2
    if tx <= sx:  # loop back: go around below
        low = max(ay + ah, by + bh) + 25
        return [(ax + aw / 2, ay + ah), (ax + aw / 2, low), (bx + bw / 2, low), (bx + bw / 2, by + bh)]
    if abs(sy - ty) < 1:
        return [(sx, sy), (tx, ty)]
    if from_gateway:  # branch to another lane: leave from the top or bottom corner
        cx = ax + aw / 2
        return [(cx, ay if ty < sy else ay + ah), (cx, ty), (tx, ty)]
    mid = sx + (tx - sx) / 2
    return [(sx, sy), (mid, sy), (mid, ty), (tx, ty)]


def build(name, lanes, steps):
    pos, lane_y, width = layout(lanes, steps)
    height = len(lanes) * LANE_H
    a = lambda s: escape(str(s), {'"': "&quot;"})
    flows = [(f"Flow_{i}_{n['to']}", i, n["to"], n.get("label", "")) for i, s in steps.items() for n in s["next"]]
    incoming = {i: [f for f in flows if f[2] == i] for i in steps}
    outgoing = {i: [f for f in flows if f[1] == i] for i in steps}

    x = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" '
         'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
         'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" '
         'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" '
         'id="Definitions_1" targetNamespace="http://bpmn.io/schema/bpmn" exporter="kaizen-map" exporterVersion="1.0">',
         '  <bpmn:collaboration id="Collaboration_1">',
         f'    <bpmn:participant id="Pool_1" name="{a(name)}" processRef="Process_1" />',
         '  </bpmn:collaboration>',
         '  <bpmn:process id="Process_1" isExecutable="false">',
         '    <bpmn:laneSet id="LaneSet_1">']
    for li, lane in enumerate(lanes):
        x.append(f'      <bpmn:lane id="Lane_{li}" name="{a(lane)}">')
        x += [f'        <bpmn:flowNodeRef>{i}</bpmn:flowNodeRef>' for i, s in steps.items() if s.get("lane", lanes[0]) == lane]
        x.append('      </bpmn:lane>')
    x.append('    </bpmn:laneSet>')
    for i, s in steps.items():
        tag = TYPES[s["type"]]
        x.append(f'    <bpmn:{tag} id="{i}" name="{a(s.get("name", ""))}">')
        if s.get("waste"):
            x.append(f'      <bpmn:documentation>Waste: {a(s["waste"])}</bpmn:documentation>')
        x += [f'      <bpmn:incoming>{f[0]}</bpmn:incoming>' for f in incoming[i]]
        x += [f'      <bpmn:outgoing>{f[0]}</bpmn:outgoing>' for f in outgoing[i]]
        x.append(f'    </bpmn:{tag}>')
    for fid, src, dst, label in flows:
        x.append(f'    <bpmn:sequenceFlow id="{fid}" name="{a(label)}" sourceRef="{src}" targetRef="{dst}" />')
    x += ['  </bpmn:process>',
          '  <bpmndi:BPMNDiagram id="Diagram_1">',
          '    <bpmndi:BPMNPlane id="Plane_1" bpmnElement="Collaboration_1">',
          f'      <bpmndi:BPMNShape id="Pool_1_di" bpmnElement="Pool_1" isHorizontal="true"><dc:Bounds x="{MARGIN}" y="{MARGIN}" width="{width - MARGIN}" height="{height}" /></bpmndi:BPMNShape>']
    for li, lane in enumerate(lanes):
        x.append(f'      <bpmndi:BPMNShape id="Lane_{li}_di" bpmnElement="Lane_{li}" isHorizontal="true">'
                 f'<dc:Bounds x="{MARGIN + POOL_HEADER}" y="{lane_y[lane]}" width="{width - MARGIN - POOL_HEADER}" height="{LANE_H}" /></bpmndi:BPMNShape>')
    for i, (px, py, w, h) in pos.items():
        marker = ' isMarkerVisible="true"' if steps[i]["type"] == "gateway" else ""
        x.append(f'      <bpmndi:BPMNShape id="{i}_di" bpmnElement="{i}"{marker}><dc:Bounds x="{px:.0f}" y="{py:.0f}" width="{w}" height="{h}" /></bpmndi:BPMNShape>')
    for fid, src, dst, _ in flows:
        pts = "".join(f'<di:waypoint x="{px:.0f}" y="{py:.0f}" />'
                      for px, py in waypoints(pos[src], pos[dst], steps[src]["type"] == "gateway"))
        x.append(f'      <bpmndi:BPMNEdge id="{fid}_di" bpmnElement="{fid}">{pts}</bpmndi:BPMNEdge>')
    x += ['    </bpmndi:BPMNPlane>', '  </bpmndi:BPMNDiagram>', '</bpmn:definitions>']
    return "\n".join(x) + "\n"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".bpmn")
    out.write_text(build(*load(src)), encoding="utf-8")
    print(f"BPMN written to {out} (open it in https://demo.bpmn.io, Camunda Modeler or Signavio)")


if __name__ == "__main__":
    main()
