import tkinter
from tkinter import ttk
from tkinter import filedialog
from fcc_for_UI import *
from hsi_for_UI import *
from edge_for_UI import *


#Global Variables
filename = ""

def foo():
    pass

def browseFile():
    global filename
    filename = filedialog.askopenfilename(initialdir = "\\", title = "Select a File", filetype = (("tif", "*.tif"), ("All Files", "*.*")))
    num_of_dir_till_file = len(filename.split("/"))
    just_file_name = filename.split("/")[num_of_dir_till_file - 1]
    label_below_button1.configure(text="Selected : " + just_file_name)


def generate_fcc():
    r_band = int(fcc_band_entry1.get())
    g_band = int(fcc_band_entry2.get())
    b_band = int(fcc_band_entry3.get())

    label_below_button2.configure(text="<Status : Running...>")
    fcc(filename, r_band, g_band, b_band)
    label_below_button2.configure(text="<FCC Generated. Go to Step 3.>")

def generate_hsi():
    label_below_button3.configure(text="<Status : Running...>")
    hsi(filename)
    label_below_button3.configure(text="<HSI Image Generated. Go to Step 4.>")

def showHue():
    displayHue(filename)

def showSaturation():
    displaySaturation(filename)

def showIntensity():
    displayIntensity(filename)

def showHSI():
    displayHSI(filename)

def detect_edge():
    label_below_button5.config(text="<Status : Running...>")
    sobel_edge_detect(filename)
    label_below_button5.config(text="<Edge Detection Complete. Go to Step 6.>")

def showEdgeHue():
    displaySobelHue(filename)

def showEdgeIntensity():
    displaySobelIntensity(filename)

#Parent Window
window = tkinter.Tk()
window.title("Topic : 10 by Swapna, Surabhi, Anshul")
window.wm_iconbitmap('icon3.ico')


#Step 1 : Browse
labelFrame1 = ttk.LabelFrame(window, text = "STEP 1: Open A File")
labelFrame1.grid(column = 0, row = 1, padx = 10, pady = 30)

button1 = tkinter.Button(labelFrame1, text = "Browse a File", command = browseFile)
button1.grid(column = 0, row = 1)

label_below_button1 = tkinter.Label(labelFrame1,  text="<Nothing Selected>")
label_below_button1.grid(column=0, row=2)




#Step 2 : FCC
labelFrame2 = ttk.LabelFrame(window, text="STEP 2: Choose Color Composite")
labelFrame2.grid(column=12, row=1, padx=10, pady=30)

    #part 2.1: band no. entry for Red display
r_label = tkinter.Label(labelFrame2, text="R:")
r_label.grid(column = 2, row = 1)
fcc_band_entry1 = tkinter.Entry(labelFrame2)
fcc_band_entry1.grid(column=3, row=1)

    #part 2.2: band no. entry for Green display
g_label = tkinter.Label(labelFrame2, text="G:")
g_label.grid(column=2, row=2)
fcc_band_entry2 = tkinter.Entry(labelFrame2)
fcc_band_entry2.grid(column=3, row=2)

    #part 2.3: band no. entry for Blue display
b_label = tkinter.Label(labelFrame2, text="B:")
b_label.grid(column=2, row=3)
fcc_band_entry3 = tkinter.Entry(labelFrame2)
fcc_band_entry3.grid(column=3, row=3)

button2 = tkinter.Button(labelFrame2, text = "Generate and Display Composite", command = generate_fcc)
button2.grid(column = 0, row = 11)

label_below_button2 = tkinter.Label(labelFrame2,  text="")
label_below_button2.grid(column=0, row=12)

#Step 3 : HSI
labelFrame3 = ttk.LabelFrame(window, text="STEP 3: Convert to HSI")
labelFrame3.grid(column=23, row=1, padx=10, pady=30)

button3 = tkinter.Button(labelFrame3, text = "Generate HSI Image", command = generate_hsi)
button3.grid(column = 0, row = 11)

label_below_button3 = tkinter.Label(labelFrame3,  text="")
label_below_button3.grid(column=0, row=12)

#Step 4 : HSI Individual
labelFrame4 = ttk.LabelFrame(window, text="STEP 4: H, S, I Images")
labelFrame4.grid(column=34, row=1, padx=10, pady=30)

button4_1 = tkinter.Button(labelFrame4, text = "Hue Image Display", command = showHue)
button4_1.grid(column = 34, row = 2)

button4_2 = tkinter.Button(labelFrame4, text = "Saturation Image Display", command = showSaturation)
button4_2.grid(column = 34, row = 3)

button4_3 = tkinter.Button(labelFrame4, text = "Intensity Image Display", command = showIntensity)
button4_3.grid(column = 34, row = 4)

button4_4 = tkinter.Button(labelFrame4, text = "HSI Image Display", command = showHSI)
button4_4.grid(column = 34, row = 5)

#Step 5 : Edge Detection
labelFrame5 = ttk.LabelFrame(window, text="STEP 5: Edge Detection")
labelFrame5.grid(column=45, row=1, padx=10, pady=30)

button5 = tkinter.Button(labelFrame5, text = "Edge on H and I", command = detect_edge)
button5.grid(column = 45, row = 2)

label_below_button5 = tkinter.Label(labelFrame5,  text="")
label_below_button5.grid(column=45, row=3)

#Step 6 : Display of edge detection
labelFrame6 = ttk.LabelFrame(window, text="STEP 6: Display Edge Detection")
labelFrame6.grid(column=56, row=1, padx=10, pady=30)

button6_1 = tkinter.Button(labelFrame6, text = "Display Sobel on Hue", command = showEdgeHue)
button6_1.grid(column = 56, row = 2)

button6_2 = tkinter.Button(labelFrame6, text = "Display Sobel on Intensity", command = showEdgeIntensity)
button6_2.grid(column = 56, row = 3)



# Run the UI
window.mainloop()
