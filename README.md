# Synchronized Wind, Solar, and Load Data for Power System Planning

## Overview


This repository contains a suite of Jupyter notebooks and their supporting data inputs showing the methods/data flow to create a set of hourly, multi-decadal, synchronized weather, electricity demand (load), wind capacity factor (CF), solar CF, and net load data products. It also shows the verification of these created load/wind CF/solar CF datasets against actuals from EIA datasets, and it shows some analysis products using these created datasets. The goal of this repository is to provide transparency into how these datasets are created and validated so that the user can have confidence when using them in power-system related applications.

The large analysis-ready datasets are available through the [unpublished Zenodo draft preview][zenodo-preview].
Reserved DOI: [10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870) (active after publication).

These datasets are meant to be used for power system modeling applications or analyses that require hourly resolution and spatiotemporal correlation between meteorological variables. Examples include hourly SCUC/SCED modeling and hourly, full sequential Monte Carlo resource adequacy evaluations. The datasets can also be used to identify extreme events as a function of resource mix and quantify the benefit in pooling together BAs with non-coincident net load peaks. Finally, the hourly values can be aggregated into hourly or seasonal capacity factors to maintain computational tractability for long-term expansion planning models.  

The workflow has two branches, the "Load Forecast Process" and the "Wind/Solar CF Process." These are shown below. State load is calculated from BA load outputs; state renewable CF is calculated from state-assigned site profiles across contributing BAs.

**Load and renewable capacity factors**

[![Weather and fleet inputs become BA and state load and renewable capacity factors, with site profiles weighted separately by BA and state.](process_flow_load_and_cf.png)](process_flow_load_and_cf.png)

These outputs are then used to create hourly net load and equivalent renewable CF values (together called "scenario metrics") for 6 different capacity ratios of wind and solar: 0/100, 25/75, 50/50, 75/25, 100/0, and actual EIA-860 mix (based on 2024 EIA-860 data). This gives 6 net load timeseries, 6 renewable CF timeseries, and 1 load timeseries for each BA containing wind CF, solar CF, and load, for a total of 13 "scenario metrics" per BA. BAs missing wind CF (due to no wind generators) or solar CF (due to no solar generators) only have 1 net load timeseries and 1 renewable CF timeseries. 

These "scenario metrics" can similarly be applied for pools of BAs or for states.

Finally, hours at or below a renewable CF threshold, or at or above a load/net-load threshold, are grouped into ‘stress events’ when consecutive or separated by a single non-qualifying hour. Identifying stress events in the renewable CF, net load, and load datasets is critical for correlating historical extreme weather events to instances with high nodal prices in a production cost model or expected unserved energy in a resource adequacy model. This allows modelers to draw a direct link between weather patterns and their impact on the economics and reliability of the power system, and how those impacts vary as a function of resource mix. 


**Scenarios, pooling, and stress events**

[![BA and state load, renewable capacity factors, and nameplate capacity feed scenario metrics and stress-event catalogs, with a separate BA pooling branch.](process_flow_scenarios_and_events.png)](process_flow_scenarios_and_events.png)

Filenames identify the notebooks linked in the index; click a diagram to enlarge it.

<a id="quick-start"></a>
<a id="install-and-run-the-first-example"></a>

To set up the environment and run a bundled-data example, see
[Running the notebooks](RUNNING_NOTEBOOKS.md).

## Notebook index

The notebooks are split into three groups: "data flow," "validation," and "analysis."

The data flow notebooks show the end-to-end process by which the BA-level load and wind/solar CF datasets are created, along with their derivative products (BA scenario metrics, pooled scenario metrics, stress event catalogs, and state load).

The validation notebooks show the BA-level load forecasts and wind/solar generation forecasts (i.e. --> wind/solar CF are multiplied by their nameplate capacities in MW using EIA-860 data) validated against EIA-930 data, and they also show how the historical weather dataset for the state of Iowa (from WTK/BCHRRR for wind energy variables and NSRDB for solar energy variables) compares to the sup3rCC dataset, which is a climate dataset created by using generative AI to downscale daily, low-resolution climate models to hourly, high-resolution datasets adequate for production cost and resource adequacy modeling.

The analysis notebooks show some analysis that can be done from the BA scenario metrics, stress event catalogs, and state load created through the "data flow" pipeline. The examples given show how an hourly, synchronized wind/solar/load dataset can be used to quantify the benefits realized by pooling BAs with different weather regimes/resources mixes, can be used to isolate meteorological patterns that could pose energy adequacy risks, and can be used to identify how risk hours may shift in future climates for a given region. 

Each notebook states its inputs, assumptions, and calculations. Results appear
inline; exported files go to `data_outputs/`.

### Data flow — 9 notebooks

