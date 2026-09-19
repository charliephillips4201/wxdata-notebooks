# Notebook inputs and outputs

This reference maps the 17 notebooks to their inputs, local outputs, and
execution requirements. The [repository README](../README.md) provides the
first-run route; [BA coverage](BA_COVERAGE.md) describes entity names, fleets,
product availability, and exclusions. The notebooks read their inputs directly:
method connections in the [process diagram](process_flow.svg) do not make one
worked example a file-generation prerequisite for the next.

- [Notebook inputs](#notebook-inputs)
- [Outputs and example boundaries](#outputs-and-example-boundaries)
- [Download the datasets](#download-the-datasets)
- [Verify the release](#verify-the-release)
- [Execution notes](#execution-notes)
- [Reading the results](#reading-the-results)
- [Sources and attribution](#sources-and-attribution)
- [Publication status](#publication-status)

Paths in this guide are relative to the repository root unless stated
otherwise. The compact collection contains **94 data files and three
manifests**. Full hourly datasets, acquisition caches, and generated notebook
artifacts are not committed to Git.

## Notebook inputs

The tables follow the methods order within each category. Saved tables and
figures can be reviewed without rerunning the stages listed here. "Historical"
means `data/wtk_bchrrr_nsrdb_2007_2023/`; "TaiESM1" means
`data/taiesm1_historical_ssp245_v022_2000_2099/`.

### Data flow: eight notebooks

| Notebook | Released hourly inputs | Bundled inputs | Additional execution requirement |
| --- | --- | --- | --- |
| [County weather-point selection](../notebooks/data_flow/county_weather_point_selection.ipynb) | None | Two Arthur County CSVs in `data/county_weather/arthur_county_point_selection_example/` | HSDS for WTK, BC-HRRR, and NSRDB grid metadata |
| [County weather and BA aggregation](../notebooks/data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb) | None | County-grid crosswalk, BA service territories, and population table in `data/county_weather/` | HSDS when the one-hour local weather caches are absent |
| [TELL load forecasting](../notebooks/data_flow/tell_load_forecast_data_flow.ipynb) | Historical MISO `ba_weather/` | Raw MISO load, load-validation metadata, and `data/model_parameters/load_weather_source_periods_2007_2023.csv` | TELL training and prediction |
| [EIA-860 regridding](../notebooks/data_flow/eia860_regridding_methodology.ipynb) | None | Plant and generator workbooks in `data/eia860/2024_raw/`; reviewed subregion mapping workbook in `data/eia860/2024_regridded_points/` | HSDS for WTK, BC-HRRR, and NSRDB grid metadata |
| [Site CF, weighting, and validation](../notebooks/data_flow/site_cf_generation_ba_weighting_validation.ipynb) | None | MISO `data/eia860/2022_regridded_points/`, SAM JSONs in `data/model_parameters/sam/`, 2023 renewable actuals, and 2022 capacity manifest | reV/PySAM generation; HSDS when local site-weather caches are absent |
| [BA scenario metrics](../notebooks/data_flow/ba_scenario_metrics_generation.ipynb) | Historical BA load, wind/solar CF, BA scenario metrics, and pooled metrics | BA metadata manifest, raw MISO load, 2022 renewable actuals, historical loss-assumption CSV, and 2022 capacity manifest | None beyond the environment |
| [Stress-event catalogs](../notebooks/data_flow/ba_stress_event_catalog.ipynb) | Historical BA and pooled scenario metrics | BA and pooled metadata manifests | None beyond the environment |
| [State load generation](../notebooks/data_flow/state_load_generation.ipynb) | Selected TaiESM1 BA loads and archived Iowa state load | BA/county mapping, `county_populations_2000_to_2020.csv`, and one selected `data/gcam_usa/` CSV | TELL for one Iowa year/case; seven other GCAM CSVs support changing the selected case |

### Validation: four notebooks

| Notebook | Released hourly inputs | Bundled inputs | Additional execution requirement |
| --- | --- | --- | --- |
| [All-BA 2023 load validation](../notebooks/validation/all_ba_2023_load_forecast_validation.ipynb) | Historical BA load | 58 `data/load_actuals/cleaned_2023/` CSVs and validation metadata | None beyond the environment |
| [MISO subregion load validation](../notebooks/validation/miso_subregion_load_forecast_validation.ipynb) | Historical direct-MISO and six subregion BA-load files | `data/load_actuals/cleaned_2023/MISO_cleaned_load_2023.csv` | None beyond the environment |
| [MISO wind, solar, and load validation](../notebooks/validation/miso_wind_solar_load_validation.ipynb) | Historical MISO BA load | `data/eia860/2022_fleet_validation_cf/`, raw MISO load, renewable actuals, and 2022 capacity manifest | None beyond the environment |
| [Iowa historical/TaiESM1 validation](../notebooks/validation/state_historical_taiesm_validation.ipynb) | Historical and TaiESM1 Iowa weather, load, wind CF, and solar CF | None | None beyond the environment |

### Analysis: five notebooks

| Notebook | Released hourly inputs | Bundled inputs | Additional execution requirement |
| --- | --- | --- | --- |
| [MISO load-duration curve](../notebooks/analysis/miso_load_duration_curve.ipynb) | None | Six subregion files in `data/load_actuals/cleaned_2023/`, using `load_actual_mw_raw`, plus six files in `data/validation/load_forecast/miso_subregion_predictions_2023/` | None beyond the environment; fully bundled first example |
| [Pairwise pooling heatmaps](../notebooks/analysis/pairwise_pooling_heatmap.ipynb) | Historical BA and pooled scenario metrics | None | None beyond the environment |
| [Monthly MISO event counts](../notebooks/analysis/miso_monthly_event_counts.ipynb) | Historical direct-MISO stress-event catalog | None | None beyond the environment |
| [Satellite and reanalysis context](../notebooks/analysis/plot_satellite_and_reanalysis.ipynb) | None | None | NASA Worldview and NOAA PSL network access |
| [Iowa seasonal risk hours](../notebooks/analysis/state_seasonal_risk_hours.ipynb) | TaiESM1 Iowa scenario metrics | None | None beyond the environment |

The load-duration example deliberately keeps observations flagged by cleaning:
it reads the raw-value column of the existing cleaned files, not their cleaned
load column. Its six bundled prediction CSVs preserve an offline route without
training a model or downloading the historical archive.

## Outputs and example boundaries

Every notebook retains review tables or figures inline. Standalone artifacts
use `notebook_outputs/<category>/<notebook-stem>/`, ignored by Git. Example
outputs do not replace released inputs or reconstruct the entire deposit.

| Notebook | Standalone output and demonstrated extent |
| --- | --- |
| County weather-point selection | Inline only: one Arthur County, Nebraska (FIPS `31005`) centroid and grid matches. The national crosswalk is a separate packaged input. |
| County weather and BA aggregation | One-hour county-weather HDF5 caches and one-hour MISO weather CSV; the Iowa calculation is inline. This CSV does not supply the full-period weather used by TELL. |
| TELL load forecasting | Training/prediction inputs, calibration results, model files, reconstructed MISO load for 2007-2023, held-out 2023 validation CSV, and two diagnostic figures. |
| EIA-860 regridding | One MISO 2024 grid-point CSV. The appendix reads a separately supplied, reviewed subregion mapping workbook; this example does not regrid every BA or the sup3rCC grid. |
| Site CF, weighting, and validation | Site-weather/site-CF HDF5 files, weighted MISO CF CSVs, validation metrics, and a figure using the separate 2022 fleet. The Iowa appendix covers only MISO-contributed Iowa sites. |
| BA scenario metrics | Reconstructed MISO scenario CSV and figure, numerical release comparison, and a one-hour pooling example. The observed-generation check uses the 2022 capacity manifest. |
| Stress-event catalogs | Four complete example-region event CSVs following the toy-to-historical method: `SWPP`, `MISO_8910`, `MISO_SUBREGION_SUM`, and `WECC`. These do not overwrite or regenerate all deposited catalogs. |
| State load generation | TELL staging files, one Iowa year/case reconstruction, and an annual figure of **raw load plus eight GCAM cases**, read from archived 2000-2099 Iowa load. The figure is not an eight-case reconstruction. |
| MISO wind, solar, and load validation | Full-year `miso_2023_loss_sensitivity_metrics.csv` and January figure `miso_20230101_20230131_loss_sensitivity.png`. |
| MISO load-duration curve | `miso_2023_load_duration_curve.png`. |
| Pairwise pooling heatmaps | Ordered-pair metrics CSV and nine heatmap PNGs: four main and five scenario-specific appendix figures. |
| Iowa seasonal risk hours | `iowa_seasonal_risk_hours.csv` with 240 rows and six portfolio PNGs. |
| Remaining five notebooks | Inline only: all-BA load validation, MISO subregion validation, Iowa historical/TaiESM1 validation, monthly MISO events, and satellite/reanalysis context. |

The one-hour weather CSV contains `time_utc`, `temperature_2m`,
`specifichumidity_2m`, `windspeed_10m`, `ghi`, `relativehumidity_2m`, and
`pressure_0m`. The county/state calculations use fixed 2020 population weights.
The state notebook expands `pop_2020` from the existing county population table
into TELL's annual input format; it does not require a second population file.
Its default GCAM case is `rcp85hotter_ssp5`. Switching cases requires changing
both the scenario setting and its explicit input path; the other seven CSVs
are supported alternatives, not inputs to the default run.

Released historical renewable scenarios use the 2024 fleet. The site-generation
and renewable-validation examples use a separate 2022 fleet; their loss
sensitivities do not replace the 2024-fleet products. Complete state CF requires
capacity-weighted contributions from every source BA. The MISO-only Iowa
appendix demonstrates that calculation for a subset, and EIA-930 provides no
state-level renewable actuals for it to validate against.

## Download the datasets

Dataset version `0.1.0` is paired with notebook candidate `v0.1.0`. Its DOI,
[10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870), is reserved for
the Zenodo draft and is registered on publication. See [publication status](#publication-status)
before treating the candidate or DOI as a published release.

Keep these **five files** together in a download folder:

- `wxdata_wtk_bchrrr_nsrdb_2007_2023.zip`
- `wxdata_sup3rcc_taiesm1_curated_2000_2099.zip`
- `README_DATASET.md`
- `LICENSE_DATA.txt`
- `RELEASE_MANIFEST.csv`

The ZIPs total about 9.3 GB. The [release check](#verify-the-release) verifies
them and extracts only its two required inputs, so it does not require a full
extraction. For other notebooks, extract the needed archive from the repository
root (both commands are shown):

```powershell
python -m zipfile -e "C:/path/to/wxdata_wtk_bchrrr_nsrdb_2007_2023.zip" "data"
python -m zipfile -e "C:/path/to/wxdata_sup3rcc_taiesm1_curated_2000_2099.zip" "data"
```

The outer ZIP names are the `0.1.0` names; internal roots remain unchanged. The
climate model is **TaiESM1** and the upstream sup3rCC version is **v0.2.2**.

```text
data/
|-- county_weather/       # county points, BA mapping, population
|-- eia860/               # raw workbooks, mapped sites, validation CF
|-- gcam_usa/             # eight selectable annual demand trajectories
|-- load_actuals/         # raw MISO and cleaned 2023 BA observations
|-- model_parameters/     # SAM settings, weather periods, loss assumptions
|-- renewable_actuals/    # MISO observed wind and solar generation
|-- validation/           # load-validation metadata and predictions
|-- wtk_bchrrr_nsrdb_2007_2023/               # downloaded; ignored by Git
`-- taiesm1_historical_ssp245_v022_2000_2099/  # downloaded; ignored by Git
manifests/                # three bundled metadata CSVs
notebook_outputs/        # local artifacts and caches; ignored by Git
```

After extracting both archives, these commands should each return `True`:

```powershell
Test-Path "data/wtk_bchrrr_nsrdb_2007_2023"
Test-Path "data/taiesm1_historical_ssp245_v022_2000_2099"
```

On Windows, use a short checkout such as `C:/work/wxdata-notebooks`:
descriptive filenames and deeply nested relative paths can exceed Windows path
limits even when files exist. The two release-check notebooks resolve paths
before opening files. Do not force-add extracted archives, acquisition caches,
or `notebook_outputs/` to Git. Keep credentials out of `data/` and source files;
use an ignored `.env` or another untracked credential store.

## Verify the release

Create and activate the environment using the [README instructions](../README.md#install-and-run-the-first-example),
then run from the repository root:

```powershell
python scripts/check_release.py --archive-dir "C:/path/to/zenodo-files"
```

The checker verifies sizes and SHA-256 hashes for both ZIPs and the dataset
README/license against `RELEASE_MANIFEST.csv`, records the manifest hash, and
extracts and verifies only two required data files. It clears saved notebook
outputs and executes fresh kernels using the **active Python interpreter**.
No upstream API access, acquisition caches, or model training is needed.

| Collection and selected input | Notebook | Expected result |
| --- | --- | --- |
| Historical direct-MISO event CSV under `ba_stress_event_catalog/` | [Monthly MISO event counts](../notebooks/analysis/miso_monthly_event_counts.ipynb) | Six scenarios, 2007-2023 coverage, 3,672 monthly grid rows, conserved event counts, and one figure |
| TaiESM1 Iowa scenario Parquet under `state_scenario_metrics/` | [Iowa seasonal risk hours](../notebooks/analysis/state_seasonal_risk_hours.ipynb) | Six scenarios with 876,000 hours each, conserved stress-hour totals, a complete 240-row CSV, and six figures |

Reports, executed notebook copies, and generated outputs go to a new directory
under `notebook_outputs/release_check/`. A failed check returns a nonzero exit
code. Use `--output-dir` to choose a **new, nonexistent directory**; the checker
refuses to reuse one. The report records the notebook commit and dirty-checkout
status, source hashes, manifest hash, environment versions, and results.

After downloading the files from the actual Zenodo draft or published record,
repeat with `--source-kind zenodo`:

```powershell
python scripts/check_release.py --archive-dir "C:/path/to/zenodo-files" --source-kind zenodo --output-dir "C:/path/to/new-release-check"
```

`--source-kind zenodo` is an operator-supplied label. The checker neither
downloads the files nor authenticates their origin. Matching supplied checksums
does not independently establish that origin. This is a **two-notebook
compatibility check**, not validation of all 17 notebooks, every released
product, or scientific correctness. It records the environment but does not
create or test installation of that environment. The unresolved Iowa pressure
difference remains a separate scientific review item.

The initial local check used prepared archives and an existing environment;
its notebook executions took about 4 and 12 seconds, excluding download and
checksum time. Runtime depends on the machine. Keep verified downloads for
repeat checks and use the exact run report as evidence of what was tested.

## Execution notes

To execute a notebook interactively, open it from `notebooks/<category>/` and
select **Restart Kernel and Run All**. Relative paths resolve to `../../data`,
`../../manifests`, and `../../notebook_outputs`. Saved output supports review;
it does not establish that an acquisition or model stage ran in your current
environment. HSDS acquisition, NASA/NOAA retrieval, TELL training, and reV/PySAM
generation require the services and dependencies named in each notebook.
Acquisition cells use local caches only when their checks accept them; otherwise
HSDS access is needed. Consult each notebook's execution/provenance note.

### Recorded verification

The **2026-09-09** record documents fresh-kernel outputs for all 17 notebooks:
14 affected notebooks ran in the follow-up batch, including live county-point
and EIA grid lookups, while three unchanged analysis notebooks retained earlier
verified runs. County aggregation used checked one-hour caches. Site CF was
regenerated for all 844 wind/solar sites from matching legacy weather caches;
hours, site IDs, weights, and shapes were checked, but original source-version
metadata was absent. Those checks do not establish the caches' source version.

That record used Windows, Python 3.10.20, pandas 2.3.3, NumPy 1.24.4, Matplotlib
3.10.9, TELL 1.3.0, reV 0.9.2, PySAM 4.1.0, h5pyd 0.18.0, nbclient 0.11.0,
ipykernel 7.2.0, and HSDS 0.9.4, with local copies of both dataset roots. HTML
rendering used nbconvert 7.17.1 in a separate Python 3.14.4 environment. The
current candidate's [environment.yml](../environment.yml) specifies its numerical
and modeling versions, notebook execution dependencies, and timezone support.

The recorded comparisons preserved validation results, pooling matrices,
event/seasonal results, training data, EIA aggregates, and toy calculations.
Scenario and Iowa load reconstructions passed their archive tolerances; rebuilt
site CF arrays and weighted series matched exactly. All 21 TELL CSVs and four
stress-event CSVs were byte-identical. Reported floating-point differences were
at most 5.7e-13 MW for loss metrics and 8.1e-13 mean-load hours/year for normalized
pooling values. All 17 notebooks rendered. A separate timestamp-parsing fix
restored previously empty observed curves in the BA scenario comparison;
missing observations remained gaps.

The **2026-09-10** style follow-up reused checked inputs and reran selected
deterministic/plotting stages; it did not rerun HSDS acquisition, reV generation,
or TELL training/prediction. These dated records and the initial two-notebook
archive check are distinct evidence. They do not establish a later full rerun,
a fresh installation, or verification of files downloaded from Zenodo.

The **2026-09-19** input consolidation reran the original and revised
load-duration notebook in fresh kernels. All 8,760 raw observations per
subregion, the combined hourly values, and all three plotted traces matched;
the output PNG was byte-identical. The revised run used the six existing
cleaned-file raw columns with the redundant raw files absent, retaining the
six bundled predictions. No model or acquisition stage ran for this check.

## Reading the results

- **Fleets and portfolios:** `Installed 2024` uses each region's own fleet;
  0%, 25%, 50%, 75%, and 100% wind portfolios split fixed combined wind-plus-solar
  **nameplate capacity**, not annual energy. CF is a fraction; adjusted CF times
  assigned capacity gives generation MW. Net load subtracts wind and solar
  generation from load. Direct `MISO` and `MISO_SUBREGION_SUM` are distinct products.
- **Calendars:** historical load/weather include leap days (149,016 UTC hours),
  while historical CF omit February 29 (148,920 hours). Renewable comparisons
  use common no-leap hours; load-only files retain the load calendar. TaiESM1
  has 876,000 hours, or 100 x 8,760. Align timestamps explicitly; see the
  [calendar and fleet reference](BA_COVERAGE.md#calendars-fleets-and-refreshing-the-guide).
- **Stress thresholds:** the historical event method computes load percentiles
  from the load series, and net-load percentiles from the portfolio values
  pooled **within each region**. The 90th, 95th, and 99th net-load thresholds are
  shared across that region's portfolios; this is distinct from pooling regions.
  Renewable-equivalent CF uses absolute 10%, 5%, and 1% cutoffs. The toy example
  uses its own displayed thresholds. Pairwise scenario-specific comparisons
  retain their separately documented thresholds.
- **Risk hours versus events:** risk hours are individual qualifying hours;
  qualifying-row summaries can count the same timestamp under several scenarios
  or thresholds. The catalog bridges runs separated by one non-risk hour,
  includes it in event duration, and records it in `gap_hours`. Monthly MISO
  analysis counts catalog event starts in UTC and uses its recorded thresholds
  and durations. A 12-hour event also qualifies for the 1- and 6-hour panels.
- **Iowa stress:** deposited state catalogs use raw TELL/TaiESM1 load and net load,
  not GCAM-scaled columns. The seasonal notebook also uses raw net load, one P95
  shared across six portfolios and the century, and an absolute 10% equivalent-CF
  cutoff. It counts hours without gap bridging; planning periods use UTC years
  and seasons use `America/Chicago` months. The raw and eight GCAM trajectories
  remain available in the archived state scenario metrics.
- **Validation units:** MAE, RMSE, and bias are MW; NRMSE is RMSE divided by mean
  actual load, a fraction; MAPE is displayed as percent; R² is dimensionless.
  `Timestamp rows` and valid paired `Hours compared` differ when observations
  are missing. TELL internal test statistics, means of four seasonal calibration
  scores, and held-out validation are distinct results, not interchangeable metrics.

Display labels and rounding do not change calculation columns or export schemas.
Input previews retain source headers; result tables state units and preserve
threshold precision and archive-comparison tolerances. Ordinary MW values use
one decimal, CF/NRMSE fractions and R² use three, and MAPE uses two. Hourly and
scenario previews select comparable times without reducing exported results.
Fixed local paths are explicit and messages show complete notebook-relative
paths with forward slashes; raw manifest paths retain their documented basis.

### Known Iowa pressure limitation

The [Iowa historical/TaiESM1 validation](../notebooks/validation/state_historical_taiesm_validation.ipynb)
reports a mean pressure difference of about **-9,369 Pa over 2007-2023**. A check
of staged 2007 source weather reproduced each archived Iowa pressure series
using the same 99 counties and fixed 2020 population weights. The difference
therefore predates the notebook's alignment and aggregation. Its original
source/grid cause remains unresolved. The notebook retains released values and
applies no unsupported correction; passing the release check does not resolve
this limitation.

## Sources and attribution

The historical weather collection covers 2007-2023. sup3rCC/TaiESM1 supplies the
2000-2099 historical and simulated future climate collection. The historical
release has 68 BA-level entries (62 BA codes and six MISO subregions); the
TaiESM1 collection is curated to eight BA-level entries, their MISO pool, and
Iowa. Availability differs by product; the [coverage reference](BA_COVERAGE.md)
distinguishes missing products, zero profiles, modeled fleets, and the
58-entity load-validation set.

| Source or model | Use and companion inputs |
| --- | --- |
| EIA-860 2024 | Operable onshore-wind/PV generators, capacities, and plant locations. Raw plant/generator workbooks and reviewed MISO-subregion mapping support the regridding example and release fleet context. |
| EIA-860 2022 | Separate validation fleet for the 2022 observed-generation comparison and 2023 renewable-loss validation. Bundled point files, validation CF, and capacity manifest retain this distinction. |
| EIA-930 | Historical BA load and observed wind/solar generation. Bundled selected raw/cleaned load and renewable series support validation. |
| 2020 Census Redistricting Data P.L. 94-171 | Block `POP100` values for population-weighted county points; compact Arthur County example and county provenance inputs. |
| TIGER/Line 2020 Blocks | Block internal-point coordinates joined to Census population; compact Arthur County example and county-point provenance. |
| WTK | Wind resource and load weather for 2007-2014; regional products in the historical archive. |
| BC-HRRR | Wind resource and load weather for 2015-2023; regional products in the historical archive. |
| NSRDB | Solar resource and load-weather GHI for 2007-2023; regional products in the historical archive. |
| sup3rCC / TaiESM1 | Climate-adjusted weather/resource inputs for 2000-2099; curated BA, pooled-region, and Iowa products. |
| TELL | Weather-informed load training/prediction and state-load processing; bundled validation and GCAM-scaling inputs. |
| reV and PySAM/SAM | Weather-to-site-CF conversion before nameplate weighting; fixed SAM JSONs and compact validation inputs. |
| GCAM-USA | Eight annual state electricity-demand trajectories. State scaling selects `param == "elecFinalBySecTWh"` and `region == "USA"`; one file is used for the default reconstruction. |
| HSDS | Remote access to gridded NREL weather/resource datasets; large downloaded HDF5 caches are not distributed. |
| Net-load loss assumptions | Scalar wind/solar losses for six portfolios. The historical CSV is bundled; future loss settings are not a separate committed input. |

### Upstream notices

The [repository license](../LICENSE) applies only to Charlie Phillips's
copyrightable contributions to the extent permitted. Inclusion here does not
relicense third-party data or software: upstream terms and attribution
requirements continue to apply.

**U.S. Energy Information Administration.** EIA-860 workbooks and EIA-930-derived
load/renewable files originate with EIA. Its U.S. government publications and
data are public domain, with source acknowledgment recommended; see
[EIA Copyrights and Reuse](https://www.eia.gov/about/copyrights_reuse.php).
Suggested acknowledgment: "Source: U.S. Energy Information Administration,
EIA-860 and EIA-930 data, accessed for this study."

**NREL and U.S. Department of Energy.** Weather-grid mappings, modeled validation
CF, and SAM inputs use NREL data or software. Retain applicable notices, credit
DOE/NREL/Alliance, and consult the
[NREL Disclaimer and Data and Software terms](https://www.nrel.gov/disclaimer.html).

**U.S. Census Bureau.** Population, FIPS, and county-point inputs derive from
2020 Census redistricting and TIGER/Line products. See the
[research transparency policy](https://www.census.gov/topics/research/research-transparency-public-access/policy.html)
and [policies and notices](https://www.census.gov/about/policies.html).

**GCAM-USA.** The eight annual state electricity-demand scenario files are model
outputs. Credit the Joint Global Change Research Institute and consult the
[GCAM-USA documentation](https://github.com/JGCRI/gcam-doc/blob/gh-pages/gcam-usa.md).

## Publication status

Notebook **`v0.1.0` is a release candidate**, paired with dataset **`0.1.0`** of
*Synchronized Wind, Solar, and Load Data for Power System Planning*. Notebook
and dataset versions are independent; the execution report identifies the exact
notebook commit and dataset manifest. A prepared candidate or reserved DOI is
not evidence of publication.

This candidate documents the new outer archive names, a repeatable checksum and
two-notebook check with isolated inputs/fresh kernels, resolved paths in those
two notebooks for Windows compatibility, and the specified numerical/modeling
environment. The documented initial successful check used prepared local
archives and an existing environment. A clean installation and verification of
files downloaded from the actual Zenodo draft are **not established by that
record**. Current run reports should state any later evidence explicitly.

Before publication:

1. Verify a clean checkout in a newly created environment from `environment.yml`.
2. Download the five files from the actual Zenodo draft and repeat the release
   check, retaining its report and environment records.
3. Confirm authorship, author-review statements, citations, license metadata,
   source/model names, coverage, calendars, and scientific limitations,
   including the unresolved Iowa pressure difference.
4. Confirm reciprocal links, the dataset version, and the exact notebook
   tag/commit. Prepare the GitHub release from that tested commit and attach
   the portable execution report and environment records; keep large data in Zenodo.
5. Obtain the author's publication decision and set the actual publication date.
