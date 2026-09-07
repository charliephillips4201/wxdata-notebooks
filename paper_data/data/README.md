# Notebook data directory

This directory combines two distribution channels:

- `source_inputs/` contains 113 compact source, provenance, model-parameter,
  and validation inputs committed with the GitHub notebooks.
- `wtk_bchrrr_nsrdb_2007_2023/` and
  `taiesm1_historical_ssp245_v022_2000_2099/` contain the large curated datasets
  distributed through Zenodo DOI
  [10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870).

The two large dataset directories are ignored by Git. Download both ZIP files
from Zenodo and extract them into this directory. From the repository root in
PowerShell, for example:

```powershell
Expand-Archive "C:/path/to/wxdata_historical_2007_2023.zip" -DestinationPath "paper_data/data"
Expand-Archive "C:/path/to/wxdata_taiesm_curated_2000_2099.zip" -DestinationPath "paper_data/data"
```

The resulting layout should be:

```text
paper_data/data/
├── source_inputs/                                  # GitHub
├── wtk_bchrrr_nsrdb_2007_2023/                    # Zenodo
└── taiesm1_historical_ssp245_v022_2000_2099/       # Zenodo
```

You can confirm that both extracted roots are present with:

```powershell
Test-Path "paper_data/data/wtk_bchrrr_nsrdb_2007_2023"
Test-Path "paper_data/data/taiesm1_historical_ssp245_v022_2000_2099"
```

Both commands should return `True`. See
[`../documentation/NOTEBOOK_INPUTS.md`](../documentation/NOTEBOOK_INPUTS.md) for
the data products used by each notebook.

Do not force-add the extracted Zenodo data, HDF5 acquisition caches, or
notebook-generated output directories to Git.
