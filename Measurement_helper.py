import os
import file
import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from collections import OrderedDict


class Cropper:
    def __init__(self, img: np.array = None):
        self.img = img


def plot_Z_profile(img, path_to_imgs, dir, p):
    cmaps = OrderedDict()
    cmaps['Perceptually Uniform Sequential'] = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']

    cmaps['Sequential'] = [
        'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
        'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
        'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

    dots = [(50, 400), (50, 750), (500, 400), (500, 750), (1000, 400), (1000, 750), (1500, 400), (1500, 750)]
    #dots = [(50, 400)]

    fig, axs = plt.subplots(4, 2, sharex=True, sharey=True, figsize=(16, 9))
    plt.subplots_adjust(wspace=0.2, hspace=0.5)

    pixel = None
    num = 0

    for k in range(axs.shape[0]):
        for l in range(axs.shape[1]):
            y_pos, x_pos = dots[num]
            pixel = img[:, y_pos, x_pos]
            x_fit = range(100)
            params, _ = curve_fit(fit_func, x_fit, pixel)
            axs[k, l].plot(np.arange(img.shape[0]), pixel)
            axs[k, l].plot(np.arange(img.shape[0]), fit_func(x_fit, params[0], params[1]), linestyle='--', label=f'a: {Decimal(params[0]):.2E}\n t: {Decimal(params[1]):.2E}')
            axs[k, l].legend(loc='lower left')
            axs[k, l].set_title(f'pixel: {dots[num]}')
            write_data(params[0], params[1], path_to_imgs, dots[num], dir, p)
            num += 1
    #fig.text(0.5, 0.04, 'image stack', ha='center')
    #fig.text(0.04, 0.5, 'grey value', va='center', rotation='vertical')
    #plt.tight_layout()
    #plt.legend()
    #plt.show()


def fit_func(x, a, t):
    return a*x + t



def write_data(a, t, path, dot, dir, p):
    path_save = r'.'
    with open(os.path.join(path_save, 'checked_files.txt'), 'a+') as f:
        f.write(f'{path};{dir};{p};{dot};{a};{t}\n')
        f.close()



def prepare_imgs(path, dir, pattern=None):
    dark_imgs = os.path.join(path, 'darks')

    imgs = os.path.join(path, dir, 'imgs', pattern)
    ref_imgs = os.path.join(path, dir, 'refs')
    return imgs, ref_imgs, dark_imgs



def cropmania(data, refs, darks):
    dots = [(50, 400), (50, 750), (500, 400), (500, 750), (1000, 400), (1000, 750), (1500, 400), (1500, 750)]

    for num in dots:
        y_dot, x_dot = dots[num]
        #pixel = np.array([x_dot-1, ],[],[])
        pixel = img[:, y_pos, x_pos]
        print(pixel)


def main():
    image_shape = (1536, 1944)
    header = 2048
    val_range = None
    rescale = False
    exposure_t = 150
    pixel_size = 74.8 / 2.95888
    pixel_size_units = '$\mu m$'
    smallest_size = None

    path_raw_data = ['.']
    #dir = r'40_kV'
    pattern = ['_0_', '_00_', '_000_', '_0000_']

    imgs = None
    refs = None
    darks = None
    for path in  path_raw_data:
        darks = file.volume.Reader(darks, mode='raw', shape=image_shape, header=header, value_range=val_range,do_rescale=rescale).load_all()
        for dir in os.listdir(path):
            refs = file.volume.Reader(refs, mode='raw', shape=image_shape, header=header, value_range=val_range,do_rescale=rescale).load_all()
            if os.path.isdir(os.path.join(path, dir)) and dir != 'darks':
                for p in pattern:
                    print(f'working on path:{path} \n dir: {dir} \n pattern: {p}')
                    imgs, refs, darks = prepare_imgs(path, dir, p)
                    data = file.volume.Reader(imgs, mode='raw', shape=image_shape, header=header, value_range=val_range, do_rescale=rescale).load_all()



                    # TODO: crop data before passing to plot
                    # crop 3x3 square around the set 'dots'
                    data_c, refs_c, darks_c = cropmania(data, refs, darks)
                    img = (data - darks) / (refs - darks)



                    plot_Z_profile(img, path, dir, p)
                    #del img, data, refs, darks

if __name__ == '__main__':
    main()
