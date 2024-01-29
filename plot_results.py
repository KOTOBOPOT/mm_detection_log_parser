import os
import pandas as pd
import json
from plotly import express as px
import argparse


def get_log(json_path):
    train_log_list = []
    val_log_list = []

    with open(json_path, "r", encoding='UTF-8') as f:
        log_line = f.readline()#log = json.load(f)

        while log_line!="":
            try:
                json_log = json.loads(log_line)
            except Exception as e:
                print(log_line)
                print(e)
            try:
              #  print(json_log)
                json_log['loss']
                # continuation means that it's train
                train_log_list.append(json_log)
            except KeyError:
                # val line
                val_log_list.append(json_log)
            log_line = f.readline()
                
    return pd.DataFrame(train_log_list), pd.DataFrame(val_log_list)


def save_train_plots(train_df, save_path):
    fig = px.line(train_df, x="iter", y="loss",)
    fig.show()

    fig.write_image(os.path.join(save_path, "loss.png"))


def save_val_plots(val_df, save_path):
    fig = px.line(val_df, x="step", y="coco/bbox_mAP_50")
    fig.show()

    fig.write_image(os.path.join(save_path, "mAP50.png"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSV results' 
                                     'saver for mmdetection logs')
    parser.add_argument('save_path')
    parser.add_argument('json_path')

    params = parser.parse_args()

    train_df, val_df = get_log(params.json_path)
    
    val_df.to_csv(os.path.join(params.save_path, "val.csv"))
    train_df.to_csv(os.path.join(params.save_path, "train.csv"))
    
    save_train_plots(train_df, params.save_path)
    save_val_plots(val_df, params.save_path)