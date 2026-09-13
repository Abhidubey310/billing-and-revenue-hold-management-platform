# Controls & Governance Framework

## Purpose

Define how automation can support billing-hold management without weakening financial, contractual or operational controls.

## Control objectives

The solution should ensure that:

- every processed case is traceable to a source record;
- incomplete data does not silently produce a decision;
- rule logic is deterministic and version controlled;
- material actions require appropriate human approval;
- overrides are visible and explained; and
- management can reconcile the processed population back to source systems.

## Control matrix

| Control area | Risk | Control response |
|---|---|---|
| Population completeness | Cases omitted from review | Reconcile source counts and held value before processing |
| Mandatory data | Invalid recommendation from incomplete records | Reject/quarantine records missing required identifiers or fields |
| Classification | Inconsistent routing | Approved rule hierarchy with explicit precedence |
| Unclear cases | Automation guesses an incorrect category | Route to Unclassified Exception / manual review |
| Priority | High-risk cases not surfaced | Defined ageing and value thresholds with test scenarios |
| Ownership | Cases have no accountable team | Category-to-owner mapping maintained as controlled reference data |
| Release decision | Automated action creates financial/control risk | Human approval before hold release or accounting-sensitive action |
| Overrides | Reviewer bypasses logic without trace | Capture user, timestamp and override reason |
| Auditability | Decision cannot be reconstructed | Persist source values, rule result, reason code and final action |
| Change management | Rule changes create unintended outcomes | Version control, peer review and UAT before deployment |
| Access | Unauthorised users change rules/actions | Role-based access and segregation of duties |
| Monitoring | Control deterioration is not detected | Exception, rework, override and SLA reporting |

## Human-in-the-loop design

Automation can safely perform:

- data validation;
- classification;
- owner assignment;
- ageing calculations;
- prioritisation;
- recommended-next-action generation; and
- management reporting.

Controlled human decisions should remain for:

- billing release;
- order cancellation;
- credit override;
- contract or pricing amendments;
- accounting treatment;
- revenue recognition; and
- material master-data corrections.

## Change governance

A production rule change should include:

1. documented business rationale;
2. impact assessment;
3. updated rule specification;
4. test cases covering expected and edge-case behaviour;
5. business/UAT approval;
6. controlled deployment; and
7. post-deployment monitoring.

## Key control KPIs

Useful control indicators include:

- percentage of source population processed;
- unclassified-exception rate;
- manual override rate;
- reopened / rework rate;
- cases breaching ageing SLA;
- Critical and High-priority backlog;
- average time to resolution; and
- reconciliation differences between source and workflow populations.

## Design principle

The objective is **controlled automation**: automate repetitive assessment and routing while keeping material financial judgement visible, reviewable and accountable.