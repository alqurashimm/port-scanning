import threading
import socket
import Tkinter as tk
from datetime import datetime
import time
from Tkinter import *
import sys, struct


def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))


def portscan(port, ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  #
    print("Scanning %s on port %d" % (ip, port))
    printSomething(port, ip)
    try:
        con = s.connect((ip, port))

        print("Host %s is open on port %d " %  (ip, port))
        printSomething(port, ip)

        con.close()

    except:
        pass



def scanhosts():

    # ip = socket.gethostbyname(target)
    begin_time = datetime.now()
    startipadd = mystring.get()
    endipadd = mystring2.get()
    startport = mystring3.get()
    float(startport)
    endport = mystring4.get()
    float(endport)
    startp = int(float(startport))  # get this from the ui
    endp = int(float(endport))
    startip = ip2int(startipadd)
    endip = ip2int(endipadd)
    ips = [startip, endip]
    for ip in range(startip, endip + 1):
        for port in range(startp, endp):
            # print "x: ", x
            t = threading.Thread(target=portscan, args=(port, int2ip(ip)))
            t.start()

            # portscan(port, ip)
            #printSomething(t)



root = tk.Tk()
mystring = tk.StringVar(root)
mystring2 = tk.StringVar(root)
mystring3 = tk.StringVar(root)
mystring4 = tk.StringVar(root)


def getvalue():
    print(mystring.get())
    # print(mystring2.get())
    # print(mystring3.get())


T = Text(root, height=1, width=35)
T.pack()
T1=Text(root,height=1,width=35)
T2= Text(root,height=1,width=35)
T3=Text(root,height=1,width=35)
T.insert(END, "Enter  start ip address to scan\n")
e1 = Entry(root, textvariable=mystring, width=20, fg="blue", bd=3, selectbackground='violet').pack()

T1.insert(END, "Enter end ip address \n")
T1.pack()
e2 = Entry(root, textvariable=mystring2, width=20, fg="blue", bd=3, selectbackground='violet').pack()

T2.insert(END, "Enter start port\n")
T2.pack()
e3 = Entry(root, textvariable=mystring3, width=20, fg="blue", bd=3, selectbackground='violet').pack()

T3.insert(END, "Enter end port\n")
T3.pack()
e4 = Entry(root, textvariable=mystring4, width=20, fg="blue", bd=3, selectbackground='violet').pack()

button1 = tk.Button(root,
                    text='Scan',
                    fg='White',
                    bg='dark green', height=3, width=10, command=scanhosts).pack()


def printSomething(port, ip):
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    prininini = "Scanning %s on port %d" % (ip, port)
    label = Label(root, text= prininini)
    #this creates a new label to the GUI
    label.pack()



root.mainloop()
