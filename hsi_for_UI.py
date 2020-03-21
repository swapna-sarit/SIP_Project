import cv2
import numpy as np
import math
from PIL import Image



def hsi(path):
    with np.errstate(divide='ignore', invalid='ignore'):
        path = path.split("/")
        legible_path = ""
        no_of_directories = len(path) - 1
        for i in range(no_of_directories):
         if i == 0:
                legible_path = legible_path + path[i]
         else:
                legible_path = legible_path + "\\" + path[i]

        fcc_bgr = cv2.imread(legible_path + "\\" +"fcc.jpg", cv2.IMREAD_UNCHANGED)

    # Load image with 32 bit floats as variable type
        fcc_bgr = np.float32(fcc_bgr) / 255

    # Separate BGR color channels
        blue = fcc_bgr[:, :, 0]
        green = fcc_bgr[:, :, 1]
        red = fcc_bgr[:, :, 2]

    # Calculate Intensity
        def calc_intensity(red, blue, green):
            return np.uint8(np.divide(blue + green + red, 3) * 255)

    # Calculate Saturation
        def calc_saturation(red, blue, green):
            min = np.minimum(np.minimum(red, green), blue)
            saturation = 1 - ((3 * min) / (red + green + blue + 0.001))  # 0.001 has been added to avoid division by zero
            return np.uint8(saturation * 255)

    # Calculate Hue
        def calc_hue(red, blue, green):
            hue = np.copy(red)

            for i in range(0, blue.shape[0]):
                for j in range(0, blue.shape[1]):
                    hue[i][j] = (0.5 * ((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j]))) / math.sqrt(
                        (red[i][j] - green[i][j]) ** 2 + ((red[i][j] - blue[i][j]) * (green[i][j] - blue[i][j])))

                    hue[i][j] = math.acos(hue[i][j])

                    if blue[i][j] > green[i][j]:
                        hue[i][j] = ((360 * math.pi) / 180.0) - hue[i][j]

            hue = hue / (2*math.pi)
            return np.uint8(hue * 255)

    # Merge channels into picture and return image
        calculated_hue = calc_hue(red, blue, green)
        calculated_saturation = calc_saturation(red, blue, green)
        calculated_intensity = calc_intensity(red, blue, green)
        hsi_np = np.zeros(fcc_bgr.shape)

        for i in range(fcc_bgr.shape[0]):
            for j in range(fcc_bgr.shape[1]):
                hsi_np[i][j] = [calculated_saturation[i][j], calculated_intensity[i][j], calculated_hue[i][j]]


    # hsi image display and save
        cv2.imwrite(legible_path + "\\" +"hsi_np_image.jpg", hsi_np)
        cv2.imwrite(legible_path + "\\" + "hue_image.jpg", calculated_hue)
        cv2.imwrite(legible_path + "\\" + "saturation_image.jpg", calculated_saturation)
        cv2.imwrite(legible_path + "\\" + "intensity_image.jpg", calculated_intensity)


def displayHSI(path):
    path = path.split("/")
    legible_path = ""
    no_of_directories = len(path) - 1
    for i in range(no_of_directories):
        if i == 0:
            legible_path = legible_path + path[i]
        else:
            legible_path = legible_path + "\\" + path[i]

    im_hsi = Image.open(legible_path + "\\" + "hsi_np_image.jpg")
    im_hsi.show(title="HSI Image")

def displayHue(path):
    path = path.split("/")
    legible_path = ""
    no_of_directories = len(path) - 1
    for i in range(no_of_directories):
        if i == 0:
            legible_path = legible_path + path[i]
        else:
            legible_path = legible_path + "\\" + path[i]

    im_hue = Image.open(legible_path + "\\" + "hue_image.jpg")
    im_hue.show(title="Hue Image")


def displaySaturation(path):
    path = path.split("/")
    legible_path = ""
    no_of_directories = len(path) - 1
    for i in range(no_of_directories):
        if i == 0:
            legible_path = legible_path + path[i]
        else:
            legible_path = legible_path + "\\" + path[i]

    im_sat = Image.open(legible_path + "\\" + "saturation_image.jpg")
    im_sat.show(title="Saturation Image")

def displayIntensity(path):
    path = path.split("/")
    legible_path = ""
    no_of_directories = len(path) - 1
    for i in range(no_of_directories):
        if i == 0:
            legible_path = legible_path + path[i]
        else:
            legible_path = legible_path + "\\" + path[i]

    im_int = Image.open(legible_path + "\\" + "intensity_image.jpg")
    im_int.show(title="Intensity Image")





    #im = cv2.imread(legible_path + "\\" +"hsi_np_image.jpg")
    ##plt.imshow(cv2.imread(legible_path + "\\" +"hsi_np_image.jpg"))
    ##plt.show()

    # intensity image display and save

    #im = cv2.imread(legible_path + "\\" + "intensity_image.jpg")
    ##plt.imshow(cv2.imread(legible_path + "\\" + "intensity_image.jpg"))
    ##plt.show()

    # saturation image display and save

    #im = cv2.imread(legible_path + "\\" + "saturation_image.jpg")
    ##plt.imshow(cv2.imread(legible_path + "\\" + "saturation_image.jpg"))
    ##plt.show()

    # hue image display and save

    #im = cv2.imread(legible_path + "\\" + "hue_image.jpg")
    ##plt.imshow(cv2.imread(legible_path + "\\" + "hue_image.jpg"))
    ##plt.show()


