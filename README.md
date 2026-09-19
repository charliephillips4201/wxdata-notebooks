# Synchronized Wind, Solar, and Load Data for Power System Planning

This repository shows how weather, electricity demand, and wind and solar
resources are combined for power-system planning. Its 17 Jupyter notebooks
explain construction methods, compare modeled and observed data, and explore
net load, pooling, and stress events. Saved tables and figures support review
on GitHub without installing software or downloading data.

A **balancing authority (BA)** manages electricity supply and demand in a
region. A **capacity factor (CF)** expresses output as a fraction of nameplate
capacity. Here, **net load** is demand minus wind and solar generation.
**MISO**, the Midcontinent Independent System Operator, is a recurring example.

## Start here

- **Review a first result:** open the [MISO load-duration notebook](notebooks/analysis/miso_load_duration_curve.ipynb).
  It compares the distribution and timing of actual and modeled 2023 load.
- **Run that example:** follow the installation steps below. All its inputs
  are included in this repository; it needs no Zenodo download or weather service.
- **Explore the methods:** use the [notebook index and input/output guide](documentation/NOTEBOOK_INPUTS.md#notebook-inputs).
  It lists all 17 notebooks in their methods order, with their requirements and outputs.
- **Check regional coverage:** the [BA coverage reference](documentation/BA_COVERAGE.md)
  lists entity names, fleets, available products, scenarios, pools, and exclusions.

The notebook release candidate is `v0.1.0`, paired with dataset version `0.1.0`.
These versions are independent. Dataset DOI
[10.5281/zenodo.21844870](https://doi.org/10.5281/zenodo.21844870) is reserved for
the Zenodo draft and becomes resolvable when that record is published. See
[publication status and remaining checks](documentation/NOTEBOOK_INPUTS.md#publication-status).

## Install and run the first example

With Conda installed, run these commands from the repository root:

```powershell
conda env create -f environment.yml
conda activate wxdata-notebooks
jupyter lab notebooks
```

On Windows, use a short checkout path such as `C:/work/wxdata-notebooks` to
avoid path-length failures. Open `analysis/miso_load_duration_curve.ipynb`
and select **Restart Kernel and Run All**. It displays one figure and saves
its PNG under `notebook_outputs/analysis/miso_load_duration_curve/`.

Other notebooks may require the [large datasets](documentation/NOTEBOOK_INPUTS.md#download-the-datasets),
a configured HSDS weather service, or TELL/reV/PySAM reconstruction. Check each
notebook's requirements before running it. The [two-notebook release check](documentation/NOTEBOOK_INPUTS.md#verify-the-release)
uses one input from each archive and needs no weather-service credentials.
[Execution notes](documentation/NOTEBOOK_INPUTS.md#execution-notes) distinguish
verified local stages from retained acquisition or model results.

## How the pieces fit

![Method relationships from source weather and load through construction, scenario metrics, validation, stress catalogs, and analysis.](documentation/process_flow.svg)

The data-flow notebooks teach bounded examples along the load and renewable
branches. The diagram shows method relationships; running one example does not
supply the complete inputs for the next. Each notebook reads its stated inputs
directly. Equations, assumptions, and interpretations stay beside the code.

| Weather collection | Period | Use |
| --- | --- | --- |
| WTK / BC-HRRR / NSRDB | 2007-2023 | Historical wind and load weather from WTK (2007-2014) and BC-HRRR (2015-2023), with NSRDB solar resource and load-weather GHI throughout. |
| sup3rCC / TaiESM1 | 2000-2099 | Historical and simulated future climate inputs for selected BA, pooled-region, and Iowa analyses. |

## Repository contents

- `notebooks/`: eight data-flow, four validation, and five analysis notebooks.
- `data/`: 94 bundled data files; larger Zenodo datasets are extracted here and ignored by Git.
- `manifests/`: three metadata manifests.
- `documentation/`: the input/output guide, BA coverage reference, and process diagram.
- `scripts/check_release.py`: the existing archive and two-notebook execution check.
- `environment.yml`: the environment specification for this candidate.

Standalone notebook outputs and working caches go under ignored
`notebook_outputs/`. The Zenodo deposit contains data, not notebooks or notebook
outputs. The private operational package, production scripts, production test
suite, and run configurations are outside this repository.

## Citation and license

Repository authorship and citation metadata are in [CITATION.cff](CITATION.cff).
Cite the dataset separately using its Zenodo record when published.

Unless otherwise noted, the original notebooks and documentation contributed
by Charlie Phillips are licensed under the
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
See [LICENSE](LICENSE). Third-party data and software retain their original
licenses and attribution requirements. The [source inventory and upstream notices](documentation/NOTEBOOK_INPUTS.md#sources-and-attribution)
preserve those acknowledgments; inclusion here does not relicense those materials.

## AI assistance

Generative AI tools were used to assist with drafting and editing portions of
the documentation and notebook code. All resulting material was reviewed,
tested, and accepted by Charlie Phillips, who takes responsibility for the
content of this repository.
