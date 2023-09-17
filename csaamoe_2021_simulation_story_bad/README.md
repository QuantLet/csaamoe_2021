[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="1100" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **csaamoe_2021_simulation_story_bad** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: csaamoe_2021_simulation_story_bad

Published in: 'Cryptocurrency as Speculative Asset and Medium of Exchange (Pernice et al., 2021)'

Description: 'This Quantlet runs the price simulation Adaption Story Bad described in the paper. Simulations are triggered with respect to shocks in the fundamental value. Additional simulations show the influence of the models parameters. To run this script, please clone the public repository from https://github.com/trudi-group/csaamoe_simulation_modules into the directory of this Quantlet.'

Keywords: 'price modelling, plotting, price shocks, simulation, cryptocurrency'

Author: Ingolf Pernice, Hermann Elendner, Anna Andresen

See also: other Quantlets in this project

Submitted: 02.09.2023

Datafile: Generic data

```

![Picture1](simulation_story_bad.png)

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
pricemodel.make_simulation_story(params=sim_params, fname="simulation_story_bad", path=SETTINGS["plotting"]["path"])

```

automatically created on 2023-09-17