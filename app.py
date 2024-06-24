# from tkinter import *
# from PIL import Image,ImageTk
# from tkinter.filedialog import askopenfile
# from tkinter import messagebox
# from PyPDF2 import PdfReader
# from functions import *
# from pdfminer.high_level import extract_text
# import os
# import pymysql


# class Pdf:
#     def __init__(self,root):
#         self.root = root
#         self.root.geometry("1000x667+180+20")
#         self.root.title("Pdf Extractor")
#         self.root.protocol("WM_DELETE_WINDOW",self.on_exit)
#         # -- icon -- 
#         self.icon = ImageTk.PhotoImage(file="images/icon.png")
#         self.root.iconphoto(False,self.icon)
#         # -- Creating frame for header --
#         frame = Frame(self.root,width=1000,height=200,bg="white")
#         frame.grid(columnspan=3,rowspan=2,row=0)
        
#         # -- Creating frame for nav frame -- 
#         frame_nav = Frame(self.root,width=1000,height=50,bg="#DADFEA")
#         frame_nav.grid(columnspan=3,rowspan=1,row=2)
#         # -- Creating frame for save and copy frame -- 
#         frame_save = Frame(self.root,width=1000,height=80,bg="#B8C5E5")
#         frame_save.grid(columnspan=3,rowspan=1,row=3)
#         # -- Creating frame for main content -- 
#         frame_con = Frame(self.root,width=1000,height=337,bg="#6187E6")
#         frame_con.grid(columnspan=3,rowspan=2,row=4)
#         # -- Getting Logo -- 
#         self.logo = ImageTk.PhotoImage(file="images/logo.png")
#         logo_label = Label(self.root,image=self.logo)
#         logo_label.place(x=50,y=10)
#         # -- Instructions Text --
#         instructions = Label(self.root,text="Select a PDF File",font="ARVO",bg="white")
#         instructions.place(x=746,y=50)
#         # -- Browse Button -- 
#         self.browse_txt = StringVar()
#         browse = Button(self.root,textvariable=self.browse_txt,command=self.open_file,font="ARVO",cursor="hand2",bg="#E53333", fg="#FFFFFF",width=15,height=1)
#         self.browse_txt.set("Browse")
#         browse.place(x=740,y=80)
#         # -- Expanding Canvas -- 
#         # -- Creating Canvas --
#         canvas = Canvas(self.root,width=600,height=250)
#         canvas.grid(columnspan=3)
#         # -- arrays to get contents
#         self.page_contents = []  # to Store all the text content 
#         self.all_images = []     # to Store all the images of PDF file
#         self.img_idx = [0]       # in this, Stored value will be assumed as index value of all_images this will change once user click on arrow btn 
#         self.display_images = [] # to Store the Data of image currently displaying on Window
#         self.counter = []        # in this new value will be added when user will click on save image 
        
#     # right arrow
#     def right_arr(self):
#         if self.img_idx[-1] < len(self.all_images) - 1: 
#             #change to the following index
#             self.new_idx = self.img_idx[-1] + 1
#             self.img_idx.pop()
#             self.img_idx.append(self.new_idx)   # self.img_idx = [1]
#             #remove displayed image if exists
#             if self.display_images:
#                 self.display_images[-1].place_forget()
#                 self.display_images.pop()
#             #create a new image in the new index & display it
#             self.new_img = self.all_images[self.img_idx[-1]]  # self.all_images[1] 
#             self.current_img = display_img(self.new_img)      # display_img(images stored on 1st index value in self.all_images list)     
#             self.display_images.append(self.current_img)
#             self.what_text.set("Image " + str(self.img_idx[-1] + 1) + " out of " + str(len(self.all_images)))
    
#     # left arrow
#     def left_arr(self):
#         if self.img_idx[-1] >= 1:
#             #change to the following index
#             self.new_idx = self.img_idx[-1] - 1
#             self.img_idx.pop()
#             self.img_idx.append(self.new_idx)
#             #remove displayed image if exists
#             if self.display_images:
#                 self.display_images[-1].place_forget()
#                 self.display_images.pop()
#             #create a new image in the new index & display it
#             self.new_img = self.all_images[self.img_idx[-1]]
#             self.current_img = display_img(self.new_img)           
#             self.display_images.append(self.current_img)
#             self.what_text.set("Image " + str(self.img_idx[-1] + 1) + " out of " + str(len(self.all_images)))
 
