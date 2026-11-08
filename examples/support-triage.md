# Example: "Add AI to triage our support tickets"

Based on a real project: a fibre network operator, about 300 customer requests a day, triaged by
hand by a team of operators. The figures below are rounded and adapted from that project; no
customer data is reproduced.

## The request

> We get around 300 support emails a day. Operators read each one, pick a category and a
> priority, and forward it to the right team. Can you build an AI that does the triage?

**A typical first answer** from a coding agent is to start building: an LLM classifier, a prompt
with the categories, an integration with the ticketing tool. That may be the right end point.
It is a poor starting point, because nobody has looked at why triage takes time.

## With `/kaizen`

### Kaizen sheet

**1. Problem.** About 300 requests a day; triage takes 2 to 3 minutes each, and 1 in 5 tickets
is sent to the wrong team and comes back (to be measured, see below).

**2. Current state**

| # | Step | Who | Tool | Work time | Wait before | Waste |
|---|------|-----|------|-----------|-------------|-------|
| 1 | Customer writes a free-text email | Customer | Email | – | – | Defects: key info often missing |
| 2 | Read the email, find the customer account | Operator | Email + CRM | 1.5 min | 2 h (queue) | Motion: searching the account |
| 3 | Pick category and priority | Operator | Ticketing | 0.5 min | – | |
| 4 | Ask the customer for missing info | Operator | Email | 1 min | – | Defects: ~25 % of tickets |
| 5 | Forward to the team | Operator | Ticketing | 0.2 min | – | |
| 6 | Team sends it back: wrong team | Team | Ticketing | 0.5 min | 4 h | Defects: ~20 % of tickets |

Lead time to the right team: about 2 hours when nothing goes wrong, a day or more when a loop
happens, which is about 4 tickets in 10 (1 − 0.75 × 0.8). Work time: 2 to 3 minutes. Flow
efficiency: about 2 % in the best case. Handoffs: 3 to 5. **The problem is waiting and loops,
not reading.**

**3. Top 3 wastes**

| Waste | Where | Hours lost / week | Estimate |
|-------|-------|-------------------|----------|
| Defects: missing info | Step 4 | ~31 h | 300 × 5 days × 25 % × 5 min round trip |
| Defects: wrong team | Step 6 | ~25 h | 300 × 5 × 20 % × 5 min (both teams) |
| Motion: finding the account | Step 2 | ~19 h | 300 × 5 × 45 s |

**4. Root cause.** Why is info missing and the team wrong? Because the request arrives as free
text. Why free text? Because the contact page is a plain email address. Why? Nobody revisited it
when the product range grew. **Root cause: the intake channel asks for nothing.**

**5. Future state**

| Step | Rung | Why not the rung above |
|------|------|------------------------|
| Free-text email | **Simplify / error-proof**: a web form with the customer number and a request type as required fields | Cannot eliminate intake |
| Ask for missing info | **Eliminated** by the required fields | – |
| Find the account | **Automate with rules**: the form passes the customer number, the CRM lookup is automatic | Already structured data, no AI needed |
| Pick category | **Rules** for form requests (type → team); **AI** only for the emails that still arrive in free text | The form covers most cases; AI only where text is unstructured |
| Priority | **Rules** for known critical cases (business sites, health facilities) + **AI suggestion** with human confirmation | Errors here are expensive: keep a person on it |
| Recurring questions | **Standardize**: 15 reply templates for the most frequent questions | Answers most of them in one step |

**6. Expected gain.** If 70 % of requests move to the form: 40 to 55 hours a week recovered,
mostly by removing loops, before any AI. The AI part then applies to the remaining 30 %
(about 90 emails a day), which changes its business case completely: run `/kaizen-roi`.

**7. Experiment.** Two weeks, one request type (billing), form + templates, no AI.
Success: share of billing tickets sent back below 5 %. Stop: form completion drops under 50 %.

**8. Not checked.** The 25 % and 20 % rates are estimates from the team: measure them for one
week (tag each loop in the ticketing tool) before committing.

### What happened in the real project

The AI classifier was built and tested in production: it cut operator time by about 25 % a day.
It was then paused, because reply templates and better intake captured most of the gain at a
lower running cost, with a documented method to restart it if volumes grow. Kaizen puts that
conclusion at the start of the project instead of the end.
