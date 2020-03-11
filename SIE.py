#!/usr/bin/env

from tkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk, ImageEnhance, ImageFilter, ImageOps
import os


# Colorize colours.
# Take your pick from https://matplotlib.org/3.1.0/gallery/color/named_colors.html
col_butt = ["grey",
           "navy", "blue", "royalblue", "darkgreen", "seagreen", "olive",
           "goldenrod", "orangered", "red", "maroon", "purple", "indigo"
           ]
# Scale widget ranges.
colour_range = [-10.0, 10.0]
brightness_range = [0.0, 10.0]
contrast_range = [-10.0, 10.0]
blur_range = [1, 10]
median_filter_range = [3, 19]

# Default image attributes.
default_colour = "1.0"
default_brightness = "1.0"
default_contrast = "1.0"
default_blur_radius = "1"
default_median_filter_size = "3"

# Image attributes.
scale_colour = scale_brightness = scale_contrast = ""
scale_blur = scale_median_filter = ""

# Button variables.
chk_butt1 = chk_butt2 = chk_butt3 = chk_butt4 = ""
chk_butt_val1 = chk_butt_val2 = chk_butt_val3 = chk_butt_val4 = ""

# Misc variables.
root = ""
label = ""
image = image_ops = image_display = image_edit = image_save = ""
img_width = img_height = 0
colorize_var = 0
filter_var = 0
scale_length = 200
image_editor_ready = False
revert_colour = False

# Misc constants.
directory = os.getcwd()
window_size = "400x550"
icon_size = "28"
icon_file = "icon.png"
ref_img = "refresh.png"
open_img = "open.png"
save_img = "save.png"
reset_img = "reset.png"
quit_img = "quit.png"
default_image = "lenna.png"


# Main editing GUI, including image and widgets display.
def edit_gui(master, img):

    global image_editor_ready
    global image_edit, label
    global root, root, root

    reset_filters()

    # Display image to be edited.
    top = Toplevel(master)
    top.geometry("+5+5")
    top.protocol("WM_DELETE_WINDOW", do_not_close_here)
    icon = PhotoImage(file=icon_file)
    root.call("wm", "iconphoto", top._w, icon)
    image_edit = ImageTk.PhotoImage(img)
    label = Label(top, image=image_edit)
    label.pack()

    action_butts()
    main_scales()
    main_butts()
    filter_scales()
    filter_butts()
    colorize_buttons()

    image_editor_ready = True


# Display main scale widgets.
def main_scales():
    global scale_colour, scale_brightness, scale_contrast

    l = Label(root, text="Colour")
    l.place(relx=0.1, rely=0.1)
    scale_colour = ttk.Scale(
        root,
        orient=HORIZONTAL,
        from_=colour_range[0],
        to=colour_range[1],
        length=scale_length,
        command=update_scale_colour
    )
    scale_colour.set(default_colour)
    scale_colour.place(relx=0.3, rely=0.1)

    l = Label(root, text="Brightness")
    l.place(relx=0.1, rely=0.15)
    scale_brightness = ttk.Scale(
        root,
        orient=HORIZONTAL,
        from_=brightness_range[0],
        to=brightness_range[1],
        length=scale_length,
        command=update_scale_brightness
    )
    scale_brightness.set(default_brightness)
    scale_brightness.place(relx=0.3, rely=0.15)

    l = Label(root, text="Contrast")
    l.place(relx=0.1, rely=0.2)
    scale_contrast = ttk.Scale(
        root,
        orient=HORIZONTAL,
        from_=contrast_range[0],
        to=contrast_range[1],
        length=scale_length,
        command=update_scale_contrast
    )
    scale_contrast.set(default_contrast)
    scale_contrast.place(relx=0.3, rely=0.2)


