# Running the notebooks

Saved results can be reviewed on GitHub without installing anything. Use this
guide to run the notebooks locally; dataset coverage and interpretation are in
the [README](README.md).

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
