
import os
import sys
import pickle
import argparse

import numpy as np
from numpy.lib.format import open_memmap

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from feeder_kinetics import Feeder_kinetics

toolbar_width = 30

# data_path_final=r'E:\SLIIT RA\Weekly stuff 2 - New approach\Comparison Paper (GCN and LRCN)\PreProcessKineticsSTGCN'

# data_path_final=r'F:\Data Sets\Skeleton\2D\Child\Kinetics Subsets\All final subsets\json-child-set-2-final-dataset'
# data_output_path=r'F:\Data Sets\Skeleton\2D\Child\Kinetics Subsets\All final subsets\json-child-set-2-final-dataset-preProcessed'

data_path_final=r'F:\Data Sets\Skeleton\2D\Child\Kinetics Subsets\All final subsets\json-adult-3-final-dataset'
data_output_path=r'F:\Data Sets\Skeleton\2D\Child\Kinetics Subsets\All final subsets\json-adult-3-final-dataset-preProcessed'


def print_toolbar(rate, annotation=''):
    # setup toolbara
    sys.stdout.write("{}[".format(annotation))
    for i in range(toolbar_width):
        if i * 1.0 / toolbar_width > rate:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('-')
        sys.stdout.flush()
    sys.stdout.write(']\r')


def end_toolbar():
    sys.stdout.write("\n")


def gendata(
        data_path,
        label_path,
        data_out_path,
        label_out_path,
        num_person_in=5,  #observe the first 5 persons 
        num_person_out=2,  #then choose 2 persons with the highest score 
        max_frame=300):

    feeder = Feeder_kinetics(
        data_path=data_path,
        label_path=label_path,
        num_person_in=num_person_in,
        num_person_out=num_person_out,
        window_size=max_frame)

    sample_name = feeder.sample_name
    sample_label = []

    #craete a .npy file and then save the preprocessed data
    fp = open_memmap(
        data_out_path,
        dtype='float32',
        mode='w+',
        shape=(len(sample_name), 3, max_frame, 25, num_person_out)) #shouldn't this be 18 rather than 25?
                                                                    #this is 25 because we are using body_25 instead of coco_18


    for i, s in enumerate(sample_name):
        data, label = feeder[i]
        print_toolbar(i * 1.0 / len(sample_name),
                      '({:>5}/{:<5}) Processing data: '.format(
                          i + 1, len(sample_name)))
        fp[i, :, 0:data.shape[1], :, :] = data
        sample_label.append(label)

    with open(label_out_path, 'wb') as f:
        pickle.dump((sample_name, list(sample_label)), f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Kinetics-skeleton Data Converter.')
    parser.add_argument(
        '--data_path', default=data_path_final)
    parser.add_argument(
        '--out_folder', default=data_output_path)
    arg = parser.parse_args()

    # part = ['train', 'val']
    part = ['train']
    for p in part:
        # data_path = '{}/kinetics_{}'.format(arg.data_path, p)
        # label_path = '{}/kinetics_{}_label.json'.format(arg.data_path, p)
        # data_out_path = '{}/{}_data.npy'.format(arg.out_folder, p)
        # label_out_path = '{}/{}_label.pkl'.format(arg.out_folder, p)

        data_path = '{}/data'.format(arg.data_path)
        label_path = '{}/data_label.json'.format(arg.data_path)
        data_out_path = '{}/data.npy'.format(arg.out_folder)
        label_out_path = '{}/data_label.pkl'.format(arg.out_folder)

        if not os.path.exists(arg.out_folder):
            os.makedirs(arg.out_folder)
        gendata(data_path, label_path, data_out_path, label_out_path)