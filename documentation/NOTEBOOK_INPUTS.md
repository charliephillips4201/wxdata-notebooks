# Notebook inputs and outputs

The notebooks read compact GitHub inputs and, where listed, hourly products
from [Zenodo](https://doi.org/10.5281/zenodo.21844870). Extract the historical
archive to `data/wtk_bchrrr_nsrdb_2007_2023/` and the curated TaiESM1 archive to
`data/taiesm1_historical_ssp245_v022_2000_2099/`. Paths below are relative to the
repository root. [BA coverage](BA_COVERAGE.md) lists the released entities,
modeled capacities, available products, and calendars.

For dataset `0.1.0`, the outer archive names are
`wxdata_wtk_bchrrr_nsrdb_2007_2023.zip` and
`wxdata_sup3rcc_taiesm1_curated_2000_2099.zip`. The internal paths below remain
unchanged. The [two-notebook release check](START_HERE.md#verify-the-release)
provides a short route through one product from each archive.

## Input classes

| Class | Location | Distribution |
| --- | --- | --- |
| Released hourly data | The two dataset roots under `data/` above | Zenodo; ignored by Git |
| Compact direct inputs | Selected folders under `data/` | 100 GitHub data files, including input provenance fields |
| Analysis metadata | Three files under `manifests/` | GitHub |
| Acquisition and model caches | Each notebook's directory under `notebook_outputs/` | Local; ignored by Git |
| Standalone tables and figures | Each notebook's directory under `notebook_outputs/` | Local; ignored by Git |

## Notebook reading conventions

Each notebook starts with its purpose and example boundary, followed by
**Inputs:** and **Outputs:**. `Setup` is unnumbered; main workflow stages use
`Step N:` and named subsections sit one level below their parent. Shared method
steps, worked examples, and historical applications retain their teaching
sequence. Supplementary material uses `Appendix A`, `Appendix B`, and so on.
Scientific interpretations stay beside their results.

Headings, captions, and plot titles use sentence case. Markdown explains
purpose, assumptions, equations, and units; comments explain non-obvious code
choices. Mathematical symbols are retained in worked examples and linked to
the corresponding Python identifiers. Code uses four-space indentation and
natural wrapping around 100 characters, with complete paths and URLs retained.

Tables use `display(...)`; progress, counts, checks, and file locations use
`print(...)`. Ordinary input previews show five rows with source-column names.
Hourly comparisons use spaced hours, and scenario comparisons use the same
timestamp or planning period. Small worked examples remain complete, including
the one-hour county example and the two-time TELL predictor preview. The
pairwise preview shows both directions for the same two regions. Shortened
previews never reduce exported results.

Calculated-result tables use readable labels and meaningful row identifiers.
Counts and discrete durations display as integers; ordinary MW results use one
decimal; CF fractions and annualized hour metrics use three. Validation tables
show `MAE (MW)`, `RMSE (MW)`, `Bias (MW)`, `NRMSE (fraction)`, `MAPE (%)`, and
`R²` where those quantities are calculated. NRMSE divides RMSE by mean actual
load. MAPE uses two decimals; NRMSE and R² use three. Archive differences retain
scientific notation and their numerical tolerances; threshold tables retain
the precision needed to reproduce their comparisons. Mixed-unit diagnostics
retain the precision needed to inspect small differences. Formatting and unit
conversion apply only to display views; calculation fields and exported CSV
schemas retain their original names and values.

`Timestamp rows` counts joined rows; `Hours compared` counts valid paired
observations. TELL internal test statistics, seasonal calibration scores, and
held-out validation are separate result groups. A seasonal mean averages four
window scores. Risk-hour summaries may count qualifying scenario/threshold
rows, while event duration includes any bridged non-risk hour; their labels
identify those different quantities.

Portfolio displays place `Installed 2024` first, followed by 0%, 25%, 50%, 75%,
and 100% wind shares of fixed total nameplate capacity. Display labels do not
change the scenario codes or exported ordering. Installed percentages are
specific to each region. `MISO` identifies the direct BA product; `MISO
subregion sum` identifies `MISO_SUBREGION_SUM`. Geographic pools remain distinct
from thresholds shared across portfolios and from scenario-specific thresholds.

Comparable figures use consistent colors for actuals, wind, solar, direct TELL
forecasts, and summed-subregion forecasts. Capacity portfolios retain their
separate categorical palette; seasonal colors, product comparisons, and
heatmap scales keep their own meanings. Main titles use 16-point type, panel
titles 12-point, axis labels 11-point, ticks 10-point, and legends 9-point.
Legends have no frame; ordinary grids use a light gray line. Dense heatmap
annotations retain their readable existing sizes. Axes state units and time
zones explicitly, without changing the underlying calendar or aggregation.

Fixed paths are written explicitly relative to the notebook. Filename
construction is retained for families of files. Local path messages use the
complete notebook-relative path with forward slashes (`Path.as_posix()`).
Resolved paths required by a library keep their I/O behavior and receive a
relative display string. Raw manifest paths retain their documented basis;
URLs, HSDS resource identifiers, and library-generated warnings retain their
original representation. Execution notes identify locally verified stages and
retained acquisition/model results; saved output alone does not imply a fresh
network retrieval or model run.

## Per-notebook inputs

Notebook names below are under `notebooks/<category>/`. The final column gives
requirements for executing the corresponding stage; saved notebook outputs
can be reviewed without acquiring those inputs again.

| Notebook | Zenodo reads | Compact GitHub inputs | Additional execution requirement |
| --- | --- | --- | --- |
| `data_flow/county_weather_point_selection.ipynb` | None | Two Arthur County example CSVs in `data/county_weather/arthur_county_point_selection_example/` | NREL HSDS for grid lookup |
| `data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb` | None | County-grid crosswalk, BA service territory, and population files under `data/county_weather/` | NREL HSDS when the one-hour county caches are absent |
| `data_flow/tell_load_forecast_data_flow.ipynb` | Historical MISO `ba_weather/` | Raw MISO load, load-validation metadata, and `data/model_parameters/load_weather_source_periods_2007_2023.csv` | TELL for model training and prediction |
| `data_flow/eia860_regridding_methodology.ipynb` | None | EIA-860 plant/generator and MISO mapping workbooks in `data/eia860/2024_raw/`; subregion example in `data/eia860/2024_regridded_points/` | NREL HSDS for WTK, BC-HRRR, and NSRDB grid lookup |
| `data_flow/site_cf_generation_ba_weighting_validation.ipynb` | None | MISO `data/eia860/2022_regridded_points/`, `data/model_parameters/sam/`, 2023 `data/renewable_actuals/`, and 2022 capacity manifest | reV/PySAM for generation; NREL HSDS when weather caches are absent |
| `data_flow/ba_scenario_metrics_generation.ipynb` | Historical BA load, wind/solar CF, BA scenario metrics, pooled metrics | Raw MISO load, renewable actuals, historical loss-assumption CSV, 2022 capacity manifest | None |
| `data_flow/ba_stress_event_catalog.ipynb` | Historical BA and pooled scenario metrics | BA and pooled metadata manifests | None |
| `data_flow/state_load_generation.ipynb` | Selected TaiESM1 BA load and Iowa state load | BA/county mapping, `data/county_weather/county_populations_2000_to_2020.csv`, and eight `data/gcam_usa/` CSVs | TELL for the selected year/case reconstruction |
| `validation/all_ba_2023_load_forecast_validation.ipynb` | Historical BA load | 58 `data/load_actuals/cleaned_2023/` CSVs and validation metadata | None |
| `validation/miso_subregion_load_forecast_validation.ipynb` | Historical MISO and six subregion BA-load files | `data/load_actuals/cleaned_2023/MISO_cleaned_load_2023.csv` | None |
| `validation/miso_wind_solar_load_validation.ipynb` | Historical MISO BA load | MISO `data/eia860/2022_fleet_validation_cf/`, raw MISO load, renewable actuals, and 2022 capacity manifest | None |
| `validation/state_historical_taiesm_validation.ipynb` | Historical and TaiESM1 Iowa weather, load, wind CF, and solar CF | None | None |
| `analysis/miso_load_duration_curve.ipynb` | None | Raw MISO load and archived MISO predictions in `data/validation/load_forecast/` | None |
| `analysis/pairwise_pooling_heatmap.ipynb` | Historical BA and pooled scenario metrics | None | None |
| `analysis/miso_monthly_event_counts.ipynb` | Historical direct-MISO stress-event catalog | None | None |
| `analysis/plot_satellite_and_reanalysis.ipynb` | None | None | NASA Worldview and NOAA PSL network access |
| `analysis/state_seasonal_risk_hours.ipynb` | TaiESM1 Iowa scenario metrics | None | None |

## Outputs and example boundaries

Every notebook retains its review tables or figures inline. Standalone files,
when produced, go under `notebook_outputs/<category>/<notebook-stem>/`. These
files are not inputs to later notebooks unless explicitly stated. A method
connection in the process diagrams does not mean an example regenerates the
full upstream release product.

| Notebook | Standalone output and demonstrated extent |
| --- | --- |
| `county_weather_point_selection` | None; displays one Arthur County centroid and its grid matches. The national crosswalk is a separate packaged input. |
| `county_hsds_download_and_ba_weather_aggregation` | One-hour county-weather HDF5 caches and one-hour MISO weather CSV; Iowa aggregation is displayed inline. |
| `tell_load_forecast_data_flow` | TELL training/prediction inputs, tuning results, model files, reconstructed MISO load, 2023 validation CSV, and figures. |
| `eia860_regridding_methodology` | One MISO 2024 grid-point CSV; the appendix shows packaged subregion assignments. |
| `site_cf_generation_ba_weighting_validation` | Site-weather and site-CF HDF5 caches, weighted MISO CF CSVs, validation metrics, and a figure using the 2022 fleet. |
| `ba_scenario_metrics_generation` | Reconstructed MISO scenario CSV and figure; numerical comparison with released scenarios and a pooling example. |
| `ba_stress_event_catalog` | Four example-region event CSVs following the toy-to-historical method. These do not regenerate all deposited catalogs. |
| `state_load_generation` | TELL-compatible staging inputs, one Iowa year/case reconstruction, and a figure of the eight full-period GCAM cases read from the archive. |
| `miso_wind_solar_load_validation` | `miso_2023_loss_sensitivity_metrics.csv` for the full year and `miso_20230101_20230131_loss_sensitivity.png` for January. |
| `miso_load_duration_curve` | MISO load-duration PNG. |
| `pairwise_pooling_heatmap` | Ordered-pair metrics CSV and nine heatmap PNGs: four main and five scenario-specific appendix figures. |
| `state_seasonal_risk_hours` | 240-row Iowa seasonal-risk-hours CSV and six portfolio PNGs. |
| Remaining five notebooks | Inline only: all-BA load validation, MISO subregion validation, Iowa historical/TaiESM1 validation, MISO monthly event counts, and satellite/reanalysis context. |

Acquisition outputs depend on HSDS and may be retained from an earlier run when
the service is unavailable. Consult the execution note in each acquisition
notebook before interpreting its saved results as a fresh reconstruction.