| Notebook | What it demonstrates |
| --- | --- |
| [County weather-point selection](notebooks/data_flow/county_weather_point_selection.ipynb) | Calculate the population-weighted lat/lon for a U.S. county. |
| [County weather and BA aggregation](notebooks/data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb) | Regrid pop-weighted county lat/lon to weather dataset grid id, download weather dataset at grid id, and create population-weighted weather datasets at BA level (ex: MISO) and state level (ex: Iowa). |
| [TELL load forecasting](notebooks/data_flow/tell_load_forecast_data_flow.ipynb) | Create load forecasts from BA-level weather datasets using TELL Python Package. Includes validation of load forecasts against 2023 EIA-930 obs. |
| [EIA-860 regridding](notebooks/data_flow/eia860_regridding_methodology.ipynb) | Identify lat/lon/capacity of solar/wind generators from EIA-860 and regrid those lat/lon to weather dataset grid id. |
| [Site CF, weighting, and validation](notebooks/data_flow/site_cf_generation_ba_weighting_validation.ipynb) | Model and validate MISO wind/solar CF; demonstrate state weighting for MISO-contributed Iowa sites in the appendix (2022 fleet). |
| [BA scenario metrics](notebooks/data_flow/ba_scenario_metrics_generation.ipynb) | Calculate BA-level net load and renewable CF for various wind/solar capacity ratios; Appendix B calculates Iowa state metrics for 2007–2023 with raw and eight GCAM load cases. |
| [Pooled scenario metrics](notebooks/data_flow/pooled_scenario_metrics_generation.ipynb) | Calculate pooled net load and renewable CF for various wind/solar capacity ratios (ex: combine five MISO subregions into MISO_NCA scenario metrics) |
| [Stress-event catalogs](notebooks/data_flow/ba_stress_event_catalog.ipynb) | Identify high-load, high-net-load, and low-renewable events from scenario_metrics dataset. |
| [State load generation](notebooks/data_flow/state_load_generation.ipynb) | Using sup3rCC climate dataset, reconstruct state-level demand (ex: Iowa) and compare raw and GCAM-scaled trajectories through 2099. |

### Validation — 5 notebooks

| Notebook | What it demonstrates |
| --- | --- |
| [BA load-duration curve](notebooks/validation/miso_load_duration_curve.ipynb) | Compare observed and modeled BA (ex: MISO) load-duration curves for 2023. |
| [All-BA 2023 load validation](notebooks/validation/all_ba_2023_load_forecast_validation.ipynb) | Compare 2023 demand forecasts and observations across all available load BAs (58 total). |
| [MISO subregion load validation](notebooks/validation/miso_subregion_load_forecast_validation.ipynb) | Compare direct MISO demand forecasts with the sum of six MISO subregions. |
| [BA wind, solar, and load validation](notebooks/validation/miso_wind_solar_load_validation.ipynb) | Validate simulated BA (ex: MISO) load and renewable output against EIA-930 actuals and compare renewable-loss assumptions. |
| [Iowa historical/TaiESM1 comparison](notebooks/validation/state_historical_taiesm_validation.ipynb) | Compare state (ex: Iowa) historical (WTK/BCHRRR/NSRDB) and TaiESM1 weather, load, and renewable CF. |

### Analysis — 4 notebooks

| Notebook | What it demonstrates |
| --- | --- |
| [Pairwise pooling heatmaps](notebooks/analysis/pairwise_pooling_heatmap.ipynb) | Compare pooling benefits for different ordered BA pairs. |
| [Monthly BA event counts](notebooks/analysis/miso_monthly_event_counts.ipynb) | Summarize & plot BA (ex: MISO) stress events by month and duration. |
| [Satellite and reanalysis context](notebooks/analysis/plot_satellite_and_reanalysis.ipynb) | View NASA/NOAA weather context for a selected stress event. |
| [State seasonal risk hours](notebooks/analysis/state_seasonal_risk_hours.ipynb) | Compare state-level (ex: Iowa) seasonal risk across six portfolios over 2000–2099. |

## Data

### Data file catalog

<a id="bundled-notebook-inputs"></a>

| Folder | Contents and purpose |
|---|---|
| [data_inputs/examples/](data_inputs/examples/) | Selected wxdata products: BA and state-level weather, load, wind/solar capacity factors, scenario metrics, and stress-event results. |
| [data_inputs/eia860/](data_inputs/eia860/) | EIA-860 generator records, weather-grid mappings, and fleet-specific capacity-factor references. |
| [data_inputs/load_actuals/](data_inputs/load_actuals/) and [data_inputs/renewable_actuals/](data_inputs/renewable_actuals/) | Observed EIA-930 electricity demand and wind/solar generation used for model training and validation. |
| [data_inputs/county_weather/](data_inputs/county_weather/) | County populations, county-to-BA service territory mappings, and lat/lon used for county-level weather data downloads. |
| [data_inputs/gcam_usa/](data_inputs/gcam_usa/) | Eight GCAM-USA electricity-demand scenario CSVs used to scale modeled hourly state load to annual demand targets. |
| [data_inputs/model_parameters/](data_inputs/model_parameters/) | SAM wind/solar configurations, loss assumptions, and weather-source selections used in the calculations. |
| [data_inputs/validation/](data_inputs/validation/) | Saved load predictions and BA metadata used by validation notebooks. |
| [manifests/](manifests/) | Sample-file provenance and checksums, fleet capacities, scenario metadata, and peak-load summaries. |
| [data_outputs/](data_outputs/) | Figures, tables, model results, and caches generated locally when notebooks run. |

