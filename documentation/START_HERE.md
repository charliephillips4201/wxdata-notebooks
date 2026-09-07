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

See [`NOTEBOOK_INPUTS.md`](NOTEBOOK_INPUTS.md) for per-notebook requirements and
[`../data/README.md`](../data/README.md) for the expected data layout.

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
3. [`ba_state_figure_10_11.ipynb`](../notebooks/analysis/ba_state_figure_10_11.ipynb)
4. [`plot_satellite_and_reanalysis.ipynb`](../notebooks/analysis/plot_satellite_and_reanalysis.ipynb)
5. [`state_seasonal_risk_hours.ipynb`](../notebooks/analysis/state_seasonal_risk_hours.ipynb)

For a visual overview, open [`process_flow.svg`](process_flow.svg) or
[`process_flow_notebooks_only.svg`](process_flow_notebooks_only.svg).

## Execution and outputs

The notebooks retain saved tables and figures so they render on GitHub. To
reproduce a notebook, open it from its category directory and use **Restart
Kernel and Run All**. Relative paths resolve from `notebooks/<category>/` to
`../../data`, `../../manifests`, and `../../notebook_outputs`.

Scratch output files are ignored by Git. HSDS acquisition, NASA/NOAA retrieval,
TELL training, and site-level reV/PySAM reconstruction can require network
access, credentials, or specialist dependencies. Never save credentials in a
notebook.

## Interpretation

Portfolio percentages are shares of combined wind-plus-solar nameplate
capacity, not shares of annual energy. Figure 10/11 thresholds use the 95th
percentile calculated over all hours and all six mixes. Risk hours are
individual qualifying hours; stress-event catalogs apply the documented
grouping and bridge rules.
