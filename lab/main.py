import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import animation
import matplotlib.image as img

def pixel_sort(img):
    fig = plt.figure()
    photo = plt.imshow(img, cmap='gray')
    maps = list(plt.cm.cmap_d.keys())

    def update(frame):
        img[frame] = np.sort(img[frame])
        photo.set_data(img)
        photo.set_cmap(np.random.choice(maps))
        return photo

    anim = animation.FuncAnimation(fig, update, frames=img.shape[0], interval=1000//60)
    plt.show()

def main():
    img = plt.imread("stinkbug.png")
    pixel_sort((np.average(img, axis=2)))


if __name__ == '__main__':
    main()


