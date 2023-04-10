print("log_info_start: GUI pokus v2")

import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import webbrowser
from encoder import Encoder
from decoder import Decoder

#GUI--------------------------------------------------------------------------------------------------------------------
master_gui = tk.Tk()
master_gui.title("GUI-ver:0.2.2")
screen_width = master_gui.winfo_screenwidth()
screen_height = master_gui.winfo_screenheight()
res_add_pic_button = "650x100"
res_add_message = "500x125"
ress_set_output_name = "200x125"
res_display_error = "250x125"
res_decode_button = "250x125"
if screen_width <= 1920 and screen_height <= 1080:
    size_window = "{a}x{b}".format(a=int(screen_width * 0.6),b=int(screen_height * 0.6))
    print("screen should be 1920x1080 or less")
else:
    size_window = "{a}x{b}".format(a=int(screen_width * 0.52),b=int(screen_height * 0.55)) #optimalizovano pro 4k spis
    res_add_pic_button = "850x300"
    res_add_message = "1600x325"
    ress_set_output_name = "600x325"
    res_display_error = "450x325"
    res_decode_button = "580x315"
    print("screen should be higher than full hd")

master_gui.geometry(size_window)
master_gui.configure(bg='#2d2d2d')
master_gui.resizable(True, True)
print(f"{size_window=}") #pak oddelat


#Upper_toolbar----------------------------------------------------------------------------------------------------------
toolbar = tk.Frame(master_gui,highlightbackground='black', highlightthickness=1.5, bg='#232323')
toolbar.pack(side=tk.TOP, fill=tk.X)
#Lower toolbar----------------------------------------------------------------------------------------------------------
toolbar_down = tk.Frame(master_gui,highlightbackground='black', highlightthickness=1.5, bg='#232323')
toolbar_down.pack(side=tk.BOTTOM, fill=tk.X)
#Action bar-------------------------------------------------------------------------------------------------------------
action_bar = tk.Frame(master_gui, bg='#2d2d2d',height=70)
action_bar.pack(side=tk.BOTTOM, fill=tk.X)
#DEF START--------------------------------------------------------------------------------------------------------------
def exit_gui_window(): #exit_button_popup
    print("log_info: oppenning 'exit_gui_window' child window")
    #button_exit['state'] = tk.DISABLED
    exit_window_gui = tk.Toplevel(master_gui)
    exit_window_gui.resizable(False, False)
    exit_window_gui.grab_set()
    exit_window_gui.title("")
    size_window_exit = "{a}x{b}".format(a=int(screen_width * 0.23), b = int(screen_height * 0.13))
    exit_window_gui.geometry(size_window_exit)
    exit_window_gui.configure(bg='#2d2d2d')
    tk.Label(exit_window_gui, text="Are you sure, that u wanna exist?", bg='#2d2d2d', fg='white', height=2).pack()
    button_menu0 = tk.Button(exit_window_gui, text='Close application',height=3,width=20, bg='#b0161d', fg='white',command= lambda: exit("log_info_end: ending whole GUI"))
    button_menu0.pack(side=tk.RIGHT)
    button_menu1 = tk.Button(exit_window_gui, text='Cancel', height=3, width=20, bg='#323232', fg='white',command= lambda: exit_window_gui.destroy() or exit_window_gui.grab_release())
    button_menu1.pack(side=tk.LEFT)

counter = 0 #pro zobrazovani a schovavani add_text_that_u_wanna_hide button
def decode_button():
    print("log_info: encode button actions start here...")
    global counter, file_path
    if counter > 0: #returns to base window display(2 image canvases)
        text_mess_button.pack_forget()
        save_encrypted_picture.pack_forget()
        canvas_decrypt.pack(side=tk.RIGHT, anchor=tk.N)
        canvas_decrypt1.pack(side=tk.LEFT, anchor=tk.N)
        canvas_decrypt.create_image(5, 5, anchor=tk.NW, image=new_image)
        canvas_decrypt1.create_image(5, 5, anchor=tk.NW, image=new_image)
        counter -= 1

    dec = Decoder(file_path)
    dec.decode()
    decode_report = tk.Toplevel(master_gui)
    decode_report.resizable(True, False)
    decode_report.geometry(res_decode_button)
    decode_report.configure(bg='#2d2d2d')
    decode_report_bar = tk.Frame(decode_report, highlightbackground='#2d2d2d', highlightthickness=1.5, bg='#2d2d2d')
    decode_label = tk.Label(decode_report_bar, text = "Encoded message:", bg='#2d2d2d', fg='white')
    decode_message = tk.Label(decode_report_bar, text = dec.__msg__, width=25)
    decode_exit = tk.Button(decode_report_bar, text="Close", bg='#2d2d2d', fg='white', command = decode_report.destroy)
    decode_label.grid(row = 1 , column = 1)
    decode_message.grid(row = 2 , column = 1, pady = 5,padx = 30)
    decode_exit.grid(row = 3 , column = 1)
    decode_report_bar.grid(row =0 , column =0)

    print("log_info: File succesfully decoded")
