#
import cv2
from torch.utils.data import Dataset

class StcarDs(Dataset):
    def __init__(self):
        self.name = 'datasets.stcar_ds.StcarDs'

    
    def __len__(self):
        return 0

    def __getitem__(self, item):
        return None

    def draw_bbox(self):
        print('画检测框')
        sum = 0
        with open('./datas/CUB/cars_train_annos.csv') as rfd:
            for row in rfd:
                row = row.strip()
                arrs0 = row.split(',')
                x1, x2, y1, y2 = int(arrs0[0]), int(arrs0[1]), int(arrs0[2]), int(arrs0[3])
                csv_file = './datas/CUB/data/{0}'.format(arrs0[5].strip())
                print('csv_file: {0};'.format(csv_file))
                img = cv2.imread(csv_file)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0))
                cv2.imshow("image", img)
                cv2.waitKey(0)
                sum += 1
                if sum > 3:
                    break