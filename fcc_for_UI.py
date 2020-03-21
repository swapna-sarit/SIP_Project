from PIL import Image



def fcc(path, R_band, G_band, B_band):
    path = path.split("/")
    legible_path = ""
    no_of_directories = len(path) - 1
    for i in range(no_of_directories):
        if i == 0:
            legible_path = legible_path + path[i]
        else:
            legible_path = legible_path + "\\" + path[i]

    im_pil = Image.open(legible_path + "\\" + path[len(path) - 1])
    im_size_x, im_size_y = im_pil.size

    #Generate a new blank image
    fcc_im = Image.new(mode = "RGB", size = (im_size_x, im_size_y))

    #Get the pixel values of input FCC band
    for i in range(im_size_y):
        for j in range(im_size_x):
            pixel_value = list(im_pil.getpixel((j,i)))
            fcc_im.putpixel((j,i), (pixel_value[R_band - 1], pixel_value[G_band - 1], pixel_value[B_band - 1]))

    fcc_im.save(legible_path + "\\fcc.jpg")
    fcc_im.show(title="Choosen Color Composite Image")


