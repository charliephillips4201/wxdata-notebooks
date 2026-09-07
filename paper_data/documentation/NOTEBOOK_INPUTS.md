# Notebook input guide

The GitHub companion contains the notebooks and compact supporting inputs. The
large hourly products come from Zenodo DOI
[10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870) and are
extracted under `paper_data/data/`. Paths below are relative to `paper_data/`.

## Input classes

| Class | Location | Distribution |
| --- | --- | --- |
| Curated hourly data | `data/wtk_bchrrr_nsrdb_2007_2023/` and `data/taiesm1_historical_ssp245_v022_2000_2099/` | Zenodo; ignored by Git |
| Compact supporting inputs | selected folders under `data/source_inputs/` | GitHub |
| Analysis metadata | three selected files under `manifests/` | GitHub |
| Acquisition caches | county/site-weather and site-capacity-factor HDF5 files | Not distributed; recreate with the documented online workflow |
| Generated artifacts | `notebook_outputs/` and category-level `outputs/` | Local, reproducible, and ignored by Git |

## Reproduction levels

- **Inspect:** Open any notebook on GitHub to review its narrative, code,
  representative tables, and embedded figures.
- **Rerun downstream analysis:** Install the environment, download the two
  Zenodo archives, and use the GitHub supporting inputs.
- **Recreate acquisition steps:** Supply the required network access,
  credentials, TELL, or NREL specialist dependencies identified below.

## Per-notebook requirements

| Notebook | Zenodo data | GitHub supporting inputs | Optional external requirement |
| --- | --- | --- | --- |
| `data_flow/county_weather_point_selection.ipynb` | None | `data/source_inputs/county_weather_provenance/` | None for the included Arthur County example |
| `data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb` | Historical `ba_weather/` for comparison | `data/source_inputs/county_weather_provenance/` | NREL HSDS access to recreate county weather |
| `data_flow/tell_load_forecast_data_flow.ipynb` | Historical `ba_weather/` and `ba_load/` | `data/source_inputs/load_actuals/`, `data/source_inputs/load_forecast_validation/`, and `data/source_inputs/load_weather_source_periods_2007_2023.csv` | TELL for full training and prediction |
| `data_flow/eia860_regridding_methodology.ipynb` | None | `data/source_inputs/eia860_2024_raw/` and `data/source_inputs/eia860_2024_regridded_points/eia860_2024_operable_miso_subregions.xlsx` | NREL HSDS access to repeat weather-grid lookup |
| `data_flow/site_cf_generation_ba_weighting_validation.ipynb` | Historical BA wind and solar capacity factors for comparison | `data/source_inputs/eia860_2022_regridded_points/`, `data/source_inputs/sam_configs/`, and `manifests/eia860_2022_operable_capacity_manifest.csv` | NREL HSDS plus reV/PySAM to recreate site weather and capacity factors |
| `data_flow/ba_scenario_metrics_generation.ipynb` | Historical BA load, wind CF, solar CF, scenario metrics, and pooled scenario metrics | `data/source_inputs/load_actuals/`, `data/source_inputs/renewable_actuals/`, `data/source_inputs/net_load_loss_assumptions/`, and `manifests/eia860_2022_operable_capacity_manifest.csv` | None |
| `data_flow/ba_stress_event_catalog.ipynb` | Historical BA and pooled scenario metrics | `manifests/ba_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv` and `manifests/pooled_region_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv` | None |
| `data_flow/state_load_generation.ipynb` | Selected 2000–2099 BA load and Iowa state load | `data/source_inputs/county_weather_provenance/`, `data/source_inputs/population/`, and `data/source_inputs/gcam_usa/` | TELL for full re-execution |
| `validation/all_ba_2023_load_forecast_validation.ipynb` | Historical BA load | `data/source_inputs/load_actuals_cleaned_2023/` and `data/source_inputs/load_forecast_validation/ba_2023_validation_metadata.csv` | None |
| `validation/miso_subregion_load_forecast_validation.ipynb` | Historical MISO and MISO-subregion BA load | `data/source_inputs/load_actuals_cleaned_2023/MISO_cleaned_load_2023.csv` | None |
| `validation/miso_wind_solar_load_validation.ipynb` | Historical MISO BA load | `data/source_inputs/eia860_2022_validation_cf/`, `data/source_inputs/load_actuals/`, `data/source_inputs/renewable_actuals/`, and `manifests/eia860_2022_operable_capacity_manifest.csv` | None |
| `validation/state_historical_taiesm_validation.ipynb` | Historical and TaiESM1 Iowa state weather, load, wind CF, and solar CF | None | None |
| `analysis/miso_load_duration_curve.ipynb` | None | MISO files under `data/source_inputs/load_actuals/` and `data/source_inputs/load_forecast_validation/` | None |
| `analysis/pairwise_pooling_heatmap.ipynb` | Historical BA scenario metrics | None | None |
| `analysis/ba_state_figure_10_11.ipynb` | Historical BA/state scenario metrics and stress-event catalogs | None | None |
| `analysis/plot_satellite_and_reanalysis.ipynb` | None | None | NASA Worldview and NOAA PSL network access; compact images remain embedded for inspection |
| `analysis/state_seasonal_risk_hours.ipynb` | TaiESM1 Iowa state scenario metrics | None | None |

The supporting-input allowlist contains 113 files totaling about 66 MB; its
largest file is approximately 10.3 MB. Large HDF5 files are excluded because
they are acquisition caches rather than analysis-ready inputs, and several
exceed GitHub's ordinary per-file limit.
