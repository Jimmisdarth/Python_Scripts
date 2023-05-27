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


        line = '\t' + read_file.readline()  # Diabazoume to prwto shma kai bazoume ena tab
        Port = ""
            
        input_signals = []      # Tha to kanoume me list of strings anti na metrame
        output_signals = []

        while entity_name not in line:
            if "in" in line:
                input_signals.append(line)
            else:
                output_signals.append(line)
            
            line = '\t' + read_file.readline()

        while '\t\t\t' in input_signals:        # Afairoume ola ta tabs
            input_signals.remove('\t\t\t')

        while '\t\t\t' in output_signals:       # Afairoume ola ta tabs
            output_signals.remove('\t\t\t')
        
        while '\t\t\t\n' in output_signals:     # Afairoume tabs kai enter mazi
            output_signals.remove('\t\t\t\n')

        Port = ""
        Port = Port.join(input_signals + output_signals)

        write_file.write("\tComponent " + entity_name + " is\n")
        write_file.write("\t\tport (\n")
        write_file.write(Port)
        write_file.write("\tend Component;\n\n")


        ## Internal Signals
        write_file.write("\t-- Internal Inputs to UUT\n")

        for signal in input_signals:
            signal = signal.replace("in", "")   # Afairoume to in apo ta shmata
            signal = signal.replace("\t", "")   # Afairoume ola ta tabs pou diabasthkan

            if "STD_LOGIC" in signal:
                signal = signal.replace(";", " := '0';")
            else:
                signal = signal.replace(";", " := (others => '0');")
            
            write_file.write("\t" + "signal " + signal)


        ## External Signals
        write_file.write("\n\t-- External Outputs to UUT\n")

        for index, signal in enumerate(output_signals):
            signal = signal.replace("out", "")          # Afairoume to out apo to shma
            signal = signal.replace("\t", "")           # afairoume ola ta tabs pou diabasthkan

            if index == len(output_signals) - 1:        # Ean einai to teleutaio shma tote tha exei
                signal = signal.replace(")", "", 1)     # tha exei ena parapanw ')'
            
            write_file.write("\t" + "signal " + signal)


        ## Clock Period
        write_file.write("\n\t-- Clock period definitions\n")
        write_file.write("\tconstant CLK_period : time := 10 ns;\n\n")


        ## Architecture Body
        write_file.write("begin\n\n")


        ## Instantiate the UUT
        write_file.write("\t-- Instantiate the Unit Under Test (UUT)\n")
        write_file.write("\tuut: " + entity_name)
        write_file.write("\n\t\tport map(")

        entity_signals = input_signals + output_signals # Enwnonoume ola ta shmata se mia lista
        
        for index, signal in enumerate(entity_signals):
            signal = signal.replace("\t\t\t", "")

            args_of_signal = signal.split()
            signal_name = args_of_signal[0]

            write_file.write("\n\t\t\t" + signal_name + " => " + signal_name)

            if index != len(entity_signals) - 1:
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

