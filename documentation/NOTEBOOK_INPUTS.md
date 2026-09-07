# Notebook input guide

The GitHub companion contains executed notebooks and only the compact inputs
they read directly. Large hourly products come from Zenodo DOI
[10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870) and are
extracted under `data/`. Paths below are relative to the repository root.

## Input classes

| Class | Location | Distribution |
| --- | --- | --- |
| Curated hourly data | `data/wtk_bchrrr_nsrdb_2007_2023/` and `data/taiesm1_historical_ssp245_v022_2000_2099/` | Zenodo; ignored by Git |
| Compact direct inputs | Selected folders under `data/` | GitHub |
| Analysis metadata | Three files under `manifests/` | GitHub |
| Acquisition caches | County/site-weather and site-CF HDF5 files | Not distributed; recreate or retain locally |
| Generated artifacts | `notebook_outputs/` | Local and ignored by Git |

## Per-notebook requirements

| Notebook | Zenodo data | GitHub inputs | Optional external requirement |
| --- | --- | --- | --- |
| `notebooks/data_flow/county_weather_point_selection.ipynb` | None | `data/county_weather/arthur_county_point_selection_example/` | NREL HSDS for grid lookup |
| `notebooks/data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb` | None | `data/county_weather/` | NREL HSDS to recreate staged county weather |
| `notebooks/data_flow/tell_load_forecast_data_flow.ipynb` | Historical `ba_weather/` and `ba_load/` | `data/load_actuals/raw/`, `data/validation/load_forecast/`, `data/model_parameters/load_weather_source_periods_2007_2023.csv` | TELL for full training and prediction |
| `notebooks/data_flow/eia860_regridding_methodology.ipynb` | None | `data/eia860/2024_raw/` and `data/eia860/2024_regridded_points/` | NREL HSDS to repeat grid lookup |
| `notebooks/data_flow/site_cf_generation_ba_weighting_validation.ipynb` | Historical BA wind and solar CF for comparison | `data/eia860/2022_regridded_points/`, `data/model_parameters/sam/`, `data/renewable_actuals/`, and the capacity manifest | NREL HSDS plus reV/PySAM for site reconstruction |
| `notebooks/data_flow/ba_scenario_metrics_generation.ipynb` | Historical BA load, wind CF, solar CF, BA metrics, and pooled metrics | `data/load_actuals/raw/`, `data/renewable_actuals/`, `data/model_parameters/net_load_loss_assumptions_2007_2023.csv`, and the capacity manifest | None |
| `notebooks/data_flow/ba_stress_event_catalog.ipynb` | Historical BA and pooled scenario metrics | BA and pooled metadata manifests | None |
| `notebooks/data_flow/state_load_generation.ipynb` | Selected 2000–2099 BA load and Iowa state load | `data/county_weather/`, `data/population/`, and `data/gcam_usa/` | TELL for full reconstruction |
| `notebooks/validation/all_ba_2023_load_forecast_validation.ipynb` | Historical BA load | `data/load_actuals/cleaned_2023/` and validation metadata | None |
| `notebooks/validation/miso_subregion_load_forecast_validation.ipynb` | Historical MISO and subregion BA load | `data/load_actuals/cleaned_2023/MISO_cleaned_load_2023.csv` | None |
| `notebooks/validation/miso_wind_solar_load_validation.ipynb` | Historical MISO BA load | `data/eia860/2022_fleet_validation_cf/`, `data/load_actuals/raw/`, `data/renewable_actuals/`, and the capacity manifest | None |
| `notebooks/validation/state_historical_taiesm_validation.ipynb` | Historical and TaiESM1 Iowa weather, load, wind CF, and solar CF | None | None |
| `notebooks/analysis/miso_load_duration_curve.ipynb` | None | MISO files under `data/load_actuals/raw/` and `data/validation/load_forecast/` | None |
| `notebooks/analysis/pairwise_pooling_heatmap.ipynb` | Historical BA scenario metrics | None | None |
| `notebooks/analysis/ba_state_figure_10_11.ipynb` | Historical BA/state scenario metrics and stress-event catalogs | None | None |
| `notebooks/analysis/plot_satellite_and_reanalysis.ipynb` | None | None | NASA Worldview and NOAA PSL network access |
| `notebooks/analysis/state_seasonal_risk_hours.ipynb` | TaiESM1 Iowa scenario metrics | None | None |

The committed input collection contains 101 data files. Files retained only as
intermediate provenance, obsolete-year validation inputs, or unused
configuration were intentionally excluded.
