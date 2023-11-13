''' Finds files in experiment folder'''
import os
import json


def find_train_logs(experiment_path, find_file='scalars.json'):
    ''''
    experiment_path - путь до папки с экспериментами конкретной модели
    find_file - название файла, который нужно найти.
    Файл исчется по самому большому количеству строк,
    содержащихся в нем
    '''
    mx = -1
    true_sub_exp_name = ''
    # iterate through all launches
    for sub_exp_name in os.listdir(experiment_path)[::-1]:
        try:
            filename = os.path.join(experiment_path, sub_exp_name,
                                    'vis_data', find_file)
            with open(filename, 'r', encoding='utf-8') as f:
                lines_amount = len(f.readlines())
                if mx < lines_amount:
                    mx = lines_amount
                    true_sub_exp_name = filename
        except Exception as e:
            print('Error occured', e)
    if true_sub_exp_name == '':
        print('NO TRAIN FILE')
    else:
        file_path = true_sub_exp_name
        return file_path


def find_test_logs(experiment_path, *args):
    ''''
    experiment_path - путь до папки с экспериментами конкретной модели
    find_file - название файла, который нужно найти.
    Файл исчется по самому большому количеству строк,
    содержащихся в нем
    '''
    # iterate through all launches
    for sub_exp_name in os.listdir(experiment_path)[::-1]:
        try:
            filename = os.path.join(experiment_path, sub_exp_name,
                                    f'{sub_exp_name}.json')
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    lines_amount = len(lines)
                    if lines_amount == 1:
                        json_test = json.loads(lines[0])
                        if list(json_test.keys())[0].startswith('coco'):
                            return filename
        except Exception as e:
            print('Error occured', e)
    print('NO TEST FILE')
