import argparse
import time

import scipy.io as sio

from src.config import read_config
from src.utils import recon_single, recon_multi


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Reconstruct signal with config file and save the result to specified path"
    )
    parser.add_argument(
        "--config_path",
        type=str,
        default="config/config1.yaml",
        help="Path to the config file",
    )
    parser.add_argument(
        "--result_path", type=str, default="recon.mat", help="Path to save the result"
    )
    args = parser.parse_args()

    config_path = args.config_path
    result_path = args.result_path

    config = read_config(config_path)
    num_devices = config["num_devices"]
    start = time.time()
    if num_devices == 1:
        signal_recon = recon_single(config, 0)
    else:
        signal_recon = recon_multi(config)
    end = time.time()
    sio.savemat(result_path, {"signal_recon": signal_recon})
    print("Reconstruction time: {:.2f}s".format(end - start))
