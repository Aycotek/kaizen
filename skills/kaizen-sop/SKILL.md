---
name: kaizen-sop
description: >
  Make an improvement stick: turn a process into standard work people actually
  use, a one-page procedure, a checklist at the point of use, the error-proofing
  to add, and the control plan that shows if it slips. Use when the user says
  "SOP", "procedure", "work instruction", "checklist", "playbook", "standard
  work", "onboarding guide", "how do we make sure this keeps working", or after
  /kaizen or /kaizen-map has defined a future state.
argument-hint: "[process or files]"
license: MIT
---

# Kaizen SOP

An improvement that lives in one person's head is gone the day they go on holiday. Standard work is not bureaucracy: it is the current best way, written down so anyone can follow it and anyone can improve it.

## Rules for a procedure people actually use

- **One page.** If it does not fit, split it by role or by case.
- **Written for the person doing the work**, in their words, at the moment they need it. Not for an auditor.
- **Steps start with a verb** and say what "done" looks like: "Check the PO number is on the invoice. If missing, send template B to the customer."
- **The key points**: for each step that often goes wrong, one line on why it matters. People skip steps whose reason they do not know.
- **Decisions as simple rules**: "If amount > 5,000 €, ask the manager. Otherwise, send."
- **Screenshots or examples** where the tool is confusing, never paragraphs explaining a screen.
- **Owner and version**: who updates it, and the date. A procedure without an owner is out of date within six months.

## Output 1: the procedure

```
Title: <verb + object>            Owner: <role>    Version: <date>
Purpose: <one line: what goes wrong without it>
Trigger: <what starts it>         Done when: <what the customer gets>
Steps:
1. ...
   Key point: ...
Exceptions: <case> → <what to do / who to ask>
```

## Output 2: the checklist

Only the steps people forget or get wrong, five to nine items, each checkable in a second. Say where it lives: in the ticket template, the form, the tool, not in a shared folder nobody opens.

## Output 3: error-proofing

For each common mistake, propose a way to make it impossible or immediately visible in the tool itself: a required field, a dropdown, a default value, a validation rule, an automatic alert. Rank them by effort. Every mistake prevented by design is a line removed from the procedure.

## Output 4: control plan

| What to watch | Normal | Alert when | Checked by | How often |
|---------------|--------|------------|------------|-----------|

Two or three indicators, no more. Include one that shows if people stopped following the standard (for example, share of cases with the checklist completed).

## Keep it alive

End with how the standard will improve: who people tell when the procedure is wrong, and when it is reviewed (after any incident, and at least every six months). Standard work is the base for the next kaizen, not the end of it.
