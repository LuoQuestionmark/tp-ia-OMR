from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

def load_img(file):
    with open (file) as p:
        im = Image.open(file)
        im = im.convert('L')
    return im

if __name__ == '__main__':
    img = load_img("./music-notes.png")
    pix = np.array(img.getdata()).reshape(img.size[1], img.size[0])
    pix = (pix>220)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(pix)
    ax2.barh(range(pix.shape[0]), np.sum(pix, axis=1))
    ax2.figure.set_size_inches(ax1.figure.get_size_inches())
    

    plt.show()
