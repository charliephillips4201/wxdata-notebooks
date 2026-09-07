# Synchronized Wind, Solar, and Load Data for Power System Planning

This repository is the public methods companion for a set of synchronized
weather, electricity-load, wind-capacity-factor, solar-capacity-factor, and
net-load data products. It contains the Jupyter notebooks, documentation, and
compact supporting inputs needed to inspect the methods and reproduce the
paper-facing analyses. The private operational pipeline, run configurations,
and large generated datasets are intentionally not included.

The large analysis-ready datasets are distributed separately through Zenodo
DOI [10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870).

## Start here

Read [`paper_data/documentation/START_HERE.md`](paper_data/documentation/START_HERE.md)
for the recommended notebook order and setup instructions. The exact input
requirements for each notebook are listed in
[`paper_data/documentation/NOTEBOOK_INPUTS.md`](paper_data/documentation/NOTEBOOK_INPUTS.md).

## Weather datasets

| Dataset | Period | Purpose |
| --- | --- | --- |
| WTK / BC-HRRR / NSRDB | 2007–2023 | Historical weather dataset combining wind-resource, solar-resource, and load-weather variables. WTK is 2007-2014 and contains wind-resource variables, BC-HRRR is 2015-2023 and contains wind resource variables, NSRDB is 2007-2023 and contains solar resource variables. Load-weather variables are primarily derived from WTK/BC-HRRR, though `ghi` is used for load forecasts and is derived from NSRDB
| Sup3rCC (TaiESM1) | 2000–2099 | Historical and simulated future climate dataset used for selected balancing-authority, pooled-region, and Iowa analyses. |

The notebooks also use:

- TELL to demonstrate weather-informed hourly electricity-load modeling;
- reV and PySAM/SAM technology models to convert wind and solar resource data
  into site and regional capacity factors;
- EIA-860 records to locate and capacity-weight renewable generators;
- EIA-930-derived observations for load and renewable-generation validation;
- GCAM-USA scenarios to scale Iowa state load trajectories; and
- percentile and event-grouping methods to identify stress hours and stress
  events under six wind/solar nameplate-capacity portfolios.

Source descriptions and upstream acknowledgments are collected in
[`paper_data/SOURCES.md`](paper_data/SOURCES.md) and
[`paper_data/data/source_inputs/README.md`](paper_data/data/source_inputs/README.md).

## Notebook collection

The canonical collection contains 17 notebooks:

```text
paper_data/
├── data_flow/      # 8 notebooks showing data construction and event methods
├── validation/     # 4 notebooks evaluating load, renewable, and climate products
├── analysis/       # 5 notebooks producing paper-facing comparisons and figures
├── documentation/  # setup, input guide, and process-flow diagrams
├── data/
│   ├── source_inputs/  # 113 compact inputs stored on GitHub
│   ├── wtk_bchrrr_nsrdb_2007_2023/               # download from Zenodo
│   └── taiesm1_historical_ssp245_v022_2000_2099/  # download from Zenodo
└── manifests/      # 3 compact analysis manifests stored on GitHub
```

The notebooks retain selected outputs inside the `.ipynb` files so figures and
tables render on GitHub. Standalone output folders, acquisition caches, and the
extracted Zenodo datasets are ignored by Git.

## Install and open the notebooks

From the repository root:

```powershell
conda env create -f environment.yml
conda activate wxdata-notebooks
jupyter lab paper_data
```

Download and extract the two Zenodo archives before rerunning notebooks that
consume the full analysis-ready datasets. Instructions are in
[`paper_data/data/README.md`](paper_data/data/README.md).

Some acquisition and reconstruction cells require network access, external
credentials, TELL, or specialist NREL dependencies. Saved notebook outputs and
the distributed inputs allow the documented method to be inspected without
rerunning every acquisition step.

## Repository boundary

This public repository does not contain the private operational CLI, source
package, run configurations, production scripts, tests, or working input
directories. Those materials are not required by the 17 public notebooks.
Fixed scientific-method inputs used directly by the notebooks—including SAM
JSON parameter files and one county-weather provenance YAML file—remain under
`paper_data/data/source_inputs/`.

## Citation

Authorship and repository citation metadata are provided in
[`CITATION.cff`](CITATION.cff). Cite the Zenodo dataset separately using the
citation displayed on its DOI record.

## AI assistance

Generative AI tools were used to assist with drafting and editing portions of
the documentation and notebook code. All resulting material was reviewed,
tested, and accepted by Charlie Phillips, who takes responsibility for the
content of this repository.

## License

This repository is being prepared for public release. A root `LICENSE` must be
added before the repository is made public. Upstream data and software retain
their own terms and attribution requirements.
