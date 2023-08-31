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
# >>>>> Understanding               >>>>> -------------------
# -----------------------------------------------------------
# -- PLOT: Showcase weight parameters

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
