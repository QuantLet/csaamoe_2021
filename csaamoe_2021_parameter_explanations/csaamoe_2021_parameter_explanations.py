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
    "memory_param_m": [15, 20, 30, 40]
    , "memory_param_v": [25, 30, 35, 40]
    , "amplitude_param_m": [0, 5, 10, 15, 25, 35]
    , "amplitude_param_v": [0, 10, 30, 35, 40, 45]
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "level_shock": 1.05
    , "duration_shock": 1
    , "n": 50
    , "n_shock": 10
    , "precision": 0.1#0.05
    , "plot_cols" : 2
    , "plot_rows" : 2
    , "ylim_prices_from": 0.99
    , "ylim_prices_to": 1.15
    , "fig_space_bottom": 0.40
    , "truncate_zH_until_period": False
    , "width": 8
    , "height": 8
}
pricemodel.make_parameter_illustration(params=sim_params, fname="parameter_explanations", path=SETTINGS["plotting"]["path"])
