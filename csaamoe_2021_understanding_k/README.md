[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="1100" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **csaamoe_2021_understanding_k** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: csaamoe_2021_understanding_k

Published in: 'Cryptocurrency as Speculative Asset and Medium of Exchange (Pernice et al., 2021)'

Description: 'This Quantlet generates the kvariation.png plot and weightsvariation.plot. Two plots to understand the workings of the presented price model better. To run this script, please clone the public repository from https://github.com/trudi-group/csaamoe_simulation_modules of Weizenbaum Institut into the directory of this Quantlet.'

Keywords: 'price modelling, plotting, simulation, cryptocurrency, price shocks'

Author: Ingolf Pernice, Hermann Elendner, Anna Andresen

See also: other Quantlets in this project

Submitted: 02.09.2023

Datafile: Generic data

```

![Picture1](weights_variation.png)

### PYTHON Code
```python

# -----------------------------------------------------------
# >>>>> General things >>>>> -------------------------------------
# -----------------------------------------------------------
# General modules
import yaml
import importlib
import sys

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
pricemodel.plot_weight_shifts(path=SETTINGS["plotting"]["path"]
                              , memory_params=[4,10]
                              , amplitude_params=[0.5,2]
                              , idx_t=50)

pricemodel.make_k_plot(
    zetas_m_from=-5
    , zetas_v_from = -5
    , zetas_m_to = 5
    , zetas_v_to = 5
    , steps = 100
    , amplitude_param_m = 1000
    , amplitude_param_v = 1000
    , memory_param_m = 1000
    , memory_param_v = 1000
    , type_k = "tanh" #"linear"
    , path=SETTINGS["plotting"]["path"]
)

```

automatically created on 2023-09-21