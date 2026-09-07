# Notebook methods companion

This directory contains the 17 canonical notebooks, their compact supporting
inputs, and the documentation needed to understand the methods. The large
hourly datasets are distributed separately through Zenodo DOI
[10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870).

Begin with [`documentation/START_HERE.md`](documentation/START_HERE.md), then
consult the per-notebook input map in
[`documentation/NOTEBOOK_INPUTS.md`](documentation/NOTEBOOK_INPUTS.md).

## Layout

```text
paper_data/
├── data_flow/      # 8 ordered construction and stress-event notebooks
├── validation/     # 4 load, renewable, and climate validation notebooks
├── analysis/       # 5 paper-facing analysis and figure notebooks
├── documentation/  # setup, input guide, and process-flow diagrams
├── data/
│   ├── source_inputs/  # compact inputs tracked by Git
│   ├── wtk_bchrrr_nsrdb_2007_2023/               # Zenodo; ignored by Git
│   └── taiesm1_historical_ssp245_v022_2000_2099/  # Zenodo; ignored by Git
├── manifests/      # 3 compact metadata manifests tracked by Git
└── SOURCES.md      # source inventory and provenance
```

There is no second development-notebook directory in this public repository.
The notebooks in `data_flow/`, `validation/`, and `analysis/` are the editable
public versions.

## What the notebook groups show

### `data_flow/`

These notebooks document county weather-point selection, county-to-BA weather
aggregation, TELL load modeling, EIA-860 renewable-site regridding, reV/PySAM
capacity-factor generation, regional capacity weighting, six wind/solar
portfolio calculations, stress-event construction, and GCAM-scaled state-load
trajectories.

### `validation/`

These notebooks compare modeled and observed BA load, evaluate MISO subregion
forecasts, compare modeled MISO wind and solar generation with EIA observations,
and compare historical and TaiESM1 Iowa weather and power-system variables.

### `analysis/`

These notebooks examine MISO load-duration curves, pairwise balancing-authority
pooling, BA and state stress-risk figures, the February 2021 weather context,
and Iowa seasonal risk hours over 2000–2099.

## Models and source datasets

- **WTK / BC-HRRR / NSRDB** form the 2007–2023 historical weather dataset.
- **Sup3rCC / TaiESM1** form the 2000–2099 historical and simulated future
  climate dataset used for the selected future analyses.
- **TELL** supplies the weather-informed load-model framework.
- **reV and PySAM/SAM** convert wind and solar resource data to site capacity
  factors before capacity-weighted regional aggregation.
- **EIA-860** supplies renewable generator locations and nameplate capacities.
- **EIA-930-derived observations** support load and renewable validation.
- **GCAM-USA** supplies eight annual electricity-demand trajectories used to
  scale the raw Iowa hourly load series.

Detailed upstream sources and notices are provided in [`SOURCES.md`](SOURCES.md)
and [`data/source_inputs/README.md`](data/source_inputs/README.md).

## Data boundary

The historical Zenodo archive covers packaged BA and state products for
2007–2023. The curated 2000–2099 archive contains AECI, SWPP, the six MISO
subregions, pooled `MISO_SUBREGION_SUM` products, and Iowa state products. The
Zenodo documentation is the authority for exact entity and product coverage.

The GitHub `source_inputs/` directory contains only the compact source,
provenance, and validation inputs required by the notebooks. Large hourly
products, acquisition HDF5 files, remote-data caches, and generated notebook
artifacts are excluded from Git.

## Running notebooks

Create the environment from the repository root:

```powershell
conda env create -f environment.yml
conda activate wxdata-notebooks
jupyter lab paper_data
```

For notebooks that consume the full curated data, download both Zenodo ZIP
files and extract them under `paper_data/data/` as described in
[`data/README.md`](data/README.md).

Open a notebook in its category directory and use **Restart Kernel and Run
All**. Inputs are referenced through `../data` and `../manifests`; generated
files are written to ignored notebook-output locations. Online HSDS,
NASA/NOAA, TELL, and reV/PySAM steps may require network access, credentials,
or specialist dependencies.

The notebooks retain compact embedded outputs so that representative tables
and figures render on GitHub. These embedded outputs are part of the notebook
files; standalone output directories are neither tracked by Git nor included
in the Zenodo data deposit.

## Portfolio interpretation

Portfolio percentages are shares of combined wind-plus-solar **nameplate
capacity**, not shares of annual energy. For total installed capacity
`C_total`, hourly renewable energy is represented as:

```text
E_t = C_total × (wind_share × wind_CF_t + solar_share × solar_CF_t) × 1 hour
```

For example, a 75/25 portfolio assigns 75% of nameplate capacity to wind and
25% to solar. Figure 10/11 risk thresholds use the 95th percentile calculated
over all hours and all six mixes. Risk hours are qualifying individual hours;
stress-event catalogs additionally apply the documented grouping and bridge
rules.

## Public/private separation

The public repository shows the methods. It intentionally excludes the private
operational package, CLI, production scripts, working run configurations,
tests, and local working-input directories. The Zenodo deposit remains
data-only and does not contain notebooks or notebook-generated outputs.
