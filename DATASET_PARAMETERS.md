# Dataset parameters

The regional tables describe the full historical release available through the
[unpublished Zenodo draft preview][zenodo-preview]. GitHub includes selected examples
from the collections below.

[BAs](#balancing-authorities-and-miso-subregions) · [States](#states-and-district-of-columbia) · [Pools](#ba-pools-and-membership)

| Collection | Weather sources | Coverage |
| --- | --- | --- |
| Historical, 2007–2023 | WTK, 2007–2014; BC-HRRR, 2015–2023; NSRDB solar, 2007–2023. | 68 BA-level entities, five pools, and the lower 48 states plus DC. |
| TaiESM1, 2000–2099 | Sup3rCC v0.2.2: historical experiment, 2000–2014; SSP2-4.5, 2015–2099. | AECI, SWPP, six MISO subregions, MISO_SUBREGION_SUM, and Iowa. |

- **Capacities:** 2024 modeled onshore-wind/PV nameplate MW. **Peaks:** 2019–2022;
  timestamps are UTC.
- **†:** At least one example from either collection is bundled; years, columns,
  or scenarios may be limited. See the [input manifest](manifests/notebook_inputs.csv).
- **—:** Zero modeled capacity, or unavailable peak information.

## Balancing authorities and MISO subregions

Screened EIA-930 observed peaks.

| Name | Code | Observed peak load (MW, 2019–2022) | Peak load time (UTC) | Wind nameplate (MW) | Solar nameplate (MW) |
| --- | --- | ---: | --- | ---: | ---: |
| PowerSouth Energy Cooperative | `AEC` | 1,103.0 | 2020-07-16 17:00 | — | — |
| Associated Electric Cooperative, Inc. | `AECI`† | 6,228.0 | 2022-12-23 16:00 | 959.4 | 1.5 |
| Avista Corporation | `AVA`† | 2,514.0 | 2022-12-22 17:00 | 349.3 | 19.2 |
| Avangrid Renewables LLC | `AVRN` | — | — | 1,695.9 | 322.0 |
| Arizona Public Service Company | `AZPS`† | 7,595.0 | 2020-07-31 01:00 | 628.5 | 919.5 |
| Balancing Authority of Northern California | `BANC`† | 4,882.0 | 2022-09-07 00:00 | — | 338.6 |
| Bonneville Power Administration | `BPAT`† | 11,068.0 | 2022-12-22 17:00 | 3,617.1 | 223.7 |
| Public Utility District No. 1 of Chelan County | `CHPD`† | 556.0 | 2022-12-22 17:00 | — | — |
| California Independent System Operator | `CISO`† | 51,104.0 | 2022-09-07 01:00 | 6,352.2 | 22,166.7 |
| Duke Energy Progress East | `CPLE`† | 12,808.0 | 2022-12-24 11:00 | — | 2,922.5 |
| Duke Energy Progress West | `CPLW` | — | — | — | 28.4 |
| Public Utility District No. 1 of Douglas County | `DOPD`† | 517.0 | 2022-12-22 16:00 | — | — |
| Duke Energy Carolinas | `DUK`† | 21,265.0 | 2022-06-15 21:00 | — | 2,157.1 |
| El Paso Electric Company | `EPE`† | 2,201.0 | 2022-07-20 00:00 | 50.4 | 251.3 |
| Electric Reliability Council of Texas, Inc. | `ERCO`† | 79,830.0 | 2022-07-20 22:00 | 38,566.7 | 22,179.5 |
| Florida Municipal Power Pool | `FMPP`† | 3,830.0 | 2019-07-31 21:00 | — | 166.9 |
| Duke Energy Florida Inc. | `FPC`† | 11,914.0 | 2022-06-23 21:00 | — | 1,936.9 |
| Florida Power & Light Company | `FPL`† | 27,283.0 | 2022-08-01 20:00 | — | 7,192.3 |
| Public Utility District No. 2 of Grant County, Washington | `GCPD`† | 990.0 | 2022-07-29 23:00 | — | — |
| Gridforce South | `GRIS` | — | — | 324.3 | — |
| Gainesville Regional Utilities | `GVL`† | 478.0 | 2021-09-03 22:00 | — | 4.8 |
| NaturEner Power Watch, LLC | `GWA` | — | — | 210.0 | — |
| Hawaiian Electric Co Inc | `HECO` | — | — | — | 319.1 |
| City of Homestead | `HST`† | 137.0 | 2020-06-26 19:00 | — | — |
| Imperial Irrigation District | `IID`† | 1,133.0 | 2021-08-04 23:00 | — | 543.2 |
| Idaho Power Company | `IPCO`† | 4,067.0 | 2021-07-01 01:00 | 714.7 | 580.9 |
| ISO New England Inc. | `ISNE`† | 25,101.0 | 2021-06-29 22:00 | 1,510.2 | 3,307.1 |
| JEA | `JEA`† | 2,816.0 | 2022-06-23 21:00 | — | 38.1 |
| Los Angeles Department of Water and Power | `LDWP`† | 6,286.0 | 2020-08-18 23:00 | 440.5 | 1,317.5 |
| Louisville Gas and Electric Company and Kentucky Utilities Company | `LGEE`† | 7,476.0 | 2022-12-23 16:00 | — | 18.1 |
| Midcontinent Independent System Operator, Inc. | `MISO`† | 116,600.0 | 2019-07-19 21:00 | 32,150.7 | 13,574.9 |
| MISO subregion 0001 | `MISO_0001`† | 16,646.0 | 2022-06-20 23:00 | 9,732.7 | 1,647.6 |
| MISO subregion 0004 | `MISO_0004`† | 9,128.0 | 2019-07-19 22:00 | 2,768.8 | 2,467.1 |
| MISO subregion 0006 | `MISO_0006`† | 16,610.0 | 2021-08-24 22:00 | 1,441.5 | 1,348.6 |
| MISO subregion 0027 | `MISO_0027`† | 31,561.0 | 2022-06-21 22:00 | 4,603.7 | 3,248.9 |
| MISO subregion 0035 | `MISO_0035`† | 16,580.0 | 2022-07-05 21:00 | 13,419.5 | 1,069.0 |
| MISO subregion 8910 | `MISO_8910`† | 31,548.0 | 2022-06-22 22:00 | 184.5 | 3,793.7 |
| New Brunswick System Operator | `NBSO` | — | — | 42.0 | 17.9 |
| Nevada Power Company | `NEVP`† | 9,357.0 | 2021-07-09 23:00 | 150.0 | 3,980.2 |
| New Smyrna Beach Utilities Commission | `NSB` | 105.0 | 2019-07-02 21:00 | — | — |
| NorthWestern Energy | `NWMT`† | 2,600.0 | 2021-05-20 09:00 | 763.6 | 179.0 |
| New York Independent System Operator | `NYIS`† | 30,919.0 | 2021-06-29 22:00 | 2,739.3 | 2,517.4 |
| PacifiCorp - East | `PACE`† | 9,494.0 | 2022-07-19 00:00 | 3,984.8 | 2,196.4 |
| PacifiCorp - West | `PACW`† | 4,187.0 | 2021-08-12 21:00 | 489.9 | 477.1 |
| Portland General Electric Company | `PGE`† | 4,471.0 | 2021-06-29 00:00 | 716.5 | 189.7 |
| PJM Interconnection, LLC | `PJM`† | 152,315.0 | 2019-07-19 22:00 | 11,451.6 | 14,791.3 |
| Public Service Company of New Mexico | `PNM`† | 2,787.0 | 2022-07-20 00:00 | 2,569.0 | 1,784.0 |
| Public Service Company of Colorado | `PSCO`† | 9,853.0 | 2021-07-29 00:00 | 4,692.3 | 2,116.3 |
| Puget Sound Energy | `PSEI`† | 5,431.0 | 2019-02-06 17:00 | 868.4 | 15.5 |
| South Carolina Public Service Authority | `SC`† | 5,342.0 | 2022-12-24 14:00 | — | 303.3 |
| Dominion Energy South Carolina | `SCEG`† | 4,800.0 | 2022-06-13 21:00 | — | 1,044.1 |
| Seattle City Light | `SCL`† | 1,906.0 | 2022-12-22 02:00 | — | — |
| Seminole Electric Cooperative | `SEC`† | 1,070.0 | 2020-09-16 21:00 | — | 74.5 |
| Southeastern Power Administration | `SEPA` | — | — | — | 275.0 |
| Southern Company Services, Inc. - Transmission | `SOCO`† | 48,073.0 | 2022-06-15 21:00 | — | 5,485.9 |
| Southwestern Power Administration | `SPA`† | 154.0 | 2022-06-16 03:00 | 499.0 | 19.5 |
| Salt River Project | `SRP`† | 7,714.0 | 2020-07-13 01:00 | 226.0 | 1,674.9 |
| Southwest Power Pool | `SWPP`† | 53,016.0 | 2022-07-19 22:00 | 33,803.1 | 869.6 |
| City of Tallahassee | `TAL`† | 616.0 | 2019-08-14 20:00 | — | 62.0 |
| Tampa Electric Company | `TEC`† | 4,485.0 | 2021-08-18 22:00 | — | 1,356.4 |
| Tucson Electric Power Company | `TEPC`† | 4,147.0 | 2020-07-12 00:00 | 379.8 | 492.2 |
| Turlock Irrigation District | `TIDC`† | 727.0 | 2022-09-07 01:00 | — | — |
| City of Tacoma Department of Public Utilities Light Division | `TPWR`† | 973.0 | 2022-12-22 18:00 | — | — |
| Tennessee Valley Authority | `TVA`† | 33,225.0 | 2022-12-24 02:00 | 1.8 | 1,308.8 |
| Western Area Power Administration - Rocky Mountain Region | `WACM`† | 4,982.0 | 2022-09-07 00:00 | 1,466.9 | 567.3 |
| Western Area Power Administration - Desert Southwest Region | `WALC`† | 2,251.0 | 2020-08-28 00:00 | 350.0 | 340.7 |
| Western Area Power Administration UGP West | `WAUW`† | 188.0 | 2021-07-02 21:00 | 71.4 | 80.0 |
| NaturEner Wind Watch, LLC | `WWA` | — | — | 189.0 | — |

## States and District of Columbia

Modeled BC-HRRR/NSRDB raw-load peaks, without GCAM scaling.

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
| Iowa | `IA`† | 10,287.9 | 2022-07-05 22:00 | 13,016.0 | 677.5 |
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

## BA pools and membership

Coincident EIA-930 observed peaks use hours valid for every required load-bearing
member, not sums of the members' individual peak loads.

| Name | Code | Observed peak load (MW, 2019–2022) | Peak load time (UTC) | Wind nameplate (MW) | Solar nameplate (MW) |
| --- | --- | ---: | --- | ---: | ---: |
| MISO North/Central aggregate | `MISO_NCA`† | 87,910.0 | 2019-07-19 21:00 | 31,966.2 | 9,781.2 |
| MISO South aggregate | `MISO_SA` | 31,548.0 | 2022-06-22 22:00 | 184.5 | 3,793.7 |
| Sum of all six MISO subregions | `MISO_SUBREGION_SUM`† | 116,500.0 | 2019-07-19 21:00 | 32,150.7 | 13,574.9 |
| Rest of East pool | `ROE` | 404,728.0 | 2019-07-17 22:00 | 51,006.4 | 45,899.4 |
| Western pool | `WECC`† | 143,047.0 | 2022-09-07 01:00 | 31,300.5 | 40,775.9 |

### Pool membership

| Pool | Member BAs / subregions |
| --- | --- |
| `MISO_NCA` (5) | `MISO_0001`, `MISO_0004`, `MISO_0006`, `MISO_0027`, `MISO_0035` |
| `MISO_SA` (1) | `MISO_8910` |
| `MISO_SUBREGION_SUM` (6) | `MISO_0001`, `MISO_0004`, `MISO_0006`, `MISO_0027`, `MISO_0035`, `MISO_8910` |
| `ROE` (27) | `AEC`, `AECI`, `CPLE`, `DUK`, `FMPP`, `FPC`, `FPL`, `GVL`, `HST`, `ISNE`, `JEA`, `LGEE`, `NSB`, `NYIS`, `PJM`, `SC`, `SCEG`, `SEC`, `SOCO`, `SPA`, `SWPP`, `TAL`, `TEC`, `TVA`, `CPLW`, `NBSO`, `SEPA` |
| `WECC` (32) | `AVA`, `AZPS`, `BANC`, `BPAT`, `CHPD`, `CISO`, `DOPD`, `EPE`, `GCPD`, `IID`, `IPCO`, `LDWP`, `NEVP`, `NWMT`, `PACE`, `PACW`, `PGE`, `PNM`, `PSCO`, `PSEI`, `SCL`, `SRP`, `TEPC`, `TIDC`, `TPWR`, `WACM`, `WALC`, `WAUW`, `AVRN`, `GRIS`, `GWA`, `WWA` |

MISO, its subregions, and their pools overlap; do not add them together.
WECC and ROE cover only their listed members.

<a id="sources-and-interpretation"></a>
<details>
<summary>Methods and sources</summary>

**Peak notes**

- The quality checks on EIA-930 data are demonstrated in **Step 3** of
  [TELL load forecasting](notebooks/data_flow/tell_load_forecast_data_flow.ipynb).
  Missing hours remain unfilled and can affect the recorded peak.
- Suspect EIA-930 data (which otherwise would have been the peak load) was flagged in BANC, NSB, SEC, and PJM. Those readings were excluded from both BA and pooled peak calculations.
- Values are displayed to one decimal. When unrounded peaks tie, the earliest
  hour is shown.

**Sources**

Source manifests are under `wxdata/paper_data/manifests/`.

- **BA capacities:** `eia860_2024_operable_capacity_manifest_wtk_bchrrr_nsrdb_2007_2023.csv`
- **State capacities:** `state_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv`
- **Pool capacities:** `pooled_region_scenario_metric_metadata_manifest_wtk_bchrrr_nsrdb_2007_2023.csv`
- **Peak values and review details:** The [peak summary](manifests/dataset_peak_load_summary_2019_2022.csv)
  lists missing-hour coverage, review decisions, and contributing pool members.
- **Pool membership:** `wxdata/configs/pool/standard_pools_2007_2023.yaml`.

</details>

[zenodo-preview]: https://zenodo.org/records/21844870?preview=1&token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImU1YTZmOTdhLTg1Y2YtNGExMC1hMzdmLTY1NThjMGRjYzg0NyIsImRhdGEiOnt9LCJyYW5kb20iOiI4NThhZTRkYjg5OWNkNjg3MjM1NTBhYjAwYzg2NWU5YiJ9.kYx9A2TU38HVcXgbed38NuUok4_YGhmQ3K7MivkrsoIbPh9I--8NjqIJIjdHz5mhtkUs9elFEc7OdQBQn4bULQ
