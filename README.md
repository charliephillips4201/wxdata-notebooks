# Synchronized Wind, Solar, and Load Data for Power System Planning

## Overview

Power-system planning needs to represent hours when high electricity demand coincides with low wind or solar output. Synchronized weather, demand, and renewable capacity factors preserve these relationships across time and locations. Hourly resolution captures shortfalls and their duration; long records show seasonal and year-to-year variability. Historical and simulated climate collections support complementary investigations of these conditions.

The workflow has two branches: weather becomes modeled electricity demand, while weather and generator fleets become renewable capacity factors. These ingredients feed scenario metrics, geographic pooling, and stress-event catalogs. State products extend the demand calculations to states. Validation assesses model performance and limitations; analysis demonstrates applications of the resulting datasets.

[Dataset preview on Zenodo (unpublished)][zenodo-preview].

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

<a id="bundled-notebook-inputs"></a>

Inputs are in `data_inputs/`; the selected archive inputs in `data_inputs/examples/`
total **457 MB** and require no extraction. The [input manifest](manifests/notebook_inputs.csv)
records their sources, selections, and checksums.

<a id="download-and-extract"></a>
<a id="verify-the-download"></a>

The [Zenodo dataset preview (unpublished)][zenodo-preview] contains two
CSV/Parquet collections, with a README, data license, and checksum manifest.

| Collection | Weather sources | Coverage |
| --- | --- | --- |
| Historical, 2007–2023 | WTK, 2007–2014; BC-HRRR, 2015–2023; NSRDB solar, 2007–2023. | 68 BA-level entities, five pools, and the lower 48 states plus DC. |
| TaiESM1, 2000–2099 | Sup3rCC v0.2.2: historical experiment, 2000–2014; SSP2-4.5, 2015–2099. | AECI, SWPP, six MISO subregions, MISO_SUBREGION_SUM, and Iowa. |

### Coverage

**Historical archive availability:**

| Group | Entities | Modeled load | Wind CF | Solar CF |
| --- | ---: | ---: | ---: | ---: |
| BA codes and MISO subregions | 68 | 60 | 40 | 56 |
| BA pools | 5 | 5 | 5 | 5 |
| Contiguous states and District of Columbia | 49 | 49 | 40 | 48 |

The 68 BA-level entities comprise **62 balancing authority (BA) codes and six
MISO subregions**. Counts describe the full historical archive; modeled-load
availability is separate from observed peaks below. Wind/solar counts exclude
zero profiles: the archive contains 59 BA wind-CF files and 59 BA solar-CF
files, of which 40 and 56 have nonzero profiles. Coverage reflects the modeled
2024 onshore-wind/PV fleet and available mappings, not every physical resource.
In the wind and solar columns, **—** means zero nameplate capacity in the
modeled fleet; the CF file is absent or an all-zero placeholder. Positive
nameplate capacity has a nonzero CF profile.

Wind and solar values are 2024 nameplate capacities; peak load and its timestamp refer to 2019–2022.

BA peaks use EIA-930 hourly demand after quality screening and review,
without interpolation. Pool peaks use synchronized sums of
load-bearing members, retaining only hours when every required member is
valid. In the peak-load columns, **—** means no usable peak or timestamp.
Peak load time is the UTC hour of that maximum; exact ties use the earliest
occurrence before rounding. See the
[supporting peak summary](manifests/dataset_peak_load_summary_2019_2022.csv) for coverage, tie counts, sources,
checksums, and screening settings.

Peaks for `BANC`, `NSB`, `SEC`, `WECC` are best estimates from available
observations after additional review and exclusion of suspect reports.
Original candidates and exclusions are recorded in the supporting summary.

<a id="load--wind--solar-35"></a>
<a id="load--solar-only-16"></a>
<a id="load-only-9"></a>
<a id="wind-and-solar-only-2"></a>
<a id="solar-only-3"></a>
<a id="wind-only-3"></a>

#### Balancing authorities and MISO subregions

