import re
import tkinter.scrolledtext as st
import tkinter as tk
from tkinter import *
import csv
import time
from binary_tree import binary1
from Lulea_Algorithm import lulia1



window = tk.Tk()

window.title("Virtual Router")


# Setting icon of master window
window.wm_iconbitmap('icone.ico')

window.geometry("1267x519")
window.configure(bg="#3A7FF6")
canvas = tk.Canvas(
    window, bg="#3A7FF6", height=1019, width=2000,
    bd=0, highlightthickness=0)
canvas.place(x=0, y=0)
canvas.create_rectangle(431, 0, 431 + 931, 0 + 919, fill="#FCFCFC", outline="")



label1=tk.Label(text="router>>")

label1.place(x=490.0, y=159,height=26)
cmd_entry = tk.Text(bd=0, bg="#f4f4f4", highlightthickness=0)
cmd_entry.place(x=540.0, y=137+25, width=280.0, height=25)
cmd_entry.focus()



data = st.ScrolledText(bg="#f4f4f4")
data.place(x=490.0, y=180+25, width=330.0, height=170)




var1=IntVar()
lulia=tk.Checkbutton(text="lulea algo    ", variable=var1,onvalue = 1, offvalue = 0 )

lulia.place(x=540.0, y=425)
var2 = IntVar()
binary=tk.Checkbutton(text="binary algo", variable=var2, onvalue = 1, offvalue = 0)
binary.place(x=680,y=425)








canvas.create_text(
    600.5, 88.0, text="IOS COMMAND LINE INTERFACE.",
    fill="#515486", font=("Arial-BoldMT", int(13.0)))

canvas.create_text(
    520.5, 400.0, text="choose an algorithm:",
    fill="#515486", font=("Arial-BoldMT", int(10.0)))

canvas.create_text(
    500.5, 480.0, text="Elapsed Time:",
    fill="#515486", font=("Arial-BoldMT", int(10.0)))




title = tk.Label(
    text="Welcome to our virtual Router", bg="#3A7FF6",
    fg="white", font=("Arial-BoldMT", int(20.0)))
title.place(x=27.0, y=120.0)


info_text = tk.Label(
    text="This i a virtual router made by Anas\nbahi and yasser belaichi that simulate\na Cisco router and use binary and lulea\nas a search algorithm.\n\n"

    "See the instructions on the right,\nto see how to use this Router.",
    bg="#3A7FF6", fg="white", justify="left",
    font=("Georgia", int(16.0)))

info_text.place(x=27.0, y=200.0)



how_to_use = st.ScrolledText(bg="#f4f4f4",
                            width = 44,
                            height = 30,
                             )
how_to_use.pack(side=RIGHT)




window.resizable(False, False)

#########function##############
def decimal_binary_for_tree(ip):
    binary_ip=""
    match = re.search(r'(\d+).(\d+).(\d+).(\d+)', ip)
    for i in range(1,5):
        to_bin=bin(int(match.group(i)))
        groupe=to_bin.replace("0b",((8-(len(to_bin)-2))*"0"))
        binary_ip+=groupe
    return binary_ip
timer1 = Label(window,
                    text="",bg="white",fg="#515486",
                    font=("Arial-BoldMT", int(8.0)))

timer1.place(x=550.0, y=470.0)




