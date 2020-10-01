from pytube import *
from tkinter import *
from tkinter.filedialog import *
file_size = 0
from tkinter.messagebox import *
# import Tkinter
def startdownload():
    global file_size
    try:
        url = urlField.get()
        print(url)
        #changing btn text
        dbtn.config(text="Please Wait...")
        dbtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return
        # creating youtube object with url
        ob = YouTube(url)

        # strms = ob.streams.all()
        # for s in strms:
        #     print(s)
        strm = ob.streams.get_highest_resolution()
        # print(strm.title)
        # print(strm.filesize)
        # print(strm.resolution)
        # # print(ob.description)
        # input("Pess D for Download:")
        strm.download(path_to_save_video)
        print('Done')
        dbtn.config(text="Start Download")
        dbtn.config(state=NORMAL)
        showinfo("Downloaded successfully", "Download successfully")
        urlField.delete(0,END)
    except Exception as e:
        print(e)
        print("ERROR!!")

#START GUI bUILDInG
main = Tk()
#setting tittle
main.title("MY Youtube Downloader")

# set the icon
main.iconbitmap("yt.ico")
main.geometry("400x350")

#heading icon
file = PhotoImage(file='yt.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)
#url textfield
urlField = Entry(main,font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10, pady=20)
dbtn = Button(main, text="Start Download", font=("verdana", 18), relief="ridge", command=startdownload)
dbtn.pack(side=TOP, pady=10)
main.mainloop()