#     # To Not directly Close the window.
#     def on_exit(self):
#         if messagebox.askyesno("Exit", "Do you want to quit the Pdf Extractor"):
#             self.root.destroy()
    
#     # -- second window for table may contain in pdf y/n
#     def table_may(self):
#         self.answer = messagebox.askyesnocancel("The Pdf file may contain tables do you want to save the tables","Continue playing?")
   
#     # -- Browse Button Function --
#     def open_file(self):
#         # clearing the counter once new file opens and restarting by 0
#         self.counter.clear()
#         self.counter.append(0)
#         # also clearing the folder single image
#         directory = "Single image"
#         for f in os.listdir(directory):
#             os.remove(os.path.join(directory, f))

#         # poping all the index from img_idx array and restarting by 0
#         for i in self.img_idx:
#             self.img_idx.pop()
#         self.img_idx.append(0)
#         self.browse_txt.set("Loading..")

#         # poping all the index from display_images array
#         if self.display_images:
#             self.display_images[-1].place_forget()
#             self.display_images.pop()
        
#         # poping all the content of page_contents Array
#         if self.page_contents:
#             for i in self.page_contents:
#                 self.page_contents.pop()
#         # poping all the previous file images from all_images array
#         for i in range(0, len(self.all_images)):
#             self.all_images.pop()

#         # code for browsing the file 
#         try:
#             browse_file = askopenfile(parent=self.root,mode="rb",title="Choose a File",filetypes=[("Pdf File","*.pdf")])
#             if browse_file:
#                 self.read_pdf = PdfReader(browse_file,strict=False)

#                 # if file is Encrypted
#                 if self.read_pdf.is_encrypted:
#                     self.read_pdf.decrypt('')
                
#                 # Extracting Process Text
#                 self.page = self.read_pdf.getPage(0)
#                 self.page_content = extract_text(browse_file)
#                 self.page_contents.append(self.page_content)

#                 # To save Tables or not 
#                 self.answer = messagebox.askyesnocancel("","The Pdf file may contain tables do you want to save the tables?")
#                 if self.answer == True:
#                     messagebox.showinfo("Path","All the Tables are stored in tables folder you can access their.")
#                     messagebox.showinfo("Note!","Previous tables stored in table folder will be removed")
#                     tables(browse_file.name)
    
#                 # -- text box -- 
#                 display_textbox(self.root,self.page_content,0,4)
#                 self.browse_txt.set("Browse")

#                 # -- Extracting Process Images --
#                 images = extract_img(browse_file.name,self.page) # This will give an Array of data of all the images 

#                 # -- appending all the Images to all_images Array
#                 for i in images:
#                     self.all_images.append(i)
                
#                 # try block to show wheather images their in file or not 
#                 try:
#                     self.img = images[self.img_idx[-1]] # 0 index or latest we can say 
#                     self.current_image = display_img(self.img) # Display Image 
#                     self.display_images.append(self.current_image) # Appending image which is on window
#                 except IndexError:
#                     messagebox.showinfo("","No Images Found.")

