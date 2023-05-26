#################################################################################
#################################################################################
#
# Diabazei ena arxeio .vhd me onoma entity: entity_name kai dhmiourgei ena
# testbench gia to sygkekrimeno entity me ola ta ejjwterika tou shmata dhlomena
# kai ena process pou trexei gia 100ns.

entity_name = "UART"
tb_entity_name = entity_name + "_tb"    # entity_tb

design_file_name = entity_name + '.vhd'
testbench_file_name = tb_entity_name + '.vhd'

with open(design_file_name, 'r') as read_file:
    with open(testbench_file_name, 'w') as write_file:
        print("Geia")


        ## Header definitions
        write_file.write("library IEEE;\n")
        write_file.write("use IEEE.STD_LOGIC_1164.ALL;\n")
        write_file.write("use IEEE.NUMERIC_STD.ALL;\n")
        write_file.write("use STD.ENV.ALL;\n\n")


        ## Entity name
        write_file.write("entity " + tb_entity_name + " is\n")
        write_file.write("--  Port ( );\n")
        write_file.write("end " + tb_entity_name + ";\n\n")


        ## Architecture definitions
        write_file.write("architecture Behavioral of " + tb_entity_name + " is\n\n")


        ## Component
        write_file.write("\t-- Unit Under Test (UUT)\n")

        line = read_file.readline()     # diabazoume ta headers
        while "Port" not in line:
            line = read_file.readline()


        line = '\t' + read_file.readline()
        Port = ""

        num_of_output_signals = 0
        num_of_input_signals = 0
        while entity_name not in line:
            Port = Port + line

            if "in" in line:
                num_of_input_signals +=1
            if "out" in line:
                num_of_output_signals +=1

            line = '\t' + read_file.readline()

        write_file.write("\tComponent " + entity_name + " is\n")
        write_file.write("\t\tport (\n")
        write_file.write(Port)
        write_file.write("\tend Component;\n\n")


        ## Internal Signals
        write_file.write("\t-- Internal Inputs to UUT\n")

        new_port = Port.split('\n')     # Dhmiourgoume mia lista apo strings pou exei ta shmata tou entity
        #new_port.remove('')

        while '\t\t\t' in new_port:     # Afairoume ola ta tabs
            new_port.remove('\t\t\t')

        while '' in new_port:           # Afairoume ta kena
            new_port.remove('')

        for i in range(num_of_input_signals):
            signal = new_port[i]
            signal.split()                      # dibazoume to port map grammh grammh
            signal = signal.replace("in", "")   # bgazoume to in apo to singal
            signal = signal.replace("\t", "")   # afairoume ola ta tabs pou diabasthkan

            if "STD_LOGIC" in signal:
                signal = signal.replace(";", " := '0';\n")
            else:
                signal = signal.replace(";", " := (others => '0');\n")
            
            write_file.write("\t" + "signal " + signal)


        ## External Signals
        write_file.write("\n\t-- External Outputs to UUT")

        # Total signals
        num_of_signals = num_of_input_signals + num_of_output_signals

        for i in range(num_of_input_signals, num_of_signals):   
            signal = new_port[i]

            signal.split()                       # dibazoume to port map grammh grammh
            signal = signal.replace("out", "")   # bgazoume to in apo to singal
            signal = signal.replace("\t", "")    # afairoume ola ta tabs pou diabasthkan

            if i == num_of_signals-1:               # Ean einai to teleutaio shma tote tha exei
                signal = signal.replace(")", "", 1) # tha exei ena parapanw ')'
            
            write_file.write("\n\t" + "signal " + signal)


        ## Clock Period
        write_file.write("\n\n\t-- Clock period definitions\n")
        write_file.write("\tconstant CLK_period : time := 10 ns;\n\n")


        ## Architecture Body
        write_file.write("begin\n\n")


        ## Instantiate the UUT
        write_file.write("\t-- Instantiate the Unit Under Test (UUT)\n")
        write_file.write("\tuut: " + entity_name)
        write_file.write("\n\t\tport map(")

        for index, line in enumerate(new_port):
            line = line.replace("\t\t\t", "")

            signal_list = line.split()
            signal_name = signal_list[0]

            write_file.write("\n\t\t\t" + signal_name + " => " + signal_name)

            if index != len(new_port) - 1:
                write_file.write(",")

        write_file.write("\n\t\t\t\t);")

        ## Clock Creation
        write_file.write("\n\n\t-- H diadiakasia gia na dhmiourgisoume to roloi")
        write_file.write("\n\tCLK_process : process")
        write_file.write("\n\tbegin")
        write_file.write("\n\t\tCLK <= '0';")
        write_file.write("\n\t\twait for clk_period/2;")
        write_file.write("\n\t\tCLK <= '1';")
        write_file.write("\n\t\twait for clk_period/2;")
        write_file.write("\n\tend process;\n")


        ## Stimulus Process
        write_file.write("\n\t-- Stimulus process definition")
        write_file.write("\n\tStimulus_process: process")

        write_file.write("\n\n\tbegin")

        write_file.write("\n\n\t\t--  Syncronous RESET is deasserted on CLK falling edge")
        write_file.write("\n\t\t--  after GSR signal disable (it remains enabled for 100 ns)\n")

        write_file.write("\n\t\twait for 100 ns;")
        write_file.write("\n\t\twait until (CLK = '0' and CLK'event);\n")

        write_file.write("\n\t\t-- UUT inputs are asserted and deasserted on CLK falling edge\n")

        write_file.write("\n\t\twait for clk_period;\n")

        write_file.write("\n\t\t-- Message and stimulation end")
        write_file.write('\n\t\treport "TEST COMPLETED";')
        write_file.write("\n\t\tstop(2);")

        write_file.write("\n\n\tend process;")


        ## Architecture Ending
        write_file.write("\n\n\nend Behavioral;")