# Display button widgets.
def main_butts():
    global chk_butt1, chk_butt2, chk_butt3, chk_butt4, chk_butt5, chk_butt6
    global chk_butt_val1, chk_butt_val2, chk_butt_val3, chk_butt_val4, chk_butt_val5, chk_butt_val6

    chk_butt_val1 = IntVar()
    chk_butt_val2 = IntVar()
    chk_butt_val3 = IntVar()
    chk_butt_val4 = IntVar()
    chk_butt_val5 = IntVar()
    chk_butt_val6 = IntVar()

    chk_butt1 = ttk.Checkbutton(
        root,
        text="Rotate 90",
        variable=chk_butt_val1,
        command=rotate_image
    )
    chk_butt1.place(relx=0.15, rely=0.3)

    chk_butt2 = ttk.Checkbutton(
        root,
        text="Rotate 180",
        variable=chk_butt_val2,
        command=rotate_image
    )
    chk_butt2.place(relx=0.45, rely=0.3)

    chk_butt3 = ttk.Checkbutton(
        root,
        text="Grayscale",
        variable=chk_butt_val3,
        command=grayscale
    )
    chk_butt3.place(relx=0.15, rely=0.35)

    chk_butt4 = ttk.Checkbutton(
        root,
        text="Mirror",
        variable=chk_butt_val4,
        command=mirror_image
    )
    chk_butt4.place(relx=0.45, rely=0.35)

    chk_butt5 = ttk.Checkbutton(
        root,
        text="1/4",
        variable=chk_butt_val5,
        command=resize_image1
    )
    chk_butt5.place(relx=0.75, rely=0.3)

    chk_butt6 = ttk.Checkbutton(
        root,
        text="1/2",
        variable=chk_butt_val6,
        command=resize_image2
    )
    chk_butt6.place(relx=0.75, rely=0.35)


# Display filter scale widgets.
def filter_scales():
    global scale_blur, scale_median_filter

    scale_blur = ttk.Scale(
        root,
        orient=HORIZONTAL,
        from_=blur_range[0],
        to=blur_range[1],
        length=scale_length,
        command=update_blur
    )
    scale_blur.set(blur_radius)
    scale_blur.place(relx=0.3, rely=0.5)

    scale_median_filter = ttk.Scale(
        root,
        orient=HORIZONTAL,
        from_=median_filter_range[0],
        to=median_filter_range[1],
        length=scale_length,
        command=update_median_filter
    )
    scale_median_filter.set(median_filter_size)
    scale_median_filter.place(relx=0.3, rely=0.55)

# Display radio button widgets.
def filter_butts():
    global filter_var

    l = Label(root, text="FILTERS")
    l.place(relx=0.02, rely=0.4)

    filter_var = IntVar()

    radio_butt0 = ttk.Radiobutton(
        root,
        text="NONE",
        variable=filter_var,
        value=0,
        command=refresh_image
    )
    radio_butt0.place(relx=0.1, rely=0.45)

    radio_butt1 = ttk.Radiobutton(
        root,
        text="Blur",
        variable=filter_var,
        value=1,
        command=refresh_image
    )
    radio_butt1.place(relx=0.1, rely=0.5)

    radio_butt2 = ttk.Radiobutton(
        root,
        text="Median",
        variable=filter_var,
        value=2,
        command=refresh_image
    )
    radio_butt2.place(relx=0.1, rely=0.55)

    radio_butt3 = ttk.Radiobutton(
        root,
        text="Smooth",
        variable=filter_var,
        value=3,
        command=refresh_image
    )
    radio_butt3.place(relx=0.2, rely=0.65)

    radio_butt4 = ttk.Radiobutton(
        root,
        text="Emboss",
        variable=filter_var,
        value=4,
        command=refresh_image
    )
    radio_butt4.place(relx=0.2, rely=0.7)

    radio_butt5 = ttk.Radiobutton(
        root,
        text="Find Edges",
        variable=filter_var,
        value=5,
        command=refresh_image
    )
    radio_butt5.place(relx=0.4, rely=0.65)

    radio_butt6 = ttk.Radiobutton(
        root,
        text="Contour",
        variable=filter_var,
        value=6,
        command=refresh_image
    )
    radio_butt6.place(relx=0.4, rely=0.7)

    radio_butt7 = ttk.Radiobutton(
        root,
        text="Poster",
        variable=filter_var,
        value=7,
        command=refresh_image
    )
    radio_butt7.place(relx=0.6, rely=0.65)

    radio_butt8 = ttk.Radiobutton(
        root,
        text="Invert",
        variable=filter_var,
        value=8,
        command=refresh_image
    )
    radio_butt8.place(relx=0.6, rely=0.7)