#                 # -- what image text -- 
#                 self.what_text = StringVar()
#                 wht_image = Label(self.root,textvariable=self.what_text,font="ARVO",bg="#DADFEA")
#                 self.what_text.set("Image " + str(self.img_idx[-1] + 1) + " out of " + str(len(self.all_images)))
#                 wht_image.place(x=465,y=215)
#                 # -- nav arrows -- 
#                 # Left arrow
#                 self.left_arrow = ImageTk.PhotoImage(file="images/arrow2.png")
#                 self.left_arrow_btn = Button(self.root,image=self.left_arrow,command=lambda:[self.left_arr(),self.what_text],bd=0,bg="#DADFEA",height=40)
#                 self.left_arrow_btn.place(x=400,y=205)
#                 # Right arrow
#                 self.right_arrow = ImageTk.PhotoImage(file="images/arrow1.png")
#                 self.right_arrow_btn = Button(self.root,image=self.right_arrow,command=lambda:[self.right_arr(),self.what_text],bd=0,bg="#DADFEA",height=40)
#                 self.right_arrow_btn.place(x=625,y=205)#x=595
#                 # -- Copy Text Button -- 
#                 self.copy_txt = Button(self.root,text="Copy Text",command=lambda:copy_text(self.page_contents,self.root),cursor="hand2",font="ARVO",width=15,height=1,bg="#3371FF",fg="#FFFFFF")
#                 self.copy_txt.place(x=200,y=275)
#                 # -- Save Single Image Button -- 
#                 self.save_single_img = Button(self.root,text="Save Image",command=lambda:save_img(self.all_images,self.img_idx,self.counter),cursor="hand2",font="ARVO",width=15,height=1,bg="#3371FF",fg="#FFFFFF")
#                 self.save_single_img.place(x=455,y=275)
#                 # -- Save all image Button -- 
#                 self.save_all_img = Button(self.root,text="Save all Images",command=lambda:save_all(self.all_images),cursor="hand2",font="ARVO",width=15,height=1,bg="#3371FF",fg="#FFFFFF")
#                 self.save_all_img.place(x=715,y=275)
#         except Exception as e:
#             messagebox.showerror("Error",f"Sorry Can't open this PDF Try Another Pdf \n{str(e)}",parent=self.root) 
#             self.browse_txt.set("Browse")   

# root = Tk()
# obj = Pdf(root)
# root.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk
# from tkinter.filedialog import askopenfile
# from tkinter import messagebox
# from PyPDF2 import PdfReader
# from functions import *
# from pdfminer.high_level import extract_text
# import os
# import pymysql

# class Pdf:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1000x667+180+20")
#         self.root.title("Pdf Extractor")
#         self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
#         # -- icon -- 
#         self.icon = ImageTk.PhotoImage(file="images/icon.png")
#         self.root.iconphoto(False, self.icon)
#         # -- Creating frame for header --
#         frame = Frame(self.root, width=1000, height=200, bg="white")
#         frame.grid(columnspan=3, rowspan=2, row=0)
        
#         # -- Creating frame for nav frame -- 
#         frame_nav = Frame(self.root, width=1000, height=50, bg="#DADFEA")
#         frame_nav.grid(columnspan=3, rowspan=1, row=2)
#         # -- Creating frame for save and copy frame -- 
#         frame_save = Frame(self.root, width=1000, height=80, bg="#B8C5E5")
#         frame_save.grid(columnspan=3, rowspan=1, row=3)
#         # -- Creating frame for main content -- 
#         frame_con = Frame(self.root, width=1000, height=337, bg="#6187E6")
#         frame_con.grid(columnspan=3, rowspan=2, row=4)
#         # -- Getting Logo -- 
#         self.logo = ImageTk.PhotoImage(file="images/logo.png")
#         logo_label = Label(self.root, image=self.logo)
#         logo_label.place(x=50, y=10)
#         # -- Instructions Text --
#         instructions = Label(self.root, text="Select a PDF File", font="ARVO", bg="white")
#         instructions.place(x=746, y=50)
#         # -- Browse Button -- 
#         self.browse_txt = StringVar()
#         browse = Button(self.root, textvariable=self.browse_txt, command=self.open_file, font="ARVO", cursor="hand2", bg="#E53333", fg="#FFFFFF", width=15, height=1)
#         self.browse_txt.set("Browse")
#         browse.place(x=740, y=80)
#         # -- Expanding Canvas -- 
#         # -- Creating Canvas --
#         canvas = Canvas(self.root, width=600, height=250)
#         canvas.grid(columnspan=3)
#         # -- arrays to get contents
#         self.page_contents = []  # to Store all the text content 
#         self.all_images = []     # to Store all the images of PDF file
#         self.img_idx = [0]       # in this, Stored value will be assumed as index value of all_images this will change once user click on arrow btn 
#         self.display_images = [] # to Store the Data of image currently displaying on Window
#         self.counter = []        # in this new value will be added when user will click on save image 
        
