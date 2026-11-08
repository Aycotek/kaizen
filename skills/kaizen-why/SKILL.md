---
name: kaizen-why
description: >
  Root cause analysis for incidents, defects, recurring bugs, customer
  complaints and process failures: 5 whys checked against facts, a fishbone
  when causes are many, and corrective plus preventive actions (8D style). Use
  when something went wrong or keeps going wrong, and when the user says
  "root cause", "5 whys", "post-mortem", "RCA", "8D", "why does this keep
  happening", or wants to stop fixing the same problem twice.
argument-hint: "[incident description or files]"
license: MIT
---

# Kaizen why

A symptom fixed comes back. A cause fixed does not. Your job is to go from what happened to what in the system allowed it to happen, using facts, and to change that.

## 1. State the problem precisely

Answer in one or two lines: what happened, where, when, how often, how many cases, what impact. "Customer invoices wrong" is a complaint; "12 of 340 October invoices billed the old price, all on contracts changed after the 20th" is a problem you can solve.

Also note what is *not* affected (other months, other contract types). The boundary between affected and not affected points to the cause.

## 2. Contain first

If the problem is still happening or still hurting customers, propose the containment action before any analysis: stop the bleeding, then investigate. Mark it as temporary.

## 3. Ask why, with evidence

| Why? | Answer | Evidence | Verified? |
|------|--------|----------|-----------|

- Each answer must be backed by a log line, a record, a document, a reproduction, or a quote from someone who saw it. Without evidence, mark it "hypothesis" and say how to verify it.
- Follow two chains when it matters: **why it happened**, and **why it was not detected** before reaching the customer.
- Stop when you reach a cause the team can change: a rule, a design, a default, a missing check, a training gap. Never stop at a person ("Julie made a mistake"): ask why the system let the mistake through.
- If an answer branches into several causes, follow each branch, or switch to a fishbone.

## 4. Fishbone, when causes are many

Group candidate causes under: Method, Tools/Systems, Data/Inputs, People/Skills, Environment, Measurement. Mark each as confirmed, ruled out or untested. Test the most likely ones first, cheapest test first.

## 5. Actions

| Type | Action | Owner (role) | Due | How we will know it worked |
|------|--------|--------------|-----|----------------------------|
| Containment | ... | | | |
| Correction (root cause) | ... | | | |
| Prevention (detection) | ... | | | |
| Spread | same weakness elsewhere? | | | |

Prefer actions that make the error impossible or immediately visible (validation, defaults, alerts, checklists at the point of use) over actions that rely on attention ("be more careful", "remind the team"). A reminder is not a corrective action.

## 6. For software bugs

The same method applies. Reproduce first, then find the commit or change that introduced it, then ask why review and tests did not catch it. The fix includes a test that fails before and passes after, and, when the same pattern exists elsewhere in the codebase, a search for its other occurrences.

## Output

Problem statement, containment, the why table (with evidence column), the root cause in one sentence, the action table, and what is still unverified.
