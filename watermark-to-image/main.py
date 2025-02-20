import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


def upload_image():

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:

        image = Image.open(file_path)


        max_size = (800, 800)
        image.thumbnail(max_size, Image.LANCZOS)

        watermark_text = simpledialog.askstring("Watermark", "Enter watermark text:")
        if watermark_text:
            add_watermark(image, watermark_text)

        img = ImageTk.PhotoImage(image)

        image_label.config(image=img)
        image_label.image = img

        root.geometry(f"{image.width}x{image.height + 100}")


def add_watermark(image, text):
    d = ImageDraw.Draw(image)

    fnt = ImageFont.load_default()

    watermark_text = text

    position = (image.width - 10, image.height - 10)

    d.text(position, watermark_text, font=fnt, fill=(255, 255, 255, 128),
           anchor="rb")

    image.show()


root = tk.Tk()
root.title("Watermark creator")
root.geometry("800x800")

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=20)

image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()