#     # right arrow
#     def right_arr(self):
#         if self.img_idx[-1] < len(self.all_images) - 1: 
#             #change to the following index
#             self.new_idx = self.img_idx[-1] + 1
#             self.img_idx.pop()
#             self.img_idx.append(self.new_idx)   # self.img_idx = [1]
#             #remove displayed image if exists
#             if self.display_images:
#                 self.display_images[-1].place_forget()
#                 self.display_images.pop()
#             #create a new image in the new index & display it
#             self.new_img = self.all_images[self.img_idx[-1]]  # self.all_images[1] 
#             self.current_img = display_img(self.new_img)      # display_img(images stored on 1st index value in self.all_images list)     
#             self.display_images.append(self.current_img)
#             self.what_text.set("Image " + str(self.img_idx[-1] + 1) + " out of " + str(len(self.all_images)))
    
#     # left arrow
#     def left_arr(self):
#         if self.img_idx[-1] >= 1:
#             #change to the following index
#             self.new_idx = self.img_idx[-1] - 1
#             self.img_idx.pop()
#             self.img_idx.append(self.new_idx)
#             #remove displayed image if exists
#             if self.display_images:
#                 self.display_images[-1].place_forget()
#                 self.display_images.pop()
#             #create a new image in the new index & display it
#             self.new_img = self.all_images[self.img_idx[-1]]
#             self.current_img = display_img(self.new_img)           
#             self.display_images.append(self.current_img)
#             self.what_text.set("Image " + str(self.img_idx[-1] + 1) + " out of " + str(len(self.all_images)))
 
#     # To Not directly Close the window.
#     def on_exit(self):
#         if messagebox.askyesno("Exit", "Do you want to quit the Pdf Extractor"):
#             self.root.destroy()
    
#     # -- second window for table may contain in pdf y/n
#     def table_may(self):
#         self.answer = messagebox.askyesnocancel("The Pdf file may contain tables do you want to save the tables","Continue playing?")
   
#     # -- Browse Button Function --
#     def open_file(self):
#         # clearing the counter once new file opens and restarting by 0
#         self.counter.clear()
#         self.counter.append(0)
#         # also clearing the folder single image
#         directory = "Single image"
#         for f in os.listdir(directory):
#             os.remove(os.path.join(directory, f))

#         # poping all the index from img_idx array and restarting by 0
#         for i in self.img_idx:
#             self.img_idx.pop()
#         self.img_idx.append(0)
#         self.browse_txt.set("Loading..")

#         # poping all the index from display_images array
#         if self.display_images:
#             self.display_images[-1].place_forget()
#             self.display_images.pop()
        
#         # poping all the content of page_contents Array
#         if self.page_contents:
#             for i in self.page_contents:
#                 self.page_contents.pop()
#         # poping all the previous file images from all_images array
#         for i in range(0, len(self.all_images)):
#             self.all_images.pop()

#         # code for browsing the file 
#         try:
#             browse_file = askopenfile(parent=self.root, mode="rb", title="Choose a File", filetypes=[("Pdf File", "*.pdf")])
#             if browse_file:
#                 self.read_pdf = PdfReader(browse_file, strict=False)

#                 # if file is Encrypted
#                 if self.read_pdf.is_encrypted:
#                     self.read_pdf.decrypt('')
                
#                 # Extracting Process Text
#                 self.page = self.read_pdf.pages[0]
#                 self.page_content = extract_text(browse_file)
#                 self.page_contents.append(self.page_content)

#                 # To save Tables or not 
#                 self.answer = messagebox.askyesnocancel("","The Pdf file may contain tables do you want to save the tables?")
#                 if self.answer == True:
#                     messagebox.showinfo("Path", "All the Tables are stored in tables folder you can access their.")
#                     messagebox.showinfo("Note!", "Previous tables stored in table folder will be removed")
#                     tables(browse_file.name)
    
