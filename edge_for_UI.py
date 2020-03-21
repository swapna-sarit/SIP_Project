import cv2
import numpy as np
import math
from PIL import Image

def sobel_edge_detect(path):
    path = path.split("/")
    legible_path = ""
    no_of_directories = len(path) - 1
    for i in range(no_of_directories):
        if i == 0:
            legible_path = legible_path + path[i]
        else:
            legible_path = legible_path + "\\" + path[i]


    intensity_img = cv2.imread(legible_path + "\\" + "intensity_image.jpg", cv2.IMREAD_UNCHANGED)
    hue_img = cv2.imread(legible_path + "\\" + "hue_image.jpg", cv2.IMREAD_UNCHANGED)

    # Define the Sobel Operators
    sobel_y = [[1, 2, 1],
               [0, 0, 0],
               [-1, -2, -1]]

    sobel_x = [[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]]

    # Define ndarrays to hold sobel_hue_magnitude and sobel_intensity_magnitude
    sobel_magnitude_i = np.zeros(intensity_img.shape)
    sobel_magnitude_h = np.zeros(hue_img.shape)

    for i in range(1, intensity_img.shape[0] - 1):
        for j in range(1, intensity_img.shape[1] - 1):
            temp = [[intensity_img[i - 1][j - 1], intensity_img[i - 1][j - 0], intensity_img[i - 1][j + 1]],
                    [intensity_img[i - 0][j - 1], intensity_img[i - 0][j - 0], intensity_img[i - 0][j + 1]],
                    [intensity_img[i + 1][j - 1], intensity_img[i + 1][j - 0], intensity_img[i + 1][j + 1]]]

            edge_y = np.sum(np.multiply(temp, sobel_y))
            edge_x = np.sum(np.multiply(temp, sobel_x))

            sobel_magnitude_i[i][j] = math.sqrt(edge_x ** 2 + edge_y ** 2)

            temp = [[hue_img[i - 1][j - 1], hue_img[i - 1][j - 0], hue_img[i - 1][j + 1]],
                    [hue_img[i - 0][j - 1], hue_img[i - 0][j - 0], hue_img[i - 0][j + 1]],
                    [hue_img[i + 1][j - 1], hue_img[i + 1][j - 0], hue_img[i + 1][j + 1]]]

            edge_y = np.sum(np.multiply(temp, sobel_y))
            edge_x = np.sum(np.multiply(temp, sobel_x))

            sobel_magnitude_h[i][j] = math.sqrt(edge_x ** 2 + edge_y ** 2)


    # Save the sobel_magnitude images
    cv2.imwrite(legible_path + "\\" + "sobel_intensity.jpg", sobel_magnitude_i)
    cv2.imwrite(legible_path + "\\" + "sobel_hue.jpg", sobel_magnitude_h)

def displaySobelHue(path):
    path = path.split("/")
    legible_path = ""
    no_of_directories = len(path) - 1
    for i in range(no_of_directories):
        if i == 0:
            legible_path = legible_path + path[i]
        else:
            legible_path = legible_path + "\\" + path[i]

    im = Image.open(legible_path + "\\" + "sobel_hue.jpg")
    im.show(title="Sobel Magnitude on Hue Image")

def displaySobelIntensity(path):
    path = path.split("/")
    legible_path = ""
    no_of_directories = len(path) - 1
    for i in range(no_of_directories):
        if i == 0:
            legible_path = legible_path + path[i]
        else:
            legible_path = legible_path + "\\" + path[i]

    im = Image.open(legible_path + "\\" + "sobel_intensity.jpg")
    im.show(title="Sobel Magnitude on Intensity Image")

