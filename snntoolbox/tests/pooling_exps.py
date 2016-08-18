"""Running experiments for max-pooling experiments

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
import os
import argparse
import json

import snntoolbox

home_path = os.environ["HOME"]
pref_dir = os.path.join(home_path, ".snntoolbox", "preferences")
log_dir = os.path.join(home_path, "workspace", "snntoolbox-log", "pool-exps")
data_dir = os.path.join(home_path, ".snntoolbox", "datasets")


def maxpool_exp(exp_name, model_name, pref_name, dataset):
    """Max-Pooling experiment routine.

    Parameters
    ----------
    exp_name : string
        the name of the experiment
    model_name : string
        the name of the model
    pref_name : string
        the name of the perference
    dataset : string
        the name of the dataset, mnist or cifar10
    """
    pref_path = os.path.join(pref_dir, pref_name)
    log_path = os.path.join(log_dir, exp_name)
    data_path = os.path.join(data_dir, dataset)

    if not os.path.exists(pref_path):
        raise ValueError("The target preference "
                         "file %s is not existed!" % (pref_path))

    print ("[MESSAGE] Loading Experiment settings.")
    settings = json.load(open(pref_path))

    settings["log_dir_of_current_run"] = log_path
    settings["runlabel"] = exp_name
    settings["dataset_path"] = data_path
    settings["filename"] = model_name

    snntoolbox.update_setup(settings)

    snntoolbox.test_full()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Running Max-Pooling \
                                     Experiments by Yuhuang Hu")
    parser.add_argument("-e", "--exp-name", type=str,
                        help="Experiment name.")
    parser.add_argument("-m", "--model-name", type=str,
                        help="The name of the model")
    parser.add_argument("-p", "--pref-name", type=str,
                        help="Destination of the json perf file.")
    parser.add_argument("-d", "--dataset", type=str,
                        help="type of the datset, mnist or cifar10")
    # as there is no setting parameters for this, not simply omit.
    parser.add_argument("--pool-type", type=str,
                        default="avg_max",
                        help="The type of max-pooling")
    args = parser.parse_args()
    maxpool_exp(**vars(args))
