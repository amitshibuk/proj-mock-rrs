from tkinter import *
import mysql.connector
from PIL import ImageTk, Image
from datetime import *
import tkinter.messagebox
import tkcap
import os

def print_ticket(p_result, t_result):
    def save():
        try:
            button.destroy()
            cap = tkcap.CAP(root)
            cap.capture("Tickets/Ticket_"+pnr_no+".png")
            tkinter.messagebox.showinfo("Message",  "Image Saved. Check Tickets Folder") #its the message pop-up
        except:
            os.remove("Tickets/Ticket_"+pnr_no+".png")
            cap.capture("Tickets/Ticket_" + pnr_no+ ".png")
            tkinter.messagebox.showinfo("Message", "Image Saved. Check Tickets Folder")


    root = Tk()
    root.title("Ticket")
    root.geometry("900x550")
    bg_img = ImageTk.PhotoImage(Image.open("Ticket2.jpg"))
    bg_label = Label(image=bg_img)
    bg_label.pack()
    global pnr_no
    tdate = datetime.now()
    pnr_no = p_result[0][1]

    #info
    train_no = Label(root, text=t_result[0][0], font=("consolas",14),fg="#2E6AD2", bg="#c1ece8")
    train_name = Label(root, text=t_result[0][1], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea", wraplength=300)
    train_int = Label(root, text=t_result[0][2], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea", wraplength=100)
    train_des = Label(root, text=t_result[0][3], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea", wraplength=100)
    train_int_time = Label(root, text=t_result[0][5], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    train_des_time = Label(root, text=t_result[0][6], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    train_dur = Label(root, text=str(t_result[0][7]) + 'hrs', font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")

    train_cost = Label(root, text='Rs '+str(p_result[0][8]), font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    ticket_no = Label(root, text=p_result[0][0], font=("consolas", 14), fg="#2E6AD2", bg="#c1ece8")
    PNR_no = Label(root, text=p_result[0][1], font=("consolas", 14), fg="#2E6AD2", bg="#c1ece8")
    Pname = Label(root, text=p_result[0][2], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    Psex = Label(root, text=p_result[0][3], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    Page = Label(root, text=p_result[0][4], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    Pdate = Label(root, text=p_result[0][6], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")
    Pseat= Label(root, text=p_result[0][5], font=("consolas", 9, "bold"), fg="#2E6AD2", bg="#e7e7ea")

    ticket_time = Label(root, text=tdate, font=("consolas", 6, "bold"), fg="#000000", bg="#b6b6be")

    #placement
    train_no.place(x=228,y=92)
    train_name.place(x=40, y=184)
    train_int.place(x=410, y=184)
    train_des.place(x=532, y=184)
    train_int_time.place(x=655, y=184)
    train_des_time.place(x=770, y=184)
    train_cost.place(x=754,y=390)
    ticket_no.place(x=50, y=95)
    train_dur.place(x=781, y=305)
    PNR_no.place(x=625, y=95)
    Pname.place(x=48, y=305)
    Psex.place(x=353, y=305)
    Page.place(x=446, y=305)
    Pdate.place(x=520, y=305)
    Pseat.place(x=660, y=305)
    ticket_time.place(x=669,y=441)

    #button
    button = Button(root, text="Save Image",padx=29, pady=20, command=save)
    button.pack(side="bottom")

    root.mainloop()