def encode_button():
    global counter
    print("log_info: decode button actions start here...")
    if counter == 0:
        text_mess_button.pack(side=tk.LEFT,padx=10,pady=10, anchor=tk.W)
        text_mess_button.config(height=1, width=41)
        save_encrypted_picture.pack(side=tk.RIGHT,padx=10,pady=10, anchor=tk.E)
        save_encrypted_picture.config(height=1, width=41)

        #--------------------------------------------------------------------------------------------------
        #canvas_decrypt.pack_forget() #dodelat, aby se to pustilo jedině, když bude pridany novy obrazek
        #canvas_decrypt1.pack_forget()
        #--------------------------------------------------------------------------------------------------

        counter += 1
file_path = ""
def select_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        print("log_info: your file's path: " + file_path)
        image_name = os.path.basename(file_path)
        print("log_info: your file's name: " + image_name)
        path_display.config(text = file_path)

def add_picture():  #on button click changes the picture
    global selected_image
    img = (Image.open(file_path))
    resized_image = img.resize((550,550))
    selected_image = ImageTk.PhotoImage(resized_image)
    canvas_decrypt1.itemconfig(canvas_decrypt_image1, image = selected_image)
    path_display.config(text="")

def display_error(content): # Displays a error message box, content = error message
    print(content)
    add_error_gui = tk.Toplevel(master_gui)
    add_error_gui.resizable(True, True)
    add_error_gui.geometry(res_display_error)
    add_error_gui.configure(bg='#2d2d2d')  
    add_error_bar = tk.Frame(add_error_gui, highlightbackground='#2d2d2d', highlightthickness=1.5, bg='#2d2d2d')
    error_announcement = tk.Label(add_error_bar, text = "Error!", bg='#2d2d2d', fg='white')
    error_description = tk.Label(add_error_bar, text = content, bg='#2d2d2d', fg='white')
    error_close = tk.Button(add_error_bar, text = "Close", bg='#2d2d2d', fg='white', command = add_error_gui.destroy)
    error_announcement.grid(row = 0, column = 1)
    error_description.grid(row = 1, column = 1)
    error_close.grid(row = 2, column = 1)
    add_error_bar.grid(row = 0, column = 0)

def add_message():
    global message_entry
    add_message_gui = tk.Toplevel(master_gui)
    add_message_gui.resizable(True,False)
    add_message_gui.geometry(res_add_message)
    add_message_gui.configure(bg='#2d2d2d')
    add_message_bar = tk.Frame(add_message_gui, highlightbackground='#2d2d2d', highlightthickness=1.5, bg='#2d2d2d')
    message_description = tk.Label(add_message_bar, text = "Your message:", bg='#2d2d2d', fg='white')
    message_confirm = tk.Button(add_message_bar, text = "Confirm message & encode", bg='#2d2d2d', fg='white', command = lambda: get_message())
    message_exit = tk.Button(add_message_bar, text = "Exit", bg='#2d2d2d', fg='white', command = add_message_gui.destroy)
    message_entry = tk.Entry(add_message_bar, width = 75)
    message_description.grid(row = 0, column = 1, padx = 208)
    message_entry.grid(row = 1, column = 1, pady = 5)
    message_confirm.grid(row = 2, column = 1, pady = 5)
    message_exit.grid(row = 3, column = 1, pady = 5)
    add_message_bar.grid(row = 0, column = 0)

def get_message():
    global user_message
    global selected_image1
    user_message = message_entry.get()
    if len(user_message) > 255 or len(user_message) < 0:
        display_error("Message is too long or short!")
    print("log_info: User message is: " + str(user_message))
    message_entry.delete(0,999)

    enc = Encoder(file_path, user_message, output_name)
    enc.encode()
    print("log_info: File succesfully encoded")
    img = (Image.open(output_name))
    resized_image = img.resize((550,550))
    selected_image1 = ImageTk.PhotoImage(resized_image)
    canvas_decrypt.itemconfig(canvas_decrypt_image, image = selected_image1)

