import numpy as np

from PIL import Image, ImageFilter


def clean_interference_line(path):
    """
    design by cc
    :param path:
    :return:
    """
    pix1 = np.array(Image.open(path).convert('L'))
    rows, cols = pix1.shape
    pix = np.array(Image.open(path).convert('RGB'))
    for x in range(1,rows):
        for y in range(cols):
            count = 0
            for i in range(3):
                if pix[x, y][i] > 130:
                    count += 1
            if count == 0:
                pix[x, y] = pix[x - 1, y]
                # pix[x, y] = 255
    im = Image.fromarray(np.uint8(pix))
    # im = clean_interference_point(pix)
    # im.show()
    return im.convert('L')


def clean_interference_point(pixdata):
    """
    design by cc
    :param pix:
    :return:
    """
    # pix = pix.convert('L')
    # pixdata = np.array(pix)
    rows,cols = pixdata.shape
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            count = 0
            if pixdata[x, y - 1] > 200:
                count = count + 1
            if pixdata[x, y + 1] > 200:
                count = count + 1
            if pixdata[x - 1, y] > 200:
                count = count + 1
            if pixdata[x + 1, y] > 200:
                count = count + 1
            if count > 2:
                pixdata[x, y] = 255
    im = Image.fromarray(np.uint8(pixdata))
    return im


def image_as_array(image):
    image = np.asarray(image)
    image.flags['WRITEABLE'] = True
    return image


def filter_image(image):
    # image = image.filter(ImageFilter.MaxFilter(5))
    # image = image.filter(ImageFilter.DETAIL)
    return image


def convert_to_pure_black_white(image):
    width = image.shape[1]
    height = image.shape[0]
    for w in range(width):
        for h in range(height):
            if image[h][w] < 170:
                image[h][w] = 0
            else:
                image[h][w] = 255
    return image


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
    return image


if __name__ == '__main__':
    filename = 'source/captcha_9.jpg'
    image = clean_interference_line(filename)
    # image = Image.open(filename).convert('L')

    # image = Image.fromarray(image)
    # image = filter_image(image)
    image = image_as_array(image)
    image = convert_to_pure_black_white(image)
    image = image_as_array(image)
    remove_noise_line(image)
    #
    image = Image.fromarray(image)
    # image = image.filter(ImageFilter.MedianFilter(5))
    # image = image.filter(ImageFilter.SMOOTH_MORE)
    image.show()
