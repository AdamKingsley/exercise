import numpy as np
from PIL import Image
import os
from util import file_util


def svd(matrix, percent=0.1):
    # matrix = u * E * v
    # u's shape is (m,m)
    # E's shape should be (n,m)
    # v's shape is (n,n)
    # E was just a bunch ordered svd value, we should transfer it into m*n matrix
    u, E, v = np.linalg.svd(matrix)
    sigma = np.zeros(shape=(int(len(E) * percent), int(len(E) * percent)))
    for i in range(sigma.shape[0]):
        sigma[i, i] = E[i]
    return np.matmul(np.matmul(u[:, :sigma.shape[0]], sigma), v[:sigma.shape[0], :])


# batch produce
def svd_batch(matrix, percents=[0.1]):
    u, E, v = np.linalg.svd(matrix)
    datas = []
    for percent in percents:
        sigma = np.zeros(shape=(int(len(E) * percent), int(len(E) * percent)))
        for i in range(sigma.shape[0]):
            sigma[i, i] = E[i]
        datas.append(np.matmul(np.matmul(u[:, :sigma.shape[0]], sigma), v[:sigma.shape[0], :]))
    return np.asarray(datas)


if __name__ == '__main__':
    file_path = 'HIMYM_NOT_SQUARE.jpg'
    # file_path = 'HIMYM_SQUARE.jpg'
    # file_path = 'TEST.jpg'
    image_data = np.asarray(Image.open(file_path))
    print(np.shape(image_data))
    R0 = image_data[:, :, 0]
    G0 = image_data[:, :, 1]
    B0 = image_data[:, :, 2]
    print(R0.shape)
    # for percent in np.arange(0.1, 1, 0.1):
    for percent in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        R1 = svd(R0, percent)
        G1 = svd(G0, percent)
        B1 = svd(B0, percent)
        # 0, 1, 2 axis = 2
        new_pic = np.stack((R1, G1, B1), axis=2)
        new_pic[new_pic > 255] = 255
        new_pic[new_pic < 0] = 0
        new_pic = Image.fromarray(new_pic.astype(np.uint8))

        file_util.check_dir('./data/')
        save_path = os.path.join('./data/', file_util.split_file(file_path)[0] + '_' + str(percent) + '.jpg')
        new_pic.save(save_path)
