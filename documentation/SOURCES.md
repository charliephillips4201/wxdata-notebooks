# Source inventory

This inventory identifies the external datasets and modeling systems used by
the public notebooks. Compact supporting inputs are stored under
`data/`; the large analysis-ready products are distributed
through Zenodo DOI
[10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870).

| Source or model | Use in the notebooks | Public companion material |
| --- | --- | --- |
| EIA-860 2024 | Operable wind and solar generators, nameplate capacities, and plant locations used for renewable-site mapping and capacity weighting. | Raw plant and generator workbooks plus the reviewed MISO-subregion mapping workbook. |
| EIA-860 2022 | Validation fleet for the 2022 reconstruction and January 2023 renewable-loss comparison. | Compact MISO point files, validation capacity-factor series, and the 2022 capacity manifest. |
| EIA-930 | Historical BA load and observed wind and solar generation used for validation. | Selected BA and MISO validation series derived from EIA observations. |
| 2020 Census Redistricting Data P.L. 94-171 | Census-block `POP100` values used to construct population-weighted county points. | Derived county provenance tables and a compact Arthur County example. |
| TIGER/Line 2020 Blocks | Census-block internal-point coordinates paired with `POP100`. | Derived county-point provenance and a compact Arthur County example. |
| WTK | Wind resource and load-weather variables for 2007–2014. | Analysis-ready regional products are in the historical Zenodo archive. |
| BC-HRRR | Wind resource and load-weather variables for 2015–2023. | Analysis-ready regional products are in the historical Zenodo archive. |
| NSRDB | Solar resource and GHI variables for 2007–2023. | Analysis-ready regional products are in the historical Zenodo archive. |
| Sup3rCC / TaiESM1 | Hourly climate-adjusted weather and resource inputs for 2000–2099. | The curated Zenodo archive contains the selected future BA, pooled-region, and Iowa products. |
| TELL | Weather-informed load-model training and prediction framework. | The load-method notebooks use TELL directly; compact validation and GCAM-scaling inputs are included. |
| reV and PySAM/SAM | Conversion of wind and solar resource variables to site capacity factors before regional capacity weighting. | Fixed SAM JSON parameter files and compact validation inputs are included. |
| GCAM-USA | Eight annual state electricity-demand trajectories used to scale raw Iowa hourly load. | Eight scenario CSVs; the notebook selects `param == "elecFinalBySecTWh"` and `region == "USA"`. |
| HSDS | Remote access layer for gridded NREL weather and resource datasets. | Acquisition notebooks demonstrate access; large downloaded HDF5 caches are not distributed. |
| Net-load loss assumptions | Scalar wind and solar loss assumptions used in the six net-load portfolios. | Historical and future loss-assumption CSVs are included. |

The 2007–2023 weather inputs are described collectively as the historical
weather dataset. Sup3rCC/TaiESM1 is described as the 2000–2099 historical and
simulated future climate dataset.

Upstream ownership, reuse notices, and suggested acknowledgments are collected
in [`../data/README.md`](../data/README.md). Upstream
materials retain their own terms. The license selected for this repository
applies only to Charlie Phillips's copyrightable contributions to the extent
permitted.
