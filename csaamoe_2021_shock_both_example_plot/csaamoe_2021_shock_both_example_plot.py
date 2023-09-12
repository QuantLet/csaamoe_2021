# -----------------------------------------------------------
# >>>>> General things >>>>> -------------------------------------
# -----------------------------------------------------------
# General modules
import numpy as np
import pandas as pd
import numpy as np
import yaml
import importlib
import sys
import os

path_settings = "./SETTINGS.yml"
path_gen_helpers = "./csaamoe_simulation_modules/gen_helpers.py"

# Change CWD
#os.chdir("/YOUR/DIRECTORY/csaamoe_2021/")

# Import settings
with open(path_settings, 'r') as stream:
    try:
        SETTINGS = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Import general helpers
spec = importlib.util.spec_from_file_location("noname", path_gen_helpers)
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)

# Import own modules
sys.path.append('./csaamoe_simulation_modules/')
import pricemodel

# -----------------------------------------------------------
# >>>>> Simulation                  >>>>> -------------------
# -----------------------------------------------------------
sim_params = {
    "memory_param_m": [40]
    , "memory_param_v": [40]
    , "amplitude_param_m": [10,15,20,25]
    , "amplitude_param_v": [20]
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 150
    , "n_tx_shock_start": 50
    , "n_tx_shock_end": 55
    , "n_fv_shock_start": 1
    , "n_fv_shock_end": 20
    , "tx_shock": [50]
    , "fv_shock": [0.006,0.055]#[0.019,0.120]#[-0.05,0.11]
    , "ylim_from": 450
    , "ylim_to": 900
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.0
    , "truncate_zH_until_period": 49
    , "fig_space_bottom": 0.20
    , "width": 8
    , "height": 5
}
pricemodel.make_simulation_shock_both(params=sim_params, fname="shock_both_example_plot", path=SETTINGS["plotting"]["path"])
