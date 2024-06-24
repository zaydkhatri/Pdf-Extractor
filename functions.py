from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from PyPDF2 import *
from PyPDF2 import PdfFileReader, generic
import tabula
import os,shutil
import zlib

try:
    from io import StringIO
except ImportError:
    from io import BytesIO as StringIO
import io

# Textbox Function
def display_textbox(root, page_content, col, row):
    txt_box = Text(root, width=65, height=15, padx=15, pady=15)
    txt_box.insert(1.0,page_content)
    txt_box.configure(state="disabled")
    txt_box.tag_add("center",1.0,"end")
    txt_box.grid(column=col, row=row, sticky=SW, padx=25, pady=10)

# Saving of tables
def tables(browse_file):
    tables = tabula.read_pdf(browse_file,stream=True,pages="all")
    folder_name = "tables"
    if os.path.isdir(folder_name):
        shutil.rmtree(folder_name)
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    for i, table in enumerate(tables, start=1):
        table.to_excel(os.path.join(folder_name,f"table_{i}.xlsx"),index=False) 

# Images Inside the Pdf
def get_color_mode(obj):
    try:
        cspace = obj['/ColorSpace']
    except KeyError:
        return None

    if cspace == '/DeviceRGB':
        return "RGB"
    elif cspace == '/DeviceCMYK':
        return "CMYK"
    elif cspace == '/DeviceGray':
        return "P"

    if isinstance(cspace, generic.ArrayObject) and cspace[0] == '/ICCBased':
        color_map = obj['/ColorSpace'][1].getObject()['/N']
        if color_map == 1:
            return "P"
        elif color_map == 3:
            return "RGB"
        elif color_map == 4:
            return "CMYK"

def get_object_images(x_obj):
    images = []
    for obj_name in x_obj:
        sub_obj = x_obj[obj_name]

        if '/Resources' in sub_obj and '/XObject' in sub_obj['/Resources']:
            images += get_object_images(sub_obj['/Resources']['/XObject'].getObject())

        elif sub_obj['/Subtype'] == '/Image':
            zlib_compressed = '/FlateDecode' in sub_obj.get('/Filter', '')
            if zlib_compressed:
               sub_obj._data = zlib.decompress(sub_obj._data)

            images.append((
                get_color_mode(sub_obj),
                (sub_obj['/Width'], sub_obj['/Height']),
                sub_obj._data
            ))
    return images

def get_pdf_images(pdf_fp):
    images = []
    try:
        pdf_in = PdfFileReader(open(pdf_fp, "rb"))
    except:
        return images

    for p_n in range(pdf_in.numPages):

        page = pdf_in.getPage(p_n)

        try:
            page_x_obj = page['/Resources']['/XObject'].getObject()
        except KeyError:
            continue

        images += get_object_images(page_x_obj)
    return images

# -- main call -- 
def extract_img(pdf_fp,page):
    images = []
    for image in get_pdf_images(pdf_fp):
        (mode, size, data) = image 
        try:       
            img = Image.open(io.BytesIO(data))        
            images.append(img)
        except Exception as e:
            if '/XObject' in page['/Resources']:
                xObject = page['/Resources']['/XObject'].getObject()
                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image':
                        size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                        data = xObject[obj].getData()
                        mode = ""
                        if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                            mode = "RGB"
                        else:
                            mode = "CMYK"
                        img = Image.frombytes(mode, size, data)
                        images.append(img)
    return images


# -- resizing of images
def resize_img(img):
    width,height = int(img.size[0]), int(img.size[1])
    if width > height:
        height = int(400/width*height)
        width = 300
    elif height > width:
        width = int(250/height*width)
        height = 250
    else:
        width,height = 250,250
    img = img.resize((width,height))
    return img
# -- main call --
def display_img(img):   
    img = resize_img(img)
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img,bg="white")
    img_label.image = img
    img_label.place(x=630,y=363)
    return img_label

# Copy Text 
def copy_text(page_content,root):
    root.clipboard_clear()
    root.clipboard_append(page_content[-1])

# Save all Images
def save_all(all_images):
    counter = 1
    folder_name = "PdfImages"
    if os.path.isdir(folder_name):
        shutil.rmtree(folder_name)
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    for i in all_images:
        if i != "RGB":
            i = i.convert("RGB")
        i.save("PdfImages/Image" + str(counter) + ".png", format="png")
        counter += 1

# Save Single Image
def save_img(all_images,img_idx,counter):
    index = all_images[img_idx[-1]]
    if index.mode != "RGB":
        index = index.convert("RGB")
    counter.append(counter[-1]+1)
    index.save("Single image/" +f"image{counter[-1]}.png", format="png")
    