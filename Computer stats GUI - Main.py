'''
This is GUI using Tkinter that will display the CPU, Memory and GPU usage in real time.
The window will refresh every 0.5 seconds.
'''
# import all necessary modules
import platform, subprocess
import tkinter as tk
from tkinter.ttk import Progressbar, Style
from turtle import color

try: 
    import psutil
except:
    print("Some packages need to be installed... please wait. ")
    subprocess.call("pip3 install psutil")
    import psutil
    print("Starting...")

#TEST AREA OUTSIDE GUI

### START OF THE APPLICATION FUNCTION ###
def app():
    #define constants
    os_name = platform.platform()
    if "Windows" in os_name:
        root_dir = "C:/" 
    elif "Linux" or "macOS" in os_name:
        root_dir = "/"
        
    #create root window
    root = tk.Tk()
    root.title("PC Monitor GUI")
    root.resizable(0,0)

    #progress bar styles
    progress_bar_style = Style()
    progress_bar_style.configure("good.Horizontal.TProgressbar", background="green")
    progress_bar_style.configure("bad.Horizontal.TProgressbar", background="red")

    ### FRAME 1 ###
    frame1 = tk.Frame(root)
    frame1.grid(column=0, row=0) #place frame 1

    #frame 1 items
    label1 = tk.Label(frame1, text="PC MONITOR\nThis is a test GUI.", font="arial", height=4, width=50)
    label1.grid(column=0,row=0) #place label 1

    ### FRAME 2 ###
    #place frame 2
    frame2 = tk.Frame(root)
    frame2.grid(column=0, row=1) 
    
    #OS
    f2_lbl_OS = tk.Label(frame2, text="Operating System:", font="arial") #label
    f2_lbl_OS.grid(column=0,row=0,sticky="E") #place label
    f2_label2 = tk.Label(frame2, text=os_name, font="arial") #value
    f2_label2.grid(column=1,row=0, columnspan=2, sticky="W") #place value

    #CPU Cores
    f2_lbl_cores = tk.Label(frame2, text="No of CPU Cores:", font="arial") #label
    f2_lbl_cores.grid(column=0,row=1,sticky="E") #place label
    f2_label3 = tk.Label(frame2, text=psutil.cpu_count(logical=False), font="arial") #value
    f2_label3.grid(column=1,row=1, sticky="W") #place value

    #CPU usage
    f2_lbl_cpuUsage = tk.Label(frame2, text="CPU Usage:", font="arial") #label
    f2_lbl_cpuUsage.grid(column=0,row=2,sticky="E") #place label
    f2_lbl_cpu_value = tk.Label(frame2, font="arial") #value
    f2_lbl_cpu_value.grid(column=1,row=2, sticky="W") #place value
    cpu_progress = Progressbar(frame2, orient="horizontal", mode="determinate", length=200, name="cpu usage") #value progress bar
    cpu_progress.grid(column=2, row=2, columnspan=2) #place value progress bar

    #total RAM
    f2_lbl_totRAM = tk.Label(frame2, text="Total Memory:", font="arial") #label
    f2_lbl_totRAM.grid(column=0,row=3,sticky="E") #place label
    f2_label5 = tk.Label(frame2, text=f"{psutil.virtual_memory()[0] / (1024*1024*1024):.2f}GB", font="arial") #value
    f2_label5.grid(column=1,row=3, sticky="W") #place value

    #RAM usage
    f2_lbl_UsedRAM = tk.Label(frame2, text="Memory Usage:", font="arial") #label
    f2_lbl_UsedRAM.grid(column=0,row=4,sticky="E") #place label
    f2_lbl_UsedRAM_value = tk.Label(frame2, font="arial") #value
    f2_lbl_UsedRAM_value.grid(column=1,row=4, sticky="W") #place value
    mem_progress = Progressbar(frame2, orient="horizontal", mode="determinate", length=200, name="mem usage") #value progress bar
    mem_progress.grid(column=2, row=4) #place value progress bar
    
    #total disk size
    f2_lbl_storage_size = tk.Label(frame2, text=f"Storage Size({root_dir}):", font="arial") #label
    f2_lbl_storage_size.grid(column=0,row=5,sticky="E") #place label
    f2_lbl_storage_size_value = tk.Label(frame2, font="arial") #value
    f2_lbl_storage_size_value.grid(column=1,row=5, sticky="W") #place value

    #disk
    f2_lbl_storage_used = tk.Label(frame2, text="Storage Usage:", font="arial") #label
    f2_lbl_storage_used.grid(column=0,row=6,sticky="E") #place label
    fe_lbl_storage_used_value = tk.Label(frame2, font="arial") #value
    fe_lbl_storage_used_value.grid(column=1,row=6, sticky="W") #place value
    storage_progress = Progressbar(frame2, orient="horizontal", mode="determinate", length=200, name="storage usage") #value progress bar
    storage_progress.grid(column=2, row=6) #place value progress bar
    
    #Temp - Linux only
    if "Linux" in os_name:
        f2_lbl_temp = tk.Label(frame2, text="Temperature:", font="arial") #label
        f2_lbl_temp.grid(column=0,row=7,sticky="E") #place label
        f2_lbl_temp_value = tk.Label(frame2, font="arial") #value
        f2_lbl_temp_value.grid(column=1,row=7, sticky="W") #place value
        temp_progress = Progressbar(frame2, orient="horizontal", mode="determinate", length=200, name="temperature", maximum=100) #value progress bar
        temp_progress.grid(column=2, row=7) #place value progress bar

    ### Frame 3 ###
    frame3 = tk.Frame(root)
    frame3.grid(column=0, row=2)
    
    # Frame 3 items
    button1 = tk.Button(frame3, relief=tk.RAISED, text="Close", command=root.destroy, width=8, height=1, font="arial")
    button1.grid(column=0,row=6, columnspan=2, padx=5, pady=5)
    
    #update functions
    def update():
        w = psutil.cpu_percent()
        f2_lbl_cpu_value["text"] = f"{w:.2f}%"
        cpu_progress["value"] = w
        if w >= 80:
            cpu_progress["style"] = "bad.Horizontal.TProgressbar"
        elif w < 80:
            cpu_progress["style"] = "good.Horizontal.TProgressbar"

        x = psutil.virtual_memory()[2]
        f2_lbl_UsedRAM_value["text"] = f"{x:.2f}%"
        mem_progress["value"] = x
        if x >= 80:
            mem_progress["style"] = "bad.Horizontal.TProgressbar"
        elif x < 80:
            mem_progress["style"] = "good.Horizontal.TProgressbar"

        if "Windows" in os_name:
            y = psutil.disk_usage(root_dir) 
            f2_lbl_storage_size_value["text"] = f"{y[0] / (1024 ** 3):.2f}Gb" 
            fe_lbl_storage_used_value["text"] = f"{y[3]}%"
            storage_progress["value"] = y[3]
            if y[3] >= 80:
                storage_progress["style"] = "bad.Horizontal.TProgressbar"
            elif y[3] < 80:
                storage_progress["style"] = "good.Horizontal.TProgressbar"
        elif "Linux" in os_name:
            y = psutil.disk_usage(root_dir) 
            f2_lbl_storage_size_value["text"] = f"{y[0] / (1024 ** 3):.2f}Gb"
            fe_lbl_storage_used_value["text"] = f"{y[3]}%"
            storage_progress["value"] = y[3]
            if y[3] >= 80:
                storage_progress["style"] = "bad.Horizontal.TProgressbar"
            elif y[3] < 80:
                storage_progress["style"] = "good.Horizontal.TProgressbar"
            z = psutil.sensors_temperatures()['cpu_thermal'][0][1]
            f2_lbl_temp_value["text"] = f"{z:.2f}°C"
            temp_progress["value"] = z
            if z >= 80:
                temp_progress["style"] = "bad.Horizontal.TProgressbar"
            elif z < 80:
                temp_progress["style"] = "good.Horizontal.TProgressbar"
        elif "macOS" in os_name:
            y = psutil.disk_usage(root_dir)
            f2_lbl_storage_size_value["text"] = f"{y[0] / (1000 ** 3):.2f}Gb" 
            fe_lbl_storage_used_value["text"] = f"{(y[0] - y[2]) / (1000 ** 3):.2f}Gb"
            storage_progress["value"] = (100 / y[0]) * (y[0] - y[2])
            if y[3] >= 80:
                storage_progress["style"] = "bad.Horizontal.TProgressbar"
            elif y[3] < 80:
                storage_progress["style"] = "good.Horizontal.TProgressbar"
        
        f2_lbl_cpu_value.after(500, update)

    update()

    #root mainloop
    root.mainloop()

if __name__ == "__main__":
    app()
