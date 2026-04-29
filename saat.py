from tkinter import Label, Tk
import time

app_windows = Tk()
app_windows.title ("Dijital Saat")
app_windows.geometry("500x500")
app_windows.resizable(1,1)
app_windows.configure(bg="black")

text_font = ("Boulder",36,'bold')
background = "black"
foreground = "white"
border_widht = 20
#saat etiketi
label = Label(app_windows,font=text_font, bg=background, fg=foreground)
label.grid(row=0,column=1,padx=10,pady=10)
#tarih etiketi
date_label = Label(app_windows,font=text_font, bg=background,fg=foreground)
date_label.grid(row=1,column=1,padx=10,pady=10)

def digital_clock ():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    #tarih alanı
    date_info = time.strftime("%d %B %Y")
    date_label.config(text=date_info)

    

digital_clock()





app_windows.mainloop()












app_windows.mainloop()