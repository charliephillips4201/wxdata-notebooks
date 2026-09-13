# Balancing-authority coverage

This guide describes the released datasets, using the release's entity names
and EIA-860 fleet definitions. The historical archive contains **68 entities:
62 BAs and six MISO subregions**. Its five pooled regions are listed separately
below. The curated TaiESM1 archive contains eight BA/subregion entities, the
MISO subregion aggregate, and Iowa.

## How to read the inventory

A classification describes the modeled products and the **2024 operable
onshore-wind and photovoltaic fleet** used in this release. `has_load` means a
modeled load series is included; `has_wind` and `has_solar` mean the corresponding
capacity in the selected regridded fleet is positive. Missing source mappings
can also yield zero modeled capacity. These flags do not describe every real-world
load or generation technology in a BA. In particular, "load only" means no
modeled wind or PV capacity in this fleet, not an absence of hydro, fossil,
nuclear, or other generation.

Wind and solar entries give installed MW followed by the released CF-file
status: **nonzero** contains nonzero modeled values, **zero** is an existing
all-zero placeholder, and **absent** has no dedicated CF file. An all-zero
placeholder does not provide a usable counterfactual technology profile.
The weather/load column reports file availability for those two products,
respectively. Validation means
membership in the packaged 2023 cleaned-load comparison, not that every product
has been independently validated. Every entity below has scenario metrics and
a stress-event catalog; the scenario column counts distinct released scenarios.

The six-scenario set is `installed_2024` plus wind/solar capacity splits 0/100,
25/75, 50/50, 75/25, and 100/0. Entities with only one modeled renewable technology
have two scenarios: installed and the corresponding 100% technology split.
Load-only entities have one installed scenario containing load. Renewable-only
entities have no load or net-load comparison. The released columns, rather than
file presence alone, determine which analyses are possible.

## Historical entities, 2007-2023

### Load + wind + solar (35)

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

### Load + solar only (16)

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

### Load only (9)

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

### Wind and solar only (2)

| Entity | Release name | Wind MW / CF | Solar MW / CF | Weather / load files | Scenarios | 2023 load validation |
| --- | --- | --- | --- | --- | --- | --- |
| `AVRN` | Avangrid Renewables LLC | 1,695.9 / nonzero | 322.0 / nonzero | no / no | 6 | no |
| `NBSO` | New Brunswick System Operator | 42.0 / nonzero | 17.9 / nonzero | yes / no | 6 | no |

### Solar only (3)

| Entity | Release name | Wind MW / CF | Solar MW / CF | Weather / load files | Scenarios | 2023 load validation |
| --- | --- | --- | --- | --- | --- | --- |
| `CPLW` | Duke Energy Progress West | 0.0 / zero | 28.4 / nonzero | no / no | 2 | no |
| `HECO` | Hawaiian Electric Co Inc | 0.0 / zero | 319.1 / nonzero | yes / no | 2 | no |
| `SEPA` | Southeastern Power Administration | 0.0 / zero | 275.0 / nonzero | yes / no | 2 | no |

### Wind only (3)

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

## Pooled regions

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

## Curated TaiESM1 and state products

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

## Calendars, fleets, and refreshing the guide

Historical BA load and weather contain 149,016 UTC hours, including leap days.
Historical CF contains 148,920 hours with February 29 removed. Renewable
scenario comparisons use their common no-leap hours; load-only scenario files
retain the historical load calendar. TaiESM1 component series contain 876,000
hours (100 x 8,760), also without February 29. Align timestamps explicitly before
comparing products; equal year labels do not guarantee equal hourly calendars.

The 2023 MISO renewable-validation example uses a **separate 2022 fleet**:
29,845.3 MW wind and 4,548.7 MW solar, recorded in the
[2022 validation capacity manifest](../manifests/eia860_2022_operable_capacity_manifest.csv).
Its loss sensitivities are validation examples and do not replace the released
2024-fleet scenario products.

This snapshot was checked on 2026-09-09 for dataset versions
`wtk_bchrrr_nsrdb_2007_2023` and
`taiesm1_historical_ssp245_v022_2000_2099` from
[the Zenodo release](https://doi.org/10.5281/zenodo.21844870).
Names use the release's BA labels; capacities and classifications come from the
[BA metadata manifest](../manifests/ba_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv),
with pool capacities from the
[pooled metadata manifest](../manifests/pooled_region_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv).
The [validation metadata](../data/validation/load_forecast/ba_2023_validation_metadata.csv)
lists the cleaned-load comparison participants.

When adopting a new release, refresh names and fleet metadata, enumerate its
extracted product files and scenario columns, verify any zero CF profiles, and
reconcile validation membership. Recheck the documented pool memberships and
calendar counts at the same time. The committed manifests and downloaded
archives are sufficient for readers to inspect this coverage; no private
pipeline checkout is required.
