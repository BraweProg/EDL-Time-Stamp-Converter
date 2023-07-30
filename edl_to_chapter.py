######################################################################################################
##  EDL-Converter for Matroska MKV                                                                  ##
##--------------------------------------------------------------------------------------------------##
##  Reads EDL-file created for Magix Sequoia/Samplitude by MAGIX Video Pro X14, jumps to the        ##
##  chapter markers. The subsequent timestamps are converted. The time divisor is identical to the  ##
##  audio sampling rate and is derived from 3rd line in the EDL-file. The chapter names are read.   ##
##  Default in Magix are names "Chapter" + chapter number. Output is in a text file (*.txt).        ##
##  The file name is the same as that of the EDL file. The directory is also the same.              ##
##  Content example:                                                                                ##
##                                                                                                  ##
##  CHAPTER01=00:23:20.000                                                                          ##
##  CHAPTER01NAME=1                                                                                 ##
##  CHAPTER02=00:40:30.000                                                                          ##
##  CHAPTER02NAME=2                                                                                 ##
##  CHAPTER03=00:00:40.560                                                                          ##
##  CHAPTER03NAME=3                                                                                 ##
##  CHAPTER04=01:04:44.000                                                                          ##
##  CHAPTER04NAME=4                                                                                 ##
##  CHAPTER05=01:24:45.000                                                                          ##
##  CHAPTER05NAME=5                                                                                 ##
##  CHAPTER06=01:27:45.000                                                                          ##
##  CHAPTER06NAME=6                                                                                 ##
##--------------------------------------------------------------------------------------------------##
##  Version:    1.0                                                                                 ##
##  30.07.2023  BraweProg                                                                           ##
######################################################################################################
import os
import time
import tkinter as tk
from tkinter import filedialog

def parse_edl(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()

    # Extract the sample rate from the third line
    sample_rate = int(content[2].split(":")[1].strip())
    print("Sample Rate", sample_rate)
    time.sleep(2) # Delay for showing sample rate

    # Find the start of the markers list
    start_line = content.index('Markerlist:\n') + 3

    markers = []
    for line in content[start_line:]:
        # End on the first empty line or EOF
        if line.strip() == '':
            break

        parts = line.split()
        # Now uses the extracted sample_rate for conversion
        time_stamp = int(parts[0]) // sample_rate 

        # Neglect lines with certain names
        name = parts[-1].strip('"')
        if any(x in name for x in ['S', 'P', 'E']):
            continue

        markers.append((time_stamp, name))

    # Return the list of markers (time stamp, name)
    return markers

def convert_edl_to_chapters(file_path):
    if file_path:
        # Parse the EDL file
        markers = parse_edl(file_path)

        # Create the output file path
        output_file_path = os.path.splitext(file_path)[0] + ".txt"

        # Write the output file
        with open(output_file_path, "w") as f:
            for i, (time, name) in enumerate(markers, start=1):
                hours = int(time // 3600)
                minutes = int((time % 3600) // 60)
                seconds = time % 60
                f.write(f"CHAPTER{i:02}={hours:02}:{minutes:02}:{seconds:06.3f}\n")
                f.write(f"CHAPTER{i:02}NAME={name}\n")

        # Show a success message
        print("EDL conversion completed successfully! Output file: %s" % output_file_path)
        print("Press Enter to continue!")
        input()

    else:
        print("Conversion cancelled.")
        print("Press Enter to continue!")
        input()

# Create the tkinter root window
root = tk.Tk()
root.withdraw() 

# Ask the user to select an EDL file
file_path = filedialog.askopenfilename(filetypes=[("EDL files", "*.edl")])

# Convert the EDL file to chapters
convert_edl_to_chapters(file_path)