def add_pic_button():
    global path_display
    global file_path
    print("log_info: add picture address def")
    print(image_name)
    add_pic_gui = tk.Toplevel(master_gui)
    add_pic_gui.resizable(False,True)
    add_pic_gui.grab_set()
    add_pic_gui.geometry(res_add_pic_button)
    add_pic_gui.configure(bg='#2d2d2d')
    add_address_bar0 = tk.Frame(add_pic_gui, highlightbackground='#2d2d2d', highlightthickness=1.5, bg='#2d2d2d')
    path_description = tk.Label(add_address_bar0, text='File path: ', bg='#2d2d2d', fg='white')
    add_image = tk.Button(add_address_bar0, text='Add image', bg='#2d2d2d', fg='white', command=lambda:add_picture()) # add picture button
    path_display = tk.Label(add_address_bar0, text=file_path, width=50)
    file_select = tk.Button(add_address_bar0, text='Select file', bg='#2d2d2d', fg='white', command=lambda:select_file())
    exit = tk.Button(add_address_bar0, text='Exit', bg='#2d2d2d', fg='white', command=add_pic_gui.destroy, padx=2.5, pady=2.5)
    path_description.grid(row = 0, column = 0, pady = 5, padx = 10)
    add_image.grid(row = 2, column= 0)
    path_display.grid(row = 0, column = 1)
    file_select.grid(row = 1, column = 0) 
    exit.grid(row = 1, column = 2, pady = 5)
    add_address_bar0.grid(row = 0, column= 0)

def set_output_name():
    global name_entry
    add_output_name_gui = tk.Toplevel(master_gui)
    add_output_name_gui.resizable(True,False) #x,y
    add_output_name_gui.geometry(ress_set_output_name)
    add_output_name_gui.configure(bg='#2d2d2d')
    add_output_name_bar = tk.Frame(add_output_name_gui, highlightbackground='#2d2d2d', highlightthickness=1.5, bg='#2d2d2d')
    label_description = tk.Label(add_output_name_bar, text = "Set name:", bg='#2d2d2d', fg='white')
    save_name = tk.Button(add_output_name_bar, text = "Set", bg='#2d2d2d', fg='white', command = lambda: get_output_name())
    output_exit = tk.Button(add_output_name_bar, text = "Exit", bg='#2d2d2d', fg='white', command = add_output_name_gui.destroy)
    name_entry = tk.Entry(add_output_name_bar, width = 25)
    label_description.grid(row = 0, column = 1, pady = 5)
    name_entry.grid(row = 1, column = 1, padx = 25)
    save_name.grid(row = 2, column = 1, pady = 5)
    output_exit.grid(row = 3, column = 1, pady = 5)
    add_output_name_bar.grid(row = 0, column = 0)

def get_output_name():
    global output_name
    output_name = name_entry.get()
    name_entry.delete(0,999)
    print("log_info: Your output file name is: " + output_name)
#DEF END----------------------------------------------------------------------------------------------------------------
#visible buttons--------------------------------------------------------------------------------------------------------
button_menu0 = tk.Button(toolbar, text='Add picture', bg='#323232', fg='white',command=add_pic_button) #add picture button
button_menu1 = tk.Button(toolbar, text='DECODE', bg='#323232', fg='white', command= decode_button) #decode button
button_menu2 = tk.Button(toolbar, text='ENCODE', bg='#323232', fg='white', command= encode_button) #encode button
button_menu3 = tk.Button(toolbar, text='Help', bg='#323232', fg='white', command= lambda: webbrowser.open_new('https://youtu.be/dQw4w9WgXcQ')) #log view button
button_exit = tk.Button(toolbar_down, font='Comic-sans', text="Exit", bg='#323232', fg='white', command= exit_gui_window) #Exit the whole gui button
button_menu0.pack(side=tk.LEFT, padx=10, pady=10)
button_menu1.pack(side=tk.LEFT, padx=10, pady=10)
button_menu2.pack(side=tk.LEFT, padx=10, pady=10)
button_menu3.pack(side=tk.RIGHT, padx=10, pady=10)
button_exit.pack(side=tk.BOTTOM, padx=10, pady=10)
#hiden by when start----------------------------------------------------------------------------------------------------
text_mess_button = tk.Button(action_bar, text='Add hidden message & encode!', bg='#323232', fg='white', command = lambda:add_message())#pop-up buttun when 'encode' is pressed
save_encrypted_picture = tk.Button(action_bar, text='Choose output file name', bg='#323232', fg='white', command=lambda:set_output_name())
#decrypted picture canvas-----------------------------------------------------------------------------------------------
image_name = "empty.png"
image_path = os.path.abspath(image_name)
img= (Image.open(image_path))
canvas_decrypt= tk.Canvas(master_gui, width= 550, height= 550)
canvas_decrypt.pack(side=tk.RIGHT, anchor=tk.N)
resized_image= img.resize((550,550)) #Image.ANTIALIAS removed, because of the support end
new_image= ImageTk.PhotoImage(resized_image)
canvas_decrypt_image = canvas_decrypt.create_image(5,5, anchor=tk.NW, image=new_image)
#end decrypted picture canvas-------------------------------------------------------------------------------------------
canvas_decrypt1= tk.Canvas(master_gui, width= 550, height= 550) #pokus
canvas_decrypt1.pack(side=tk.LEFT, anchor=tk.N)
canvas_decrypt_image1 = canvas_decrypt1.create_image(5,5, anchor=tk.NW, image=new_image)
#END of the master-gui--------------------------------------------------------------------------------------------------
master_gui.mainloop()