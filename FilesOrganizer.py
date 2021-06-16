import tkinter
from tkinter import*
from tkinter import ttk,filedialog,messagebox
import os,shutil

class Sorting_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Files Organizer | Developed by Amar and Piyush")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.wm_iconbitmap('folder.ico')
        self.logo_icon=PhotoImage(file="images/folder2.png")
        title=Label(
            self.root,text="Files Organizer",
            padx=10, 
            image=self.logo_icon, 
            compound= LEFT ,
            font=("impact",40),
            bg="#023548",
            fg="white",
            anchor="w",
            height=100
            ).place(x=0,y=0,relwidth=2)


        #=======Section1======#

        self.var_foldername=StringVar()

        lbl_select_folder=Label(
            self.root,text="Select Folder",
            font=("times new roman",25),
            bg="white"
            ).place(x=50,y=120)

        folder_name=Entry(
            self.root,
            textvariable=self.var_foldername,
            font=("times new roman",15),
            state='readonly',
            bg="lightyellow"
            ).place(x=250,y=120,height=40,width=600)

        btn_browse=Button(
            self.root,
            command=self.browse_function,
            text="BROWSE",
            font=("times new roman",15,"bold"),
            bg="#262626",
            fg="white",
            activebackground="#262626",
            activeforeground="white",
            cursor="hand2"
            ).place(x=900,y=120,height=45,width=150)

        hr=Label(
            self.root,bg="lightgray"
            ).place(x=50,y=190,height=2,width=1250)

         #=======Section2======#
         #=======All Extensions======#

        self.image_extensions=["Image Extensions",".png",".jpg",".jpeg",".PNG"]
        self.audio_extensions=["Audio Extensions",".amr",".mp3"]
        self.video_extensions=["Video Extensions",".mp4",".avi",".mpeg4",".3gp"]
        self.doc_extensions=["Document Extensions",".doc",".pdf",".ppt",".xlsx",".pptx",".xls",".docx",".zip",".rar","csv","txt"]

        self.folders={
                'videos':self.video_extensions,
                'audios':self.audio_extensions,
                'images':self.image_extensions,
                'documents':self.doc_extensions
                }

        lbl_support_ext=Label(
            self.root,text="Various Supported File Extensions",
            font=("times new roman",25),
            bg="white"
            ).place(x=50,y=210)

        self.image_box=ttk.Combobox(self.root,values=self.image_extensions,state="readonly" , font=("new times roman", 15), justify=CENTER)
        self.image_box.place(x=60,y=265,width=270,height=35)
        self.image_box.current(0)

        self.video_box=ttk.Combobox(self.root,values=self.video_extensions,state="readonly" , font=("new times roman", 15), justify=CENTER)
        self.video_box.place(x=380,y=265,width=270,height=35)
        self.video_box.current(0)

        self.audio_box=ttk.Combobox(self.root,values=self.audio_extensions,state="readonly" , font=("new times roman", 15), justify=CENTER)
        self.audio_box.place(x=700,y=265,width=270,height=35)
        self.audio_box.current(0)

        self.doc_box=ttk.Combobox(self.root,values=self.doc_extensions,state="readonly" , font=("new times roman", 15), justify=CENTER)
        self.doc_box.place(x=1020,y=265,width=270,height=35)
        self.doc_box.current(0)


        #=======Section3======#
        #=======All Image Icons======#

        self.image_icon=PhotoImage(file="images/image3.png",)
        self.audio_icon=PhotoImage(file="images/music2.png")
        self.video_icon=PhotoImage(file="images/video2.png")
        self.document_icon=PhotoImage(file="images/doc2.png")
        self.others_icon=PhotoImage(file="images/question-mark2.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=320,width=1250,height=300)

        self.lbl_total_files=Label(Frame1,text="Total Files : ",font=("times new roman",20),bg="white")
        self.lbl_total_files.place(x=10,y=10)

        self.lbl_total_image=Label(Frame1,bd=2, relief=RAISED, image=self.image_icon , compound=TOP, font=("times new roman",20,"bold"),bg="#827B60",fg="black")
        self.lbl_total_image.place(x=20,y=60,width=230,height=200)

        self.lbl_total_audio=Label(Frame1, bd=2, relief=RAISED, image=self.audio_icon, compound=TOP, font=("times new roman",20,"bold"),bg="#5E5A80",fg="black")
        self.lbl_total_audio.place(x=260,y=60,width=230,height=200)

        self.lbl_total_video=Label(Frame1,bd=2, relief=RAISED, image=self.video_icon, compound=TOP, font=("times new roman",20,"bold"),bg="#ADD8E6",fg="black")
        self.lbl_total_video.place(x=500,y=60,width=230,height=200)

        self.lbl_total_document=Label(Frame1,bd=2, relief=RAISED, image=self.document_icon, compound=TOP, font=("times new roman",20,"bold"),bg="#BAB86C",fg="black")
        self.lbl_total_document.place(x=740,y=60,width=230,height=200)

        self.lbl_total_others=Label(Frame1,bd=2, relief=RAISED, image=self.others_icon, compound=TOP, font=("times new roman",20,"bold"),bg="silver",fg="black")
        self.lbl_total_others.place(x=980,y=60,width=230,height=200)

         #=======Section4======#

        lbl_status=Label(
            self.root,text="STATUS :",
            font=("times new roman",20,"bold"),
            bg="white"
            ).place(x=50,y=625)

        self.lbl_st_total=Label(
            self.root,text="",
            font=("times new roman",18),
            fg="green",
            bg="white"
            )
        self.lbl_st_total.place(x=300,y=625)

        self.lbl_st_moved=Label(
            self.root,text="",
            font=("times new roman",18),
            fg="blue",
            bg="white"
            )
        self.lbl_st_moved.place(x=500,y=625)

        self.lbl_st_left=Label(
            self.root,text="",
            font=("times new roman",18),
            fg="orange",
            bg="white"
            )
        self.lbl_st_left.place(x=700,y=625)

        #=====Buttons======#

        self.btn_clear=Button(
            self.root,
            command=self.clear,
            text="CLEAR",
            font=("times new roman",15,"bold"),
            bg="#607d8b",
            fg="white",
            activebackground="#607d8b",
            activeforeground="white",
            cursor="hand2"
            )
        self.btn_clear.place(x=880,y=625,height=45,width=200)

        self.btn_start=Button(
            self.root,
            state=DISABLED,
            command=self.start_function,
            text="START",
            font=("times new roman",15,"bold"),
            bg="#ff5722",
            fg="white",
            activebackground="#ff5722",
            activeforeground="white",
            cursor="hand2"
            )
        self.btn_start.place(x=1100,y=625,height=45,width=200)

    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.count=0
        combine_list=[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True:
                self.count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                   # print(folder_name)
                   for x in folder_name[1]:
                       combine_list.append(x)
                   if ext.lower() in folder_name[1] and folder_name[0]=="images":
                       images+=1
                   if ext.lower() in folder_name[1] and folder_name[0]=="audios":
                       audios+=1
                   if ext.lower() in folder_name[1] and folder_name[0]=="videos":
                       videos+=1
                   if ext.lower() in folder_name[1] and folder_name[0]=="documents":
                       documents+=1

        #This is for calculating others file only
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True:
                ext="."+i.split(".")[-1] 
                if ext.lower() not in combine_list:
                    others+=1

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_document.config(text="Total Documents\n"+str(documents))
        self.lbl_total_others.config(text="Other Files\n"+str(others))
        self.lbl_total_files.config(text="Total Files: "+str(self.count))


    def browse_function(self):
        op=filedialog.askdirectory(title="SELECT FOLDER FOR SORTING")
        if op!=None:
            #print(op)
            self.var_foldername.set(str(op))
            self.directory=self.var_foldername.get()
            self.other_name= "others"
            self.rename_folder()
            self.all_files=os.listdir(self.directory)  # put all files in list
            length=len(self.all_files)
            count=1
            self.Total_count()
            self.btn_start.config(state=NORMAL)
    
    def start_function(self):
        c=0
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directory,i))==True:
                    c+=1
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_st_total.config(text="TOTAL: "+str(self.count))
                    self.lbl_st_moved.config(text="MOVED: "+str(c))
                    self.lbl_st_left.config(text="LEFT: "+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()              
                    
            messagebox.showinfo("Success","All Files has been Sorted Successfully")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showinfo("Error","Please Select Folder")

    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")
        self.lbl_total_image.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_document.config(text="")
        self.lbl_total_others.config(text="")
        self.lbl_total_files.config(text="Total Files")


    def rename_folder(self):
        for folder in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory,folder))==True:
                os.rename(os.path.join(self.directory,folder),os.path.join(self.directory,folder.lower()))


    def create_move(self,ext,file_name):
        find=False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:      
                if folder_name not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory,folder_name))
                shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,folder_name))
                find=True
                break
        if find!=True:
            if self.other_name not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory,self.other_name))
            shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,self.other_name))



root=Tk()
obj=Sorting_App(root)
root.mainloop()