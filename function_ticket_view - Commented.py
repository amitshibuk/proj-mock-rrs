from tkinter import *
import mysql.connector
from PIL import ImageTk, Image
from datetime import *
import tkinter.messagebox
import tkcap
import os

#remember to gather all the date before calling this fucntion
def print_ticket(p_result, t_result):
    #the screenshot saving fucntion
    def save():
        try:
            button.destroy() #this will destroy the button before screenshot, also prevents user from spamming
            cap = tkcap.CAP(root)
            cap.capture("Tickets/Ticket_"+pnr_no+".png") #mention relative path and file name here, you see the global below? its for this
            tkinter.messagebox.showinfo("Message",  "Image Saved. Check Tickets Folder") #its the message pop-up
        except:
            os.remove("Tickets/Ticket_"+pnr_no+".png") #incase a file already exits, this command will remove it
            cap.capture("Tickets/Ticket_" + pnr_no+ ".png") #these are the same stuff again
            tkinter.messagebox.showinfo("Message", "Image Saved. Check Tickets Folder")


    root = Tk()
    #Title of window
    root.title("Ticket")
    #DImensions of the window
    root.geometry("900x550")
    #This was the base image I used got the ticket. The image has the same dimenstions as the window
    bg_img = ImageTk.PhotoImage(Image.open("C:/Users/amits/Documents/school Stuff/CLASS 12/Computer Science/Project/Ticket1.jpg"))
    #Here I just imported image and added it
    bg_label = Label(image=bg_img)
    bg_label.pack()
    global pnr_no
    #This is to print the date time etc part at the bottom
    tdate = datetime.now()
    pnr_no = p_result[0][1]

    #Info, these are all the informations collected from the Train info
    #the gathering and stuff for the files was done before this fucntion is called.
    #We just bring in the information as a parameter (under t_result and P_result)
    #these are the train stuff below
    train_no = Label(root, text=t_result[0][0], font=("consolas",14),fg="#2E6AD2", bg="#c1ece8")
    train_name = Label(root, text=t_result[0][1], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea", wraplength=300)
    train_int = Label(root, text=t_result[0][2], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea", wraplength=100)
    train_des = Label(root, text=t_result[0][3], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea", wraplength=100)
    train_int_time = Label(root, text=t_result[0][5], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    train_des_time = Label(root, text=t_result[0][6], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    train_cost = Label(root, text='Rs '+str(t_result[0][7]), font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    #these are the passanger stuff
    ticket_no = Label(root, text=p_result[0][0], font=("consolas", 14), fg="#2E6AD2", bg="#c1ece8")
    PNR_no = Label(root, text=p_result[0][1], font=("consolas", 14), fg="#2E6AD2", bg="#c1ece8")
    Pname = Label(root, text=p_result[0][2], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    Psex = Label(root, text=p_result[0][3], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    Page = Label(root, text=p_result[0][4], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    Pdate = Label(root, text=p_result[0][6], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    Pseat= Label(root, text=p_result[0][5], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")

    ticket_time = Label(root, text=tdate, font=("consolas", 6, "bold"), fg="#000000", bg="#b6b6be")

    #placement, so basically I just used the coordinates of the pixel from which i wanted these to start displaying.
    #you can find xy coordinates in any good image editor
    train_no.place(x=228,y=92)
    train_name.place(x=40, y=184)
    train_int.place(x=410, y=184)
    train_des.place(x=532, y=184)
    train_int_time.place(x=655, y=184)
    train_des_time.place(x=770, y=184)
    train_cost.place(x=754,y=390)
    ticket_no.place(x=50, y=95)
    PNR_no.place(x=625, y=95)
    Pname.place(x=48, y=305)
    Psex.place(x=353, y=305)
    Page.place(x=476, y=305)
    Pdate.place(x=568, y=305)
    Pseat.place(x=763, y=305)
    ticket_time.place(x=669,y=441)

    #this is the save stuff button,
    #it just calls the function 'save'. AT THE TOP!
    button = Button(root, text="Save Image",padx=29, pady=20, command=save)
    button.pack(side="bottom")

    root.mainloop()