# Synchronized Wind, Solar, and Load Data for Power System Planning

This repository is the public methods companion for synchronized weather,
electricity-load, wind-capacity-factor, solar-capacity-factor, net-load, and
stress-event datasets. It contains 17 executed Jupyter notebooks,
documentation, and the compact inputs used directly by those notebooks. The
private operational pipeline, run configurations, and large generated datasets
are intentionally not included.

The large analysis-ready datasets are distributed separately through Zenodo
DOI [10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870).

## Start here

Read [`documentation/START_HERE.md`](documentation/START_HERE.md) for the
recommended notebook order and setup instructions. Exact requirements for each
notebook are listed in
[`documentation/NOTEBOOK_INPUTS.md`](documentation/NOTEBOOK_INPUTS.md).

## Weather datasets

| Dataset | Period | Purpose |
| --- | --- | --- |
| WTK / BC-HRRR / NSRDB | 2007–2023 | Historical weather dataset combining wind-resource, solar-resource, and load-weather variables. WTK is 2007-2014 and contains wind-resource variables, BC-HRRR is 2015-2023 and contains wind resource variables, NSRDB is 2007-2023 and contains solar resource variables. Load-weather variables are primarily derived from WTK/BC-HRRR, though `ghi` is used for load forecasts and is derived from NSRDB
| Sup3rCC (TaiESM1) | 2000–2099 | Historical and simulated future climate dataset used for selected balancing-authority, pooled-region, and Iowa analyses. |

The notebooks also use TELL for weather-informed load modeling; reV and
PySAM/SAM for wind and solar capacity factors; EIA-860 generator records;
EIA-930-derived load and renewable observations; GCAM-USA state electricity
demand scenarios; and percentile/event-grouping methods for power-system stress
analysis.

## Repository layout

```text
wxdata-notebooks/
├── notebooks/
│   ├── data_flow/      # 8 construction and stress-event notebooks
│   ├── validation/     # 4 load, renewable, and climate validation notebooks
│   └── analysis/       # 5 paper-facing analysis and figure notebooks
├── data/               # compact GitHub inputs plus ignored Zenodo data roots
├── manifests/          # 3 analysis metadata manifests
├── documentation/      # setup, input guide, sources, and process diagrams
├── environment.yml
├── CITATION.cff
└── LICENSE
```

All notebooks retain their saved outputs so tables and figures render directly
on GitHub. Standalone generated files are written under the ignored
`notebook_outputs/` directory and are not part of the Zenodo deposit.

## Install and open the notebooks

From the repository root:

```powershell
conda env create -f environment.yml
conda activate wxdata-notebooks
jupyter lab notebooks
```

Download and extract the two Zenodo archives into `data/` before rerunning
notebooks that consume the full analysis-ready datasets. See
[`data/README.md`](data/README.md).

Some acquisition and reconstruction steps require network access, NREL HSDS,
TELL, or reV/PySAM. Saved notebook outputs allow the complete documented method
to be reviewed without rerunning those external acquisition steps.

## Repository boundary

This repository does not contain the private operational CLI, Python package,
production scripts, run configurations, tests, or working data trees. The
Zenodo record remains data-only and does not contain notebooks or notebook
outputs.

Source descriptions and upstream acknowledgments are collected in
[`documentation/SOURCES.md`](documentation/SOURCES.md) and
[`data/README.md`](data/README.md).

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

Unless otherwise noted, the original notebooks and documentation contributed
by Charlie Phillips are licensed under the
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
See [`LICENSE`](LICENSE).

Third-party data and software retain their original licenses and attribution
requirements. Inclusion in this repository does not relicense those materials.
