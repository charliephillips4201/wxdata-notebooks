# Synchronized Wind, Solar, and Load Data for Power System Planning

## Overview

These 18 notebooks explain and evaluate synchronized hourly weather, modeled
electricity demand, and wind and solar capacity factors (CF) for power-system
planning. They show how these inputs produce renewable scenarios, net-load
time series, and stress-event catalogs. Saved tables and figures can be read
directly on GitHub.

![Weather and fleet inputs feed load and renewable models, scenario metrics, validation, and analysis.](process_flow.svg)

**Suggested review order:**

1. [Weather motivation](notebooks/analysis/plot_satellite_and_reanalysis.ipynb).
2. [Balancing authority (BA) scenarios](notebooks/data_flow/ba_scenario_metrics_generation.ipynb) and [MISO_NCA pooling](notebooks/data_flow/pooled_scenario_metrics_generation.ipynb).
3. [Stress-event catalogs](notebooks/data_flow/ba_stress_event_catalog.ipynb).
4. [MISO wind, solar, and load validation](notebooks/validation/miso_wind_solar_load_validation.ipynb) and [subregion validation](notebooks/validation/miso_subregion_load_forecast_validation.ipynb).
5. [Monthly stress events](notebooks/analysis/miso_monthly_event_counts.ipynb) and [pairwise pooling](notebooks/analysis/pairwise_pooling_heatmap.ipynb).

