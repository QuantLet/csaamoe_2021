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
# >>>>> Understanding               >>>>> -------------------
# -----------------------------------------------------------
# -- PLOT: Showcase weight parameters

params_1 = {
    "memory_param_m": [15, 20, 30, 40]
    , "memory_param_v": [25, 30, 35, 40]
    , "amplitude_param_m": [0, 5, 15, 25, 35]
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
    , "precision": 0.05
    , "plot_cols" : 2
    , "plot_rows" : 2
    , "ylim_prices_from": 0.99
    , "ylim_prices_to": 1.15
    , "fig_space_bottom": 0.40
    , "truncate_zH_until_period": False
    , "width": 8
    , "height": 8
}
pricemodel.make_parameter_illustration(params=params_1, fname="parameter_explanations", path=SETTINGS["plotting"]["path"])

params_2 = {
    "memory_param_m": 40
    , "memory_param_v": 40
    , "amplitude_param_m": [0, 15, 20, 25]
    , "amplitude_param_v": 30
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "level_shock_1": 1.50
    , "level_shock_2": 1.00
    , "level_shock_3": 0.75
    , "level_shock_4": 1.00
    , "n": 130
    , "n_shock_1": 10
    , "n_shock_2": 40
    , "n_shock_3": 70
    , "n_shock_4": 100
    , "ylim_prices_from": 0.5
    , "ylim_prices_to": 3
    , "ylim_modelvars_from": 0
    , "ylim_modelvars_to": 1200
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.05
    , "fig_space_bottom": 0.40
    , "truncate_zH_until_period": False
}
pricemodel.make_simulation_shift_fv(params=params_2, fname="jump_up_and_down", path=SETTINGS["plotting"]["path"])

# params_3 = "deprecated"

params_4 = {
    "memory_param_m": 40
    , "memory_param_v": 40
    , "amplitude_param_m": [0, 5, 15, 25]
    , "amplitude_param_v": 30
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "level_shock": 600
    , "n": 100
    , "n_shock": 10
    , "duration_shock": 20
    , "ylim_prices_from": 0.8
    , "ylim_prices_to": 1.3
    , "ylim_modelvars_from": 250
    , "ylim_modelvars_to": 1200
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.05
    , "fig_space_bottom": 0.40
    , "truncate_zH_until_period": False
}
pricemodel.make_simulation_temporary_shock_txvol(params=params_4, fname="shock_to_cash_balance", path=SETTINGS["plotting"]["path"])

params_5 = {
    "memory_param_m": 40
    , "memory_param_v": 40
    , "amplitude_param_m": [0, 20, 22.5, 25]
    , "amplitude_param_v": 30
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 360
    , "level_shock_1": 0.025
    , "level_shock_2": 0.025
    , "n_shock_1_start": 30
    , "n_shock_1_end": 130
    , "n_shock_2_start": 230
    , "n_shock_2_end": 330
    , "ylim_prices_from": 0.8
    , "ylim_prices_to": 5
    , "ylim_modelvars_from": 200
    , "ylim_modelvars_to": 1200
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.05
    , "fig_space_bottom": 0.40
    , "truncate_zH_until_period": False
}
pricemodel.make_simulation_increasing_fv(params=params_5, fname="showoff_stabilization", path=SETTINGS["plotting"]["path"])

# params_6 = "deprecated"

params_7_1 = {
    "memory_param_m": [4]
    , "memory_param_v": [4]
    , "amplitude_param_m": [0]
    , "amplitude_param_v": [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 9, 10]
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "level_shock": [-0.01, -0.005, 0.01, 0.02, 0.08, 0.18]
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
    , "xlim_to": 10
    , "y_label": r'($F_{t}$ - $S_{t}$) in % with t $\in P_{\mathtt{after}}$'
    , "line_lable_before_equality": r'$F_{t}=$'
}
pricemodel.make_plots_parameter_convergence(
    variable="prices"
    , typ_shock="linear_increase"
    , typ_plot="gap"
    , params=params_7_1
    , path=SETTINGS["plotting"]["path"]
    , fname="conv_levels_linear_shock_qv_4_qm_0"
)

