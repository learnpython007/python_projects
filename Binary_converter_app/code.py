binary_values = (128,64,32,16,8,4,2,1)
hexi = {15:"F",14:"E",13:"D",12:"C",11:"B",10:"A",9:"9",8:"8",7:"7",6:"6",5:"5",4:"4",3:"3",2:"2",1:"1",0:"0"}
hex_values = (8,4,2,1)

    
def binary_call(value):
    error = 0
    binary = []
    first = []
    second = []
    decimal = 0
    first_val = 0
    second_val = 0
    
    if len(value) > 8 or len(value) < 8:
        error = 1
    else:
        for num in value:
            if num == "1" or num == "0":
                binary.append(int(num))
                if len(binary) < 5:
                    first.append(int(num))
                else:
                    second.append(int(num))
            else:
                error = 1
        
        count = 0
        for x in binary:
            if x == 1:
                decimal = decimal + binary_values[count]
                count = count + 1
            elif x == 0:
                count = count + 1
            else:
                error = 1
        
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
        print(decimal,hexi.get(first_val),hexi.get(second_val),error)
        return decimal,hexi.get(first_val),hexi.get(second_val),error





        
def decimal_call(value):
    error = 0
    binary = []
    first_val = 0
    second_val = 0
    try:
        value = int(value)
    except:
        error = 1
        
    else:    
        if value > 256 or value < 0:
            error = 1
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
        
        for key, value in hexi.items():
            if first_val == key:
                hex1 = value
            if second_val == key:
                hex2 = value
        print(binary,hex1,hex2,error)    
        return(binary,hex1,hex2,error)





def hexidecimal_call(value):
    error = 0
    binary = []
    hex_input = []
    decimal = 0
    count = 0

    for val in value.upper():
        for key, hex in hexi.items():
            if val == hex:
                hex_input.append(key)
    print(hex_input)
                
    try:
        hex1 = hex_input[0]
        hex2 = hex_input[1]
        
        if len(hex_input) != 2:
            error = 1
    
        z = 0
        for x in hex_values:
            if hex1 >= hex_values[z]:
                binary.append(1)
                hex1 -= hex_values[z]
                z += 1
            else:
                binary.append(0)
                z += 1
        print(binary)
                
        z = 0
        for x in hex_values:
            if hex2 >= hex_values[z]:
                binary.append(1)
                hex2 -= hex_values[z]
                z += 1
            else:
                binary.append(0)
                z += 1
        print(binary)

        for x in binary:
            if x == 1:
                decimal = decimal + binary_values[count]
                count = count + 1
            elif x == 0:
                count = count + 1
        print(decimal)
    except:
        error = 1
    print(binary, decimal, error)
    return(binary, decimal, error)
