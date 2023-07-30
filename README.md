# EDL-Time-Stamp-Converter
A program in Python 3.11, for converting EDL time stamps into Matroska chapter markers, which can be processed by MKVToolNix.
With graphical user interface Tkinter, OS Windows 10/11, file explorer.

Reads an EDL file, see example below. The EDL file is in ASCII format, plain test. Neglects everything before the line starting with 'Marker List:'.
The next two lines are head lines. The to be processed content begins in the third line below 'Marker List:'
The following time stamps in row 'Play-in' are converted. Rows 'Type-ID', 'CP', 'EM', 'ISRC' are neglected. Takes the name in row 'name' as chapter name.
Rows with 'name' containg 'S', 'P' and 'E' are neglected. The time factor to convert the values in row 'Play-In' into seconds is the audio sampling rate
and is taken from the 3rd line of the EDL file. Default is 48000. The resulting time stamp has the format "hh:mm:ss.sss".
Output is into an ASCII text file (*.txt). Each processed input line results in two output lines, first one with CHAPTERxy='time stamp' and second one with CHAPTERxyNAME='name'.
Process all lines until you reach EOF or the first empty line.
The input file name has .edl as ending. The output file name is the same as of the EDL file, but endig .txt. The directory is also the same.

Example EDL file (between <>):
<
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
>
Example chapter marker file as output of the above input file (between <>):
<
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
>
