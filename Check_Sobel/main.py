################################################


sim_results_file_name = "tb_results.txt"
results_file_name= "results.txt"
final_result_name = "errors.txt"


with open(sim_results_file_name, 'r') as simulation_file:
    with open(results_file_name, 'r') as result_file:
        with open(final_result_name, 'w') as write_file:

            sim_line = simulation_file.readline()
            res_line = result_file.readline()

            count = 0
            error = 0
        
            while len(sim_line) > 0 and len(res_line) > 0:
                error = int(sim_line, 2) - int(res_line)

                write_file.write(str(error) + '\n')

                if error != 0:
                    count += 1

                sim_line = simulation_file.readline()
                res_line = result_file.readline()

            print("\nBRETHIKAN " + str(count) + " SFALMATA")

            if count == 0:
                print("EPITYXES TEST DEN BRETHIKE OUTE ENA SFALMA\n")
        