| Name | Code | Observed peak load (MW, 2019–2022) | Peak load time (UTC) | Wind nameplate (MW) | Solar nameplate (MW) |
| --- | --- | ---: | --- | ---: | ---: |
| PowerSouth Energy Cooperative | `AEC` | 1,103.0 | 2020-07-16 17:00 | — | — |
| Associated Electric Cooperative, Inc. | `AECI` | 6,228.0 | 2022-12-23 16:00 | 959.4 | 1.5 |
| Avista Corporation | `AVA` | 2,514.0 | 2022-12-22 17:00 | 349.3 | 19.2 |
| Avangrid Renewables LLC | `AVRN` | — | — | 1,695.9 | 322.0 |
| Arizona Public Service Company | `AZPS` | 7,595.0 | 2020-07-31 01:00 | 628.5 | 919.5 |
| Balancing Authority of Northern California | `BANC` | 4,882.0 | 2022-09-07 00:00 | — | 338.6 |
| Bonneville Power Administration | `BPAT` | 11,068.0 | 2022-12-22 17:00 | 3,617.1 | 223.7 |
| Public Utility District No. 1 of Chelan County | `CHPD` | 556.0 | 2022-12-22 17:00 | — | — |
| California Independent System Operator | `CISO` | 51,104.0 | 2022-09-07 01:00 | 6,352.2 | 22,166.7 |
| Duke Energy Progress East | `CPLE` | 12,808.0 | 2022-12-24 11:00 | — | 2,922.5 |
| Duke Energy Progress West | `CPLW` | — | — | — | 28.4 |
| Public Utility District No. 1 of Douglas County | `DOPD` | 517.0 | 2022-12-22 16:00 | — | — |
| Duke Energy Carolinas | `DUK` | 21,265.0 | 2022-06-15 21:00 | — | 2,157.1 |
| El Paso Electric Company | `EPE` | 2,201.0 | 2022-07-20 00:00 | 50.4 | 251.3 |
| Electric Reliability Council of Texas, Inc. | `ERCO` | 79,830.0 | 2022-07-20 22:00 | 38,566.7 | 22,179.5 |
| Florida Municipal Power Pool | `FMPP` | 3,830.0 | 2019-07-31 21:00 | — | 166.9 |
| Duke Energy Florida Inc. | `FPC` | 11,914.0 | 2022-06-23 21:00 | — | 1,936.9 |
| Florida Power & Light Company | `FPL` | 27,283.0 | 2022-08-01 20:00 | — | 7,192.3 |
| Public Utility District No. 2 of Grant County, Washington | `GCPD` | 990.0 | 2022-07-29 23:00 | — | — |
| Gridforce South | `GRIS` | — | — | 324.3 | — |
| Gainesville Regional Utilities | `GVL` | 478.0 | 2021-09-03 22:00 | — | 4.8 |
| NaturEner Power Watch, LLC | `GWA` | — | — | 210.0 | — |
| Hawaiian Electric Co Inc | `HECO` | — | — | — | 319.1 |
| City of Homestead | `HST` | 137.0 | 2020-06-26 19:00 | — | — |
| Imperial Irrigation District | `IID` | 1,133.0 | 2021-08-04 23:00 | — | 543.2 |
| Idaho Power Company | `IPCO` | 4,067.0 | 2021-07-01 01:00 | 714.7 | 580.9 |
| ISO New England Inc. | `ISNE` | 25,101.0 | 2021-06-29 22:00 | 1,510.2 | 3,307.1 |
| JEA | `JEA` | 2,816.0 | 2022-06-23 21:00 | — | 38.1 |
| Los Angeles Department of Water and Power | `LDWP` | 6,286.0 | 2020-08-18 23:00 | 440.5 | 1,317.5 |
| Louisville Gas and Electric Company and Kentucky Utilities Company | `LGEE` | 7,476.0 | 2022-12-23 16:00 | — | 18.1 |
| Midcontinent Independent System Operator, Inc. | `MISO` | 116,600.0 | 2019-07-19 21:00 | 32,150.7 | 13,574.9 |
| MISO subregion 0001 | `MISO_0001` | 16,646.0 | 2022-06-20 23:00 | 9,732.7 | 1,647.6 |
| MISO subregion 0004 | `MISO_0004` | 9,128.0 | 2019-07-19 22:00 | 2,768.8 | 2,467.1 |
| MISO subregion 0006 | `MISO_0006` | 16,610.0 | 2021-08-24 22:00 | 1,441.5 | 1,348.6 |
| MISO subregion 0027 | `MISO_0027` | 31,561.0 | 2022-06-21 22:00 | 4,603.7 | 3,248.9 |
| MISO subregion 0035 | `MISO_0035` | 16,580.0 | 2022-07-05 21:00 | 13,419.5 | 1,069.0 |
| MISO subregion 8910 | `MISO_8910` | 31,548.0 | 2022-06-22 22:00 | 184.5 | 3,793.7 |
| New Brunswick System Operator | `NBSO` | — | — | 42.0 | 17.9 |
| Nevada Power Company | `NEVP` | 9,357.0 | 2021-07-09 23:00 | 150.0 | 3,980.2 |
| New Smyrna Beach Utilities Commission | `NSB` | 105.0 | 2019-07-02 21:00 | — | — |
| NorthWestern Energy | `NWMT` | 2,600.0 | 2021-05-20 09:00 | 763.6 | 179.0 |
| New York Independent System Operator | `NYIS` | 30,919.0 | 2021-06-29 22:00 | 2,739.3 | 2,517.4 |
| PacifiCorp - East | `PACE` | 9,494.0 | 2022-07-19 00:00 | 3,984.8 | 2,196.4 |
| PacifiCorp - West | `PACW` | 4,187.0 | 2021-08-12 21:00 | 489.9 | 477.1 |
| Portland General Electric Company | `PGE` | 4,471.0 | 2021-06-29 00:00 | 716.5 | 189.7 |
| PJM Interconnection, LLC | `PJM` | 152,315.0 | 2019-07-19 22:00 | 11,451.6 | 14,791.3 |
| Public Service Company of New Mexico | `PNM` | 2,787.0 | 2022-07-20 00:00 | 2,569.0 | 1,784.0 |
| Public Service Company of Colorado | `PSCO` | 9,853.0 | 2021-07-29 00:00 | 4,692.3 | 2,116.3 |
| Puget Sound Energy | `PSEI` | 5,431.0 | 2019-02-06 17:00 | 868.4 | 15.5 |
| South Carolina Public Service Authority | `SC` | 5,342.0 | 2022-12-24 14:00 | — | 303.3 |
| Dominion Energy South Carolina | `SCEG` | 4,800.0 | 2022-06-13 21:00 | — | 1,044.1 |
| Seattle City Light | `SCL` | 1,906.0 | 2022-12-22 02:00 | — | — |
| Seminole Electric Cooperative | `SEC` | 1,070.0 | 2020-09-16 21:00 | — | 74.5 |
| Southeastern Power Administration | `SEPA` | — | — | — | 275.0 |
| Southern Company Services, Inc. - Transmission | `SOCO` | 48,073.0 | 2022-06-15 21:00 | — | 5,485.9 |
| Southwestern Power Administration | `SPA` | 154.0 | 2022-06-16 03:00 | 499.0 | 19.5 |
| Salt River Project | `SRP` | 7,714.0 | 2020-07-13 01:00 | 226.0 | 1,674.9 |
| Southwest Power Pool | `SWPP` | 53,016.0 | 2022-07-19 22:00 | 33,803.1 | 869.6 |
| City of Tallahassee | `TAL` | 616.0 | 2019-08-14 20:00 | — | 62.0 |
| Tampa Electric Company | `TEC` | 4,485.0 | 2021-08-18 22:00 | — | 1,356.4 |
| Tucson Electric Power Company | `TEPC` | 4,147.0 | 2020-07-12 00:00 | 379.8 | 492.2 |
| Turlock Irrigation District | `TIDC` | 727.0 | 2022-09-07 01:00 | — | — |
| City of Tacoma Department of Public Utilities Light Division | `TPWR` | 973.0 | 2022-12-22 18:00 | — | — |
| Tennessee Valley Authority | `TVA` | 33,225.0 | 2022-12-24 02:00 | 1.8 | 1,308.8 |
| Western Area Power Administration - Rocky Mountain Region | `WACM` | 4,982.0 | 2022-09-07 00:00 | 1,466.9 | 567.3 |
| Western Area Power Administration - Desert Southwest Region | `WALC` | 2,251.0 | 2020-08-28 00:00 | 350.0 | 340.7 |
| Western Area Power Administration UGP West | `WAUW` | 188.0 | 2021-07-02 21:00 | 71.4 | 80.0 |
| NaturEner Wind Watch, LLC | `WWA` | — | — | 189.0 | — |

