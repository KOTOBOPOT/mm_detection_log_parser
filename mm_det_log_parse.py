import json
import tqdm
import pandas as pd


def read_log(json_path):
    with open(json_path, 'r') as f:
        logs = f.readlines()
    return logs


class LogParser:

    def __init__(self, json_path):
        self.json_path = json_path

        self.raw_json = read_log(json_path)
        self.split_log_into_val_train(self.raw_json)

        self.train_df = pd.DataFrame(self.train_log)
        self.val_df = pd.DataFrame(self.val_log)

    def split_log_into_val_train(self, logs: list):
        ''' List of strings '''
        val_log = []
        train_log = []

        for log in tqdm.tqdm(logs):
            j_log = json.loads(log)
            if 'coco/bbox_mAP' in j_log.keys():
                val_log.append(j_log)
            elif 'lr' in j_log.keys():
                train_log.append(j_log)
            else:
                print('unknown log type')
        self.train_log = train_log
        self.val_log = val_log

    def get_best_model_filename(self, metric='coco/bbox_mAP_50'):
        index = self.val_df[metric].argmax()
        return f"epoch_{int(self.val_df.iloc[index,:]['step'])}.pth"

    def get_best_score(self, metric='coco/bbox_mAP_50'):
        return self.val_df[metric].max()