# Display radio button widgets.
def colorize_buttons():
    global colorize_var

    colorize_var = 0

    col_butt0 = Button(
        root,
        bg=col_butt[0],
        command=lambda: colour_and_refresh(0)
    )
    ref = PhotoImage(file=ref_img)
    col_butt0.config(image=ref, width="20", height="20")
    col_butt0.image = ref
    col_butt0.place(relx=0.1, rely=0.8)

    col_butt1 = Button(
        root,
        bg=col_butt[1],
        command=lambda: colour_and_refresh(1)
    )
    col_butt1.place(relx=0.2, rely=0.8)
    col_butt1.config(width="2", height="1")

    col_butt2 = Button(
        root,
        bg=col_butt[2],
        command=lambda: colour_and_refresh(2)
    )
    col_butt2.place(relx=0.25, rely=0.8)
    col_butt2.config(width="2", height="1")

    col_butt3 = Button(
        root,
        bg=col_butt[3],
        command=lambda: colour_and_refresh(3)
    )
    col_butt3.place(relx=0.3, rely=0.8)
    col_butt3.config(width="2", height="1")

    col_butt4 = Button(
        root,
        bg=col_butt[4],
        command=lambda: colour_and_refresh(4)
    )
    col_butt4.place(relx=0.35, rely=0.8)
    col_butt4.config(width="2", height="1")

    col_butt5 = Button(
        root,
        bg=col_butt[5],
        command=lambda: colour_and_refresh(5)
    )
    col_butt5.place(relx=0.4, rely=0.8)
    col_butt5.config(width="2", height="1")

    col_butt6 = Button(
        root,
        bg=col_butt[6],
        command=lambda: colour_and_refresh(6)
    )
    col_butt6.place(relx=0.45, rely=0.8)
    col_butt6.config(width="2", height="1")

    col_butt7 = Button(
        root,
        bg=col_butt[7],
        command=lambda: colour_and_refresh(7)
    )
    col_butt7.place(relx=0.5, rely=0.8)
    col_butt7.config(width="2", height="1")

    col_butt8 = Button(
        root,
        bg=col_butt[8],
        command=lambda: colour_and_refresh(8)
    )
    col_butt8.place(relx=0.55, rely=0.8)
    col_butt8.config(width="2", height="1")

    col_butt9 = Button(
        root,
        bg=col_butt[9],
        command=lambda: colour_and_refresh(9)
    )
    col_butt9.place(relx=0.6, rely=0.8)
    col_butt9.config(width="2", height="1")

    col_butt10 = Button(
        root,
        bg=col_butt[10],
        command=lambda: colour_and_refresh(10)
    )
    col_butt10.place(relx=0.65, rely=0.8)
    col_butt10.config(width="2", height="1")

    col_butt11 = Button(
        root,
        bg=col_butt[11],
        command=lambda: colour_and_refresh(11)
    )
    col_butt11.place(relx=0.7, rely=0.8)
    col_butt11.config(width="2", height="1")

    col_butt12 = Button(
        root,
        bg=col_butt[12],
        command=lambda: colour_and_refresh(12)
    )
    col_butt12.place(relx=0.75, rely=0.8)
    col_butt12.config(width="2", height="1")


# Save colorize colour and refresh image.
def colour_and_refresh(val):
    global colorize_var
    colorize_var = val
    refresh_image()


# Update colour attribute from colour scale widget.
def update_scale_colour(value):
    global image_edit

    value = eval(value)
    image_edit.paste(ImageEnhance.Color(image).enhance(value))
    refresh_image()


# Update brightness attribute from brightness scale widget.
def update_scale_brightness(value):
    global image_edit

    value = eval(value)
    image_edit.paste(ImageEnhance.Brightness(image).enhance(value))
    refresh_image()


# Update contrast attribute from contrast scale widget.
def update_scale_contrast(value):
    global image_edit

    value = eval(value)
    image_edit.paste(ImageEnhance.Contrast(image).enhance(value))
    refresh_image()


# Convert to black and white and refresh image.
def grayscale():
    refresh_image()


# Rotate and refresh image.
def rotate_image():
    refresh_image()


# Mirror and refresh image.
def mirror_image():
    refresh_image()


def resize_image1():
    if chk_butt_val5.get() == 1 and chk_butt_val6.get() == 1:
        chk_butt_val6.set(0)

    refresh_image()


def resize_image2():
    if chk_butt_val5.get() == 1 and chk_butt_val6.get() == 1:
        chk_butt_val5.set(0)

    refresh_image()


# Update blur radius from blur scale widget.
def update_blur(value):
    global blur_radius

    blur_radius = eval(value)


# Update median filter size from median filter scale widget.
def update_median_filter(value):
    global median_filter_size

    mfs = int(median_filter_size)
    median_filter_size = int(eval(value))

    # Ensure median filter size is odd number to prevent error.
    if median_filter_size % 2 == 0:
        if median_filter_size > mfs:
            median_filter_size += 1
        else:
            median_filter_size -= 1
        scale_median_filter.set(median_filter_size)


# Refresh image with updated image attributes.
def refresh_image():
    global image_save, image_ops, image_display

    if image_editor_ready is False:  # do not refresh image until main scale widgets have been defined
        return None

    image_refresh = refresh_image_with_main_attributes()
    image_ops = image_refresh
    image_display = ImageTk.PhotoImage(image_ops)
    label.configure(image=image_display)
    label.image = image_display

    image_ops = refresh_image_with_selected_filter(image_refresh)
    image_refresh = image_ops
    image_ops = refresh_image_with_selected_colour(image_refresh)

    image_save = image_ops