All 68 entities have scenario metrics and stress catalogs. Load validation
covers 58 of the 60 load entities; AEC and NSB lack usable packaged actuals.

#### BA pools

Load and CF are included within the pooled scenario-metrics files. All five
historical pools have six scenarios and stress catalogs.

| Name | Code | Observed peak load (MW, 2019–2022) | Peak load time (UTC) | Wind nameplate (MW) | Solar nameplate (MW) |
| --- | --- | ---: | --- | ---: | ---: |
| MISO North/Central aggregate | `MISO_NCA` | 87,910.0 | 2019-07-19 21:00 | 31,966.2 | 9,781.2 |
| MISO South aggregate | `MISO_SA` | 31,548.0 | 2022-06-22 22:00 | 184.5 | 3,793.7 |
| Sum of all six MISO subregions | `MISO_SUBREGION_SUM` | 116,500.0 | 2019-07-19 21:00 | 32,150.7 | 13,574.9 |
| Rest of East pool | `ROE` | 404,728.0 | 2019-07-17 22:00 | 51,006.4 | 45,899.4 |
| Western pool | `WECC` | 143,047.0 | 2022-09-07 01:00 | 31,300.5 | 40,775.9 |

#### Pool membership

| Pool | Member BAs / subregions |
| --- | --- |
| `MISO_NCA` (5) | `MISO_0001`, `MISO_0004`, `MISO_0006`, `MISO_0027`, `MISO_0035` |
| `MISO_SA` (1) | `MISO_8910` |
| `MISO_SUBREGION_SUM` (6) | `MISO_0001`, `MISO_0004`, `MISO_0006`, `MISO_0027`, `MISO_0035`, `MISO_8910` |
| `ROE` (27) | `AEC`, `AECI`, `CPLE`, `DUK`, `FMPP`, `FPC`, `FPL`, `GVL`, `HST`, `ISNE`, `JEA`, `LGEE`, `NSB`, `NYIS`, `PJM`, `SC`, `SCEG`, `SEC`, `SOCO`, `SPA`, `SWPP`, `TAL`, `TEC`, `TVA`, `CPLW`, `NBSO`, `SEPA` |
| `WECC` (32) | `AVA`, `AZPS`, `BANC`, `BPAT`, `CHPD`, `CISO`, `DOPD`, `EPE`, `GCPD`, `IID`, `IPCO`, `LDWP`, `NEVP`, `NWMT`, `PACE`, `PACW`, `PGE`, `PNM`, `PSCO`, `PSEI`, `SCL`, `SRP`, `TEPC`, `TIDC`, `TPWR`, `WACM`, `WALC`, `WAUW`, `AVRN`, `GRIS`, `GWA`, `WWA` |

