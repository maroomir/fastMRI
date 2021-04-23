import fastmri_examples.unet.unet_knee_sc_leaderboard_20201111
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.set_defaults(
        challenge="singlecoil",
        data_path="D:\Git\FastMRI\Data",
        mask_type="random",
        sample_rate=0.1)
    args = parser.parse_args()
    fastmri_examples.unet.unet_knee_sc_leaderboard_20201111.cli_main(args=args)
