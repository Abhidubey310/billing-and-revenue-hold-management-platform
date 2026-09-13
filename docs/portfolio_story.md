# Portfolio Story

## 30-second version

I designed a synthetic Billing & Revenue Hold Management Platform to demonstrate how a fragmented manual hold-review process can be converted into a controlled exception workflow. The solution classifies each held order, assigns accountable ownership, prioritises cases using ageing and financial exposure, recommends the next action and preserves an auditable reason for every decision.

The important part is not the Python itself. The project demonstrates how I move from a Finance problem to process redesign, control logic, automation, human review and measurable benefits.

## Interview version

### Situation

Billing holds can accumulate across Finance, Sales, Delivery and Customer teams. When they are managed manually, teams repeatedly review the same cases, ownership is inconsistent, ageing is difficult to manage and significant billing value can remain blocked without a clear action path.

### Task

Design a scalable approach that would help a finance team answer five questions consistently:

1. Why is the order on hold?
2. Who should own the resolution?
3. How urgent is it?
4. What should happen next?
5. Can the recommendation be explained and audited?

### Action

I created a synthetic data model and designed a transparent decision hierarchy. I then built a prototype that:

- validates the incoming hold population;
- standardises the hold reason into defined categories;
- routes cases to accountable teams;
- calculates case ageing;
- combines ageing and billing value into priority;
- generates a recommended next action;
- routes unclear cases to manual review rather than guessing; and
- models the potential capacity and ROI impact using editable assumptions.

I deliberately separated automated triage from financial decision-making. The tool can recommend and prioritise, but billing release, accounting treatment and contractual decisions remain controlled human actions.

### Result

On the included synthetic portfolio, the engine converts 12 held orders and £423.3k of illustrative billing value into a prioritised action queue, including four Critical and six High-priority cases.

The broader outcome demonstrated is a move from **manual case-by-case review** to **exception-led management with clearer accountability, controls and management visibility**.

## What this project demonstrates

- Finance Transformation
- Order-to-Cash / billing operations
- Revenue-risk and ageing analysis
- Process redesign
- Control and governance design
- Business-rule automation
- Exception management
- Python / pandas application
- Benefits realisation and ROI thinking
- Business-to-technology translation

## Safe disclosure statement

This repository is independently recreated using fictional entities, synthetic data and generic industry rules. It should be discussed as evidence of relevant transformation capability, not as the exact implementation, codebase, data or operating procedure of any employer.