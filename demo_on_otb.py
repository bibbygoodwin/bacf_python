import os

import numpy as np

from background_aware_correlation_filter import BackgroundAwareCorrelationFilter
from utils.arg_parse import parse_args

if __name__ == "__main__":
    # This demo script runs the SRDCF tracker on the included "Couple" video.
    # Load video information
    params = parse_args()
    for target in params.target_seq:
        print("Current sequence : {}".format(target))
        srdcf_tracker = BackgroundAwareCorrelationFilter(params, target)
        # Run SRDCF
        rect_position = srdcf_tracker.track()
        target_dir = "{0}/{1}".format(params.run_id, target)
        target_file = '{0}/{1}_{2}.csv'.format(target_dir, params.model_name, target)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        np.savetxt(target_file, rect_position, delimiter=',')