[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="1100" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **csaamoe_2021_instability_simulation_plot_cv_4_qv2** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: csaamoe_2021_instability_simulation_plot_cv_4_qv2

Published in: 'Cryptocurrency as Speculative Asset and Medium of Exchange (Pernice et al., 2021)'

Description: 'Description: This Quantlet runs the price simulation Instability Simulations described in the paper with certain parameters (see SETTINGS.yml). Simulations are triggered with respect to shocks in the fundamental value. Additional simulations show the influence of the models parameters. To run this script, please clone the public repository from https://github.com/trudi-group/csaamoe_simulation_modules into the directory of this Quantlet.'

Keywords: 'price modelling, plotting, price shocks, simulation, cryptocurrency'

Author: Ingolf Pernice, Hermann Elendner, Anna Andresen

See also: other Quantlets in this project

Submitted: 02.09.2023

Datafile: Generic data

```

![Picture1](instability_simulation_plot_cv_4_qv2.png)

### PYTHON Code
```python

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
df = pricemodel.make_instability_simulations_plot(params=sim_params, fname="instability_simulation_plot_cv_4_qv2", path=SETTINGS["plotting"]["path"])

```

automatically created on 2023-09-17