# Apply new attributes to original image file.
def refresh_image_with_main_attributes():
    new_colour = scale_colour.get()
    new_brightness = scale_brightness.get()
    new_contrast = scale_contrast.get()

    image_orig = Image.open(root.image_file)

    image_1 = ImageEnhance.Color(image_orig).enhance(new_colour)
    image_2 = ImageEnhance.Brightness(image_1).enhance(new_brightness)
    image_3 = ImageEnhance.Contrast(image_2).enhance(new_contrast)

    return image_3


# Apply new filter to image.
def refresh_image_with_selected_filter(image_refresh):
    global image_ops, image_display, revert_colour, img_width, img_height

    if 0 <= filter_var.get() <= 12:

        if filter_var.get() == 0:
            filter_var.set(0)
        if filter_var.get() == 1:
            image_ops = image_refresh.filter(ImageFilter.GaussianBlur(radius=float(blur_radius)))
            image_display = ImageTk.PhotoImage(image_ops)
        if filter_var.get() == 2:
            image_ops = image_refresh.filter(ImageFilter.MedianFilter(size=int(median_filter_size)))
            image_display = ImageTk.PhotoImage(image_ops)
        if filter_var.get() == 3:
            image_ops = image_refresh.filter(ImageFilter.SMOOTH_MORE)
            image_display = ImageTk.PhotoImage(image_ops)
        if filter_var.get() == 4:
            image_ops = image_refresh.filter(ImageFilter.EMBOSS)
            image_display = ImageTk.PhotoImage(image_ops)
        if filter_var.get() == 5:
            image_ops = image_refresh.filter(ImageFilter.FIND_EDGES)
            image_display = ImageTk.PhotoImage(image_ops)
        if filter_var.get() == 6:
            image_ops = image_refresh.filter(ImageFilter.CONTOUR)
            image_display = ImageTk.PhotoImage(image_ops)
        if filter_var.get() == 7:
            image_ops = ImageOps.posterize(image_refresh, bits=int(2))
            image_display = ImageTk.PhotoImage(image_ops)
        if filter_var.get() == 8:
            image_ops = ImageOps.invert(image_refresh)
            image_display = ImageTk.PhotoImage(image_ops)

        label.configure(image=image_display)
        label.image = image_display

    if chk_butt_val1.get() == 1:
        image_ops = image_ops.rotate(90, expand=True)
        image_display = ImageTk.PhotoImage(image_ops)
        label.configure(image=image_display)
        label.image = image_display

    if chk_butt_val2.get() == 1:
        image_ops = image_ops.rotate(180)
        image_display = ImageTk.PhotoImage(image_ops)
        label.configure(image=image_display)
        label.image = image_display

    if chk_butt_val3.get() == 1:
        if not revert_colour:
            image_ops = ImageOps.grayscale(image_ops)
            image_display = ImageTk.PhotoImage(image_ops)
            label.configure(image=image_display)
            label.image = image_display
        else:
            chk_butt_val3.set(0)
            revert_colour = False

    if chk_butt_val4.get() == 1:
        image_ops = ImageOps.mirror(image_ops)
        image_display = ImageTk.PhotoImage(image_ops)
        label.configure(image=image_display)
        label.image = image_display

    if chk_butt_val5.get() == 1:
        if chk_butt_val1.get() == 1:   # if rotate 90 deg. swap image width and height before resizing.
            image_ops.thumbnail((img_height * 0.25, img_width * 0.25))
        else:
            image_ops.thumbnail((img_width * 0.25, img_height * 0.25))

        image_display = ImageTk.PhotoImage(image_ops)
        label.configure(image=image_display)
        label.image = image_display

    if chk_butt_val6.get() == 1:
        if chk_butt_val1.get() == 1:   # if rotate 90 deg. swap image width and height before resizing.
            image_ops.thumbnail((img_height * .5, img_width * .5))
        else:
            image_ops.thumbnail((img_width * .5, img_height * .5))

        image_display = ImageTk.PhotoImage(image_ops)
        label.configure(image=image_display)
        label.image = image_display

    return image_ops


