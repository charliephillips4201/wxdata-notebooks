# Start here

This repository contains 17 editable, executed notebooks, their compact direct
inputs, and supporting documentation. Large analysis-ready datasets are
distributed through Zenodo DOI
[10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870).

## Set up

1. Clone the repository.
2. Run `conda env create -f environment.yml` from the repository root.
3. Activate it with `conda activate wxdata-notebooks`.
4. Download both data archives from Zenodo.
5. Extract both archives into `data/`.
6. Run `jupyter lab notebooks`.

On Windows, choose a short checkout path such as `C:\work\wxdata-notebooks`.
The data filenames are descriptive and can exceed Windows relative-path limits
when the checkout is deeply nested.

See [`NOTEBOOK_INPUTS.md`](NOTEBOOK_INPUTS.md) for per-notebook requirements and
[`../data/README.md`](../data/README.md) for the expected data layout.
The [BA coverage guide](BA_COVERAGE.md) explains entity names, fleet definitions,
missing versus zero products, and the 58-entity validation set.

## Verify the release

The `v0.1.0` notebook candidate is paired with dataset `0.1.0`. Keep the two ZIPs,
dataset README, license, and manifest together in a download folder. After
creating and activating the environment above, run from the repository root:

```powershell
python scripts/check_release.py --archive-dir "C:/path/to/zenodo-files"
```

The checker verifies both ZIPs and the supporting-file checksums, extracts only
its two required inputs, clears saved outputs, and executes fresh kernels using
the active Python interpreter. It writes an execution report and new notebook
outputs under `notebook_outputs/`. A failed check returns a nonzero exit code.

| Collection and input | Notebook | Expected result |
| --- | --- | --- |
| WTK / BC-HRRR / NSRDB direct-MISO event CSV | [Monthly MISO event counts](../notebooks/analysis/miso_monthly_event_counts.ipynb) | Six scenarios, 2007-2023 coverage, 3,672 monthly grid rows, conserved event counts, one figure |
| Sup3rCC / TaiESM1 Iowa scenario Parquet | [Iowa seasonal risk hours](../notebooks/analysis/state_seasonal_risk_hours.ipynb) | Six scenarios with 876,000 hours each, conserved stress-hour totals, a 240-row CSV and six figures |

No upstream API access, model training, or acquisition caches are needed for
these two examples. The two ZIPs total about 9.3 GB; retain verified downloads
for repeat checks. The notebook executions took about 4 and 12 seconds in the
initial local check, excluding downloading and checksum verification; runtime
depends on the machine and environment.

After downloading the files from the actual Zenodo draft or published record,
repeat with `--source-kind zenodo`. That option labels the source you supply;
the checker does not download files or independently establish their origin.
Use `--output-dir` to choose where a new run's report and outputs are retained.

The report records the exact notebook commit, source hashes, manifest hash,
environment versions, and results. Test a clean checkout in a newly created
environment before describing a release as reproducibly installed. The older
17-notebook execution notes below and this two-notebook archive check are
different evidence. Neither establishes scientific correctness of all products.

See [release notes and publication review](RELEASE_v0.1.0.md) for the remaining
review items, including the known Iowa pressure difference.

## Recommended route

### Data flow

1. [`county_weather_point_selection.ipynb`](../notebooks/data_flow/county_weather_point_selection.ipynb)
2. [`county_hsds_download_and_ba_weather_aggregation.ipynb`](../notebooks/data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb)
3. [`tell_load_forecast_data_flow.ipynb`](../notebooks/data_flow/tell_load_forecast_data_flow.ipynb)
4. [`eia860_regridding_methodology.ipynb`](../notebooks/data_flow/eia860_regridding_methodology.ipynb)
5. [`site_cf_generation_ba_weighting_validation.ipynb`](../notebooks/data_flow/site_cf_generation_ba_weighting_validation.ipynb)
6. [`ba_scenario_metrics_generation.ipynb`](../notebooks/data_flow/ba_scenario_metrics_generation.ipynb)
7. [`ba_stress_event_catalog.ipynb`](../notebooks/data_flow/ba_stress_event_catalog.ipynb)
8. [`state_load_generation.ipynb`](../notebooks/data_flow/state_load_generation.ipynb)

### Validation

1. [`all_ba_2023_load_forecast_validation.ipynb`](../notebooks/validation/all_ba_2023_load_forecast_validation.ipynb)
2. [`miso_subregion_load_forecast_validation.ipynb`](../notebooks/validation/miso_subregion_load_forecast_validation.ipynb)
3. [`miso_wind_solar_load_validation.ipynb`](../notebooks/validation/miso_wind_solar_load_validation.ipynb)
4. [`state_historical_taiesm_validation.ipynb`](../notebooks/validation/state_historical_taiesm_validation.ipynb)

