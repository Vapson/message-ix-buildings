# Message-ix-Buildings

This is a fork of the [Message-ix Buildings](https://github.com/main/message-ix-buildings) repository. This extension primarily extend the original codebase to support **daily resolution** output for the CHILLED model.


## Description

This branch builds upon the original codebase to estimate daily heating/cooling energy intensity using climate model data and scenarios. It integrates spatial and temporal data inputs to produce high-resolution, grid-based output suitable for large-scale analysis. The resulting energy intensities are then combined with the projection of building stock dynamics from the STURM to derive energy demand.


## Main Inputs & Outputs

- **Inputs**:  
  - Daily near-surface air temperature (`tas`, i.e., daily mean temperature)  
  - Building types and associated thermal/structural parameters  
  - Behavioral and operational assumptions (e.g., set-point temperatures)

- **Outputs**:  
  - **Annual** Annual energy demand intensity, weighted by population distribution (in Excel format)  
  - **Daily** Daily energy demand intensity, weighted by population distribution (in NetCDF format)  
  - Outputs are categorized by **country** and corresponding **climate zones**


## Run CHILLED

Before running the model, you need to configure the following files:

- **Setup configuration file**: Set parameters in `./chilled/util/config.py`
- **Setup script configuration**: Set parameters in `run_preprocess.py` and `run_preprocess.py`
- **Run script configuration**: run the following files in order
  - `run_preprocess.py`
  - `run_main.py`


#### Default Settings

In our default version, the following key configurations are applied to save running time and disk space:
- daily_output = True
- gridded_maps_output = False (e.g. gn_sol, ... except for [E_c_ac, E_c_fan, E_h])
- daily_gridded_maps_output = True (including vdd_tmax_c, E_c_ac, E_c_fan, vdd_h, E_h)
- monthly_gridded_maps_output = False (including E_c_ac, E_c_fan, E_h)
**Note:**  
Daily output is recommended because the gridded climate impact only needs to be simulated once. Subsequent further postprocessing can be performed efficiently without rerunning the entire simulation. However, please be aware that exporting daily outputs can consume significant disk space.
Monthly gridded outputs provide a useful compromise between temporal detail and storage efficiency for long-term scenario analysis under different SSPs.




