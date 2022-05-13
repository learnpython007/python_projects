'''
This app converta a binary value to a decimal on and vice verca. 
'''

print("Welcome the the unit converter. \n")

### RUN THE APP
running = True
while running:
    
    binary = []
    binary_values = [128,64,32,16,8,4,2,1]
    decimal = 0
    y = 0
    hexi = {15:"F",14:"E",13:"D",12:"C",11:"B",10:"A",9:"9",8:"8",7:"7",6:"6",5:"5",4:"4",3:"3",2:"2",1:"1",0:"0"}
    hex_values = [8,4,2,1]
    hex_input = []
    first = []
    first_val = 0
    second = []
    second_val = 0
    
    print("What unit do you have? \n    1 - Binary \n    2 - Decimal \n    3 - Hexidecimal")
    unit = input("Selection: ")
#Binary
    if unit == "1": 
        value = input("Please input your binary value: ")
        if len(value) > 8 or len(value) < 8:
            print("\nThat was not an 8bit binary value. ")
            break
        else:
            for num in value:
                if num == "1" or num == "0":
                    binary.append(int(num))
                    if len(binary) < 5:
                        first.append(int(num))
                    else:
                        second.append(int(num))
                else:
                    print("\nERROR! Only 1's and 0's can be used!")
                    break
            print(f"\nThe binary you have inputted is: {binary}")
            for x in binary:
                if x == 1:
                    decimal = decimal + binary_values[y]
                    y = y + 1
                elif x == 0:
                    y = y + 1
                else:
                    print("\nThat was not a binary number!!!")
                    break
            z = 0
            for x in first:
                if x == 1:
                    first_val = first_val + hex_values[z]
                    z = z + 1
                elif x == 0:
                    z = z + 1
            z = 0
            for x in second:
                if x == 1:
                    second_val = second_val + hex_values[z]
                    z = z + 1
                elif x == 0:
                    z = z + 1
        
        print(f"The hexidecimal value for this is {hexi.get(first_val)}{hexi.get(second_val)}")
        print(f"The decimal value for this is {decimal}")
#Decimal
    elif unit == "2": 
        value = int(input("Please input your decimal value (0-255): "))
        if value > 256 or value < 0:
            print("\nThat was not a value within range. ")
            break
        else:
            for num in binary_values:
                if value - num >= 0:
                    binary.append(1)
                    value = value - num
                elif value - num < 0:
                    binary.append(0)
            z = 0
            while z < 4:
                if binary[z] == 1:
                    first_val = first_val + hex_values[z]
                    z = z + 1
                elif binary[z] == 0:
                    z = z + 1
            z = 0
            z2 = 4
            while z2 < 8:
                if binary[z2] == 1:
                    second_val = second_val + hex_values[z]
                    z = z + 1
                    z2 = z2 + 1
                elif binary[z2] == 0:
                    z = z + 1
                    z2 = z2 + 1
            
        while len(binary) < 8:
            binary.append(0)
        print(f"The hexidecimal value for this is {hexi.get(first_val)}{hexi.get(second_val)}")
        print(f"The binary value for this is {binary}")
#Hexidecimal
    elif unit == "3": 
        value = input("Please input your hexidecimal value: ")
        for val in value.upper():
            for key, hex in hexi.items():
                if val == hex:
                    hex_input.append(key)
                    
        hex1 = hex_input[0]
        hex2 = hex_input[1]
        
        z = 0
        for x in hex_values:
            if hex1 >= hex_values[z]:
                binary.append(1)
                hex1 -= hex_values[z]
                z += 1
            else:
                binary.append(0)
                z += 1
                
        z = 0
        for x in hex_values:
            if hex2 >= hex_values[z]:
                binary.append(1)
                hex2 -= hex_values[z]
                z += 1
            else:
                binary.append(0)
                z += 1

        #ADD DECIMAL VALUE
        for x in binary:
            if x == 1:
                decimal = decimal + binary_values[y]
                y = y + 1
            elif x == 0:
                y = y + 1
        print()        
        print(f"The binary value for this is {binary}")
        print(f"The decimal value for this is {decimal}")
        
        
    else:
        print("That was not an option. ")
    
# END THE APP OR CONTINUE WITH ANOTHER
    again = ""
    while again != "Y" or "N":
        again = input("Do you want to input another value? (y or n) ")
        if again.upper() == "Y":
            break
        elif again.upper() == "N":
            print("Thanks for using this app! ")
            running = False
            break
