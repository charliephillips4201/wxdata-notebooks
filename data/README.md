# Notebook data

This directory contains the compact inputs used directly by the public
notebooks and is also the extraction location for the two larger Zenodo data
archives.

## Layout

```text
data/
├── county_weather/       # county points, BA mapping, and population inputs
├── eia860/               # raw and regridded EIA-860 renewable-site inputs
├── gcam_usa/             # eight state electricity-demand scenarios
├── load_actuals/         # raw MISO and cleaned 2023 BA observations
├── model_parameters/     # SAM settings, source periods, and loss assumptions
├── renewable_actuals/    # MISO observed wind and solar generation
├── validation/           # load-validation metadata and predictions
├── wtk_bchrrr_nsrdb_2007_2023/               # Zenodo; ignored by Git
└── taiesm1_historical_ssp245_v022_2000_2099/  # Zenodo; ignored by Git
```

The compact collection contains 100 data files used directly by the notebooks,
including provenance fields retained with those inputs. State-load population
weights use `county_weather/county_populations_2000_to_2020.csv` (`pop_2020`);
the notebook expands those fixed weights into the annual format TELL requires.
Large acquisition HDF5 caches and generated notebook artifacts are not
distributed. See the [input/output guide](../documentation/NOTEBOOK_INPUTS.md)
and [BA coverage guide](../documentation/BA_COVERAGE.md).

## Add the Zenodo datasets

Download both archives from DOI
[10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870), then extract
them from the repository root:

```powershell
python -m zipfile -e "C:/path/to/wxdata_wtk_bchrrr_nsrdb_2007_2023.zip" "data"
python -m zipfile -e "C:/path/to/wxdata_sup3rcc_taiesm1_curated_2000_2099.zip" "data"
```

Confirm the two roots:

```powershell
Test-Path "data/wtk_bchrrr_nsrdb_2007_2023"
Test-Path "data/taiesm1_historical_ssp245_v022_2000_2099"
```

Both commands should return `True`. Do not force-add either data root,
acquisition caches, or `notebook_outputs/` to Git.

These are the archive filenames for dataset version `0.1.0`. Only the outer ZIP
names changed; the internal roots shown above remain unchanged. The climate
model is **TaiESM1** and the upstream Sup3rCC data version is **v0.2.2**.

Keep the three accompanying Zenodo files (`README_DATASET.md`, `LICENSE_DATA.txt`,
and `RELEASE_MANIFEST.csv`) beside the ZIPs. The
[release check](../documentation/START_HERE.md#verify-the-release) uses that folder
to verify checksums and extract just its two inputs into an isolated location.
It does not need a full extraction into `data/`.

On Windows, use a short checkout path such as `C:\work\wxdata-notebooks`.
Deeply nested relative paths can fail even when the extracted file exists.
The two release-check notebooks resolve their paths before opening files.

## Upstream notices

The repository license applies only to Charlie Phillips's copyrightable
contributions to the extent permitted. Upstream materials retain their own
terms and attribution requirements.

### U.S. Energy Information Administration

EIA-860 workbooks and EIA-930-derived load and renewable-generation files
originate with the U.S. Energy Information Administration. EIA states that its
U.S. government publications and data are public domain and recommends source
acknowledgment. See the official
[EIA Copyrights and Reuse policy](https://www.eia.gov/about/copyrights_reuse.php).

Suggested acknowledgment: “Source: U.S. Energy Information Administration,
EIA-860 and EIA-930 data, accessed for this study.”

### NREL and U.S. Department of Energy

Weather-grid mappings, modeled capacity-factor validation series, and SAM
configuration inputs use NREL data or software. Retain the applicable notice,
credit DOE/NREL/Alliance, and consult the
[NREL Disclaimer and Data and Software terms](https://www.nrel.gov/disclaimer.html).

### U.S. Census Bureau

Population, FIPS, and county-point inputs derive from 2020 Census redistricting
and TIGER/Line products. See the Census Bureau
[research transparency policy](https://www.census.gov/topics/research/research-transparency-public-access/policy.html)
and [policies and notices](https://www.census.gov/about/policies.html).

### GCAM-USA

The eight annual state electricity-demand scenario files are GCAM-USA model
outputs. Credit the Joint Global Change Research Institute and consult the
[GCAM-USA documentation](https://github.com/JGCRI/gcam-doc/blob/gh-pages/gcam-usa.md).

## Credentials

Never place API keys, HSDS credentials, access tokens, or local configuration
files in this directory. Store credentials only in an ignored `.env` file or
another untracked credential store.