The MISO pools overlap: MISO_SUBREGION_SUM combines MISO_NCA and MISO_SA.
Do not add these alternative aggregates together. WECC and Rest of East
represent the listed members, not complete geographic censuses.

#### TaiESM1 BA and pool products

The eight TaiESM1 BA/subregion entities have weather, load, wind/solar CF,
six-scenario metrics, and stress catalogs. Only MISO_SUBREGION_SUM is included
as a pool.

#### States and District of Columbia

The full historical release covers the contiguous 48 states and DC; Alaska and
Hawaii are excluded. All 49 entities have load, weather, scenario metrics, and
stress-event catalogs.

Modeled state peaks use **BC-HRRR/NSRDB**-driven `load_mw__raw` during
2019–2022, without GCAM scaling.

| Name | Code | Modeled peak load (MW, 2019–2022) | Peak load time (UTC) | Wind nameplate (MW) | Solar nameplate (MW) |
| --- | --- | ---: | --- | ---: | ---: |
| Alabama | `AL` | 17,369.4 | 2022-06-22 21:00 | — | 666.3 |
| Arizona | `AZ` | 20,796.6 | 2021-06-19 01:00 | 1,234.5 | 5,056.5 |
| Arkansas | `AR` | 8,580.5 | 2022-07-20 22:00 | — | 1,793.7 |
| California | `CA` | 64,776.4 | 2022-09-07 00:00 | 6,487.2 | 21,330.5 |
| Colorado | `CO` | 11,891.2 | 2021-07-28 23:00 | 5,378.8 | 2,371.2 |
| Connecticut | `CT` | 5,509.3 | 2020-07-27 23:00 | 5.0 | 301.0 |
| Delaware | `DE` | 2,166.1 | 2019-07-19 22:00 | 2.0 | 98.1 |
| District of Columbia | `DC` | 1,564.7 | 2019-07-19 22:00 | — | 25.0 |
| Florida | `FL` | 54,315.1 | 2019-06-25 21:00 | — | 10,857.6 |
| Georgia | `GA` | 31,236.9 | 2022-06-22 21:00 | — | 5,015.3 |
| Idaho | `ID` | 5,648.0 | 2021-06-30 00:00 | 1,132.3 | 501.6 |
| Illinois | `IL` | 29,721.6 | 2019-07-19 22:00 | 7,904.4 | 2,953.6 |
| Indiana | `IN` | 20,314.5 | 2021-08-24 22:00 | 3,640.7 | 2,506.2 |
| Iowa | `IA` | 10,287.9 | 2022-07-05 22:00 | 13,016.0 | 677.5 |
| Kansas | `KS` | 8,469.1 | 2022-07-19 22:00 | 9,165.3 | 65.9 |
| Kentucky | `KY` | 17,642.8 | 2021-08-12 21:00 | — | 429.7 |
| Louisiana | `LA` | 10,336.8 | 2022-07-20 22:00 | — | 1,070.4 |
| Maine | `ME` | 2,091.2 | 2020-07-27 23:00 | 1,032.5 | 816.6 |
| Maryland | `MD` | 13,293.0 | 2019-07-19 22:00 | 190.0 | 665.2 |
| Massachusetts | `MA` | 10,677.2 | 2020-07-27 23:00 | 101.6 | 1,441.2 |
| Michigan | `MI` | 21,343.9 | 2022-06-21 23:00 | 3,777.3 | 1,144.1 |
| Minnesota | `MN` | 14,281.9 | 2021-07-28 00:00 | 4,969.6 | 1,650.9 |
| Mississippi | `MS` | 10,456.1 | 2022-06-22 21:00 | 184.5 | 1,219.7 |
| Missouri | `MO` | 19,511.6 | 2022-07-05 22:00 | 2,453.7 | 469.9 |
| Montana | `MT` | 3,544.4 | 2021-07-27 23:00 | 1,897.9 | 179.0 |
| Nebraska | `NE` | 5,718.2 | 2022-07-19 22:00 | 3,462.8 | 137.6 |
| Nevada | `NV` | 8,753.0 | 2021-07-10 01:00 | 150.0 | 5,084.4 |
| New Hampshire | `NH` | 2,116.2 | 2020-07-27 23:00 | 214.1 | 11.5 |
| New Jersey | `NJ` | 21,694.5 | 2020-07-20 21:00 | 9.0 | 1,169.5 |
| New Mexico | `NM` | 4,328.7 | 2022-07-19 23:00 | 4,429.0 | 2,325.4 |
| New York | `NY` | 31,545.6 | 2020-07-27 22:00 | 2,724.3 | 2,668.6 |
| North Carolina | `NC` | 31,399.4 | 2022-12-24 13:00 | 397.0 | 6,727.7 |
| North Dakota | `ND` | 3,810.2 | 2022-07-18 22:00 | 4,529.1 | — |
| Ohio | `OH` | 25,667.5 | 2019-07-19 22:00 | 1,121.8 | 3,243.0 |
| Oklahoma | `OK` | 13,225.0 | 2022-07-19 23:00 | 12,748.9 | 173.5 |
| Oregon | `OR` | 10,942.9 | 2021-06-29 01:00 | 3,858.1 | 1,044.6 |
| Pennsylvania | `PA` | 28,134.1 | 2019-07-19 22:00 | 1,556.0 | 880.5 |
| Rhode Island | `RI` | 1,637.3 | 2020-07-27 23:00 | 48.0 | 415.3 |
| South Carolina | `SC` | 16,216.0 | 2022-12-24 13:00 | — | 1,701.6 |
| South Dakota | `SD` | 4,254.6 | 2022-07-18 22:00 | 3,458.5 | 209.0 |
| Tennessee | `TN` | 19,439.9 | 2022-12-24 13:00 | 1.8 | 593.6 |
| Texas | `TX` | 102,483.6 | 2022-07-20 22:00 | 42,282.9 | 22,465.6 |
| Utah | `UT` | 6,693.8 | 2021-07-08 01:00 | 389.7 | 2,199.2 |
| Vermont | `VT` | 965.5 | 2020-07-27 23:00 | 151.0 | 148.4 |
| Virginia | `VA` | 19,336.9 | 2019-07-19 22:00 | — | 4,690.7 |
| Washington | `WA` | 18,104.1 | 2022-12-22 17:00 | 3,509.6 | 274.4 |
| West Virginia | `WV` | 3,917.7 | 2019-07-19 22:00 | 856.0 | 146.7 |
| Wisconsin | `WI` | 11,668.4 | 2022-06-21 23:00 | 826.4 | 2,111.4 |
| Wyoming | `WY` | 1,103.0 | 2020-08-19 00:00 | 3,727.0 | 242.0 |