### Analysis

1. [`miso_load_duration_curve.ipynb`](../notebooks/analysis/miso_load_duration_curve.ipynb)
2. [`pairwise_pooling_heatmap.ipynb`](../notebooks/analysis/pairwise_pooling_heatmap.ipynb)
3. [`miso_monthly_event_counts.ipynb`](../notebooks/analysis/miso_monthly_event_counts.ipynb)
4. [`plot_satellite_and_reanalysis.ipynb`](../notebooks/analysis/plot_satellite_and_reanalysis.ipynb)
5. [`state_seasonal_risk_hours.ipynb`](../notebooks/analysis/state_seasonal_risk_hours.ipynb)

This order follows the methods. Each notebook reads its stated inputs directly;
small examples are not file-generation prerequisites for later notebooks.

For a visual overview, open [`process_flow.svg`](process_flow.svg) or
[`process_flow_notebooks_only.svg`](process_flow_notebooks_only.svg).

## Execution and outputs

The notebooks retain saved tables and figures so they render on GitHub. To
reproduce a notebook, open it from its category directory and use **Restart
Kernel and Run All**. Relative paths resolve from `notebooks/<category>/` to
`../../data`, `../../manifests`, and `../../notebook_outputs`.

Standalone tables, figures, and working caches go under the ignored
`notebook_outputs/<category>/<notebook>/` directory. Some notebooks have only
inline outputs; the [input/output guide](NOTEBOOK_INPUTS.md) lists both cases.
HSDS acquisition, NASA/NOAA retrieval, TELL training, and reV/PySAM reconstruction
require the services or specialist dependencies named in each notebook. The
acquisition stages require HSDS access when their local caches are absent.
Saved output is review evidence; it is not proof that a stage ran in your current
environment.

### Cleanup verification, 2026-09-09

All 17 notebooks now have verified fresh-kernel outputs. The follow-up batch
reran its 14 affected notebooks, including the county point-selection and EIA-860
live grid lookups after HSDS became available. The three unchanged analysis
notebooks retain their earlier verified outputs. County-weather aggregation used
checked one-hour caches. Site CF generation reran all 844 wind/solar sites from
legacy weather caches whose hours, site IDs, weights, and shapes matched the
requests; their original source-version metadata was absent.

The runs used Windows, Python 3.10.20, pandas 2.3.3, NumPy 1.24.4,
Matplotlib 3.10.9, TELL 1.3.0, reV 0.9.2, PySAM 4.1.0, h5pyd 0.18.0,
nbclient 0.11.0, ipykernel 7.2.0, and HSDS 0.9.4. Inputs were local copies of
`wtk_bchrrr_nsrdb_2007_2023` and
`taiesm1_historical_ssp245_v022_2000_2099`; the
[coverage guide](BA_COVERAGE.md) records the release and fleet definitions.
HTML rendering used nbconvert 7.17.1 in a separate Python 3.14.4 environment.

Before/after comparisons preserved the validation tables, all nine pooling
matrices, event/seasonal results, TELL training data, EIA aggregates, and stress
toy calculations. Reconstructed scenario and Iowa load products passed their
existing archive-comparison tolerances. Rebuilt site CF arrays and weighted
series matched the existing results exactly; loss metrics differed by at most
5.7e-13 MW. Expanding the existing 2020 county population column reproduced the
removed repeated-population CSV exactly, including row order and CSV text.
The follow-up batch reduced pairwise input reads from 66 to 11. Its normalized
heatmap values differ by at most 8.1e-13 mean-load hours/year from floating-point
summation order; raw metrics, hour counts, thresholds, and Iowa seasonal results
remain exact. All 21 TELL CSVs and all four stress-event CSVs are byte-identical.

One comparison error was corrected separately: the BA scenario notebook now
parses observed load and generation timestamps before joining them, restoring
previously empty observed curves. Missing observations remain gaps. The Iowa
pressure discrepancy was traced to staged source weather; its evidence and
unresolved upstream cause are documented beside the
[pressure comparison](../notebooks/validation/state_historical_taiesm_validation.ipynb).
All 17 notebooks rendered successfully; local links, tables, figures, and both
process diagrams were checked.

## Interpretation

Portfolio percentages are shares of combined wind-plus-solar nameplate
capacity, not shares of annual energy. Risk hours are individual qualifying
hours; event counts count the grouped events from the stress catalogs. The
MISO monthly-event notebook uses recorded event starts, threshold values, and
bridge rules from those catalogs. Historical CF and TaiESM1 products omit leap
days; see the [calendar definitions](BA_COVERAGE.md#calendars-fleets-and-refreshing-the-guide)
before combining hourly products.
