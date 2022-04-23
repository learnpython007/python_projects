#!/bin/python3

'''
This is GUI using Tkinter that will display the CPU, Memory and GPU usage in real time.
The window will refresh every 0.5 seconds.
'''

from hashlib import new
import platform, subprocess
import tkinter as tk
from tkinter.ttk import Progressbar
try: 
    import psutil
except:
    print("Some packages need to be installed... please wait. ")
    subprocess.call("pip3 install psutil")
    print("Starting...")
    import psutil

def app():

    #define constants
    os_name = platform.system()
    if os_name == "Windows":
        pass #display  stats specific to windows
    elif os_name == "Linux":
        pass #display  stats specific to linux

    #create root window
    root = tk.Tk()
    root.title("PC Monitor GUI")
    root.resizable(0,0)

    ### FRAME 1 ###
    frame1 = tk.Frame(root)
    frame1.grid() #place frame 1

    #frame 1 items
    label1 = tk.Label(frame1, text="PC MONITOR\nThis is a test GUI.", font="arial", height=4, width=50)
    label1.grid(column=0,row=0) #place label 1

    ### FRAME 2 ###
    #place frame 2
    frame2 = tk.Frame(root)
    frame2.grid(column=0, row=1) 
    
    #frame 2 items
    f2_lbl_OS = tk.Label(frame2, text="Operating System:", font="arial") #label
    f2_lbl_OS.grid(column=0,row=0,sticky="E") #place label
    f2_label5 = tk.Label(frame2, text=os_name, font="arial") #value
    f2_label5.grid(column=1,row=0, sticky="W") #place value

    f2_lbl_cores = tk.Label(frame2, text="No of CPU Cores:", font="arial") #label
    f2_lbl_cores.grid(column=0,row=1,sticky="E") #place label
    f2_label6 = tk.Label(frame2, text=psutil.cpu_count(), font="arial") #value
    f2_label6.grid(column=1,row=1, sticky="W") #place value

    f2_lbl_cpuUsage = tk.Label(frame2, text="CPU Usage:", font="arial") #label
    f2_lbl_cpuUsage.grid(column=0,row=2,sticky="E") #place label
    f2_lbl_cpu_value = tk.Label(frame2, font="arial") #value
    f2_lbl_cpu_value.grid(column=1,row=2, sticky="W") #place value
    cpu_progress = Progressbar(frame2, orient="horizontal", mode="determinate", length=200, name="cpu usage") #value progress bar
    cpu_progress.grid(column=2, row=2, columnspan=2) #place value progress bar

    f2_lbl_totRAM = tk.Label(frame2, text="Total Memory:", font="arial") #label
    f2_lbl_totRAM.grid(column=0,row=3,sticky="E") #place label
    f2_label8 = tk.Label(frame2, text=f"{psutil.virtual_memory()[0] / (1024*1024*1024):.2f}GB", font="arial") #value
    f2_label8.grid(column=1,row=3, sticky="W") #place value

    f2_lbl_UsedRAM = tk.Label(frame2, text="Memory Usage:", font="arial") #label
    f2_lbl_UsedRAM.grid(column=0,row=4,sticky="E") #place label
    f2_label9 = tk.Label(frame2, font="arial") #value
    f2_label9.grid(column=1,row=4, sticky="W") #place value
    mem_progress = Progressbar(frame2, orient="horizontal", mode="determinate", length=200, name="mem usage") #value progress bar
    mem_progress.grid(column=2, row=4) #place value progress bar

    ### Frame 3 ###
    frame3 = tk.Frame(root)
    frame3.grid()
    
    # Frame 3 items
    button1 = tk.Button(frame3, relief=tk.RAISED, text="Close", command=root.destroy, width=8, height=1, font="arial")
    button1.grid(column=0,row=6, columnspan=2, padx=5, pady=5)
    
    #update functions
    def update():
        x = psutil.cpu_percent()
        y = psutil.virtual_memory()[2]
        f2_lbl_cpu_value["text"] = f"{x:.2f}%"
        cpu_progress["value"] = x
        f2_label9["text"] = f"{y:.2f}%"
        mem_progress["value"] = y
        f2_lbl_cpu_value.after(500, update)

    

    update()

    #root mainloop
    root.mainloop()

if __name__ == "__main__":
    app()