[Quick start](#quick-start) · [All notebooks](#notebook-index) · [Data and coverage](#data) · [Interpretation](#interpretation) · [Citation](#sources-and-citation)

<a id="install-and-run-the-first-example"></a>

## Quick start

To rerun the examples, install Git and Conda. On Windows, use a short parent
folder such as `C:/work`.

```powershell
git clone https://github.com/charliephillips4201/wxdata-notebooks.git
cd wxdata-notebooks
conda env create -f environment.yml
conda activate wxdata-notebooks
jupyter lab notebooks/validation/miso_load_duration_curve.ipynb
```

Select **Restart Kernel and Run All**. Each notebook reads its own inputs;
run from its notebook directory. Default data examples use bundled files.
External-service requirements are listed below.

## Notebook index

Each notebook states its inputs, assumptions, and calculations. Results appear
inline; exported files go to `data_outputs/`.

### Data flow — 9 notebooks

| Notebook | Inputs / requirements | Outputs |
| --- | --- | --- |
| [County weather-point selection](notebooks/data_flow/county_weather_point_selection.ipynb) | Arthur County Census inputs; HSDS. | Population-weighted point and weather-grid IDs. |
| [County weather and BA aggregation](notebooks/data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb) | County mappings/population; HSDS if uncached. | One-hour MISO weather and Iowa aggregation example. |
| [TELL load forecasting](notebooks/data_flow/tell_load_forecast_data_flow.ipynb) | MISO weather/load; TELL. | Model training, forecasts, and held-out 2023 validation. |
| [EIA-860 regridding](notebooks/data_flow/eia860_regridding_methodology.ipynb) | 2024 fleet/mapping; HSDS. | MISO renewable-site grid assignments. |
| [Site CF, weighting, and validation](notebooks/data_flow/site_cf_generation_ba_weighting_validation.ipynb) | 2022 fleet/actuals; reV/PySAM; HSDS if uncached. | Site and weighted MISO CF; validation. |
| [BA scenario metrics](notebooks/data_flow/ba_scenario_metrics_generation.ipynb) | MISO load/CF and capacity metadata. | Six scenarios and full archive comparison. |
| [Pooled scenario metrics](notebooks/data_flow/pooled_scenario_metrics_generation.ipynb) | Five MISO subregions and capacity metadata. | MISO_NCA scenarios and full archive comparison. |
| [Stress-event catalogs](notebooks/data_flow/ba_stress_event_catalog.ipynb) | BA/pool scenarios. | Toy example and four regional event catalogs. |
| [State load generation](notebooks/data_flow/state_load_generation.ipynb) | TaiESM1 BA/Iowa load and GCAM inputs; TELL. | Iowa year/case reconstruction and archived trajectories. |

### Validation — 5 notebooks

| Notebook | Inputs / requirements | Outputs |
| --- | --- | --- |
| [MISO load-duration curve](notebooks/validation/miso_load_duration_curve.ipynb) | Subregion observations and forecasts. | 2023 load-duration comparison. |
| [All-BA 2023 load validation](notebooks/validation/all_ba_2023_load_forecast_validation.ipynb) | Forecasts/observations for 58 entities. | Coverage, error metrics, and scatter plots. |
| [MISO subregion load validation](notebooks/validation/miso_subregion_load_forecast_validation.ipynb) | Direct MISO and six subregion forecasts; actuals. | Direct-versus-summed load comparison. |
| [MISO wind, solar, and load validation](notebooks/validation/miso_wind_solar_load_validation.ipynb) | MISO load, 2022 renewable fleet, and actuals. | Full-year loss sensitivity and January comparison. |
| [Iowa historical/TaiESM1 comparison](notebooks/validation/state_historical_taiesm_validation.ipynb) | Iowa weather, load, and CF from both collections. | Distributions, diagnostics, and pressure limitation. |

### Analysis — 4 notebooks

| Notebook | Inputs / requirements | Outputs |
| --- | --- | --- |
| [Pairwise pooling heatmaps](notebooks/analysis/pairwise_pooling_heatmap.ipynb) | Scenarios for 10 BAs and MISO_SUBREGION_SUM. | 110 ordered-pair comparisons and heatmaps. |
| [Monthly MISO event counts](notebooks/analysis/miso_monthly_event_counts.ipynb) | Historical MISO event catalog. | Event frequency by month and duration. |
| [Satellite and reanalysis context](notebooks/analysis/plot_satellite_and_reanalysis.ipynb) | NASA Worldview and NOAA PSL access. | Weather context images. |
| [Iowa seasonal risk hours](notebooks/analysis/state_seasonal_risk_hours.ipynb) | TaiESM1 Iowa scenarios, 2000–2099. | Seasonal risk hours across six portfolios. |

## Data

<a id="bundled-notebook-inputs"></a>

Inputs are in `data_inputs/`; the selected archive inputs in `data_inputs/examples/`
total **457 MB** and require no extraction. The [input manifest](manifests/notebook_inputs.csv)
records their sources, selections, and checksums.

<a id="download-and-extract"></a>
<a id="verify-the-download"></a>

The full [Zenodo dataset](https://doi.org/10.5281/zenodo.21844870) contains two
CSV/Parquet collections, with a README, data license, and checksum manifest.

| Collection | Weather sources and period | Coverage |
| --- | --- | --- |
| Historical, 2007–2023 | WTK, 2007–2014; BC-HRRR, 2015–2023; NSRDB solar, 2007–2023. | 68 BA-level entities, five pools, and the lower 48 states plus DC. |
| TaiESM1, 2000–2099 | Sup3rCC v0.2.2: historical experiment, 2000–2014; SSP2-4.5, 2015–2099. | AECI, SWPP, six MISO subregions, MISO_SUBREGION_SUM, and Iowa. |

### Coverage

**Historical archive availability:**

| Entity group | Entities | Load | Wind CF | Solar CF |
| --- | ---: | ---: | ---: | ---: |
| BA codes and MISO subregions | 68 | 60 | 40 | 56 |
| BA pools | 5 | 5 | 5 | 5 |
| Contiguous states and District of Columbia | 49 | 49 | 40 | 48 |

The 68 BA-level entities comprise **62 BA codes and six MISO subregions**.
Wind/solar counts include only nonzero profiles. Coverage reflects the modeled
2024 onshore-wind/PV fleet and available mappings, not every physical resource.
Pool load and CF are columns within pooled scenario metrics.

Below, wind/solar cells give nameplate MW and CF status. **Zero** means an
all-zero placeholder, not a usable counterfactual profile; **absent** means no
CF file. The validation column refers only to the 2023 load comparison:
58 of the 60 load entities participate; AEC and NSB lack usable packaged actuals.
Every listed entity has scenario metrics and a stress catalog.

#### Load + wind + solar (35)

| Entity | Release name | Wind MW / CF | Solar MW / CF | Weather / load files | Scenarios | 2023 load validation |
| --- | --- | --- | --- | --- | --- | --- |
| `AECI` | Associated Electric Cooperative, Inc. | 959.4 / nonzero | 1.5 / nonzero | yes / yes | 6 | yes |
| `AVA` | Avista Corporation | 349.3 / nonzero | 19.2 / nonzero | yes / yes | 6 | yes |
| `AZPS` | Arizona Public Service Company | 628.5 / nonzero | 919.5 / nonzero | yes / yes | 6 | yes |
| `BPAT` | Bonneville Power Administration | 3,617.1 / nonzero | 223.7 / nonzero | yes / yes | 6 | yes |
| `CISO` | California Independent System Operator | 6,352.2 / nonzero | 22,166.7 / nonzero | yes / yes | 6 | yes |
| `EPE` | El Paso Electric Company | 50.4 / nonzero | 251.3 / nonzero | yes / yes | 6 | yes |
| `ERCO` | Electric Reliability Council of Texas, Inc. | 38,566.7 / nonzero | 22,179.5 / nonzero | yes / yes | 6 | yes |
| `IPCO` | Idaho Power Company | 714.7 / nonzero | 580.9 / nonzero | yes / yes | 6 | yes |
| `ISNE` | ISO New England Inc. | 1,510.2 / nonzero | 3,307.1 / nonzero | yes / yes | 6 | yes |
| `LDWP` | Los Angeles Department of Water and Power | 440.5 / nonzero | 1,317.5 / nonzero | yes / yes | 6 | yes |
| `MISO` | Midcontinent Independent System Operator, Inc. | 32,150.7 / nonzero | 13,574.9 / nonzero | yes / yes | 6 | yes |
| `MISO_0001` | MISO subregion 0001 | 9,732.7 / nonzero | 1,647.6 / nonzero | yes / yes | 6 | yes |
| `MISO_0004` | MISO subregion 0004 | 2,768.8 / nonzero | 2,467.1 / nonzero | yes / yes | 6 | yes |
| `MISO_0006` | MISO subregion 0006 | 1,441.5 / nonzero | 1,348.6 / nonzero | yes / yes | 6 | yes |
| `MISO_0027` | MISO subregion 0027 | 4,603.7 / nonzero | 3,248.9 / nonzero | yes / yes | 6 | yes |
| `MISO_0035` | MISO subregion 0035 | 13,419.5 / nonzero | 1,069.0 / nonzero | yes / yes | 6 | yes |
| `MISO_8910` | MISO subregion 8910 | 184.5 / nonzero | 3,793.7 / nonzero | yes / yes | 6 | yes |
| `NEVP` | Nevada Power Company | 150.0 / nonzero | 3,980.2 / nonzero | yes / yes | 6 | yes |
| `NWMT` | NorthWestern Energy | 763.6 / nonzero | 179.0 / nonzero | yes / yes | 6 | yes |
| `NYIS` | New York Independent System Operator | 2,739.3 / nonzero | 2,517.4 / nonzero | yes / yes | 6 | yes |
| `PACE` | PacifiCorp - East | 3,984.8 / nonzero | 2,196.4 / nonzero | yes / yes | 6 | yes |
| `PACW` | PacifiCorp - West | 489.9 / nonzero | 477.1 / nonzero | yes / yes | 6 | yes |
| `PGE` | Portland General Electric Company | 716.5 / nonzero | 189.7 / nonzero | yes / yes | 6 | yes |
| `PJM` | PJM Interconnection, LLC | 11,451.6 / nonzero | 14,791.3 / nonzero | yes / yes | 6 | yes |
| `PNM` | Public Service Company of New Mexico | 2,569.0 / nonzero | 1,784.0 / nonzero | yes / yes | 6 | yes |
| `PSCO` | Public Service Company of Colorado | 4,692.3 / nonzero | 2,116.3 / nonzero | yes / yes | 6 | yes |
| `PSEI` | Puget Sound Energy | 868.4 / nonzero | 15.5 / nonzero | yes / yes | 6 | yes |
| `SPA` | Southwestern Power Administration | 499.0 / nonzero | 19.5 / nonzero | yes / yes | 6 | yes |
| `SRP` | Salt River Project | 226.0 / nonzero | 1,674.9 / nonzero | yes / yes | 6 | yes |
| `SWPP` | Southwest Power Pool | 33,803.1 / nonzero | 869.6 / nonzero | yes / yes | 6 | yes |
| `TEPC` | Tucson Electric Power Company | 379.8 / nonzero | 492.2 / nonzero | yes / yes | 6 | yes |
| `TVA` | Tennessee Valley Authority | 1.8 / nonzero | 1,308.8 / nonzero | yes / yes | 6 | yes |
| `WACM` | Western Area Power Administration - Rocky Mountain Region | 1,466.9 / nonzero | 567.3 / nonzero | yes / yes | 6 | yes |
| `WALC` | Western Area Power Administration - Desert Southwest Region | 350.0 / nonzero | 340.7 / nonzero | yes / yes | 6 | yes |
| `WAUW` | Western Area Power Administration UGP West | 71.4 / nonzero | 80.0 / nonzero | yes / yes | 6 | yes |

#### Load + solar only (16)

| Entity | Release name | Wind MW / CF | Solar MW / CF | Weather / load files | Scenarios | 2023 load validation |
| --- | --- | --- | --- | --- | --- | --- |
| `BANC` | Balancing Authority of Northern California | 0.0 / zero | 338.6 / nonzero | yes / yes | 2 | yes |
| `CPLE` | Duke Energy Progress East | 0.0 / zero | 2,922.5 / nonzero | yes / yes | 2 | yes |
| `DUK` | Duke Energy Carolinas | 0.0 / zero | 2,157.1 / nonzero | yes / yes | 2 | yes |
| `FMPP` | Florida Municipal Power Pool | 0.0 / zero | 166.9 / nonzero | yes / yes | 2 | yes |
| `FPC` | Duke Energy Florida Inc. | 0.0 / zero | 1,936.9 / nonzero | yes / yes | 2 | yes |
| `FPL` | Florida Power & Light Company | 0.0 / zero | 7,192.3 / nonzero | yes / yes | 2 | yes |
| `GVL` | Gainesville Regional Utilities | 0.0 / zero | 4.8 / nonzero | yes / yes | 2 | yes |
| `IID` | Imperial Irrigation District | 0.0 / zero | 543.2 / nonzero | yes / yes | 2 | yes |
| `JEA` | JEA | 0.0 / zero | 38.1 / nonzero | yes / yes | 2 | yes |
| `LGEE` | Louisville Gas and Electric Company and Kentucky Utilities Company | 0.0 / zero | 18.1 / nonzero | yes / yes | 2 | yes |
| `SC` | South Carolina Public Service Authority | 0.0 / zero | 303.3 / nonzero | yes / yes | 2 | yes |
| `SCEG` | Dominion Energy South Carolina | 0.0 / zero | 1,044.1 / nonzero | yes / yes | 2 | yes |
| `SEC` | Seminole Electric Cooperative | 0.0 / zero | 74.5 / nonzero | yes / yes | 2 | yes |
| `SOCO` | Southern Company Services, Inc. - Transmission | 0.0 / zero | 5,485.9 / nonzero | yes / yes | 2 | yes |
| `TAL` | City of Tallahassee | 0.0 / zero | 62.0 / nonzero | yes / yes | 2 | yes |
| `TEC` | Tampa Electric Company | 0.0 / zero | 1,356.4 / nonzero | yes / yes | 2 | yes |

#### Load only (9)

| Entity | Release name | Wind MW / CF | Solar MW / CF | Weather / load files | Scenarios | 2023 load validation |
| --- | --- | --- | --- | --- | --- | --- |
| `AEC` | PowerSouth Energy Cooperative | 0.0 / absent | 0.0 / absent | yes / yes | 1 | no |
| `CHPD` | Public Utility District No. 1 of Chelan County | 0.0 / absent | 0.0 / absent | yes / yes | 1 | yes |
| `DOPD` | Public Utility District No. 1 of Douglas County | 0.0 / absent | 0.0 / absent | yes / yes | 1 | yes |
| `GCPD` | Public Utility District No. 2 of Grant County, Washington | 0.0 / absent | 0.0 / absent | yes / yes | 1 | yes |
| `HST` | City of Homestead | 0.0 / absent | 0.0 / absent | yes / yes | 1 | yes |
| `NSB` | New Smyrna Beach Utilities Commission | 0.0 / absent | 0.0 / absent | yes / yes | 1 | no |
| `SCL` | Seattle City Light | 0.0 / absent | 0.0 / absent | yes / yes | 1 | yes |
| `TIDC` | Turlock Irrigation District | 0.0 / absent | 0.0 / absent | yes / yes | 1 | yes |
| `TPWR` | City of Tacoma Department of Public Utilities Light Division | 0.0 / absent | 0.0 / absent | yes / yes | 1 | yes |

#### Wind and solar only (2)

| Entity | Release name | Wind MW / CF | Solar MW / CF | Weather / load files | Scenarios | 2023 load validation |
| --- | --- | --- | --- | --- | --- | --- |
| `AVRN` | Avangrid Renewables LLC | 1,695.9 / nonzero | 322.0 / nonzero | no / no | 6 | no |
| `NBSO` | New Brunswick System Operator | 42.0 / nonzero | 17.9 / nonzero | yes / no | 6 | no |

#### Solar only (3)

| Entity | Release name | Wind MW / CF | Solar MW / CF | Weather / load files | Scenarios | 2023 load validation |
| --- | --- | --- | --- | --- | --- | --- |
| `CPLW` | Duke Energy Progress West | 0.0 / zero | 28.4 / nonzero | no / no | 2 | no |
| `HECO` | Hawaiian Electric Co Inc | 0.0 / zero | 319.1 / nonzero | yes / no | 2 | no |
| `SEPA` | Southeastern Power Administration | 0.0 / zero | 275.0 / nonzero | yes / no | 2 | no |

#### Wind only (3)

| Entity | Release name | Wind MW / CF | Solar MW / CF | Weather / load files | Scenarios | 2023 load validation |
| --- | --- | --- | --- | --- | --- | --- |
| `GRIS` | Gridforce South | 324.3 / nonzero | 0.0 / zero | no / no | 2 | no |
| `GWA` | NaturEner Power Watch, LLC | 210.0 / nonzero | 0.0 / zero | no / no | 2 | no |
| `WWA` | NaturEner Wind Watch, LLC | 189.0 / nonzero | 0.0 / zero | no / no | 2 | no |

<details>
<summary>Pooled regions: membership and capacity</summary>

All five historical pools contain load, wind CF, and solar CF within six-scenario
metrics, plus stress catalogs. WECC and Rest of East use the member lists below.

| Pool | Definition | Wind MW | Solar MW | Members |
| --- | --- | --- | --- | --- |
| `MISO_SUBREGION_SUM` | Sum of all six MISO subregions | 32,150.7 | 13,574.9 | `MISO_0001`, `MISO_0004`, `MISO_0006`, `MISO_0027`, `MISO_0035`, `MISO_8910` |
| `MISO_NCA` | MISO North/Central aggregate | 31,966.2 | 9,781.2 | `MISO_0001`, `MISO_0004`, `MISO_0006`, `MISO_0027`, `MISO_0035` |
| `MISO_SA` | MISO South aggregate | 184.5 | 3,793.7 | `MISO_8910` |
| `WECC` | Western pool | 31,300.5 | 40,775.9 | `AVA`, `AZPS`, `BANC`, `BPAT`, `CHPD`, `CISO`, `DOPD`, `EPE`, `GCPD`, `IID`, `IPCO`, `LDWP`, `NEVP`, `NWMT`, `PACE`, `PACW`, `PGE`, `PNM`, `PSCO`, `PSEI`, `SCL`, `SRP`, `TEPC`, `TIDC`, `TPWR`, `WACM`, `WALC`, `WAUW`, `AVRN`, `GRIS`, `GWA`, `WWA` |
| `ROE` | Rest of East pool | 51,006.4 | 45,899.4 | `AEC`, `AECI`, `CPLE`, `DUK`, `FMPP`, `FPC`, `FPL`, `GVL`, `HST`, `ISNE`, `JEA`, `LGEE`, `NSB`, `NYIS`, `PJM`, `SC`, `SCEG`, `SEC`, `SOCO`, `SPA`, `SWPP`, `TAL`, `TEC`, `TVA`, `CPLW`, `NBSO`, `SEPA` |

The MISO pools overlap: MISO_SUBREGION_SUM combines MISO_NCA and MISO_SA.
Do not add these alternative aggregates together.

</details>

<details>
<summary>TaiESM1 and state products</summary>

The eight TaiESM1 BA/subregion entities have weather, load, wind/solar CF,
six-scenario metrics, and stress catalogs. Only MISO_SUBREGION_SUM is included
as a pool, and only Iowa as a state. Iowa includes raw TELL load plus eight
GCAM-USA demand pathways; those pathways change demand, not climate or CF.
State stress catalogs use raw TELL load.

</details>

Coverage metadata: [BA capacities/scenarios](manifests/ba_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv),
[pool capacities/scenarios](manifests/pooled_region_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv),
and [load-validation membership](data_inputs/validation/load_forecast/ba_2023_validation_metadata.csv).

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

Cite the [Zenodo dataset](https://doi.org/10.5281/zenodo.21844870) and use
[CITATION.cff](CITATION.cff) for the notebooks. Original notebooks and documentation
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
