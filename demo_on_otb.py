import os

import numpy as np

from background_aware_correlation_filter import BackgroundAwareCorrelationFilter
from utils.arg_parse import parse_args

from background_aware_correlation_filter import BackgroundAwareCorrelationFilte
from image_process.feature import get_pyhog
from utils.get_sequence import get_sequence_info, load_image

# if __name__ == "__main__":
#     # This demo script runs the BACF tracker on the included "Bolt" video.
#     params = parse_args()
#     for target in params.target_seq:
#         print("Current sequence : {}".format(target))
#         srdcf_tracker = BackgroundAwareCorrelationFilter(params, target)
#         # Run SRDCF
#         rect_position = srdcf_tracker.track()
#         target_dir = "{0}/{1}".format(params.run_id, target)
#         target_file = '{0}/{1}_{2}.csv'.format(target_dir, params.model_name, target)
#         if not os.path.exists(target_dir):
#             os.makedirs(target_dir)
#         np.savetxt(target_file, rect_position, delimiter=',')

if __name__ == "__main__":
    # This demo script runs the BACF tracker on the included "Bolt" video.
    params = parse_args()
    tracker = BackgroundAwareCorrelationFilte(get_pyhog, admm_lambda=params.admm_lambda,
                                              cell_selection_thresh=params.cell_selection_thresh,
                                              dim_feature=params.dim_feature,
                                              filter_max_area=params.filter_max_area,
                                              feature_ratio=params.feature_ratio,
                                              interpolate_response=params.interpolate_response,
                                              learning_rate=params.learning_rate,
                                              search_area_scale=params.search_area_scale,
                                              reg_window_power=params.reg_window_power,
                                              n_scales=params.n_scales,
                                              newton_iterations=params.newton_iterations,
                                              output_sigma_factor=params.output_sigma_factor,
                                              refinement_iterations=params.refinement_iterations,
                                              reg_lambda=params.reg_lambda,
                                              reg_sparsity_threshold=params.reg_sparsity_threshold,
                                              reg_window_edge=params.reg_window_edge,
                                              reg_window_min=params.reg_window_min,
                                              scale_step=params.scale_step,
                                              search_area_shape=params.search_area_shape,
                                              save_without_showing=params.save_without_showing,
                                              debug=params.debug,
                                              visualization=params.visualization)

    for target in params.target_seq:
        print("Current sequence : {}".format(target))
        # tracker = BackgroundAwareCorrelationFilter(params, target)
        gt_label, image_names, n_frame, init_rect = get_sequence_info(params.path_to_sequences, target)
        images = load_image(image_names)
        # Initialise for current images
        initial_position, initial_scale_factor = tracker.init(images[0], init_rect)
        track = tracker.gen_tracker(images)
        # Run BACF
        for i, (rect_pos, position, scale_factor) in enumerate(track(initial_position, initial_scale_factor)):
            print("{} at {}".format(rect_pos, i))