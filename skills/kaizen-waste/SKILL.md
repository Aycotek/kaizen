---
name: kaizen-waste
description: >
  Waste walk for office and digital work: find where time goes in a team, a
  process, an inbox, a meeting routine, a reporting cycle or a codebase workflow,
  using the eight wastes (DOWNTIME), and rank them by hours lost per week. Use
  when the user says "where does our time go", "waste", "muda", "we are always
  busy but nothing moves", "too many meetings", "too much admin", or asks what
  to fix first in how a team works.
argument-hint: "[team, process or source files]"
license: MIT
---

# Kaizen waste walk

In a factory you walk the floor and see the piles. In an office the piles are invisible: unread inboxes, approvals waiting, the same data typed three times. Your job is to make them visible, and to put a number on each.

## 1. Go and see

Work from evidence the user gives you: a week of calendar, a ticket export, an email thread, a process description, a screen recording transcript, a shared drive listing. If there is none, interview the user with these questions, at most five, one at a time if they answer briefly:

1. What do you redo most often, and why?
2. What do you wait for most often, and from whom?
3. Where do you copy information from one tool to another?
4. Which report, meeting or check would nobody miss if it stopped?
5. What do you search for more than once a week?

## 2. Classify (DOWNTIME)

| Waste | Signs to look for |
|-------|-------------------|
| **D**efects | rework, corrections, "can you resend", missing fields, back-and-forth |
| **O**verproduction | reports nobody opens, CC to ten people, features nobody uses |
| **W**aiting | approvals, queues, replies, weekly batches, dependencies on one person |
| **N**on-used talent | experts on data entry, ideas from the team that go nowhere |
| **T**ransport | re-keying, copy-paste between tools, files sent back and forth |
| **I**nventory | backlogs, unread items, half-finished work, open tabs as a to-do list |
| **M**otion | searching, app switching, looking for the latest version of a file |
| **E**xtra processing | checks with no known reason, extra signatures, polishing internal documents |

## 3. Waste register

| # | Waste | Where (step, tool) | Evidence | Hours lost / week | How estimated | Fix (first idea) | Effort |
|---|-------|--------------------|----------|-------------------|---------------|------------------|--------|

- **Evidence** is a number, a quote or an example from the sources. No evidence, no line: put it in "to check" instead.
- **Hours lost / week**: frequency × time per occurrence × people affected. Show the multiplication. Give a range when unsure.
- **Fix**: the first rung that would work (eliminate, combine, simplify, error-proof, rules, AI, keep human). Elimination comes first.
- **Effort**: S (under a day), M (under a month), L.

## 4. Output

1. The register, sorted by hours lost.
2. **Quick wins**: high hours, effort S. Usually two or three, often needing no tool at all.
3. **The one to fix first**, and why.
4. Total hours per week across the register, and what share of team time it represents if the team size is known.
5. **To check**: suspected wastes without evidence yet, and how to measure them in a week.

Never blame a person: a waste is always the result of how the work is set up. Phrase every line so it can be read out loud in front of the team.
