# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:54:28 2025

@author: wangq
"""
import os
os.chdir(r'/hdrive/all_users/wangq')

import datetime
import sys
sys.stdout.reconfigure(line_buffering=True)
from argparse import ArgumentParser

from rich.progress import track  # type: ignore


from message_ix_buildings.chilled.core.climate_for_daily import (
    # aggregate_urban_rural_files,
    # create_climate_variables,
    # make_vdd_total_maps,
    # process_construction_shares,
    # process_country_maps,
    # process_final_maps,
    # process_floor_area_maps,
    # process_iso_tables,
    create_daily_climate_variables_and_iso_tables
)

from message_ix_buildings.chilled.util.config import Config  # type: ignore
from message_ix_buildings.chilled.util.util import get_logger

log = get_logger(__name__, log_prefix=f"{Config.gcm}_{Config.rcp}")



def parse_arguments(arguments):
    """

    :return:
    """
    parser = ArgumentParser(add_help=True)

    parser.add_argument(
        "-version",
        "--version",
        default="arch2025_2thRun",
        help="Version of inputs to run. Default: ALPS2023.",
    )
    parser.add_argument(
        "-gcm",
        "--gcm",
        default="KACE-1-0-G",
        help="GCM to run. Options: GFDL-ESM4, IPSL-CM6A-LR, MPI-ESM1-2-HR, MRI-ESM2-0,  UKESM1-0-LL,\
           'ACCESS-ESM1-5', 'BCC-CSM2-MR', 'CMCC-ESM2', 'CNRM-ESM2-1',\
           'CanESM5', 'EC-Earth3', 'FGOALS-g3', 'GISS-E2-1-G'\
           'INM-CM4-8', 'KACE-1-0-G', 'MIROC6', 'NorESM2-MM',\
            Default: GFDL-ESM4.",
    )
    parser.add_argument(
        "-rcp",
        "--rcp",
        default="historical",
        help="RCP to run. Options: ssp126, ssp245, ssp370, ssp585, historical. \
            Default: historical.",
    )

    # Parse arguments
    parsed_arguments = parser.parse_known_args(args=arguments)[0]

    return parsed_arguments


def print_arguments(parsed_arguments):
    """
    :param parsed_arguments:

    """

    # Print arguments
    log.info(
        "\n"
        + "---------- Parsed arguments ------------"
        + "\n"
        + "Selected version: "
        + parsed_arguments.version
        + "\n"
        + "Selected GCM: "
        + parsed_arguments.gcm
        + "\n"
        + "Selected RCP scenario: "
        + parsed_arguments.rcp
    )


# create climate outputs
def create_config(parsed_arguments):
    cfg = Config(
        vstr=parsed_arguments.version,
        gcm=parsed_arguments.gcm,
        rcp=parsed_arguments.rcp,
    )

    return cfg


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parsed_args = parse_arguments(arguments=args)

    # Run the core functions
    start = datetime.datetime.now()
    print_arguments(parsed_arguments=parsed_args)
    cfg = create_config(parsed_arguments=parsed_args)

    for step in track([cfg], description="Running core functions..."):
        # (process_construction_shares(step),)
        # (process_floor_area_maps(step),)
        # (process_country_maps(step),)        
        (create_daily_climate_variables_and_iso_tables(step, start),)
 


if __name__ == "__main__":
    main()