params_7_2 = {
    "memory_param_m": [4]
    , "memory_param_v": [4]
    , "amplitude_param_m": [0]
    , "amplitude_param_v": [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 9, 10]
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "level_shock": [0.5, 0.75, 1.5, 2, 5, 10]
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
    , "xlim_to": 10
    , "y_label": r'($F_{t}$ - $S_{t}$) in % with t $\in P_{\mathtt{after}}$'
    , "line_lable_before_equality": r'$F_{t}=$'
}
pricemodel.make_plots_parameter_convergence(
    variable="prices"
    , typ_shock="jump"
    , typ_plot="gap"
    , params=params_7_2
    , path=SETTINGS["plotting"]["path"]
    , fname="conv_levels_jump_shock_qv_4_qm_0"
)

params_7_3 = {
    "memory_param_m": [40]
    , "memory_param_v": [40]
    , "amplitude_param_m": [10]
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
    , params=params_7_3
    , path=SETTINGS["plotting"]["path"]
    , fname="conv_levels_linear_shock_qv_40_qm_10"
)

params_7_4 = {
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
    , params=params_7_4
    , path=SETTINGS["plotting"]["path"]
    , fname="conv_levels_jump_shock_qv_40_qm_0"
)

params_7_5 = {
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
    , "level_shock": [-0.01, -0.005, 0.01, 0.02, 0.08, 0.18]
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
    , typ_shock="linear_increase"
    , typ_plot="gap"
    , params=params_7_5
    , path=SETTINGS["plotting"]["path"]
    , fname="conv_levels_linear_shock_qv_40_qm_0"
)

