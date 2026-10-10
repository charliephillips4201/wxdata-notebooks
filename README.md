# Synchronized Wind, Solar, and Load Data for Power System Planning

## Overview

This repository contains companion notebooks and selected sample data used by
the examples. The samples contain selected regions, years, variables, and
scenarios. The full dataset and detailed coverage documentation are provided
separately through Zenodo.

[Full dataset on Zenodo (unpublished draft preview)][zenodo-preview].

Power-system planning needs to represent hours when high electricity demand coincides with low wind or solar output. Synchronized weather, demand, and renewable capacity factors preserve these relationships across time and locations. Hourly resolution captures shortfalls and their duration; long records show seasonal and year-to-year variability. Historical and simulated climate collections support complementary investigations of these conditions.

The workflow has two branches: weather becomes modeled electricity demand, while weather and generator fleets become renewable capacity factors. These ingredients feed scenario metrics, geographic pooling, and stress-event catalogs. State products extend the demand calculations to states. Validation assesses model performance and limitations; analysis demonstrates applications of the resulting datasets.

**Load and renewable capacity factors**

[![Weather and fleet inputs become modeled load and renewable capacity factors, with notebook filenames labeling the corresponding stages.](process_flow_load_and_cf.png)](process_flow_load_and_cf.png)

**Scenarios, pooling, and stress events**

[![Synchronized load and renewable capacity factors feed BA scenarios, geographic pooling, and stress-event catalogs, with notebook filenames labeling the corresponding stages.](process_flow_scenarios_and_events.png)](process_flow_scenarios_and_events.png)

Filenames identify the notebooks linked in the index; click a diagram to enlarge it.

<a id="quick-start"></a>
<a id="install-and-run-the-first-example"></a>

## Notebook index

Each notebook states its inputs, assumptions, and calculations. Results appear
inline; exported files go to `data_outputs/`.

### Data flow — 9 notebooks

| Notebook | What it demonstrates |
| --- | --- |
| [County weather-point selection](notebooks/data_flow/county_weather_point_selection.ipynb) | Select a population-weighted weather point for Arthur County. |
| [County weather and BA aggregation](notebooks/data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb) | Aggregate county weather for MISO and Iowa. |
| [TELL load forecasting](notebooks/data_flow/tell_load_forecast_data_flow.ipynb) | Train MISO demand models and validate forecasts against 2023 observations. |
| [EIA-860 regridding](notebooks/data_flow/eia860_regridding_methodology.ipynb) | Map 2024 MISO renewable capacity to weather grids. |
| [Site CF, weighting, and validation](notebooks/data_flow/site_cf_generation_ba_weighting_validation.ipynb) | Model and validate capacity-weighted MISO wind and solar CF. |
| [BA scenario metrics](notebooks/data_flow/ba_scenario_metrics_generation.ipynb) | Calculate MISO generation and net load for six renewable portfolios. |
| [Pooled scenario metrics](notebooks/data_flow/pooled_scenario_metrics_generation.ipynb) | Combine five MISO subregions into MISO_NCA scenario metrics. |
| [Stress-event catalogs](notebooks/data_flow/ba_stress_event_catalog.ipynb) | Identify high-load, high-net-load, and low-renewable events in four regions. |
| [State load generation](notebooks/data_flow/state_load_generation.ipynb) | Reconstruct Iowa demand and compare raw and GCAM-scaled trajectories. |

### Validation — 5 notebooks

| Notebook | What it demonstrates |
| --- | --- |
| [MISO load-duration curve](notebooks/validation/miso_load_duration_curve.ipynb) | Compare observed and modeled MISO load-duration curves for 2023. |
| [All-BA 2023 load validation](notebooks/validation/all_ba_2023_load_forecast_validation.ipynb) | Compare 2023 demand forecasts and observations across 58 entities. |
| [MISO subregion load validation](notebooks/validation/miso_subregion_load_forecast_validation.ipynb) | Compare direct MISO demand forecasts with the sum of six subregions. |
| [MISO wind, solar, and load validation](notebooks/validation/miso_wind_solar_load_validation.ipynb) | Validate MISO load and renewable output and compare renewable-loss assumptions. |
| [Iowa historical/TaiESM1 comparison](notebooks/validation/state_historical_taiesm_validation.ipynb) | Compare Iowa historical and TaiESM1 weather, load, and renewable CF. |

### Analysis — 4 notebooks

| Notebook | What it demonstrates |
| --- | --- |
| [Pairwise pooling heatmaps](notebooks/analysis/pairwise_pooling_heatmap.ipynb) | Compare pooling effects across 110 ordered region pairs. |
| [Monthly MISO event counts](notebooks/analysis/miso_monthly_event_counts.ipynb) | Summarize MISO stress events by month and duration. |
| [Satellite and reanalysis context](notebooks/analysis/plot_satellite_and_reanalysis.ipynb) | View NASA/NOAA weather context for a selected stress event. |
| [Iowa seasonal risk hours](notebooks/analysis/state_seasonal_risk_hours.ipynb) | Compare Iowa seasonal risk across six portfolios over 2000–2099. |

## Data

### Sample data included in this repository

<a id="bundled-notebook-inputs"></a>

The repository includes **94 selected release inputs**:
86 historical files and 8 TaiESM1 files, totaling approximately **457 MB**.
The samples retain selected regions, years, columns, or scenarios;
they are not complete copies of the released datasets.
Each notebook lists any additional software or external-data requirements.

