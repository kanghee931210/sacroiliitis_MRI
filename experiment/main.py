"""
: Title        : Sacroiliitis patient's MRI classification experiment.
: Author       : Jeongmin Seo
: Initial Date : 2018.11.29 (ver. 0.1)
: Version Num. : 0.1 (since 2018.11.29)
: Description  :
    Implementation required for MRI data preprocessing and Sacroiliitis
    patient classification experiments.
"""

"""####################### import requirement library ########################"""

import os
import re
import sys
import argparse
import torch.nn as nn
import torch.optim as optim


"""##################### import requirement custom code ######################"""
from . import model_selector as selector
from .util.model_util import *


"""####################### import requirement library ########################"""

parser = argparse.ArgumentParser(description="Sacroiliitis patient's MRI classification experiment.")
parser.add_argument('--data_root', type=str, help="set data root")
parser.add_argument('--text_root', type=str, help="set train test split file root")
parser.add_argument('--split_num', type=int, help='set train test split number')
parser.add_argument('--save_root', type=str, default="./")
parser.add_argument('--img_size', type=int, default=224, help="set train image size")
parser.add_argument('--learning_rate', '--lr', type=float, default=0.001, help="set train learning rate")
parser.add_argument('--batch_size', '--bs', type=int, default=16, help="set batch size")
parser.add_argument('--epoch', type=int, default=10000, help="set train epoch number")
parser.add_argument('--pretrained', type=str, default='true')
parser.add_argument('--model', type=str,
                    choices=['resnet18', 'resnet34', 'resnet50', 'resnet101','resnet152'], help='set model')


"""############################ main loop fuction ############################"""

def main():

    global args
    args = parser.parse_args()
    model = selector.set_model(args.model, args.pretrained)

    # TODO: data load step

    loss_func = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), args.learning_rate, momentum=0.9)

    for epoch in range(1, args.epoch+1):
        train_acc, train_loss, model = train_1epoch(model, train_loader, optimizer, loss_func, epoch, args.epoch)
        print("Train Accuacy:", train_acc, "Train Loss:", train_loss)
        test_acc, test_loss, pred = test_1epoch(model, test_loader, loss_func, epoch, args.epoch)
        print("Validation Accuracy:", test_acc, "Validation Loss:", test_loss)


if __name__ == "__main__":
    main()

#  A  A
# (‘ㅅ‘=)
# J.M.Seo