For state products, **—** in a wind or solar column means the CF file is absent.
Wind CF is absent for AL, AR, DC, FL, GA, KY, LA, SC, and VA; solar CF is absent for ND.
The other 40 wind and 48 solar profiles are nonzero. These are dataset coverage
limits, not claims about every real-world resource.

The curated TaiESM1 release includes **Iowa only** in all six state product
folders. This repository bundles **selected Iowa state inputs only**, from both
collections; the national historical coverage above requires the full archive.

BA/pool and validation metadata: [BA capacities/scenarios](manifests/ba_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv),
[pool capacities/scenarios](manifests/pooled_region_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv),
and [load-validation membership](data_inputs/validation/load_forecast/ba_2023_validation_metadata.csv).

### GCAM-USA demand cases

The TaiESM1 Iowa load product contains **nine demand trajectories** for
2000-2099: raw TELL load (`load_mw__raw`) and eight GCAM-USA-scaled cases.
The case identifiers preserve the labels in the supporting GCAM source files:

| GCAM source label | SSP3 case | SSP5 case |
| --- | --- | --- |
| RCP4.5, cooler | `rcp45cooler_ssp3` | `rcp45cooler_ssp5` |
| RCP4.5, hotter | `rcp45hotter_ssp3` | `rcp45hotter_ssp5` |
| RCP8.5, cooler | `rcp85cooler_ssp3` | `rcp85cooler_ssp5` |
| RCP8.5, hotter | `rcp85hotter_ssp3` | `rcp85hotter_ssp5` |

GCAM annual state electricity-demand targets (TWh) are interpolated to each
year. One multiplier scales every raw TELL hourly value within that year,
preserving the hourly shape while matching annual energy; hourly load is in MW.
Each case is stored in `load_mw__gcam_<case>`.

These **demand cases** are separate from the **six renewable portfolios** in
`scenario`. All eight retain the same TaiESM1 historical/SSP2-4.5 weather and
wind/solar CF. In the full state scenario product, select one portfolio and one
matching load/net-load case; alternative demand trajectories are not additive.
State stress catalogs and the seasonal-risk notebook use raw load/net load.

The bundled Iowa `state_load/` file includes all nine demand trajectories; the
bundled `state_scenario_metrics/` subset retains only timestamps, renewable
scenario, equivalent renewable CF, and raw net load. Historical state products
have no GCAM demand cases. The supporting GCAM CSVs cover all 50 states and DC,
but the released GCAM-scaled state products cover Iowa only.

The [state-load example](notebooks/data_flow/state_load_generation.ipynb)
reconstructs Iowa in 2039 using `rcp85hotter_ssp5`; its annual comparison reads
all nine archived trajectories.

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
