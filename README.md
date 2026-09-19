# Synchronized Wind, Solar, and Load Data for Power System Planning

## Overview

These 17 Jupyter notebooks explain how weather, electricity demand, and wind
and solar resources are combined to study net load, resource sharing, and
stress events. Read the saved tables and figures on GitHub, or run the
examples locally. The first example uses only bundled data.

A **balancing authority (BA)** manages electricity supply and demand in a
region. **Capacity factor (CF)** is output divided by nameplate capacity;
**net load** is demand minus wind and solar generation. **MISO** is the
Midcontinent Independent System Operator.

[Quick start](#quick-start) · [Notebook index](#notebook-index) ·
[Data](#data) · [Interpretation](#interpretation) · [Sources and citation](#sources-and-citation)

![Weather and fleet inputs feed load and renewable models, scenario metrics, validation, and analysis.](process_flow.svg)

These are method relationships. Each notebook reads its stated inputs;
running one worked example does not generate all inputs for the next.

<a id="install-and-run-the-first-example"></a>

## Quick start

With Git and Conda installed, start in a short parent folder, such as
`C:/work` on Windows, to avoid path-length problems.

1. Clone the repository and enter its folder:

   ```powershell
   git clone https://github.com/charliephillips4201/wxdata-notebooks.git
   cd wxdata-notebooks
   ```

2. Create and activate the environment:

   ```powershell
   conda env create -f environment.yml
   conda activate wxdata-notebooks
   ```

3. Open the first example:

   ```powershell
   jupyter lab notebooks/analysis/miso_load_duration_curve.ipynb
   ```

4. Select **Restart Kernel and Run All**. The notebook checks 8,760 hours,
   displays a load-duration figure, and saves
   `data_outputs/analysis/miso_load_duration_curve/miso_2023_load_duration_curve.png`.

Choose another example from the index below. Run its cells from top to bottom;
the notebook folder is the working directory for its relative paths. Saved
outputs support reading without installation, but rerunning requires the listed
inputs and services.

## Notebook index

The repository includes **94 supporting data files and three manifests**.
In the tables, **bundled** means included here; **historical** and **TaiESM1**
refer to the two [downloadable collections](#data). All examples display
results inline. Saved files go under
`data_outputs/<category>/<notebook-stem>/` and are ignored by Git.

### Data flow — 8 notebooks

| Notebook | Inputs and requirements | Outputs |
| --- | --- | --- |
| [County weather-point selection](notebooks/data_flow/county_weather_point_selection.ipynb) | Bundled Arthur County Census/TIGER CSVs; HSDS grid metadata. | One population-weighted centroid and three grid IDs, inline. |
| [County weather and BA aggregation](notebooks/data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb) | Bundled county mapping, service territories, population; HSDS if one-hour weather caches are absent. | Weather HDF5 caches and one-hour MISO weather CSV; Iowa weighting example inline. |
| [TELL load forecasting](notebooks/data_flow/tell_load_forecast_data_flow.ipynb) | Historical MISO weather; bundled raw load, validation metadata, and weather-source periods; TELL. | Training/prediction inputs, calibration, model files, 2007–2023 forecasts, held-out 2023 validation, two figures. |
| [EIA-860 regridding](notebooks/data_flow/eia860_regridding_methodology.ipynb) | Bundled 2024 workbooks and reviewed subregion mapping; HSDS grid metadata. | MISO grid-point CSV and mapping summaries. |
| [Site CF, weighting, and validation](notebooks/data_flow/site_cf_generation_ba_weighting_validation.ipynb) | Bundled 2022 fleet, SAM settings, renewable actuals, capacity manifest; reV/PySAM; HSDS if site-weather caches are absent. | Site-weather/CF HDF5 files, weighted MISO CF CSVs, validation metrics and figure; Iowa subset example. |
| [BA scenario metrics](notebooks/data_flow/ba_scenario_metrics_generation.ipynb) | Historical BA load/CF/scenarios and pooled metrics; bundled metadata, losses, raw MISO load, 2022 renewable actuals/capacities. | Reconstructed MISO scenario CSV, June 2022 comparison figure, archive checks, one-hour pooling example. |
| [Stress-event catalogs](notebooks/data_flow/ba_stress_event_catalog.ipynb) | Historical BA/pooled scenarios and bundled manifests. | Toy calculations and four regional event CSVs: SWPP, MISO_8910, MISO_SUBREGION_SUM, WECC. |
| [State load generation](notebooks/data_flow/state_load_generation.ipynb) | TaiESM1 BA/Iowa load; bundled county mapping/population and selected GCAM case; TELL. | One Iowa year/case reconstruction, staging files, archive comparison, load plots, and nine archived annual trajectories. |

### Validation — 4 notebooks

| Notebook | Inputs and requirements | Outputs |
| --- | --- | --- |
| [All-BA 2023 load validation](notebooks/validation/all_ba_2023_load_forecast_validation.ipynb) | Historical BA load; 58 bundled cleaned-observation CSVs and validation metadata. | Coverage, complete metric table, three scatter plots; inline only. |
| [MISO subregion load validation](notebooks/validation/miso_subregion_load_forecast_validation.ipynb) | Historical direct-MISO and six subregion forecasts; bundled cleaned MISO actuals. | Coverage, metrics, scatter plot; inline only. |
| [MISO wind, solar, and load validation](notebooks/validation/miso_wind_solar_load_validation.ipynb) | Historical MISO load; bundled 2022 fleet CF/capacities, raw load, renewable actuals. | Full-year loss-sensitivity metric CSV and January comparison PNG. |
| [Iowa historical/TaiESM1 comparison](notebooks/validation/state_historical_taiesm_validation.ipynb) | Iowa weather, load, wind CF, and solar CF from both collections. | Coverage, component diagnostics, duration curves; inline only. |

### Analysis — 5 notebooks

| Notebook | Inputs and requirements | Outputs |
| --- | --- | --- |
| [MISO load-duration curve](notebooks/analysis/miso_load_duration_curve.ipynb) | Bundled raw-value columns in six cleaned observation files and six saved subregion forecasts. | Load-duration PNG; no download or training needed. |
| [Pairwise pooling heatmaps](notebooks/analysis/pairwise_pooling_heatmap.ipynb) | Historical BA and pooled scenarios. | Ordered-pair metric CSV and nine heatmaps: four main and five portfolio appendices. |
| [Monthly MISO event counts](notebooks/analysis/miso_monthly_event_counts.ipynb) | Historical direct-MISO stress-event catalog. | One three-panel figure; inline only. |
| [Satellite and reanalysis context](notebooks/analysis/plot_satellite_and_reanalysis.ipynb) | NASA Worldview and NOAA PSL network access. | Five embedded images; no saved files. |
| [Iowa seasonal risk hours](notebooks/analysis/state_seasonal_risk_hours.ipynb) | TaiESM1 Iowa scenario metrics, using raw net load and equivalent renewable CF. | A 240-row CSV and six portfolio PNGs. |

**Example boundaries.** The one-hour weather example does not supply TELL's
full historical inputs. The regridding example covers MISO 2024, while site-CF
validation uses a separate 2022 fleet. Its Iowa appendix covers only
MISO-contributed sites; complete state CF needs all source BAs. EIA-930 provides
no state-level renewable actuals for that example. County/state weather uses
fixed 2020 population weights. The state-load example expands bundled
`pop_2020` into TELL's annual format and defaults to `rcp85hotter_ssp5`;
changing cases requires updating the setting and its input path. Its final
figure reads all nine archived trajectories rather than reconstructing them.

## Data

| Folder | Purpose |
| --- | --- |
| `data_inputs/` | Bundled supporting files and extracted Zenodo datasets. Precomputed reference products are inputs to these examples. |
| `data_outputs/` | Figures, tables, models, and caches created by running notebooks; contents are ignored by Git. |

When updating an older checkout, move downloaded dataset folders from `data/`
to `data_inputs/` and existing results from `notebook_outputs/` to `data_outputs/`.
Git updates the bundled inputs automatically.

Dataset version **0.1.0**: [Zenodo DOI 10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870).
See the [publication status](#verification-and-publication-status) below.

| Collection | Sources and period | Coverage |
| --- | --- | --- |
| Historical | WTK wind/load weather, 2007–2014; BC-HRRR wind/load weather, 2015–2023; NSRDB solar resource and GHI, 2007–2023. | 68 entities (62 BAs and six MISO subregions), five pools, and state products for the lower 48 states plus DC; availability varies. |
| TaiESM1 | sup3rCC v0.2.2: simulated historical climate, 2000–2014, then SSP2-4.5, 2015–2099. | AECI, SWPP, six MISO subregions, their combined pool, and Iowa. |

### Download and extract

Keep these five files together in a download folder:

- `wxdata_wtk_bchrrr_nsrdb_2007_2023.zip`
- `wxdata_sup3rcc_taiesm1_curated_2000_2099.zip`
- `README_DATASET.md`
- `LICENSE_DATA.txt`
- `RELEASE_MANIFEST.csv`

The archives total about 9.3 GB. Extract the collection required by your
notebook into `data_inputs/`, using these commands from the repository root:

```powershell
python -m zipfile -e "C:/path/to/wxdata_wtk_bchrrr_nsrdb_2007_2023.zip" "data_inputs"
python -m zipfile -e "C:/path/to/wxdata_sup3rcc_taiesm1_curated_2000_2099.zip" "data_inputs"
```

The resulting folders are `data_inputs/wtk_bchrrr_nsrdb_2007_2023/` and
`data_inputs/taiesm1_historical_ssp245_v022_2000_2099/`, alongside the bundled inputs.
The archive checker below can run without full extraction. Keep downloaded
datasets, acquisition caches, generated outputs, and credentials out of Git.

### Verify the download

With the environment active, run from the repository root:

```powershell
python scripts/check_release.py --archive-dir "C:/path/to/zenodo-files" --source-kind zenodo
```

For locally prepared archives, use `--source-kind local`. This label records
where you obtained the files; the checker does not download or authenticate
them. It verifies sizes and SHA-256 hashes for both ZIPs, the dataset
README/license, and two extracted inputs, then executes two fresh kernels
using the active Python interpreter:

- **Monthly MISO events:** six portfolios, 2007–2023, 3,672 monthly grid rows,
  conserved event counts, and one figure.
- **Iowa seasonal risk:** six portfolios with 876,000 hours each, conserved
  stress-hour totals, a complete 240-row CSV, and six figures.

Reports, executed copies, and figures go to a new folder under
`data_outputs/release_check/`. Optional `--output-dir` must name a
nonexistent directory. Failures return a nonzero exit code. Reports retain
the commit, dirty-checkout status, source/manifest hashes, package versions,
and results. This verifies compatibility for two notebooks; it does not
establish a clean installation, validate all products, or resolve scientific
limitations.

### Coverage

Coverage describes the **2024 operable onshore-wind/PV reference fleet**.
"Load only" means no modeled wind/PV in that fleet, not an absence of other
generation. Missing source mappings can yield zero modeled capacity. The
validation flag identifies the cleaned 2023 load comparison, not validation
of every product.

Wind/solar entries show nameplate MW and CF-file status: **nonzero**, **zero**
(an all-zero placeholder), or **absent**. A zero placeholder is not a usable
counterfactual resource profile. `has_load` denotes included modeled load;
`has_wind`/`has_solar` denote positive modeled capacity. Weather/load entries
report availability in that order. Every listed entity has scenario metrics
and a stress catalog.

The six portfolios are `installed_2024` and wind/solar nameplate splits 0/100,
25/75, 50/50, 75/25, and 100/0. A single-technology entity has two portfolios;
a load-only entity has one. Renewable-only entities have no load/net-load
comparison. Inspect columns as well as file availability.

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

There are 60 modeled-load entities and 58 validation entities. `AEC` and `NSB`
have released modeled load but lack usable packaged cleaned 2023 actuals.
`MISO` is the direct total-MISO model; the six `MISO_####` rows are constituent
subregion models and must not be added to total MISO a second time. `AMPL`,
`CEA`, and `OVEC` occur in mapping/provenance inputs but have no entity products
in this release.

The 59 wind and 59 solar CF files contain 40 nonzero wind profiles and 56
nonzero solar profiles. The other 19 wind and three solar files are entirely
zero; nine entities have neither dedicated CF file. Weather is present for 63
entities. This distinction explains why counting files, capacity flags, and
validation participants gives different totals.

<details>
<summary>Pooled regions: membership and capacity</summary>

All five historical pools have six-scenario metrics and stress-event catalogs.
They do not have separate dedicated pooled weather/load/CF files in the
archive. Load and generation are combined from member products; the renewable
capacity represented by each pool is shown below. "Rest of East" and "WECC"
refer to these listed memberships, not complete geographic censuses.

| Pool | Definition | Wind MW | Solar MW | Members |
| --- | --- | --- | --- | --- |
| `MISO_SUBREGION_SUM` | Sum of all six MISO subregions | 32,150.7 | 13,574.9 | `MISO_0001`, `MISO_0004`, `MISO_0006`, `MISO_0027`, `MISO_0035`, `MISO_8910` |
| `MISO_NCA` | MISO North/Central aggregate | 31,966.2 | 9,781.2 | `MISO_0001`, `MISO_0004`, `MISO_0006`, `MISO_0027`, `MISO_0035` |
| `MISO_SA` | MISO South aggregate | 184.5 | 3,793.7 | `MISO_8910` |
| `WECC` | Western pool | 31,300.5 | 40,775.9 | `AVA`, `AZPS`, `BANC`, `BPAT`, `CHPD`, `CISO`, `DOPD`, `EPE`, `GCPD`, `IID`, `IPCO`, `LDWP`, `NEVP`, `NWMT`, `PACE`, `PACW`, `PGE`, `PNM`, `PSCO`, `PSEI`, `SCL`, `SRP`, `TEPC`, `TIDC`, `TPWR`, `WACM`, `WALC`, `WAUW`, `AVRN`, `GRIS`, `GWA`, `WWA` |
| `ROE` | Rest of East pool | 51,006.4 | 45,899.4 | `AEC`, `AECI`, `CPLE`, `DUK`, `FMPP`, `FPC`, `FPL`, `GVL`, `HST`, `ISNE`, `JEA`, `LGEE`, `NSB`, `NYIS`, `PJM`, `SC`, `SCEG`, `SEC`, `SOCO`, `SPA`, `SWPP`, `TAL`, `TEC`, `TVA`, `CPLW`, `NBSO`, `SEPA` |

The three MISO pools overlap. `MISO_SA` contains one member, and
`MISO_SUBREGION_SUM` contains all members of both `MISO_NCA` and `MISO_SA`.
Keep these alternative aggregations separate when computing totals. The
MISO subregion validation notebook compares their full six-member sum with the
direct MISO forecast on the same observed-load hours.

</details>

<details>
<summary>TaiESM1 and state products</summary>

| Entity group | Members | Released products |
| --- | --- | --- |
| BA/subregion | `AECI`, `SWPP`, `MISO_0001`, `MISO_0004`, `MISO_0006`, `MISO_0027`, `MISO_0035`, `MISO_8910` | Weather, load, nonzero wind and solar CF, six-scenario metrics, stress catalogs |
| Pool | `MISO_SUBREGION_SUM` | Six-scenario metrics and stress catalog |
| State | Iowa (`IA`) | Weather, raw and eight GCAM-scaled load cases, wind and solar CF, six-scenario metrics, stress catalog |

These products span 2000-2099 and use the fixed installed-capacity scenarios;
"future" does not mean the generator fleet grows with time. The direct `MISO`
entity and the other four historical pools are not included in the curated
TaiESM1 archive. The Iowa historical/TaiESM1 notebook compares the shared
2007-2023 period; it is a model-product comparison, not observed-future validation.
The historical archive also provides state products for 49 states/district
entities: load, weather, metrics and catalogs for all 49, solar CF for 48,
and wind CF for 40. Iowa has all six component/product families in both releases.

</details>

The coverage snapshot was checked on **2026-09-09**. Its sources are the
[BA manifest](manifests/ba_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv),
[pool manifest](manifests/pooled_region_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv),
[validation membership](data_inputs/validation/load_forecast/ba_2023_validation_metadata.csv),
and the archived files. For a new dataset version, recheck memberships,
capacities, scenario columns, zero profiles, and calendars.

## Interpretation

- **Load and geography:** TELL load is modeled demand. Direct `MISO` and
  `MISO_SUBREGION_SUM` are different estimates; do not add them together.
  State boundaries and BA territories are different aggregations. The first
  load-duration example intentionally uses `load_actual_mw_raw`, retaining
  observations flagged during cleaning.
- **Fleets and portfolios:** shares describe wind-plus-solar nameplate
  capacity, not energy. Combined reference capacity is fixed, including in
  future years. The renewable-validation examples use a separate **2022
  fleet**, with 29,845.3 MW wind and 4,548.7 MW solar in the
  [validation capacity manifest](manifests/eia860_2022_operable_capacity_manifest.csv).
  Loss sensitivities do not replace the 2024-fleet products.
- **Calendars:** historical load/weather include leap days (149,016 UTC hours);
  historical CF omits them (148,920 hours). Renewable comparisons use common
  no-leap hours; load-only scenarios retain the load calendar. TaiESM1 has
  876,000 no-leap hours. Align timestamps explicitly. Simulated historical
  climate supports statistical comparisons, not matching individual observed
  weather events.
- **Stress thresholds:** load percentiles use the load series. Net-load P90,
  P95, and P99 thresholds are calculated from portfolio values pooled within
  each region, then shared across its portfolios; this is distinct from
  pooling regions. Equivalent renewable CF uses
  absolute 10%, 5%, and 1% cutoffs. Pairwise pooling retains its separately
  documented, scenario-specific thresholds.
- **Hours and events:** catalogs bridge one non-risk hour, include it in
  duration, and record it in `gap_hours`. Monthly MISO analysis counts event
  starts in UTC; a 12-hour event also qualifies for the 1- and 6-hour panels.
  P10–P90 shading represents variation across years, not uncertainty in the
  mean. Qualifying-row totals can count a timestamp under multiple portfolios
  or thresholds.
- **Iowa demand and seasons:** state catalogs use raw TELL load and net load;
  seasonal risk analysis uses raw net load. It shares one net-load P95 across all
  six portfolios and the century, uses an absolute 10% CF cutoff, and counts
  hours without gap bridging. Planning periods use UTC years; seasons use
  `America/Chicago` months. The eight GCAM-scaled load cases remain available
  separately; they change demand, not the underlying climate or resource CF.
- **Validation metrics:** MAE, RMSE, and bias are MW; NRMSE is RMSE divided by
  mean actual load; MAPE is percent; R² is dimensionless. Timestamp coverage
  can exceed valid paired hours. TELL internal tests, mean seasonal calibration
  scores, and held-out validation are different results. Display rounding
  changes neither calculation precision nor exported schemas.

**Known Iowa pressure limitation:** the historical/TaiESM1 comparison reports
a mean difference of approximately **−9,369 Pa over 2007–2023**. A check of
staged 2007 weather reproduced both archived series using the same 99 counties
and fixed 2020 population weights, placing the difference upstream of notebook
alignment and aggregation. The source/grid cause remains unresolved. No
unsupported correction is applied; a passing compatibility check does not
resolve this limitation.

## Sources and citation

Use [CITATION.cff](CITATION.cff) for repository citation metadata and cite the
[Zenodo dataset](https://doi.org/10.5281/zenodo.21844870) separately. Charlie
Phillips's original notebooks and documentation are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see [LICENSE](LICENSE).
Third-party materials retain their upstream terms and attribution requirements.

| Source | Role and attribution |
| --- | --- |
| EIA-860 2024 / 2022 | Generator locations and capacities: 2024 reference fleet and separate 2022 validation fleet. |
| EIA-930 | Observed load and renewable generation for training and validation. EIA publications/data are public domain; acknowledge EIA under its [reuse guidance](https://www.eia.gov/about/copyrights_reuse.php). |
| WTK, BC-HRRR, NSRDB | Historical weather and solar resources for the periods listed under [Data](#data). |
| sup3rCC / TaiESM1 | Downscaled historical/SSP2-4.5 climate inputs. |
| TELL | Weather-sensitive BA load models and county-to-state load processing. |
| reV / PySAM / SAM | Site-generation modeling and nameplate-weighted CF; bundled SAM configurations. |
| HSDS | Remote weather-grid access; acquisition caches are not distributed. Credit DOE/NREL/Alliance for relevant data/software and retain [upstream notices](https://www.nrel.gov/disclaimer.html). |
| 2020 Census / TIGER-Line | Block `POP100` and internal-point coordinates for population weighting; compact Arthur County examples and national mapping inputs. Retain Census [research-transparency](https://www.census.gov/topics/research/research-transparency-public-access/policy.html) and [policy notices](https://www.census.gov/about/policies.html). |
| GCAM-USA | Eight annual electricity-demand pathways; credit the Joint Global Change Research Institute and [GCAM-USA documentation](https://github.com/JGCRI/gcam-doc/blob/gh-pages/gcam-usa.md). Scaling selects `param == "elecFinalBySecTWh"` and `region == "USA"`. |
| Scalar loss assumptions | Historical portfolio losses are bundled; future loss settings are not a separate committed input. Reference resource CF and loss-adjusted scenario CF have different roles. |

### Verification and publication status

Notebook candidate **v0.1.0** and dataset **0.1.0** are versioned independently.
The release preparation reserved the dataset DOI; a branch or reserved DOI
alone does not establish publication. Use the linked record for availability
and retain the exact notebook commit and manifest with your results.

The 2026-09-19 readability review compared 12 fully rerun notebooks and two
using existing trained-model/site-CF products with their originals. Compared
scientific results and CSV exports were unchanged. The other three retained
their saved remote-data outputs; their local calculations or unchanged request
code were checked separately. The two-archive compatibility check also passed
on 2026-09-19. Site-CF checks used matching legacy weather caches whose original
source-version metadata was absent. These records do not establish a clean installation or verification
of files downloaded from Zenodo. Before declaring a reproducible release,
check a fresh environment and the actual downloaded files, retain the report,
and review attribution and the scientific limitations above. Earlier detailed
execution notes remain in Git history and the pinned release revision.

**AI assistance:** generative AI assisted with notebook code and documentation.
Charlie Phillips reviewed and accepted the work and remains responsible for
the repository's content.
