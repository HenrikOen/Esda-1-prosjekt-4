import numpy as np
import matplotlib.pyplot as plt
import csv
import os



#Definin the file paths
Network_filter_path      = "Malinger\\Network_filter_dB.csv"

Scope_diode_path         = "Malinger\\Scope_diode.csv"
spectrum_diode_dB_path   = "Malinger\\Spectrum_diode_overdiodeAndWave_RMS(dB).csv"

scope_output_path        = "Malinger\\Scope_output2.csv"
spectrum_output_dB_path  = "Malinger\\Spectrum_output_RMS(dB).csv"

freq_list = [1000, 2000, 3000, 4000, 5000]
magnetude_list = [1, 2, 3, 4, 5]

#Defining function to convert csv file to lists.
def file_to_list(file, freq_column, magnetude_column):
    freq_list=[]
    magnetude_list=[]
    n=0
    with open(file, 'r') as file:
        data=csv.reader(file)
        for row in data:
            
            if len(row)==0:
                continue
            elif not (row[0][0].isdigit()):
                continue
            freq_list.append(float(row[freq_column]))
            magnetude_list.append(float(row[magnetude_column]))
        return freq_list, magnetude_list
    

#Defining function for finding the magnitude value of a given frequency.
def freq_to_mag(freq, freq_list, mag_list):
    nearest_index = 0
    for i in range(len(freq_list)):
        if abs(freq_list[i-1]-freq)<abs(freq_list[nearest_index-1]-freq): 
            nearest_index = i
    freq = freq_list[nearest_index-1]
    mag = mag_list[nearest_index-1]
    return freq, mag
    
   






#Applying the function file_to_lists to the csv files
Network_filter_x, Network_filter_y = file_to_list(Network_filter_path,0,2)
Scope_diode_before_x, Scope_diode_before_y       = file_to_list(Scope_diode_path,0,1)
Scope_diode_after_x, Scope_diode_after_y = file_to_list(Scope_diode_path,0,2)

spectrum_diode_dB_before_x, spectrum_diode_dB_before_y  = file_to_list(spectrum_diode_dB_path,0,1)
spectrum_diode_dB_after_x, spectrum_diode_after_dB_y  = file_to_list(spectrum_diode_dB_path,0,3)

spectrum_output_dB_before_x, spectrum_output_dB_before_y   = file_to_list(spectrum_output_dB_path,0,1)
spectrum_output_dB_after_x, spectrum_output_dB_after_y = file_to_list(spectrum_output_dB_path,0,3)

scope_output_before_x, scope_output_before_y        = file_to_list(scope_output_path,0,1)
scope_output_after_x, scope_output_after_y        = file_to_list(scope_output_path,0,2)



#Creating a folder
folder_path = 'Graphs'
os.makedirs(folder_path, exist_ok=True)



#plotting and saving the graphs


# filter:
desired_ticks = [1000, 2000, 3000, 5000, 7000, 10000]
desired_labels = [f"${int(tick/1000)}$" if tick != 10000 else f"${10}$" for tick in desired_ticks]
plt.semilogx(Network_filter_x, Network_filter_y)
plt.xticks(desired_ticks, desired_labels)
plt.title('Amplitude response - filter')
plt.xlabel('Frequency [kHz]')
plt.ylabel('Magnitude [dB]')
plt.grid()

Network_filter_x_2500, Network_filter_y_2500= freq_to_mag(2500, Network_filter_x, Network_filter_y)
plt.text(Network_filter_x_2500+200, Network_filter_y_2500-1, f'({2.5}, {round(Network_filter_y_2500,3)})', fontsize=12, verticalalignment='bottom')
plt.plot(Network_filter_x_2500, Network_filter_y_2500, marker='o', markersize=7, color='red')
# Network_filter_x_1250, Network_filter_y_1250= freq_to_mag(1250, Network_filter_x, Network_filter_y)
# plt.text(Network_filter_x_1250+100, Network_filter_y_1250-1, f'({1250}, {round(Network_filter_y_1250,3)})', fontsize=12, verticalalignment='bottom')
# plt.plot(Network_filter_x_1250, Network_filter_y_1250, marker='o', markersize=7, color='red')
plt.savefig('Graphs\Amplitude_Response_filter.png')





# #diode:
plt.figure()
plt.plot(np.array(Scope_diode_before_x)*1000, Scope_diode_before_y)
plt.plot(np.array(Scope_diode_after_x)*1000, Scope_diode_after_y)
plt.title('Oscilloscope - diode')
plt.xlabel('Time [ms]')
plt.ylabel('Magnitude [V]')
plt.legend(['Input signal', 'Output signal'])
plt.grid()
plt.savefig('Graphs\Oscilloscope_diode.png')

plt.figure()
plt.plot(np.array(spectrum_diode_dB_before_x)/1000, spectrum_diode_dB_before_y)
plt.plot(np.array(spectrum_diode_dB_after_x)/1000, spectrum_diode_after_dB_y)
plt.title('Frequency spectrum - diode')
plt.xlabel('Frequency [kHz]')
plt.ylabel('Magnitude [dB]')
plt.grid()
plt.legend(['Input signal', 'Output signal'])


plt.savefig('Graphs\Frequency_spectrum_diode.png')


#result:
plt.figure()
plt.plot(np.array(spectrum_output_dB_before_x)/1000, spectrum_output_dB_before_y)
plt.plot(np.array(spectrum_output_dB_after_x)/1000, spectrum_output_dB_after_y)

plt.title('Frequency spectrum - Output')
plt.xlabel('Frequency [kHz]')
plt.ylabel('Magnitude [dB]')
plt.grid()
plt.legend(['$x_1(t)$', '$\\hat{x}_2(t)$'])

spectrum_output_dB_after_x_2500, spectrum_output_dB_after_y_2500= freq_to_mag(2500,spectrum_output_dB_after_x, spectrum_output_dB_after_y)
plt.text(spectrum_output_dB_after_x_2500/1000+.200, spectrum_output_dB_after_y_2500-1, f'({2.5}, {round(spectrum_output_dB_after_y_2500,3)})', fontsize=12, verticalalignment='bottom')
plt.plot(np.array(spectrum_output_dB_after_x_2500)/1000, spectrum_output_dB_after_y_2500, marker='o', markersize=7, color='red')
spectrum_output_dB_after_x_1250, spectrum_output_dB_after_y_1250 = freq_to_mag(1250, spectrum_output_dB_after_x, spectrum_output_dB_after_y)
plt.text(spectrum_output_dB_after_x_1250/1000 + .200, spectrum_output_dB_after_y_1250 - 7, f'({1.25}, {round(spectrum_output_dB_after_y_1250, 3)})', fontsize=12, verticalalignment='bottom')
plt.plot(np.array(spectrum_output_dB_after_x_1250)/1000, spectrum_output_dB_after_y_1250, marker='o', markersize=7, color='red')

plt.savefig('Graphs\Frequency_spectrum_Output.png')

plt.figure()
plt.plot(np.array(scope_output_before_x)*1000, scope_output_before_y)
plt.plot(np.array(scope_output_after_x)*1000, np.array(scope_output_after_y))
plt.title('Oscilloscope - Output')
plt.xlabel('Time [ms]')
plt.ylabel('Magnitude [V]')
plt.grid()
plt.legend(['$x_1(t)$', '$\\hat{x}_2(t)$'], loc='upper right')

plt.savefig('Graphs\Oscilloscope_Output.png')



