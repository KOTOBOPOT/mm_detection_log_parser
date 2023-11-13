import os
import shutil
import argparse

from mm_det_log_parse import LogParser
from find_files import find_train_logs


def save_plots(json_path, save_folder, exp_name):
    save_path = os.path.join(save_folder, exp_name)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    parser = LogParser(json_path)
    parser.train_df.to_csv(os.path.join(save_path, f'{exp_name}_train.csv'),)
    parser.val_df.to_csv(os.path.join(save_path, f'{exp_name}_val.csv'),)
    shutil.copy(json_path, os.path.join(save_path, 'scalars.json'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSV results'
                                     'saver for mmdetection logs')
    parser.add_argument('save_folder')
    parser.add_argument('experiments_path')
    parser.add_argument('experiment_name')

    params = parser.parse_args()
    path_to_search = os.path.join(params.experiments_path,
                                  params.experiment_name)
    json_path = find_train_logs(path_to_search)
    save_plots(json_path, params.save_folder, params.experiment_name)

# python plot_results.py save_folder exps model_exps