The `data_inputs/examples/` folder contains **94 precomputed sample files** (86 historical files and 8 TaiESM1 files, totaling approximately **457 MB**)
These totals exclude the other supporting inputs listed above. 

These files are a sample from the full Zenodo dataset. For their coverage,
source paths, notebook consumers, and checksums, see the
[input manifest](manifests/notebook_inputs.csv).

Some notebook stages require additional software or external data access.
See [Running the notebooks](RUNNING_NOTEBOOKS.md) and the requirements stated
in each notebook.

### Full dataset on Zenodo

The [unpublished draft preview on Zenodo][zenodo-preview] provides the full
collections and their detailed `README_DATASET.md`, including regional coverage,
peak loads, nameplate capacities, pool membership, GCAM cases, schemas, and limitations.

- **Historical, 2007–2023:** WTK/BC-HRRR/NSRDB data for BAs, pools, and the lower 48 states plus DC.
- **TaiESM1, 2000–2099:** curated Sup3rCC climate data for selected BAs, MISO_SUBREGION_SUM, and Iowa.

Download and extract full archives **outside this repository**, separate from
the bundled sample directories. Update notebook paths when using the full data;
do not extract archives over the bundled files.

See [Dataset parameters](DATASET_PARAMETERS.md) for BA, state, and pool
capacities, peak loads and dates, and † markers identifying bundled GitHub examples.

### HSDS and external data access

Some data-flow stages use National Lab of Rockies Highly Scalable Data Service **HSDS** to read WTK, NSRDB, BCHRRR, and SUP3RCC data. County-point selection and EIA-860 regridding use it for grid matching; county-weather and site-weather downloads use it when compatible local caches are unavailable.

The notebooks currently expect a local HSDS service at
`http://localhost:5101`, configured to access the `nrel-pds-hsds` bucket.
Creating the Conda environment does not configure or start this service.
Weather caches are not bundled with the repository.

HSDS is not needed to view saved notebook results or run examples that use only
bundled inputs. See [Running the notebooks](RUNNING_NOTEBOOKS.md) for
stage-specific requirements and the relevant notebook cells for connection
settings.

Instructions for setting up a local HSDS server can be found here: https://web.archive.org/web/20250423214155/https://nrel.github.io/rex/misc/examples.hsds.html#setting-up-a-local-hsds-server

## Important notes for using the data

- **Fleet assumptions:** Scenario calculations use a fixed 2024 reference
  fleet; renewable validation uses a separate 2022 fleet. Wind/solar percentages
  describe shares of nameplate capacity. Their shares of generated energy vary
  with weather.

- **Time alignment:** Align hourly data by UTC timestamp. Historical load and
  weather include February 29; renewable capacity factors and combined
  historical scenario metrics omit it. TaiESM1 uses a no-leap calendar and
  supports statistical climate comparisons rather than matching individual
  observed weather events.

- **Pooling:** Regional capacity factors are capacity-weighted. Pooling does
  not simulate transmission or dispatch constraints. Total MISO, its subregions,
  and overlapping pools represent alternative groupings and should not be
  added together.

For detailed portfolio definitions and loss adjustments, see
[scenario calculations](notebooks/data_flow/ba_scenario_metrics_generation.ipynb).
For event thresholds and grouping rules, see
[stress-event catalogs](notebooks/data_flow/ba_stress_event_catalog.ipynb).

## Known limitations

Iowa's TaiESM1 pressure averages approximately **9,369 Pa below the historical
series** over 2007–2023. The upstream cause remains unresolved, and no correction
has been applied. See the
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

AI Disclaimer: OpenAI Codex assisted with writing code and documentation

[zenodo-preview]: https://zenodo.org/records/21844870?preview=1&token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImU1YTZmOTdhLTg1Y2YtNGExMC1hMzdmLTY1NThjMGRjYzg0NyIsImRhdGEiOnt9LCJyYW5kb20iOiI4NThhZTRkYjg5OWNkNjg3MjM1NTBhYjAwYzg2NWU5YiJ9.kYx9A2TU38HVcXgbed38NuUok4_YGhmQ3K7MivkrsoIbPh9I--8NjqIJIjdHz5mhtkUs9elFEc7OdQBQn4bULQ
