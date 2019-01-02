"""####################### import requirement library ########################"""

from torch.utils.data import Dataset
import os
import random
from PIL import Image


# TODO: make split text file and modify getitem method
class MRIDataset(Dataset):

    def __init__(self, dic, root_dir, mode, transform=None):
        self.keys = list(dic.keys())
        self.values = list(dic.values())
        self.dic = dic
        self.root_dir = root_dir
        self.transform = transform
        self.mode = mode

    def __len__(self):
        return len(self.keys)

    def __getitem__(self, idx):
        cur_key = self.keys[idx]
        if self.mode == 'train':
            # nb_frame = self.values[cur_key][0]
            nb_frame = self.dic[cur_key][0]
            self.clips_idx = random.randint(1, int(nb_frame))
            self.video = cur_key.split('/')[0]
        elif self.mode == 'val':
            split_key = cur_key.split('-')
            self.video = split_key[0]
            self.clips_idx = int(split_key[1])
        else:
            raise ValueError('There are only train and val mode')

        label = self.dic[cur_key][1]
        video_name = self.keys[idx].split('-')[0]
        data_root = os.path.join(self.root_dir, video_name)
        cur_data_list = os.listdir(data_root)

        data_path = os.path.join(data_root, cur_data_list[self.clips_idx-1])
        data = Image.open(data_path)

        if self.transform:
            data = self.transform(data)

        if self.mode == 'train':
            sample = (data, label)
        elif self.mode == 'val':
            sample = (self.video, data, label)
        else:
            raise ValueError('There are only train and val mode')
        return sample