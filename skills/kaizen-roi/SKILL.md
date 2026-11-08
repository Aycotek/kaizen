---
name: kaizen-roi
description: >
  Honest business case for a process change, an automation or an AI project:
  baseline, gains, the cost of errors, run and build costs, payback, a
  sensitivity check and the criteria to stop. Use when the user asks "is it
  worth it", "ROI", "business case", "how much will we save", "justify this
  project", "build vs buy", or needs to convince a manager or a client with
  numbers.
argument-hint: "[project or files]"
license: MIT
---

# Kaizen ROI

Most business cases count the gain and forget the rest. Yours counts what the change will really cost, including its mistakes, and says when to stop. A decision-maker trusts a business case that shows its weak points.

## 1. Baseline (today, without the change)

Volume per period, time per case, people involved, loaded hourly cost, error rate and the cost of one error, lead time. For every figure, write the source: measured, from the user, from a document, or assumption. If a key figure is an assumption, say what one week of measurement would look like.

## 2. Gains

- **Time saved** = volume × minutes saved per case × share of cases where the change applies.
- **Errors avoided** = volume × (error rate before − after) × cost of one error.
- **Faster lead time**, only if it has a value you can name (cash collected earlier, customers not lost, penalty avoided). Otherwise list it as a benefit without a number.
- Time saved is only money if it is reused or not hired. Say which: "frees 0.4 FTE for X" is honest; "saves 18 k€" when nobody leaves or changes tasks is not.

## 3. Costs

- **Build**: people's time (including the business side: interviews, tests, training), licenses, integration.
- **Run**: subscriptions, API or compute usage, maintenance (count about 15 to 20 % of build per year if unknown), monitoring.
- **Errors of the new system**: volume × error rate after × cost of one error. An automation that is right 90 % of the time on 1,000 cases makes 100 mistakes. Someone pays for them.
- **Change**: training, the dip in productivity during the switch, the people still needed for exceptions.

## 4. Result

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Gains | | | |
| Costs | | | |
| Net | | | |

Payback period, and net value over three years. Keep it in the user's currency, rounded: false precision undermines trust.

## 5. Sensitivity

Recompute with the two or three most uncertain assumptions at their pessimistic value. State the break-even point: "worth it as long as the model is right on at least 82 % of cases" or "only above 150 cases a week". This one sentence is often the most useful line of the whole case.

## 6. Compare with the cheaper option

Always compare with at least one option lower on the ladder: eliminate the step, simplify the form, a template, a rule. If a cheaper option gets most of the gain, recommend it, even if it is less impressive.

## 7. Stop criteria

Write before starting what would make the team stop: a measured gain below X after N weeks, an error rate above Y, a cost above Z. Deciding this in advance is what lets a project be stopped cleanly instead of drifting.

## Output

Baseline table with sources, gains, costs, the three-year table, payback, sensitivity and break-even, the cheaper option, stop criteria, and the assumptions to verify first. One page.
