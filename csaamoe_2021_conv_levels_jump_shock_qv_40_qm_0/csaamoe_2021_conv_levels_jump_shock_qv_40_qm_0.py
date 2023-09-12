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
    , "amplitude_param_m": [0]
    , "amplitude_param_v": [4*x for x in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 9, 10]]
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "level_shock": [0.5, 0.75, 1, 1.5, 3, 5, 10, 100]
    , "duration_shock": 50
    , "n": 100
    , "n_shock": 20
    , "precision": 0.0
    , "truncate_zH_until_period": False
    , "sd_threshold_convergence": 0.1
    , "rounding_threshold_monotony": 5
    , "ylim_from": -101
    , "ylim_to": 101
    , "xlim_from": 0
    , "xlim_to": 40
    , "y_label": r'($F_{t}$ - $S_{t}$) in % with t $\in P_{\mathtt{after}}$'
    , "line_lable_before_equality": r'$F_{t}=$'
}
pricemodel.make_plots_parameter_convergence(
    variable="prices"
    , typ_shock="jump"
    , typ_plot="gap"
    , params=sim_params
    , path=SETTINGS["plotting"]["path"]
    , fname="conv_levels_jump_shock_qv_40_qm_0"
)
