# EDL-Time-Stamp-Converter
Video editing programs (e.g. Video De Luxe, Video Pro Xxx) from Magix offer the option of outputting HD and FHD as DVD or BD, including chapter markers between which you can jump back and forth during playback. When outputting UHD and UHD2, this option has not yet been available, as no BDs can be created for UHD/2.
So far, as a workaround, I've created UHD/2 files as MP4, imported them into MKVToolNix and created chapter markers there, in certain periods of time, e.g. every 2 minutes. This enables a rough navigation. The output from MKVToolNix produces containers in MKV format (Matroska).

However, the video editing programs mentioned allow EDL editing lists to be generated for the in-house products Sequoia and Samplitude, which contain chapter markers and time information. A cutting list, Edit Decision List (EDL), is the description of an edited version of a film or video. However, MKVToolNix cannot process these lists directly. This program converts the EDL lists from Magix into a form that MKVToolNix can process.

Workflow: Standard chapter markers must be created and exported in the video editing programs, so that the converter can handle them.

![grafik](https://github.com/BraweProg/EDL-Time-Stamp-Converter/assets/125688979/00f9ccbf-0a2e-4c65-935b-7d8c63d666c7)
![grafik](https://github.com/BraweProg/EDL-Time-Stamp-Converter/assets/125688979/3e57bb51-d7cc-48e8-9e82-427992a27637)

Convert the EDL-file. You can then use MKVToolNix to download the MP4 file from your Video editing program and multiplex the video with the converter's EDL file and get a video file with the extension .mkv.

![grafik](https://github.com/BraweProg/EDL-Time-Stamp-Converter/assets/125688979/e88a6464-07fd-443f-b565-822ed9150f4b)

This program, written in Python 3.11, can convert Magix EDL time stamps into Matroska chapter markers, which can be processed by MKVToolNix.
With graphical user interface Tkinter, OS independent, opens a file explorer.

Reads an EDL file, see example below. The EDL file is in ASCII format, plain test. Neglects everything before the line starting with 'Marker List:'.
The next two lines are head lines. The to be processed content begins in the third line below 'Marker List:'
The following time stamps in row 'Play-in' are converted. Rows 'Type-ID', 'CP', 'EM', 'ISRC' are neglected. Takes the name in row 'name' as chapter name.
Rows with 'name' containg 'S', 'P' and 'E' are neglected. The time factor to convert the values in row 'Play-In' into seconds is the audio sampling rate
and is taken from the 3rd line of the EDL file. Default is 48000. The resulting time stamp has the format "hh:mm:ss.sss".
Output is into an ASCII text file (*.txt). Each processed input line results in two output lines, first one with CHAPTERxy='time stamp' and second one with CHAPTERxyNAME='name'.
Processes all lines until EOF or the first empty line is reached.
The input file name has .edl as ending. The output file name is the same as of the EDL file, but endig .txt. The directory is also the same.

Example EDL file:

Samplitude EDL File Format Version 1.7 
Title: "2023 Norwegen.MVD" 
Sample Rate: 48000 
Output Channels: 2 
Software VideoDeLuxe 
Softversion 20.0.3.181

Markerlist:
#Play-In     Type-ID CP EM ISRC           Name
#----------- ------- -- -- -------------- ----
           0     106                      "Kapitel 1"
           0     101                      "S"
      806400     106                      "Kapitel 2"
      806400     116                      "P"
     1478400     106                      "Kapitel 3"
     2150400     106                      "Kapitel 4"
     2822400     106                      "Kapitel 5"
     3494400     106                      "Kapitel 6"

Example converted EDL file:

CHAPTER01=00:00:00.000
CHAPTER01NAME=1
CHAPTER02=00:00:16.000
CHAPTER02NAME=2
CHAPTER03=00:00:30.000
CHAPTER03NAME=3
CHAPTER04=00:00:44.000
CHAPTER04NAME=4
CHAPTER05=00:00:58.000
CHAPTER05NAME=5
CHAPTER06=00:01:12.000
CHAPTER06NAME=6