Sample files are bundled in `data_inputs/examples/` and require no extraction.
Other supporting inputs are in `data_inputs/`; generated results go to `data_outputs/`.

The [input manifest](manifests/notebook_inputs.csv) records each bundled file's
source, selected years/columns/scenarios, notebook consumers, size, and checksum.
Its `path` locates the bundled file; `source_path` identifies the original
archive-relative release file.

### Full dataset on Zenodo

<a id="ba-pools"></a>
<a id="balancing-authorities-and-miso-subregions"></a>
<a id="coverage"></a>
<a id="download-and-extract"></a>
<a id="gcam-usa-demand-cases"></a>
<a id="load--solar-only-16"></a>
<a id="load--wind--solar-35"></a>
<a id="load-only-9"></a>
<a id="pool-membership"></a>
<a id="solar-only-3"></a>
<a id="states-and-district-of-columbia"></a>
<a id="taiesm1-ba-and-pool-products"></a>
<a id="verify-the-download"></a>
<a id="wind-and-solar-only-2"></a>
<a id="wind-only-3"></a>

The [unpublished draft preview on Zenodo][zenodo-preview] provides the full
collections and their detailed `README_DATASET.md`, including regional coverage,
peak loads, nameplate capacities, pool membership, GCAM cases, schemas, and limitations.

- **Historical, 2007–2023:** WTK/BC-HRRR/NSRDB data for BAs, pools, and the lower 48 states plus DC.
- **TaiESM1, 2000–2099:** curated Sup3rCC climate data for selected BAs, MISO_SUBREGION_SUM, and Iowa.

Download and extract full archives **outside this repository**, separate from
the bundled sample directories. Update notebook paths when using the full data;
do not extract archives over the bundled files.

## Interpretation

- **Modeled quantities:** demand is modeled; net load is demand minus modeled
  wind and solar generation. Equivalent renewable CF is combined renewable
  generation divided by combined nameplate capacity.
- **Fleets and scenarios:** the fixed 2024 fleet supports the installed mix and
  wind/solar nameplate splits of 0/100, 25/75, 50/50, 75/25, and 100/0. Shares
  describe capacity, not energy. Single-technology BA entities have two
  portfolios; load-only BAs have one. Renewable-only entities have no net load.
  Renewable validation uses a separate **2022 fleet**. Source CF and
  loss-adjusted scenario CF should not be interchanged.
- **Time alignment:** all timestamps are UTC. Historical load/weather retain
  leap days; renewable CF omits them. TaiESM1 uses a no-leap calendar and
  supports statistical comparisons, not matching observed weather events.
- **Pooling:** CF is capacity-weighted; these aggregates do not model
  transmission or dispatch constraints. Direct MISO, its subregions, and its
  overlapping pools are alternative representations and are not additive.
- **Events:** catalog net-load thresholds are shared across portfolios within
  each region. Events can bridge one non-risk hour, included in duration.
  The stress-catalog and analysis notebooks explain their different thresholds
  and counting conventions.
- **Known pressure limitation:** Iowa's TaiESM1 pressure averages about
  **9,369 Pa below the historical series** over 2007–2023. The source/grid cause
  remains unresolved; no correction has been applied. See the
  [Iowa diagnostics](notebooks/validation/state_historical_taiesm_validation.ipynb).

## Sources and citation

Reserved dataset DOI: `10.5281/zenodo.21844870` (active after publication).
Use [CITATION.cff](CITATION.cff) for the notebooks. Original notebooks and documentation
use [CC BY 4.0](LICENSE); bundled archive inputs retain their [data license](data_inputs/examples/LICENSE_DATA.txt).
Third-party materials retain their own terms.

Sources include EIA-860/930 (fleet and observations), WTK/BC-HRRR/NSRDB and
Sup3rCC/TaiESM1 (weather), TELL (load), reV/PySAM (renewables), Census/TIGER
(population and geography), and GCAM-USA (demand pathways). Retain the
[EIA attribution](https://www.eia.gov/about/copyrights_reuse.php),
[weather-source notices](https://www.nrel.gov/disclaimer.html),
[Census research](https://www.census.gov/topics/research/research-transparency-public-access/policy.html)
and [policy notices](https://www.census.gov/about/policies.html), and
[GCAM-USA attribution](https://github.com/JGCRI/gcam-doc/blob/gh-pages/gcam-usa.md).

<a id="verification-and-publication-status"></a>

Recorded execution checks found matching reference results for the compared
examples; they do not establish a clean installation or validate every product.
Site-CF validation used legacy weather caches without original source-version
metadata. Dataset and notebook versions are independent; consult Zenodo for
release availability and retain the notebook revision with your results.

OpenAI Codex assisted with code and documentation. Charlie Phillips reviewed
the work and remains responsible for its content and interpretation.

[zenodo-preview]: https://zenodo.org/records/21844870?preview=1&token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImU1YTZmOTdhLTg1Y2YtNGExMC1hMzdmLTY1NThjMGRjYzg0NyIsImRhdGEiOnt9LCJyYW5kb20iOiI4NThhZTRkYjg5OWNkNjg3MjM1NTBhYjAwYzg2NWU5YiJ9.kYx9A2TU38HVcXgbed38NuUok4_YGhmQ3K7MivkrsoIbPh9I--8NjqIJIjdHz5mhtkUs9elFEc7OdQBQn4bULQ