#                 # -- text box -- 
#                 display_textbox(self.root, self.page_content, 0, 4)
#                 self.browse_txt.set("Browse")

#                 # -- Extracting Process Images --
#                 images = extract_img(browse_file.name, self.page) # This will give an Array of data of all the images 

#                 # -- appending all the Images to all_images Array
#                 for i in images:
#                     self.all_images.append(i)
                
#                 # try block to show whether images are in file or not 
#                 try:
#                     self.img = images[self.img_idx[-1]] # 0 index or latest we can say 
#                     self.current_image = display_img(self.img) # Display Image 
#                     self.display_images.append(self.current_image) # Appending image which is on window
#                 except IndexError:
#                     messagebox.showinfo("", "No Images Found.")

#                 # -- what image text -- 
#                 self.what_text = StringVar()
#                 wht_image = Label(self.root, textvariable=self.what_text, font="ARVO", bg="#DADFEA")
#                 self.what_text.set("Image " + str(self.img_idx[-1] + 1) + " out of " + str(len(self.all_images)))
#                 wht_image.place(x=465, y=215)
#                 # -- nav arrows -- 
#                 # Left arrow
#                 self.left_arrow = ImageTk.PhotoImage(file="images/arrow2.png")
#                 self.left_arrow_btn = Button(self.root, image=self.left_arrow, command=lambda: [self.left_arr(), self.what_text], bd=0, bg="#DADFEA", height=40)
#                 self.left_arrow_btn.place(x=400, y=205)
#                 # Right arrow
#                 self.right_arrow = ImageTk.PhotoImage(file="images/arrow1.png")
#                 self.right_arrow_btn = Button(self.root, image=self.right_arrow, command=lambda: [self.right_arr(), self.what_text], bd=0, bg="#DADFEA", height=40)
#                 self.right_arrow_btn.place(x=625, y=205) #x=595
#                 # -- Copy Text Button -- 
#                 self.copy_txt = Button(self.root, text="Copy Text", command=lambda: copy_text(self.page_contents, self.root), cursor="hand2", font="ARVO", width=15, height=1, bg="#3371FF", fg="#FFFFFF")
#                 self.copy_txt.place(x=200, y=275)
#                 # -- Save Single Image Button -- 
#                 self.save_single_img = Button(self.root, text="Save Image", command=lambda: save_img(self.all_images, self.img_idx, self.counter), cursor="hand2", font="ARVO", width=15, height=1, bg="#3371FF", fg="#FFFFFF")
#                 self.save_single_img.place(x=455, y=275)
#                 # -- Save all image Button -- 
#                 self.save_all_img = Button(self.root, text="Save all Images", command=lambda: save_all(self.all_images), cursor="hand2", font="ARVO", width=15, height=1, bg="#3371FF", fg="#FFFFFF")
#                 self.save_all_img.place(x=715, y=275)
#         except Exception as e:
#             messagebox.showerror("Error", f"Sorry Can't open this PDF Try Another Pdf \n{str(e)}", parent=self.root) 
#             self.browse_txt.set("Browse")   

# root = Tk()
# obj = Pdf(root)
# root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from PyPDF2 import PdfReader
from functions import *
from pdfminer.high_level import extract_text
import os

