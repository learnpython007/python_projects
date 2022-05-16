'''
This app converta a binary value to a decimal on and vice verca. 
'''

from aifc import Error
import tkinter as tk
import code

def app():
    root = tk.Tk()
    root.title("Unit Converter")
    root.resizable(0,0)
    
    welcome = tk.Label(root, text="Welcome to the Unit Converter", width=50)
    welcome.grid(row=0, sticky="WE")
      
    frame1 = tk.Frame(root, width=30)
    frame1.grid(row=1)
    
    frame2 = tk.Frame(root)
    frame2.grid(row=2)
    
    selection_lbl = tk.Label(frame1, text="Please insert your value")
    selection_lbl.grid(row=0, column=0, columnspan=3)
    
    selection_input = tk.Entry(frame1,width=10)
    selection_input.grid(row=1, columnspan=3)
    
    seletion_lbl = tk.Label(frame1,text="What unit do you have?")
    seletion_lbl.grid(row=2, columnspan=3)
    
    r = tk.StringVar()
    
    options = ("Binary", "Decimal", "Hexidecimal")
    for opt in options:
        tk.Radiobutton(frame1, indicatoron=False, width=15, text=opt, variable=r, value=opt, command=lambda:clicked(r.get())).grid(padx=100, sticky="W")

    def clicked(value):
        if value == "Binary":
            try:
                output = code.binary_call(selection_input.get())
                output_value_dec["text"] = ""
                output_value_dec["text"] = output[0]
                output_value_hex["text"] = output[1]+output[2]
            except:
                error()
        elif value == "Decimal":
            try:
                output = code.decimal_call(selection_input.get())
                output_value_bin["text"] = output[0]
                output_value_dec["text"] = ""
                output_value_hex["text"] = output[1]+output[2]
            except:
                error()
        elif value == "Hexidecimal":
            try:
                output = code.hexidecimal_call(selection_input.get())
                output_value_bin["text"] = output[0]
                output_value_dec["text"] = output[1]+output[2]
                output_value_hex["text"] = ""
            except:
                error()
            
    
    def error():
        if Error:
            output_value_bin["text"] = "ERROR"
            output_value_dec["text"] = "ERROR"
            output_value_hex["text"] = "ERROR"
            
    output_lbl_bin = tk.Label(frame2, text="The binary version is: ")
    output_lbl_bin.grid(row=0, column=0) 
    output_lbl_dec = tk.Label(frame2, text="The decimal version is: ")
    output_lbl_dec.grid(row=1, column=0)
    output_lbl_hex = tk.Label(frame2, text="The hexidecimal version is: ")
    output_lbl_hex.grid(row=2, column=0)
    output_value_bin = tk.Label(frame2)
    output_value_bin.grid(row=0, column=1, sticky="W")
    output_value_dec = tk.Label(frame2)
    output_value_dec.grid(row=1, column=1, sticky="W")
    output_value_hex = tk.Label(frame2)
    output_value_hex.grid(row=2, column=1, sticky="W")
    
        
    try:
        root.mainloop()
    except:
        root.destroy()
    
app()
