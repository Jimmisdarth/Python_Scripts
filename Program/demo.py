## Binary file reader
## Diabazei ena binary arxeiou me onoma TEST.BIN to opoio exei apothikeusei entoles
## megethous 4 byte se Big endian kai tis eggrafei se ena allo arxeio Commands.txt
## me morfh Little endian

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

            first_byte  = read_file.read(size_to_read)
            second_byte = read_file.read(size_to_read)
            third_byte  = read_file.read(size_to_read)
            fourth_byte = read_file.read(size_to_read)

            count = count + 1    
    
    