def show_command():






    get_value=cmd_entry.get("0.0", tk.END)



    data.config(state=NORMAL)



    file=open("table_routage.csv","r")
    readble_file=csv.reader(file)
    dellimeter = next(readble_file)
    data.delete("0.0", END)


    if  len(re.findall("show ip route static",get_value))!=0 or len(re.findall("SHOW IP ROUTE STATIC",get_value))!=0 :

        text1 = ""
        for i in readble_file:
            text1 += "S    " + i[0] + "is directly \nconnected, " + i[4] + "\n"
        data.insert(tk.INSERT, text1)
    elif  len(re.findall("show cef",get_value))!=0 or  len(re.findall("SHOW CEF",get_value))!=0:



        text2 = "network" + "                 " + "interface\n"
        text2 += "\n"
        for i in readble_file:
            text2 += i[0] + "\t \t \t" + i[4] + "\n"
        data.insert(tk.INSERT, text2)
    elif len(re.findall("ping *",get_value))!=0 or   len(re.findall("PING *",get_value))!=0:


        if var1.get()==1:
            match = re.findall(r'\d+.\d+.\d+.\d+', get_value)
            text3 = "Type escape sequence to abort.Sending 5, 100-byte ICMP Echos to " + match[
                0] + "\ntimeout is 2 seconds:\n"
            data.insert(tk.INSERT, text3)
            start = time.time()
            try:

                lulia1.lockup(match[0])
                end = time.time()
                elapsed_time=(end-start)
                data.insert(tk.INSERT, "Success rate is 100 percent (5/5), round-trip time with lulea lockup ="+str(elapsed_time)+"s")
                timer1.config(text=str(elapsed_time)+" s")
            except:

                time.sleep(2)
                data.insert(tk.INSERT, ".....Success rate is 0 percent (0/5)")
                end = time.time()
                elapsed_time = (end - start)
                timer1.config(text=str(elapsed_time) + " s")


        elif var2.get() == 1:

            match = re.findall(r'\d+.\d+.\d+.\d+', get_value)
            text3 = "Type escape sequence to abort.Sending 5, 100-byte ICMP Echos to " + match[
                0] + "\ntimeout is 2 seconds:\n"
            data.insert(tk.INSERT, text3)
            start = time.time()

            try:
                binary1.loockup(match[0])
                end = time.time()
                elapsed_time = (end - start)
                print(elapsed_time)

                data.insert(tk.INSERT, "!!!!!Success rate is 100 percent (5/5), round-trip time with binary lockup =" + str(elapsed_time) + "s")
                timer1.config(text=str(elapsed_time) + " s")
            except:


                time.sleep(2)
                end = time.time()
                elapsed_time = (end - start)

                data.insert(tk.INSERT, ".....Success rate is 0 percent (0/5)")
                timer1.config(text=str(elapsed_time) + " s")


    elif  len(re.findall("ip route \d+.\d+.\d+.\d+ *",get_value ))!=0 or len(re.findall("IP ROUTE \d+.\d+.\d+.\d+ *",get_value ))!=0:
        patterne=re.search(r'(\d+.\d+.\d+.\d+) * (\d+.\d+.\d+.\d+) * ethernet (\d)',get_value)
        mask=patterne.group(2)
        mask1=0
        if patterne.group(2)=="255.0.0.0":
            mask1=8
        elif patterne.group(2)=="255.0.0.0":
            mask1=16
        else:
            mask1=24
        file=open("table_routage.csv","a",newline="")
        write_file=csv.writer(file)
        ip=patterne.group(1)
        interface="ethernet"+patterne.group(3)
        write_file.writerow([patterne.group(1)+"/"+str(mask1), mask, decimal_binary_for_tree(ip), decimal_binary_for_tree(mask),interface])
        file.close()
        binary1.insert_ip(ip,mask1,interface)
        lulia1.insert(ip,mask1,interface)
        lulia1.leaf_pushing()
        lulia1.final()

        
        
        
        


    elif len(re.findall("clear ip route*",get_value ))!=0 or len(re.findall("CLEAR IP ROUTE*",get_value ))!=0:
        file=open("table_routage.csv","w",newline="")
        write_file = csv.writer(file)
        filed_name = ["network", "mask", "binary_network", "mask_binary", "interface"]
        write_file.writerow(filed_name)
        file.close()
    else:
        data.insert(tk.INSERT, "command not found")







        
    data.config(state=DISABLED)


run=tk.Button(text="run",command=show_command)
run.place(x=830, y=159,height=26,width=50)
data.config(state=DISABLED)
how_to_use.insert(tk.INSERT,"show cef\n \n")
how_to_use.insert(tk.INSERT,"To display the IPv4 Cisco Express Forwarding(CEF) table\n\n")

how_to_use.insert(tk.INSERT,"show ip route static\n\n")
how_to_use.insert(tk.INSERT,"show routing table entries for static routes\n\n")

how_to_use.insert(tk.INSERT,"ping\n\n")
how_to_use.insert(tk.INSERT,"test the accessibility of IP network. \n\n")

how_to_use.insert(tk.INSERT,"ip route network mask interface \n\n")
how_to_use.insert(tk.INSERT,"This command defines a static route for a \nspecific destination network.\n\n")

how_to_use.insert(tk.INSERT,"clear ip route\n\n")

how_to_use.insert(tk.INSERT,"To clear the routing table of all routes\n\n")

how_to_use.insert(tk.INSERT,"NB!\n\n")
how_to_use.insert(tk.INSERT,"Insert command and click run,dont forget to choose an algorithm\n")
how_to_use.insert(tk.INSERT,"Elapsed time shows the difference of\ncomplexity between binary and\nlulia algorithm when you ping.\n\n")


how_to_use.tag_add('word1','1.0','1.end')
how_to_use.tag_config('word1', font='arial 15 bold',foreground="#3A7FF6")
how_to_use.tag_add('word2','5.0','5.end')
how_to_use.tag_config('word2', font='arial 15 bold',foreground="#3A7FF6")
how_to_use.tag_add('word3','9.0','9.end')
how_to_use.tag_config('word3', font='arial 15 bold',foreground="#3A7FF6")
how_to_use.tag_add('word4','13.0','13.end')
how_to_use.tag_config('word4', font='arial 15 bold',foreground="#3A7FF6")
how_to_use.tag_add('word5','18.0','18.end')
how_to_use.tag_config('word5', font='arial 15 bold ',foreground="#3A7FF6")
how_to_use.tag_add('word6','22.0','22.end')
how_to_use.tag_config('word6',font='arial 15 bold ',foreground="#3A7FF6")
how_to_use.config(state=DISABLED)



window.mainloop()
