"""Tests for the BPMN generator.  python -m unittest discover tests"""
import json
import subprocess
import sys
import tempfile
import unittest
import xml.dom.minidom
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills" / "kaizen-map" / "scripts" / "to_bpmn.py"
sys.path.insert(0, str(SCRIPT.parent))
import to_bpmn  # noqa: E402


def run(process):
    with tempfile.TemporaryDirectory() as d:
        src = Path(d) / "p.json"
        src.write_text(json.dumps(process), encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), str(src)], capture_output=True, text=True)
        out = src.with_suffix(".bpmn")
        return r, (out.read_text(encoding="utf-8") if out.exists() else None)


class TestToBpmn(unittest.TestCase):
    def test_example_is_valid_bpmn(self):
        xml_text = to_bpmn.build(*to_bpmn.load(SCRIPT.parent / "example.json"))
        doc = xml.dom.minidom.parseString(xml_text)
        ids = {e.getAttribute("id") for e in doc.getElementsByTagName("*") if e.getAttribute("id")}
        refs = {e.getAttribute("bpmnElement") for e in doc.getElementsByTagName("*") if e.getAttribute("bpmnElement")}
        self.assertTrue(refs <= ids, "every diagram shape points to an existing element")
        flows = doc.getElementsByTagName("bpmn:sequenceFlow")
        edges = doc.getElementsByTagName("bpmndi:BPMNEdge")
        self.assertEqual(len(flows), len(edges), "every flow is drawn")
        self.assertEqual(len(doc.getElementsByTagName("bpmn:lane")), 4)

    def test_every_node_inside_its_lane(self):
        name, lanes, steps = to_bpmn.load(SCRIPT.parent / "example.json")
        pos, lane_y, _ = to_bpmn.layout(lanes, steps)
        for i, (x, y, w, h) in pos.items():
            top = lane_y[steps[i].get("lane", lanes[0])]
            self.assertTrue(top <= y and y + h <= top + to_bpmn.LANE_H, f"{i} drawn outside its lane")

    def test_loop_does_not_break_layout(self):
        r, out = run({"lanes": ["A"], "steps": [
            {"id": "s", "type": "start", "lane": "A", "next": ["t"]},
            {"id": "t", "name": "Do", "lane": "A", "next": ["g"]},
            {"id": "g", "type": "gateway", "name": "OK?", "lane": "A", "next": [{"to": "t", "label": "no"}, {"to": "e", "label": "yes"}]},
            {"id": "e", "type": "end", "lane": "A"}]})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('name="no"', out)

    def test_unknown_next_is_rejected(self):
        r, out = run({"lanes": ["A"], "steps": [{"id": "s", "type": "start", "lane": "A", "next": ["ghost"]}]})
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("ghost", r.stderr)
        self.assertIsNone(out)

    def test_missing_start_is_rejected(self):
        r, _ = run({"lanes": ["A"], "steps": [{"id": "t", "lane": "A"}]})
        self.assertIn("no start", r.stderr)

    def test_special_characters_are_escaped(self):
        r, out = run({"name": "R&D <test>", "lanes": ["Q&A"], "steps": [
            {"id": "s", "type": "start", "lane": "Q&A", "name": 'Say "hi" & go', "next": ["e"]},
            {"id": "e", "type": "end", "lane": "Q&A"}]})
        self.assertEqual(r.returncode, 0, r.stderr)
        xml.dom.minidom.parseString(out)


if __name__ == "__main__":
    unittest.main()
