# EDL-Time-Stamp-Converter
Video editing programs (e.g. Video De Luxe, Video Pro Xxx) from Magix offer the option of outputting HD and FHD as DVD or BD, including chapter markers between which you can jump back and forth during playback. When outputting UHD and UHD2, this option has not yet been available, as no BDs can be created for UHD/2.
So far, as a workaround, I've created UHD/2 files as MP4, imported them into MKVToolNix and created chapter markers there, in certain periods of time, e.g. every 2 minutes. This enables a rough navigation. The output from MKVToolNix produces containers in MKV format (Matroska).

However, the video editing programs mentioned allow EDL editing lists to be generated for the in-house products Sequoia and Samplitude, which contain chapter markers and time information. A cutting list, Edit Decision List (EDL), is the description of an edited version of a film or video. However, MKVToolNix cannot process these lists directly. This program converts the EDL lists from Magix into a form that MKVToolNix can process.

Workflow: Standard chapter markers must be created and exported in the video editing programs, so that the converter can handle them.
![grafik](https://github.com/BraweProg/EDL-Time-Stamp-Converter/assets/125688979/00f9ccbf-0a2e-4c65-935b-7d8c63d666c7)
![grafik](https://github.com/BraweProg/EDL-Time-Stamp-Converter/assets/125688979/3e57bb51-d7cc-48e8-9e82-427992a27637)
Convert the EDL-file. You can then use MKVToolNix to download the MP4 file from your Video editing program and multiplex the video with the converter's EDL file and get a video file with the extension .mkv.

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
Title: "2021 Schweiz.MVD" 
Sample Rate: 48000 
Output Channels: 2 
Software VideoDeLuxe 
Softversion 20.0.3.176 

Source Table Entries: 319 
   1 "E:\Bilder\2021_Schweiz\P1030989.JPG" VIDEO
   2 "E:\Bilder\2021_Schweiz\P1010270.MP4" VIDEO
   3 "E:\Bilder\2021_Schweiz\P1010271.JPG" VIDEO
   4 "E:\Bilder\2021_Schweiz\P1010272.MP4" VIDEO
   5 "E:\Bilder\2021_Schweiz\P1010273.MP4" VIDEO
   6 "E:\Bilder\2021_Schweiz\P1010275.MP4" VIDEO
   7 "E:\Bilder\2021_Schweiz\P1010276.JPG" VIDEO

Track 6: "Spur:" Solo: 0 Mute: 0 
#Source Track Play-In     Play-Out    Record-In   Record-Out  Vol(dB)  MT LK FadeIn       %     CurveType                          FadeOut      %     CurveType                          Name
#------ ----- ----------- ----------- ----------- ----------- -------- -- -- ------------ ----- ---------------------------------- ------------ ----- ---------------------------------- -----

Track 7: "Spur:" Solo: 0 Mute: 0 
#Source Track Play-In     Play-Out    Record-In   Record-Out  Vol(dB)  MT LK FadeIn       %     CurveType                          FadeOut      %     CurveType                          Name
#------ ----- ----------- ----------- ----------- ----------- -------- -- -- ------------ ----- ---------------------------------- ------------ ----- ---------------------------------- -----
     34     7    26378880    26954880       72000      648000     0.00  0  0        48000     0 "*default"                                48000     0 "*default"                         "DSC_0941.JPG"
    291     7    80657280    81233280       72000      648000     0.00  0  0        48000     0 "*default"                                48000     0 "*default"                         "IMG20210925143514.jpg"
    290     7    81185280    81761280       72000      648000     0.00  0  0        48000     0 "*default"                                48000     0 "*default"                         "IMG20210925143522.jpg"
    294     7    81713280    82289280       72000      648000     0.00  0  0        48000     0 "*default"                                48000     0 "*default"                         "0-02-05-377c57867f9461ac49eff9cc94054ff3977cc1f3fc38d786f561b72dc83afcdf_78b9fcc0f56670c0.jpg"
    292     7    84353280    84929280       72000      648000     0.00  0  0        48000     0 "*default"                                48000     0 "*default"                         "IMG20210925160357.jpg"

Pan for Track 6:
#Play-In      Pan(0...2)
#----------- ---------
           0   1.00000

Volume for Track 7:
#Play-In       Vol(dB)
#----------- ---------
           0    -0.000

Pan for Track 7:
#Play-In      Pan(0...2)
#----------- ---------
           0   1.00000

Volume for Track 8:
#Play-In       Vol(dB)
#----------- ---------
           0    -0.000

Pan for Track 8:
#Play-In      Pan(0...2)
#----------- ---------
           0   1.00000


Markerlist:
#Play-In     Type-ID CP EM ISRC           Name
#----------- ------- -- -- -------------- ----
           0     106                      "Chapter 1"
           0     101                      "S"
      364800     106                      "Chapter 2"
      892800     106                      "Chapter 3"
     1305600     106                      "Chapter 4"
     1833600     106                      "Chapter 5"
     2615040     106                      "Chapter 6"
   209011788     102                      "E"

Example chapter marker file as output of the above input file:
CHAPTER01=00:00:00.000
CHAPTER01NAME=Chapter 1
CHAPTER02=00:01:16.000
CHAPTER02NAME=Chapter 2
CHAPTER03=00:03:06.000
CHAPTER03NAME=Chapter 3
CHAPTER04=00:04:32.000
CHAPTER04NAME=Chapter 4
CHAPTER05=00:06:22.000
CHAPTER05NAME=Chapter 5
CHAPTER06=00:09:04.800
CHAPTER06NAME=Chapter 6
