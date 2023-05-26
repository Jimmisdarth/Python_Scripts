## Binary file reader
## Diabazei ena binary arxeiou me onoma TEST.BIN to opoio exei apothikeusei entoles
## megethous 4 byte se Big endian kai tis eggrafei se ena allo arxeio Commands.txt
## me morfh Little endian

def assemblyInstr(machine_code):
    scale = 16 ## equals to hexadecimal

    binary_code = bin(int(machine_code, scale))[2:]

    if binary_code[4:5+1] == "00":  #DP
        print("Data Processing")

    elif binary_code[4:5+1] == "01": #Memory
        print("Memory")

        Rd = int(machine_code[16:19+1], base=16)
        Rn = int(machine_code[12:15+1], base=16)
        Imm12 = int(machine_code[20:31+1], base=16)

        if binary_code[6:11+1] == "011001": #LDR+
            print("LDR "+Rd+", ["+Rn+"+"+Imm12+"]")

    elif binary_code[4:5+1] == "10": #Branch
        if binary_code[6:6+1] == "1":
            if(binary_code[7:7+1] == "0"):
                print("B")
            else:
                print("BL")


    #print(machine_code)
    #print(binary_code)

with open('TEST.BIN', 'rb') as read_file:
    with open('Commands.txt', 'w') as write_file:

        size_to_read = 1
        count = 0

        first_byte  = read_file.read(size_to_read)
        second_byte = read_file.read(size_to_read)
        third_byte  = read_file.read(size_to_read)
        fourth_byte = read_file.read(size_to_read)

        while len(first_byte) > 0:
            if count % 16 == 0:
                write_file.write('\n\n\t')
            elif count % 4 == 0:
                write_file.write('\n\t')

            write_file.write('X"')

            write_file.write(fourth_byte.hex().upper())
            write_file.write(third_byte.hex().upper())
            write_file.write(second_byte.hex().upper())
            write_file.write(first_byte.hex().upper())

            write_file.write('", ')

            machine_code = fourth_byte.hex()+third_byte.hex()+second_byte.hex()+first_byte.hex()
            assemblyInstr(machine_code)

            first_byte  = read_file.read(size_to_read)
            second_byte = read_file.read(size_to_read)
            third_byte  = read_file.read(size_to_read)
            fourth_byte = read_file.read(size_to_read)

            count = count + 1    
