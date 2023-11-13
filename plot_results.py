import os
import argparse

from mm_det_log_parse import LogParser


def save_plots(json_path, save_folder, exp_name):
    parser = LogParser(json_path)
    parser.train_df.to_csv(os.path.join(save_folder, f'{exp_name}_train.csv'),)
    parser.val_df.to_csv(os.path.join(save_folder, f'{exp_name}_val.csv'),)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSV results saver for mmdetection logs')
    parser.add_argument('json_path')
    parser.add_argument('save_folder')
    parser.add_argument('--experiment_name', default='experiment',)
    params = parser.parse_args()
    save_plots(params.json_path, params.save_folder, params.experiment_name)

# python plot_results.py 'пример логов/diffusion.json'  save_folder/ --experiment_name name
