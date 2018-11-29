#use pip install matplotlib if you do not have the library
#use pip install seaborn if you do not have the library

import matplotlib.pyplot as plt
from pylab import frombuffer
import wave
import seaborn as sns

#open wav file in read mode, r
with wave.open('couchplayin.wav','r') as wave_read:
    #getnframes() returns the number of frames in the wav file
    #readframes() returns the data to read in bytes
    wave_frames = wave_read.readframes(wave_read.getnframes())
    #frombuffer changes bytes to integer for plotting
    wave_frames = frombuffer(wave_frames, int)
    #sns.set_style gives a dark background. it is a seaborn function
    sns.set_style('darkgrid')
    #and then plot
    plt.plot(wave_frames, color = 'blue')
    #show() displays the graph
    plt.show()

#Brought to you by Scriptkidd. Follow me on Instagram @a_scriptkidd for more cool tutorials. My GitHub is Scriptkidd98 Editor is JetBrains PyCharm
