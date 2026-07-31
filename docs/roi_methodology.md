# Illustrative ROI Methodology

This portfolio model demonstrates how the potential value of billing-hold automation can be estimated. It does **not** claim measured savings from any employer or production implementation.

## Core calculations

### Processing effort saved

```text
Annual cases = Monthly cases × Working months
Manual hours = Annual cases × Manual minutes per case ÷ 60
Assisted hours = Annual cases × Assisted minutes per case ÷ 60
Direct hours saved = Manual hours − Assisted hours
```

### Rework reduction

```text
Rework hours before = Annual cases × Rework rate before × Rework minutes ÷ 60
Rework hours after = Annual cases × Rework rate after × Rework minutes ÷ 60
Rework hours saved = Rework hours before − Rework hours after
```

### Financial benefit

```text
Annual gross benefit = Total hours saved × Loaded hourly cost
Annual net benefit = Annual gross benefit − Annual support cost
First-year ROI = (Annual gross benefit − First-year cost) ÷ First-year cost
Payback months = One-time build cost ÷ Monthly net benefit
```

## Example assumptions

The sample model assumes:

- 600 hold cases per month;
- 12 minutes of manual processing per case;
- 4 minutes per case after automation support;
- an 8% rework rate before automation and 2% after;
- a £22 illustrative loaded hourly cost;
- £18,000 one-time implementation cost; and
- £6,000 annual support cost.

## Illustrative result

Using those assumptions, the model estimates:

- 1,104 hours of annual capacity released;
- approximately 0.61 FTE equivalent;
- £24,288 annual gross benefit;
- £18,288 annual net benefit;
- approximately 11.8 months to payback; and
- 1.2% first-year ROI after build and support costs.

From year two onward, the economics improve because the one-time build cost is no longer repeated.

## Important interpretation

Time saved is not automatically the same as cash saved. Benefits may appear as:

- released team capacity;
- faster billing resolution;
- reduced rework;
- improved control coverage;
- earlier revenue release; or
- avoided future hiring.

Any production business case should replace every illustrative assumption with measured process data and approved finance inputs.
