import os
import gc
import time

import psutil
import file
import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from collections import OrderedDict


class Cropper:
    def __init__(self, img: np.array = None):
        self.img = img





def plot_Z_profile(img, path_to_imgs, dir, a, f):
    cmaps = OrderedDict()
    cmaps['Perceptually Uniform Sequential'] = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']

    cmaps['Sequential'] = [
        'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
        'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
        'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']


    dots = [(50, 400), (50, 750), (500, 400), (500, 750), (1000, 400), (1000, 750), (1500, 400), (1500, 750)]
    #dots_r = [(50, 1250), (50, 1600), (500, 1250), (500, 1600), (1000, 1250), (1000, 1600), (1500, 1250), (1500, 1600)]


    fig, axs = plt.subplots(4, 2, sharex=True, sharey=True, figsize=(16, 9))
    plt.subplots_adjust(wspace=0.2, hspace=0.5)


    num = 0
    for k in range(axs.shape[0]):
        for l in range(axs.shape[1]):
            y_pos, x_pos = dots[num]
            pixel = img[:, y_pos, x_pos]
            x_fit = range(100)
            params, _ = curve_fit(fit_func, x_fit, pixel)
            axs[k, l].plot(np.arange(img.shape[0]), pixel)
            axs[k, l].plot(np.arange(img.shape[0]), fit_func(x_fit, params[0], params[1]), linestyle='--', label=f'm: {Decimal(params[0]):.2E}\n t: {Decimal(params[1]):.2E}')
            axs[k, l].legend(loc='upper right')
            axs[k, l].set_title(f'pixel: {dots[num]}')
            write_data(params[0], params[1], path_to_imgs, dots[num], dir, f, a)
            num += 1
    fig.text(0.5, 0.04, 'image stack', ha='center')
    fig.text(0.04, 0.5, 'grey value', va='center', rotation='vertical')
    #plt.tight_layout()
    plt.legend()
    fig.suptitle(f'Energy:{dir}  Filter:{f}  Area:{a}', fontsize=16)
    print(f'creating plot with Energy:{dir}  Filter:{f}  Area:{a}')
    plt.savefig(os.path.join(path_to_imgs, dir, f'{dir}_{f}{a}.pdf'))
    del img
    gc.collect()
    #plt.show()


def fit_func(x, a, t):
    return a*x + t


def write_data(m, t, path, dot, dir, f, a):
    path_save = r'\\132.187.193.8\junk\sgrischagin'
    with open(os.path.join(path_save, 'checked_files.txt'), 'a+') as file:
        file.write(f'{path};{dir};{f};{a};{dot};{m};{t}\n')
        file.close()


def prepare_imgs(path, dir, filter, area):
    darks = os.path.join(path, 'darks')
    refs = os.path.join(path, dir, 'refs')
    imgs = os.path.join(path, dir, 'imgs', filter, area)
    return imgs, refs, darks


def main():
    image_shape = (1536, 1944)
    header = 2048
    val_range = None
    rescale = False
    #exposure_t = 150
    #pixel_size = 74.8 / 2.95888
    pixel_size_units = '$\mu m$'
    smallest_size = None

    path_raw_data = r'\\132.187.193.8\junk\sgrischagin\2021-08-09-Sergej_SNR_Stufelkeil_40-75kV'
    path_darks = r'\\132.187.193.8\junk\sgrischagin\2021-08-09-Sergej_SNR_Stufelkeil_40-75kV\darks'
    #dir = r'40_kV'
    filter = ['_none_', '_1mm Al_', '_2mm Al_']
    areas = ['_1-area_', '_2-area_', '_3-area_', '_4-area_']

    imgs = None
    refs = None
    darks = None
    exeptions = ['40kV', '45kV', '50kV', '55kV', '60kV', '100kV']

    darks = file.volume.Reader(path_darks, mode='raw', shape=image_shape, header=header, value_range=val_range, do_rescale=rescale).load_all()
    for dir in os.listdir(path_raw_data):
        if 'kV' in dir:
            if dir not in exeptions:
                for f in filter:
                    for a in areas:
                        print(f'used memory (before reading imags and refs): {round(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)} MB')
                        path_imgs, path_refs, _ = prepare_imgs(path_raw_data, dir, f, a)
                        imgs = file.volume.Reader(path_imgs, mode='raw', shape=image_shape, header=header, value_range=val_range,do_rescale=rescale).load_all()
                        refs = file.volume.Reader(path_refs, mode='raw', shape=image_shape, header=header, value_range=val_range, do_rescale=rescale).load_all()

                        # TODO: crop data before passing to plot. Crop 3x3 square around the set 'dots'
                        img = (imgs - darks) / (refs - darks)
                        print(f'used memory: {round(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)} MB')
                        print('open up plot_Z_profile()')
                        plot_Z_profile(img, path_raw_data, dir, a, f)
                        del imgs, refs
                        print('cleaning up imgs, refs.')
                        gc.collect()
                        print('sleeping for test purpose')
                        time.sleep(2)


if __name__ == '__main__':
    main()