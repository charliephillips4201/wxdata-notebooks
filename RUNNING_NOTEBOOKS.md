# Running the notebooks

Saved results can be reviewed on GitHub without installing anything. Use this
guide to run the notebooks locally; dataset coverage and interpretation are in
the [README](README.md).

## Get the repository

With Git installed, open a terminal in the directory where you want the checkout:

```shell
git clone https://github.com/charliephillips4201/wxdata-notebooks.git
cd wxdata-notebooks
```

Alternatively, choose **Code → Download ZIP** on the
[GitHub repository](https://github.com/charliephillips4201/wxdata-notebooks), extract
the ZIP, and open a terminal in the extracted folder containing `environment.yml`.
The selected example data are included; the first example does not require the
full Zenodo archives.

## Set up the environment

With Conda installed, run these commands from the repository root (the folder
containing `environment.yml`):

```shell
conda env create -f environment.yml
conda activate wxdata-notebooks
python -m ipykernel install --user --name wxdata-notebooks --display-name "Python (wxdata-notebooks)"
jupyter lab notebooks
```

This registers the environment as **Python (wxdata-notebooks)**. In each
notebook, use **Kernel → Change Kernel** to select it, even if another kernel
is already selected. Published notebooks retain `wxdata` or `python3` kernel
names, which do not guarantee the repository environment is active.

On later visits, only activate the environment and start JupyterLab;
environment creation and kernel registration are one-time steps.

On Windows, a short checkout path such as `C:/work/wxdata-notebooks` helps avoid
path-length problems with the dataset filenames.

## Run a first example

Open [MISO load-duration curve](notebooks/validation/miso_load_duration_curve.ipynb)
under `validation/` in JupyterLab. Select the kernel above, then
**Restart Kernel and Run All**. Keep `YEAR = 2023` to use the bundled inputs.

All inputs for this example are bundled. It needs no dataset download, weather
service, or model training. It displays one figure and saves:

```text
data_outputs/validation/miso_load_duration_curve/miso_2023_load_duration_curve.png
```

Keep notebooks in their existing folders: their paths are relative to those
folders. Each notebook states its inputs and writes generated files under
`data_outputs/` where applicable. The [notebook index](README.md#notebook-index)
lists the other examples and their requirements.

Examples with bundled inputs can run independently. You do not need to execute
the entire data-flow pipeline first; check the selected notebook's requirements,
then run its cells from top to bottom.

## Notebooks with additional requirements

| Notebook or stage | What rerunning requires |
| --- | --- |
| [County point selection](notebooks/data_flow/county_weather_point_selection.ipynb) and [EIA regridding](notebooks/data_flow/eia860_regridding_methodology.ipynb): grid matching | A configured local HSDS service at `http://localhost:5101` with access to `nrel-pds-hsds`. Earlier preparation steps use bundled files. |
| [County weather aggregation](notebooks/data_flow/county_hsds_download_and_ba_weather_aggregation.ipynb): weather staging | Weather caches that pass the notebook's checks, or the same HSDS service to download missing files. |
| [Site CF generation](notebooks/data_flow/site_cf_generation_ba_weighting_validation.ipynb) | Local reV/PySAM model execution, plus checked weather caches or HSDS for missing weather files. |
| [TELL load forecasting](notebooks/data_flow/tell_load_forecast_data_flow.ipynb) | Local calibration, model training, and prediction with TELL. The [state-load example](notebooks/data_flow/state_load_generation.ipynb) instead runs allocation and scaling from bundled BA forecasts. |
| [Satellite and reanalysis context](notebooks/analysis/plot_satellite_and_reanalysis.ipynb) | Network access to NASA Worldview and NOAA PSL. |

The environment specification includes the modeling libraries; it does not
start an HSDS service or supply its access configuration. Acquisition settings
and cache checks are beside the relevant notebook stages. Acquisition H5 caches
are not bundled with the repository.

## Troubleshooting

- **Missing imports or the wrong Python environment:** select **Python (wxdata-notebooks)**
  under **Kernel → Change Kernel**, then restart the kernel and run all cells.
  If that kernel is missing, activate the Conda environment and repeat the kernel
  registration command above.
- **Missing input files:** keep notebooks in their original folders and confirm
  that the repository's `data_inputs/` folder was cloned or extracted too. Paths
  are relative to each notebook folder. Keep the example's documented year and
  region when using bundled data; another selection may require full-release inputs.
- **Connection refused at `localhost:5101`:** a required local HSDS service is not
  reachable. Follow the [HSDS guidance](README.md#hsds-and-external-data-access)
  and the notebook's connection settings. Creating the Conda environment does not
  start HSDS; the first example above does not need it.
