# Notebook companion v0.1.0

This release candidate pairs 17 methods, validation, and analysis notebooks
with version `0.1.0` of **Synchronized Wind, Solar, and Load Data for Power System
Planning**. The dataset DOI is [10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870).
It is reserved for the draft and is registered on publication. Dataset and
notebook versions are independent; the execution report identifies the exact
tested notebook commit and dataset manifest.

## Changes

- Download instructions use `wxdata_wtk_bchrrr_nsrdb_2007_2023.zip` and
  `wxdata_sup3rcc_taiesm1_curated_2000_2099.zip`. Archive-internal paths stay the same.
- A repeatable local release check verifies hashes and executes the MISO event
  and Iowa seasonal-risk notebooks with fresh kernels and isolated inputs.
- The two notebooks resolve their input/output paths to avoid the Windows
  relative-path failure found during the initial archive check.
- The environment specifies the numerical and modeling versions used for this
  candidate, with notebook execution and timezone dependencies explicit.

## Review route

1. Read the dataset README for coverage and interpretation. The historical
   collection covers 68 BA-level entries (62 BA codes and six MISO subregions);
   the TaiESM1 collection is curated to eight BA-level entries, their MISO pool,
   and Iowa. Availability differs by product.
2. Follow [Verify the release](START_HERE.md#verify-the-release) for two examples.
   The expected outputs are a MISO figure and an Iowa CSV with 240 rows plus six figures.
3. Use [Notebook inputs and outputs](NOTEBOOK_INPUTS.md) to map other products
   to their notebooks. Data-flow examples do not regenerate the whole deposit.
4. Review the known [Iowa pressure comparison](../notebooks/validation/state_historical_taiesm_validation.ipynb).
   Its roughly -9,369 Pa difference was traced to staged source weather; the
   upstream cause remains unresolved. Passing the two analysis checks does not
   resolve this scientific limitation.

## Publication checks

Prepare the GitHub release from the exact tested commit. Attach the portable
execution report and environment records as review evidence; keep large data
files in Zenodo. Before publishing, complete the following review:

- Verify a clean checkout in the documented freshly created environment.
- Download the five files from the actual Zenodo draft and repeat the check.
- Confirm authorship, author-review statements, citations, license metadata,
  source/model names, coverage, calendars, and scientific limitations.
- Confirm reciprocal links, the dataset version, and the notebook tag/commit.
- Obtain the author's publication decision and set the actual publication date.

The initial successful local check used prepared archives and an existing
environment. Current release-check reports state what has subsequently been
verified. A prepared candidate or reserved DOI is not evidence of publication.
