# Start here

This repository contains the editable, reviewer-facing notebooks, compact
embedded outputs, documentation, and small supporting inputs. The large
analysis-ready datasets are distributed separately through Zenodo DOI
[10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870).

## Set up the notebooks

1. Clone the repository.
2. From the repository root, run `conda env create -f environment.yml`.
3. Activate the environment with `conda activate wxdata-notebooks`.
4. Download `wxdata_historical_2007_2023.zip` and
   `wxdata_taiesm_curated_2000_2099.zip` from the Zenodo record.
5. Extract both ZIP files into `paper_data/data/`. The GitHub-provided
   `source_inputs/` directory remains beside the two extracted dataset
   directories.
6. Run `jupyter lab paper_data` from the repository root.

See [`NOTEBOOK_INPUTS.md`](NOTEBOOK_INPUTS.md) for the exact input boundary and
[`../data/README.md`](../data/README.md) for the expected extracted layout.

## Recommended route

The curated route contains 17 notebooks: eight data-flow, four validation, and
five analysis notebooks.

### `data_flow/`

Follow these notebooks in order:

1. [`county_weather_point_selection.ipynb`](../data_flow/county_weather_point_selection.ipynb)
   — select representative county weather-grid points.
2. [`county_hsds_download_and_ba_weather_aggregation.ipynb`](../data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb)
   — download county weather, aggregate it to balancing authorities, and show
   the state aggregation extension.
3. [`tell_load_forecast_data_flow.ipynb`](../data_flow/tell_load_forecast_data_flow.ipynb)
   — train, validate, and apply TELL.
4. [`eia860_regridding_methodology.ipynb`](../data_flow/eia860_regridding_methodology.ipynb)
   — map EIA-860 renewable plants to weather grids.
5. [`site_cf_generation_ba_weighting_validation.ipynb`](../data_flow/site_cf_generation_ba_weighting_validation.ipynb)
   — generate site capacity factors, aggregate them to balancing authorities,
   validate them, and demonstrate the EIA-860 2022 MISO-to-Iowa state subset.
6. [`ba_scenario_metrics_generation.ipynb`](../data_flow/ba_scenario_metrics_generation.ipynb)
   — generate and validate six hourly BA wind/solar portfolios and demonstrate
   pooled `MISO_SUBREGION_SUM` aggregation.
7. [`ba_stress_event_catalog.ipynb`](../data_flow/ba_stress_event_catalog.ipynb)
   — calculate percentile ranks, thresholds, risk hours, and grouped stress
   events for individual and pooled regions.
8. [`state_load_generation.ipynb`](../data_flow/state_load_generation.ipynb)
   — create raw Iowa load and eight GCAM-scaled hourly load trajectories.

### `validation/`

1. [`all_ba_2023_load_forecast_validation.ipynb`](../validation/all_ba_2023_load_forecast_validation.ipynb)
   — validate 2023 balancing-authority load forecasts.
2. [`miso_subregion_load_forecast_validation.ipynb`](../validation/miso_subregion_load_forecast_validation.ipynb)
   — validate the six MISO subregion forecasts.
3. [`miso_wind_solar_load_validation.ipynb`](../validation/miso_wind_solar_load_validation.ipynb)
   — compare January 2023 MISO observed and modeled wind, solar, and load using
   the EIA-860 2022 fleet and renewable-loss sensitivities.
4. [`state_historical_taiesm_validation.ipynb`](../validation/state_historical_taiesm_validation.ipynb)
   — compare historical and TaiESM1 Iowa weather, load, wind capacity factor,
   and solar capacity factor.

### `analysis/`

1. [`miso_load_duration_curve.ipynb`](../analysis/miso_load_duration_curve.ipynb)
   — aggregate six MISO subregions and compare observed and modeled 2023
   load-duration curves.
2. [`pairwise_pooling_heatmap.ipynb`](../analysis/pairwise_pooling_heatmap.ipynb)
   — reproduce the pairwise BA pooling heatmaps.
3. [`ba_state_figure_10_11.ipynb`](../analysis/ba_state_figure_10_11.ipynb)
   — reproduce the BA and state stress-risk comparisons.
4. [`plot_satellite_and_reanalysis.ipynb`](../analysis/plot_satellite_and_reanalysis.ipynb)
   — connect the February 2021 event to NASA and NOAA weather context.
5. [`state_seasonal_risk_hours.ipynb`](../analysis/state_seasonal_risk_hours.ipynb)
   — calculate Iowa seasonal risk hours for 2000–2099.

For a visual overview, open [`process_flow.svg`](process_flow.svg) or
[`process_flow_notebooks_only.svg`](process_flow_notebooks_only.svg).

## Reproducing notebook results

The notebooks are saved with compact embedded outputs so GitHub visitors can
review representative tables and figures without rerunning them. To reproduce
an output, open the notebook and use **Restart Kernel and Run All**.

Notebook paths are intentionally relative: `../data`, `../manifests`, and
`../notebook_outputs`. Scratch files under `notebook_outputs/` and generated
category-level `outputs/` directories are ignored by Git and are not part of
the Zenodo data deposit.

The HSDS download, NASA/NOAA weather-context retrieval, TELL training, and
site-level reV/PySAM reconstruction steps can require network access,
credentials, or specialist dependencies. GitHub supporting inputs, Zenodo
analysis-ready data, and compact embedded outputs allow the downstream method
to be inspected without rerunning every acquisition step.

Store credentials only in an ignored `.env` file or another untracked local
credential store. Never enter credentials into a notebook cell that will be
saved or committed.

## Portfolio interpretation

Portfolio percentages are shares of combined wind-plus-solar **nameplate
capacity**, not shares of annual energy. For total capacity `C_total`, hourly
renewable energy is represented as:

```text
E_t = C_total × (wind_share × wind_CF_t + solar_share × solar_CF_t) × 1 hour
```

Figure 10/11 risk thresholds use the 95th percentile calculated over all hours
and all six mixes. Risk hours are individual qualifying hours; event catalogs
add the documented grouping and bridge rules.

## Distribution boundary

The 2007–2023 archive contains the packaged historical BA and state products.
The curated 2000–2099 archive contains AECI, SWPP, the six MISO subregions,
pooled `MISO_SUBREGION_SUM` products, and the Iowa state products documented in
the Zenodo README. Other TaiESM1 regions are outside this curated release.

The public GitHub repository contains methods notebooks and their compact
dependencies. It does not contain the private operational pipeline, production
run configurations, or full generated datasets.