class Pdf:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x667+180+20")
        self.root.title("Pdf Extractor")
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        # -- icon --
        self.icon = ImageTk.PhotoImage(file="images/icon.png")
        self.root.iconphoto(False, self.icon)
        # -- Creating frame for header --
        frame = Frame(self.root, width=1000, height=200, bg="white")
        frame.grid(columnspan=3, rowspan=2, row=0)
        
        # -- Creating frame for nav frame --
        frame_nav = Frame(self.root, width=1000, height=50, bg="#DADFEA")
        frame_nav.grid(columnspan=3, rowspan=1, row=2)
        # -- Creating frame for save and copy frame --
        frame_save = Frame(self.root, width=1000, height=80, bg="#B8C5E5")
        frame_save.grid(columnspan=3, rowspan=1, row=3)
        # -- Creating frame for main content --
        frame_con = Frame(self.root, width=1000, height=337, bg="#6187E6")
        frame_con.grid(columnspan=3, rowspan=2, row=4)
        # -- Getting Logo --
        self.logo = ImageTk.PhotoImage(file="images/logo.png")
        logo_label = Label(self.root, image=self.logo)
        logo_label.place(x=50, y=10)
        # -- Instructions Text --
        instructions = Label(self.root, text="Select a PDF File", font="ARVO", bg="white")
        instructions.place(x=746, y=50)
        # -- Browse Button --
        self.browse_txt = StringVar()
        browse = Button(self.root, textvariable=self.browse_txt, command=self.open_file, font="ARVO", cursor="hand2", bg="#E53333", fg="#FFFFFF", width=15, height=1)
        self.browse_txt.set("Browse")
        browse.place(x=740, y=80)
        # -- Expanding Canvas --
        # -- Creating Canvas --
        canvas = Canvas(self.root, width=600, height=250)
        canvas.grid(columnspan=3)
        # -- arrays to get contents
        self.page_contents = []  # to Store all the text content 
        self.all_images = []     # to Store all the images of PDF file
        self.img_idx = [0]       # in this, Stored value will be assumed as index value of all_images this will change once user click on arrow btn 
        self.display_images = [] # to Store the Data of image currently displaying on Window
        self.counter = []        # in this new value will be added when user will click on save image 
        
    # right arrow
    def right_arr(self):
        if self.img_idx[-1] < len(self.all_images) - 1:
            #change to the following index
            self.new_idx = self.img_idx[-1] + 1
            self.img_idx.pop()
            self.img_idx.append(self.new_idx)   # self.img_idx = [1]
            #remove displayed image if exists
            if self.display_images:
                self.display_images[-1].place_forget()
                self.display_images.pop()
            #create a new image in the new index & display it
            self.new_img = self.all_images[self.img_idx[-1]]  # self.all_images[1] 
            self.current_img = display_img(self.new_img)      # display_img(images stored on 1st index value in self.all_images list)     
            self.display_images.append(self.current_img)
            self.what_text.set("Image " + str(self.img_idx[-1] + 1) + " out of " + str(len(self.all_images)))
    
    # left arrow
    def left_arr(self):
        if self.img_idx[-1] >= 1:
            #change to the following index
            self.new_idx = self.img_idx[-1] - 1
            self.img_idx.pop()
            self.img_idx.append(self.new_idx)
            #remove displayed image if exists
            if self.display_images:
                self.display_images[-1].place_forget()
                self.display_images.pop()
            #create a new image in the new index & display it
            self.new_img = self.all_images[self.img_idx[-1]]
            self.current_img = display_img(self.new_img)           
            self.display_images.append(self.current_img)
            self.what_text.set("Image " + str(self.img_idx[-1] + 1) + " out of " + str(len(self.all_images)))
 
    # To Not directly Close the window.
    def on_exit(self):
        if messagebox.askyesno("Exit", "Do you want to quit the Pdf Extractor"):
            self.root.destroy()
    
    # -- second window for table may contain in pdf y/n
    def table_may(self):
        self.answer = messagebox.askyesnocancel("The Pdf file may contain tables do you want to save the tables","Continue playing?")
   
    # -- Browse Button Function --
    def open_file(self):
        # clearing the counter once new file opens and restarting by 0
        self.counter.clear()
        self.counter.append(0)
        # also clearing the folder single image
        directory = "Single image"
        for f in os.listdir(directory):
            os.remove(os.path.join(directory, f))

        # poping all the index from img_idx array and restarting by 0
        for i in self.img_idx:
            self.img_idx.pop()
        self.img_idx.append(0)
        self.browse_txt.set("Loading..")

        # poping all the index from display_images array
        if self.display_images:
            self.display_images[-1].place_forget()
            self.display_images.pop()
        
        # poping all the content of page_contents Array
        if self.page_contents:
            for i in self.page_contents:
                self.page_contents.pop()
        # poping all the previous file images from all_images array
        for i in range(0, len(self.all_images)):
            self.all_images.pop()

        # code for browsing the file 
        try:
            browse_file = askopenfile(parent=self.root, mode="rb", title="Choose a File", filetypes=[("Pdf File", "*.pdf")])
            if browse_file:
                self.read_pdf = PdfReader(browse_file, strict=False)

                # if file is Encrypted
                if self.read_pdf.is_encrypted:
                    self.read_pdf.decrypt('')
                
                # Extracting Process Text
                self.page = self.read_pdf.pages[0]
                self.page_content = extract_text(browse_file)
                self.page_contents.append(self.page_content)

                # To save Tables or not 
                self.answer = messagebox.askyesnocancel("","The Pdf file may contain tables do you want to save the tables?")
                if self.answer == True:
                    messagebox.showinfo("Path","All the Tables are stored in tables folder you can access their.")
                    messagebox.showinfo("Note!","Previous tables stored in table folder will be removed")
                    tables(browse_file.name)
    
                # -- text box -- 
                display_textbox(self.root, self.page_content, 0, 4)
                self.browse_txt.set("Browse")

                # -- Extracting Process Images --
                images = extract_img(browse_file.name, self.page)  # This will give an Array of data of all the images 

                # -- appending all the Images to all_images Array
                for i in images:
                    self.all_images.append(i)
                
                # try block to show whether images their in file or not 
                try:
                    self.img = images[self.img_idx[-1]]  # 0 index or latest we can say 
                    self.current_image = display_img(self.img)  # Display Image 
                    self.display_images.append(self.current_image)  # Appending image which is on window
                except IndexError:
                    messagebox.showinfo("", "No Images Found.")

                # -- what image text -- 
                self.what_text = StringVar()
                wht_image = Label(self.root, textvariable=self.what_text, font="ARVO", bg="#DADFEA")
                self.what_text.set("Image " + str(self.img_idx[-1] + 1) + " out of " + str(len(self.all_images)))
                wht_image.place(x=465, y=215)
                # -- nav arrows -- 
                # Left arrow
                self.left_arrow = ImageTk.PhotoImage(file="images/arrow2.png")
                self.left_arrow_btn = Button(self.root, image=self.left_arrow, command=self.left_arr, cursor="hand2", bg="#DADFEA")
                self.left_arrow_btn.place(x=150, y=220)
                # right arrow
                self.right_arrow = ImageTk.PhotoImage(file="images/arrow1.png")
                self.right_arrow_btn = Button(self.root, image=self.right_arrow, command=self.right_arr, cursor="hand2", bg="#DADFEA")
                self.right_arrow_btn.place(x=770, y=220)
                # save btn
                self.save_txt = StringVar()
                save_btn = Button(self.root, textvariable=self.save_txt, command=self.save, font="ARVO", cursor="hand2", bg="#9AD2A5", fg="#000000", width=12, height=1)
                self.save_txt.set("Save Image")
                save_btn.place(x=465, y=320)
                # copy btn
                self.copy_txt = StringVar()
                copy_btn = Button(self.root, textvariable=self.copy_txt, command=self.copy, font="ARVO", cursor="hand2", bg="#87C3D1", fg="#000000", width=12, height=1)
                self.copy_txt.set("Copy Text")
                copy_btn.place(x=465, y=360)
                
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.browse_txt.set("Browse")
    
    # -- Saving Single Image -- 
    def save(self):
        try:
            # Getting current file name
            file_name = "Single image/image" + str(self.counter[-1]) + ".jpg"
            # Getting current displayed Image
            self.img_to_save = self.all_images[self.img_idx[-1]]
            # Saving Image
            save_img(self.img_to_save, file_name)
            messagebox.showinfo("", "File Saved!")
            # Updating counter by 1
            self.new_counter = self.counter[-1] + 1
            self.counter.pop()
            self.counter.append(self.new_counter)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    # -- Copying Text --
    def copy(self):
        self.page_content = self.page_contents[-1]
        self.root.clipboard_clear()
        self.root.clipboard_append(self.page_content)
        messagebox.showinfo("", "Text Copied!")


if __name__ == "__main__":
    root = Tk()
    app = Pdf(root)
    root.mainloop()