params_8 = {
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
pricemodel.make_simulation_shock_both(params=params_8, fname="shock_both_example_plot", path=SETTINGS["plotting"]["path"])

params_9_0 = {
    "memory_param_m": [40]
    , "memory_param_v": [40]
    , "amplitude_param_m": [10, 20, 30, 40]
    , "amplitude_param_v": [20]
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 300
    , "n_tx_shock_start": 100
    , "n_tx_shock_end": 101
    , "n_fv_shock_start": 1
    , "n_fv_shock_end": 20
    , "tx_shock": [100]
    , "fv_shock": np.linspace(-0.25, 0.15, 200)
    , "xlim_from": 0
    , "xlim_to": 100
    , "ylim_from": 0
    , "ylim_to": 0.00075
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.0
    , "truncate_zH_until_period": 49
    , "staging_head": 30
    , "staging_tail": 30
    , "thresh_var_stability": 1e-10
    , "fig_space_bottom": 0.20
}
df = pricemodel.make_instability_simulations_plot(params=params_9_0, fname="instability_simulation_plot_cv_40_qv20", path=SETTINGS["plotting"]["path"])


params_9_1 = {
    "memory_param_m": [4]
    , "memory_param_v": [4]
    , "amplitude_param_m": [1, 2, 3, 4]
    , "amplitude_param_v": [2]
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 300
    , "n_tx_shock_start": 100
    , "n_tx_shock_end": 101
    , "n_fv_shock_start": 1
    , "n_fv_shock_end": 20
    , "tx_shock": [100]
    , "fv_shock": np.linspace(-0.25, 0.15, 200)
    , "xlim_from": 0
    , "xlim_to": 100
    , "ylim_from": 0
    , "ylim_to": 0.002
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.0
    , "truncate_zH_until_period": 49
    , "staging_head": 30
    , "staging_tail": 30
    , "thresh_var_stability": 1e-10
    , "fig_space_bottom": 0.20
}
df = pricemodel.make_instability_simulations_plot(params=params_9_1, fname="instability_simulation_plot_cv_4_qv2", path=SETTINGS["plotting"]["path"])


params_9_2 = {
    "memory_param_m": [40]
    , "memory_param_v": [40]
    , "amplitude_param_m": [10, 20, 30, 40]
    , "amplitude_param_v": [40]
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 300
    , "n_tx_shock_start": 100
    , "n_tx_shock_end": 101
    , "n_fv_shock_start": 1
    , "n_fv_shock_end": 20
    , "tx_shock": [100]
    , "fv_shock": np.linspace(-0.25, 0.15, 200)
    , "xlim_from": 0
    , "xlim_to": 100
    , "ylim_from": 0
    , "ylim_to": 0.00075
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.0
    , "truncate_zH_until_period": 49
    , "staging_head": 30
    , "staging_tail": 30
    , "thresh_var_stability": 1e-10
    , "fig_space_bottom": 0.20
}
df = pricemodel.make_instability_simulations_plot(params=params_9_2, fname="instability_simulation_plot_cv_40_qv40", path=SETTINGS["plotting"]["path"])


params_9_3 = {
    "memory_param_m": [40]
    , "memory_param_v": [40]
    , "amplitude_param_m": [10, 20, 30, 40]
    , "amplitude_param_v": [10]
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 300
    , "n_tx_shock_start": 100
    , "n_tx_shock_end": 101
    , "n_fv_shock_start": 1
    , "n_fv_shock_end": 20
    , "tx_shock": [100]
    , "fv_shock": np.linspace(-0.25, 0.15, 200)
    , "xlim_from": 0
    , "xlim_to": 100
    , "ylim_from": 0
    , "ylim_to": 0.00075
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.0
    , "truncate_zH_until_period": 49
    , "staging_head": 30
    , "staging_tail": 30
    , "thresh_var_stability": 1e-10
    , "fig_space_bottom": 0.20
}
df = pricemodel.make_instability_simulations_plot(params=params_9_3, fname="instability_simulation_plot_cv_40_qv10", path=SETTINGS["plotting"]["path"])


params_12_0 = {
    "memory_param_m": 4
    , "memory_param_v": 4
    , "amplitude_param_m": [0,3.1,3.2,3.3]
    , "amplitude_param_v": 2
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 200
    , "n_tx_shock_start": 100
    , "n_tx_shock_end": 131
    , "n_fv_shock_up_start": 20
    , "n_fv_shock_up_end": 51
    , "n_fv_shock_down_start": 100
    , "n_fv_shock_down_end": 131
    , "tx_shock": 10
    , "fv_shock_up": 6/300
    , "fv_shock_down": 0
    , "ylim_prices_from": 0.95
    , "ylim_prices_to": 1.8
    , "ylim_modelvars_from": 400
    , "ylim_modelvars_to": 1200
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.0
    , "truncate_zH_until_period": False
    , "fig_space_bottom": 0.40
}
pricemodel.make_simulation_story(params=params_12_0, fname="simulation_story_good", path=SETTINGS["plotting"]["path"])


params_12_1 = {
    "memory_param_m": 4
    , "memory_param_v": 4
    , "amplitude_param_m": [0,3.1,3.2,3.3]
    , "amplitude_param_v": 2
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 150
    , "n_tx_shock_start": 51
    , "n_tx_shock_end": 81
    , "n_fv_shock_up_start": 20
    , "n_fv_shock_up_end": 51
    , "n_fv_shock_down_start": 100
    , "n_fv_shock_down_end": 101
    , "tx_shock": 10/3
    , "fv_shock_up": 2/300
    , "fv_shock_down": 0
    , "ylim_prices_from": 0.95
    , "ylim_prices_to": 1.3#1.3
    , "ylim_modelvars_from": 400
    , "ylim_modelvars_to": 1200
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.01
    , "truncate_zH_until_period": False
    , "fig_space_bottom": 0.40
}
pricemodel.make_simulation_story(params=params_12_1, fname="simulation_story_good_lockstep", path=SETTINGS["plotting"]["path"])

params_12_2 = {
    "memory_param_m": 4
    , "memory_param_v": 4
    , "amplitude_param_m": [0, 3.1, 3.2, 3.3]
    , "amplitude_param_v": 2
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 200
    , "n_tx_shock_start": 100
    , "n_tx_shock_end": 131
    , "n_fv_shock_up_start": 20
    , "n_fv_shock_up_end": 51
    , "n_fv_shock_down_start": 100
    , "n_fv_shock_down_end": 101
    , "tx_shock": 0
    , "fv_shock_up": 6 / 300
    , "fv_shock_down": - 6 / 300
    , "ylim_prices_from": 0.95
    , "ylim_prices_to": 1.8
    , "ylim_modelvars_from": 400
    , "ylim_modelvars_to": 1200
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.0
    , "truncate_zH_until_period": False
    , "fig_space_bottom": 0.40
}
pricemodel.make_simulation_story(params=params_12_2, fname="simulation_story_bad", path=SETTINGS["plotting"]["path"])

# -----------------------------
params_12_0 = {
    "memory_param_m": 40
    , "memory_param_v": 40
    , "amplitude_param_m": [0, 10, 20, 30 ]
    , "amplitude_param_v": 2
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 200
    , "n_tx_shock_start": 100
    , "n_tx_shock_end": 131
    , "n_fv_shock_up_start": 20
    , "n_fv_shock_up_end": 21
    , "n_fv_shock_down_start": 100
    , "n_fv_shock_down_end": 101
    , "tx_shock": 10
    , "fv_shock_up": (6 / 300) * 30
    , "fv_shock_down": 0#- (6 / 300) * 30
    , "ylim_prices_from": 0.95
    , "ylim_prices_to": 3
    , "ylim_modelvars_from": 400
    , "ylim_modelvars_to": 1200
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.0
    , "truncate_zH_until_period": False
    , "fig_space_bottom": 0.50
}
pricemodel.make_simulation_story(params=params_12_0, fname="simulation_story_good", path=SETTINGS["plotting"]["path"])


params_12_1 = {
    "memory_param_m": 40
    , "memory_param_v": 40
    , "amplitude_param_m": [0, 10, 20, 25]
    , "amplitude_param_v": 2
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 200
    , "n_tx_shock_start": 21
    , "n_tx_shock_end": 52
    , "n_fv_shock_up_start": 20
    , "n_fv_shock_up_end": 21
    , "n_fv_shock_down_start": 100
    , "n_fv_shock_down_end": 101
    , "tx_shock": 10
    , "fv_shock_up": (6 / 300) * 30
    , "fv_shock_down": 0  # - (6 / 300) * 30
    , "ylim_prices_from": 0.95
    , "ylim_prices_to": 3
    , "ylim_modelvars_from": 400
    , "ylim_modelvars_to": 1200
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.0
    , "truncate_zH_until_period": False
    , "fig_space_bottom": 0.50
}
pricemodel.make_simulation_story(params=params_12_1, fname="simulation_story_good_lockstep", path=SETTINGS["plotting"]["path"])

params_12_2 = {
    "memory_param_m": 40
    , "memory_param_v": 40
    , "amplitude_param_m": [0, 10, 20, 30]
    , "amplitude_param_v": 2
    , "m_total_baseline": 1000
    , "onchain_vol_usd_baseline": 500
    , "v_circ_baseline": 1
    , "fv_iter_start": 1
    , "prices_iter_start_1": 1
    , "prices_iter_start_2": 1
    , "n": 200
    , "n_tx_shock_start": 100
    , "n_tx_shock_end": 131
    , "n_fv_shock_up_start": 20
    , "n_fv_shock_up_end": 21
    , "n_fv_shock_down_start": 100
    , "n_fv_shock_down_end": 101
    , "tx_shock": 0
    , "fv_shock_up": (6 / 300) * 30
    , "fv_shock_down": - (6 / 300) * 30
    , "ylim_prices_from": 0.95
    , "ylim_prices_to": 3
    , "ylim_modelvars_from": 400
    , "ylim_modelvars_to": 1200
    , "plot_rows": 1
    , "plot_cols": 2
    , "precision": 0.0
    , "truncate_zH_until_period": False
    , "fig_space_bottom": 0.50
}
pricemodel.make_simulation_story(params=params_12_2, fname="simulation_story_bad", path=SETTINGS["plotting"]["path"])
