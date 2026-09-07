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
├── population/           # static county population used for state load
├── renewable_actuals/    # MISO observed wind and solar generation
├── validation/           # load-validation metadata and predictions
├── wtk_bchrrr_nsrdb_2007_2023/               # Zenodo; ignored by Git
└── taiesm1_historical_ssp245_v022_2000_2099/  # Zenodo; ignored by Git
```

Only inputs read by a canonical notebook are committed. Large acquisition HDF5
caches and generated notebook artifacts are not distributed.

## Add the Zenodo datasets

Download both archives from DOI
[10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870), then extract
them from the repository root:

```powershell
Expand-Archive "C:/path/to/wxdata_historical_2007_2023.zip" -DestinationPath "data"
Expand-Archive "C:/path/to/wxdata_taiesm_curated_2000_2099.zip" -DestinationPath "data"
```

Confirm the two roots:

```powershell
Test-Path "data/wtk_bchrrr_nsrdb_2007_2023"
Test-Path "data/taiesm1_historical_ssp245_v022_2000_2099"
```

Both commands should return `True`. Do not force-add either data root,
acquisition caches, or `notebook_outputs/` to Git.

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
