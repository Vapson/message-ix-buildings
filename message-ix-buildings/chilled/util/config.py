import datetime
from dataclasses import dataclass
from typing import Literal

import numpy as np

#from message_ix_buildings.chilled.functions.user_settings import DICT_USER_SETTINGS



@dataclass
class Config:
    """Configuration for :mod:`.message_ix_buildings.chilled`."""

    #: Select user to set the paths to the project and data directories.
    #:
    #: One of: "ALE", "ED", "MEAS", "MEAS_EBRO", "MEAS_UNICC", "QZW".
    user: Literal["ALE", "ED", "MEAS", "MEAS_EBRO", "MEAS_UNICC", 'QZW'] = "QZW"

    #: Set the version of the module run.
    #:
    #: This is used to name the output files and directories.
    vstr: str = "arch2025_2thRun"

    #: Select the climate model.
    #:
    #: One of: "GFDL-ESM4", "IPSL-CM6A-LR", "MPI-ESM1-2-HR", "MRI-ESM2-0", "UKESM1-0-LL"...
    gcm: Literal[
        "GFDL-ESM4", "IPSL-CM6A-LR", "MPI-ESM1-2-HR", "MRI-ESM2-0", "UKESM1-0-LL"
    ] = "GFDL-ESM4"

    #: Select RCP scenario.
    #:
    #: One of: "ssp126", "ssp245", "ssp370", "ssp585", "historical".
    rcp: Literal["ssp126", "ssp245", "ssp370", "ssp585", "historical"] = "historical"

    #: List all possible RCP scenarios.
    rcps = ["ssp126", "ssp245", "ssp370", "ssp585", "historical"]

    #: Set what data to use for the RCP scenario.
    #: If rcp is "baseline", then use "ssp126" data.
    #: Otherwise, use the data corresponding to the RCP scenario selected.
    #rcpdata = "ssp126" if rcp == "baseline" else rcp

    #: Select the version of the country data and floor surface.
    vstrcntry = "v4"  # version string for country data and floor surface

    #: Set paranalysys mode
    #:
    #: 1 = run entire parametric analysis
    #: 0 = run only ref case
    paranalysis_mode = 1  # 1 = run entire parametric analysis; 0 = run only ref case

    #: Select whether to run simple (standard) degree days calculation.
    #:
    #: 1 = run simple (standard) degree days calculation
    #: 0 = don't run
    runsdd = 0  # 1= run simple (standard) degree days calculation; 0 = don't run

    #: Select whether to run testing mode.
    #:
    #: 1 = selects only two years for testing
    #: 0 = select all years (full calculation)
    testing_mode = 0

    #: Select whether to fix population to SSP2.
    popfix = True  # If True, fix to SSP2, else.... (see script 4/5)

    #: Select construction setting.
    constr_setting = 1

    #: Select floor setting. One of:
    #:
    #: - "std_cap": standard capacity
    #: - "per_cap": per capita
    floor_setting: Literal["std_cap", "per_cap"] = "std_cap"

    #: Select building archetypes setting. One of:
    #:
    #: - "fixed": fixed values (same for all regions)
    #: - "regional": different values by MESSAGE region
    arch_setting: Literal["fixed", "regional"] = "regional"

    #: Select urban/rural disaggregations.
    #: Multiple options are allowed. Options:
    #:
    #: - "urban": urban areas
    #: - "rural": rural areas
    urts = ["urban", "rural"]

    #: Select option whether to have verbose output
    verbose = True

    #: Select whether to run cooling calculations.
    #:
    #: 1 = calculate
    #: 0 = skip
    cool = 1

    #: Select whether to run heating calculations.
    #:
    #: 1 = calculate
    #: 0 = skip
    heat = 1

    #: Select solar gain calculation. One of:
    #:
    #: - "TOT": from windows and roof
    #: - "VERT": from windows only
    #: - "HOR": from windows only
    solar_gains: Literal["TOT", "VERT", "HOR"] = "TOT"

    #: Select temperature variable. One of:
    #:
    #: - "tas": near-surface air temperature
    #: - "twb": wet-bulb temperature
    var: Literal["tas", "twb"] = "tas"

    #: Set variable based on temperature variable.
    if var == "tas":
        davar = "tas"
    elif var == "twb":
        davar = "twb"

    overwrite = 0
    
    
    
    #: Spatial resolution
    #: Currently only "R11" is supported.
    #: TODO: In the future, support "R12".
    node: Literal["R11"] = "R11"
    
    
    # output file choice
    daily_output = True
    # gn_sol, ... except for [E_c_ac, E_c_fan, E_h]
    gridded_maps_output = False
    
    # E_c_ac, E_c_fan, E_h
    daily_gridded_maps_output = False
    monthly_gridded_maps_output = True


    project_path: str = r'./Chilled_daily'
    dle_path: str = r'./Chilled_daily/message-ix-buildings-qz/message_ix_buildings/data/dle'
    message_region_file: str = r'./Chilled_daily/message-ix-buildings-qz/message_ix_buildings/data/MESSAGEix_country_region_map.xlsx'
    clim_input = str = r'./climate_data'

    
    #: NetCDF settings
    netcdf4_format = "NETCDF4_CLASSIC"
    comp = dict(zlib=True, complevel=6)  # Compression between 0 and 9 (highest)

    #: Climate years dictionary settings.    
    if rcp == 'historical':
        yeardic = {
            "2015": ("1985", "2014"),
            "2020": ("1985", "2014"),
            "2030": ("1985", "2014"),
            "2040": ("1985", "2014"),
            "2050": ("1985", "2014"),
            "2060": ("1985", "2014"),
            "2070": ("1985", "2014"),
            "2080": ("1985", "2014"),
            "2090": ("1985", "2014"),
            "2100": ("1985", "2014"),
        }
        
    else:    
        yeardic = {
            "2015": ("2015", "2015"),
            "2020": ("2016", "2025"),
            "2030": ("2026", "2035"),
            "2040": ("2036", "2045"),
            "2050": ("2046", "2055"),
            "2060": ("2056", "2065"),
            "2070": ("2066", "2075"),
            "2080": ("2076", "2085"),
            "2090": ("2086", "2095"),
            "2100": ("2096", "2100"),
        }
        
    
    #: Fixed values for buildings settings.
    bal_temps = [18.3, 21.1, 26]  # [21.1] #  For simple cooling degree days
    arb_fan = 2
    t_sp_h = np.int8(20)  # Indoor setpoint temperature for heating
    P_f = 55  # power of fan (W)
    area_fan = 25  # Numer of m2 per fan
    gridshape2 = (600, 1440)

    #: Attributes for netCDF files
    y2_attrs_dic = {
        "title": "map_area_env",
        "authors": "Alessio Mastrucci & Edward Byers",
        #"date": str(datetime.datetime.now()),
        "institution": "IIASA Energy Program",
        "contact": "mastrucc@iiasa.ac.at; byers@iiasa.ac.at; ",
        "arch_setting": arch_setting,
    }

    #: Threshold for number of days (?)
    #: TODO: check if this is the correct description.
    nd_thresh = 5
