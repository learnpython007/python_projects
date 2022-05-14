'''
This app converta a binary value to a decimal on and vice verca. 
'''

import tkinter as tk
import code

def app():
    root = tk.Tk()
    root.title("Unit Converter")
    root.resizable(0,0)
    
    welcome = tk.Label(root, text="Welcome to the Unit Converter", width=50)
    welcome.grid(row=0, sticky="WE")
    
    def new_window():
        frame1 = tk.Frame(root, width=30)
        frame1.grid(row=1)
        
        frame2 = tk.Frame(root)
        frame2.grid(row=2)
        
        seletion_lbl = tk.Label(frame1,text="What unit do you have?")
        seletion_lbl.grid(row=0, columnspan=3)
        
        r = tk.StringVar()
        
        def clicked(value):
            if value == "Binary":
                selection_lbl["text"] = "Please insert your Binary value \n(8 bit, 1's and 0's only)"
                selection_button["command"] = submit_binary
                selection_lbl.grid(row=4, column=0, columnspan=3)
                selection_input.grid(row=5, column=0, columnspan=3)
                selection_button.grid(row=6, columnspan=3)
            elif value == "Decimal":
                selection_lbl["text"] = "Please insert your Decimal value \n(0-255)"
                selection_button["command"] = submit_decimal
                selection_lbl.grid(row=4, column=0, columnspan=3)
                selection_input.grid(row=5, column=0, columnspan=3)
                selection_button.grid(row=6, columnspan=3)
            elif value == "Hexidecimal":
                selection_lbl["text"] = "Please insert your Hexidecimal value \n(2 characters, 0-9, A-f)"
                selection_button["command"] = submit_hexi
                selection_lbl.grid(row=4, column=0, columnspan=3)
                selection_input.grid(row=5, column=0, columnspan=3)
                selection_button.grid(row=6, columnspan=3)
                
        def submit_binary():
            selection_button.destroy()
            output = code.binary_call(selection_input.get())
            try:
                if output[3] == 1:
                    error_lbl.grid(column=0, row=0, columnspan=3)
                    reset_button.grid(row=1, column=0, columnspan=2)
            except:
                error_lbl.grid(column=0, row=0, columnspan=3)
                reset_button.grid(row=1, column=0, columnspan=2)
            else:
                output_lbl_dec.grid(row=0, column=0, sticky="E")
                output_value_1 = tk.Label(frame2, text=output[0])
                output_value_1.grid(row=0, column=1, sticky="W")
                output_lbl_hex.grid(row=1, column=0, sticky="E")
                output_value_2 = tk.Label(frame2, text=f"{output[1]}{output[2]}")
                output_value_2.grid(row=1, column=1, sticky="W")
                reset_button.grid(row=2, column=0, columnspan=2)
            
        def submit_decimal():
            selection_button.destroy()
            output = code.decimal_call(selection_input.get())
            try:
                if output[3] == 1:
                    error_lbl.grid(column=0, row=0, columnspan=3)
                    reset_button.grid(row=1, column=0, columnspan=2)
            except:
                error_lbl.grid(column=0, row=0, columnspan=3)
                reset_button.grid(row=1, column=0, columnspan=2)
            else:
                output_lbl_bin.grid(row=0, column=0, sticky="E")
                output_value_1 = tk.Label(frame2, text=output[0])
                output_value_1.grid(row=0, column=1, sticky="W")
                output_lbl_hex.grid(row=1, column=0, sticky="E")
                output_value_2 = tk.Label(frame2, text=f"{output[1]}{output[2]}")
                output_value_2.grid(row=1, column=1, sticky="W")
                reset_button.grid(row=2, column=0, columnspan=2)
            
        def submit_hexi():
            selection_button.destroy()
            output = code.hexidecimal_call(selection_input.get())
            try:
                if output[2] == 1:
                    error_lbl.grid(column=0, row=0, columnspan=3)
                    reset_button.grid(row=1, column=0, columnspan=2)
            except:
                error_lbl.grid(column=0, row=0, columnspan=3)
                reset_button.grid(row=1, column=0, columnspan=2)
            else:
                output_lbl_bin.grid(row=0, column=0, sticky="E")
                output_value_1 = tk.Label(frame2, text=output[0])
                output_value_1.grid(row=0, column=1, sticky="W")
                output_lbl_dec.grid(row=1, column=0, sticky="E")
                output_value_2 = tk.Label(frame2, text=output[1])
                output_value_2.grid(row=1, column=1, sticky="W")
                reset_button.grid(row=2, column=0, columnspan=2)
                
        def reset_fields():
            frame1.destroy()
            frame2.destroy()
            new_window()

        options = ("Binary", "Decimal", "Hexidecimal")
        for opt in options:
            tk.Radiobutton(frame1, indicatoron=False, width=15, text=opt, variable=r, value=opt, command=lambda:clicked(r.get())).grid(padx=100, sticky="W")

        selection_lbl = tk.Label(frame1)
        selection_input = tk.Entry(frame1,width=10, )
        selection_button = tk.Button(frame1, text="Submit",width=8)
        output_lbl_bin = tk.Label(frame2, text="The binary version is: ")
        output_lbl_dec = tk.Label(frame2, text="The decimal version is: ")
        output_lbl_hex = tk.Label(frame2, text="The hexidecimal version is: ")
        reset_button = tk.Button(frame2, text="New", width=8, command=reset_fields)
        error_lbl = tk.Label(frame2, text="ERROR")
    try:
        new_window()
        root.mainloop()
    except:
        root.destroy()
    
app()
