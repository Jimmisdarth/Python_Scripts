file_name = "gen.txt"


with open(file_name, 'w') as write_file:
    print("Gidi")

    for i in range(3):
        write_file.write("\tSubtractor_S" + str(i) + "x: Subtractor\n")
        write_file.write("\t	generic map(\n")
        write_file.write("\t		WIDTH => WIDTH\n")
        write_file.write("\t			)\n")
        write_file.write("\t	port map(\n")
        write_file.write("\t		A => Pixels_in.Pixel_" + str(i) + "2,	-- A - B\n")
        write_file.write("\t	    B => Pixels_in.Pixel_" + str(i) + "0,\n\n")

        write_file.write("\t		S => Stage1_Sums.S" + str(i) + "x\n")
        write_file.write("\t			);\n\n")

    for i in range(3):
        write_file.write("\tSubtractor_S" + str(i) + "y: Subtractor\n")
        write_file.write("\t	generic map(\n")
        write_file.write("\t		WIDTH => WIDTH\n")
        write_file.write("\t			)\n")
        write_file.write("\t	port map(\n")
        write_file.write("\t		A => Pixels_in.Pixel_0" + str(i) + ",	-- A - B\n")
        write_file.write("\t	    B => Pixels_in.Pixel_2" + str(i) + ",\n\n")

        write_file.write("\t		S => Stage1_Sums.S" + str(i) + "y\n")
        write_file.write("\t			);\n\n")



# for i in range(3):
#         for j in range(3):
#             write_file.write("\tDFF_Pixel_" + str(i) + str(j) + ": DFF\n")
#             write_file.write("\t		generic map(\n")
#             write_file.write("\t			WIDTH => WIDTH\n")
#             write_file.write("\t				)\n")
#             write_file.write("\t		port map(\n")
#             write_file.write("\t			CLK   => CLK,\n")
#             write_file.write("\t			RESET => RESET,\n")
#             write_file.write("\t			D     => i_Pixels.Pixel_" + str(i) + str(j) + ",\n")
#             write_file.write("\t			Q     => Pixels_in.Pixel_" + str(i) + str(j) + "\n")
#             write_file.write("\t				);\n\n")