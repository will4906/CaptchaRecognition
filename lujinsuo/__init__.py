import numpy as np

from PIL import Image, ImageFilter


def convert_to_pure_black_white(image):
    width = image.shape[1]
    height = image.shape[0]
    for w in range(width):
        for h in range(height):
            if image[h][w] < 150:
                image[h][w] = 0
            else:
                image[h][w] = 255


def remove_noise_line(image):
    width = image.shape[1]
    height = image.shape[0]
    for w in range(width):
        count = 0
        for h in range(height):
            if image[h][w] < 100:
                count += 1
            else:
                if 5 > count > 0:
                    for c in range(count):
                        image[h - c - 1][w] = 255
                count = 0

    for h in range(height):
        count = 0
        for w in range(width):
            if image[h][w] < 100:
                count += 1
            else:
                if 5 > count > 0:
                    for c in range(count):
                        image[h][w - c - 1] = 255
                count = 0


if __name__ == '__main__':
    filename = 'source/captcha_9.jpg'
    image = np.asarray(Image.open(filename).convert('L'))
    image.flags['WRITEABLE'] = True
    convert_to_pure_black_white(image)
    remove_noise_line(image)

    image = Image.fromarray(image)
    image = image.filter(ImageFilter.ModeFilter(5))
    image.show()