# Apply new colour to image.
def refresh_image_with_selected_colour(image_refresh):
    global image_ops, image_display, revert_colour

    if colorize_var != 0:
        if chk_butt_val3.get() == 0:
            chk_butt_val3.set(1)
            image_ops = ImageOps.grayscale(image_refresh)
            image_display = ImageTk.PhotoImage(image_ops)
            revert_colour = True

        if colorize_var == 1:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[1], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 2:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[2], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 3:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[3], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 4:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[4], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 5:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[5], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 6:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[6], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 7:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[7], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 8:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[8], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 9:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[9], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 10:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[10], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 11:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[11], white="white")
            image_display = ImageTk.PhotoImage(image_ops)
        if colorize_var == 12:
            image_ops = ImageOps.colorize(image_ops, black=col_butt[12], white="white")
            image_display = ImageTk.PhotoImage(image_ops)

        label.configure(image=image_display)
        label.image = image_display

    return image_ops


# Set attributes to default values and refresh image.
def reset():
    global filter_var, colorize_var, revert_colour

    filter_var.set(0)
    colorize_var = 0
    revert_colour = False

    # Reset widgets.
    scale_colour.set(default_colour)
    scale_brightness.set(default_brightness)
    scale_contrast.set(default_contrast)

    reset_check_buttons()
    reset_filters()

    scale_blur.set(default_blur_radius)
    scale_median_filter.set(default_median_filter_size)

    refresh_image()


# Reset check buttons.
def reset_check_buttons():
    global chk_butt_val1, chk_butt_val2, chk_butt_val3, chk_butt_val4

    chk_butt_val1.set(0)
    chk_butt_val2.set(0)
    chk_butt_val3.set(0)
    chk_butt_val4.set(0)
    chk_butt_val5.set(0)
    chk_butt_val6.set(0)


# Reset all filter settings to their default values.
def reset_filters():
    global blur_radius, median_filter_size

    blur_radius = int(default_blur_radius)
    median_filter_size = int(default_median_filter_size)


# Select new image file.
def open_file():
    global image, img_width, img_height
    image_f = root.image_file            # save the original filename in case no new image is selected

    root.image_file = filedialog.askopenfilename(initialdir=directory, title="Open File")

    # quit if no file is selected.
    if root.image_file == "":
        root.image_file = image_f        # revert back to the original filename if none is selected
        return None
    else:
        image = Image.open(root.image_file)
        img_width, img_height = image.size
        reset()
        refresh_image()


# Save edited image as a new file (original filename suffixed by "_new" ).
def save_image():
    refresh_image()

    file_name, file_extension = os.path.splitext(root.image_file)
    file_new = str(file_name + "_new" + file_extension)
    filename = os.path.basename(file_new)
    file_save = filedialog.asksaveasfilename(
        initialdir=directory,
        title="Save File",
        initialfile=filename,
        defaultextension=file_extension
    )

    # Return to editing if no file is selected.
    if file_save == "":
        return None

    image_save.save(file_save)


# Action buttons.
def action_butts():
    open=PhotoImage(file=open_img)
    act_butt1 = Button(
        root,
        command=lambda: open_file()
    )
    act_butt1.place(relx=0, rely=0)
    act_butt1.config(image=open, width=icon_size, height=icon_size)
    act_butt1.image=open

    save=PhotoImage(file=save_img)
    act_butt2 = Button(
        root,
        command=lambda: save_image()
    )
    act_butt2.place(relx=0.07, rely=0)
    act_butt2.config(image=save, width=icon_size, height=icon_size)
    act_butt2.image=save

    res=PhotoImage(fil=reset_img)
    act_butt3 = Button(
        root,
        command=lambda: reset()
    )
    act_butt3.place(relx=0.14, rely=0)
    act_butt3.config(image=res, width=icon_size, height=icon_size)
    act_butt3.image=res

    quit=PhotoImage(fil=quit_img)
    act_butt4 = Button(
        root,
        command=lambda: exit_app()
    )
    act_butt4.place(relx=0.21, rely=0)
    act_butt4.config(image=quit, width=icon_size, height=icon_size)
    act_butt4.image=quit


# Exit application.
def exit_app():
    root.destroy()
    quit()


# No action.
def do_not_close_here():
    messagebox.showinfo("Info", "Please exit from the editor window.")


# Main body of program.
def main():
    global root, image, img_width, img_height

    root = Tk()
    root.geometry(window_size)
    root.title("Simple Image Editor")
    root.protocol("WM_DELETE_WINDOW", exit_app)
    root.attributes("-topmost", True)
    root.update()

    # Window icon.
    icon = PhotoImage(file=icon_file)
    root.call("wm", "iconphoto", root._w, icon)

    # root.image_file = default_image
    root.image_file = filedialog.askopenfilename(initialdir=directory, title="Open File")
    image = Image.open(root.image_file)

    img_width, img_height = image.size

    edit_gui(root, image)

    root.mainloop()


if __name__ == "__main__":
    main()
