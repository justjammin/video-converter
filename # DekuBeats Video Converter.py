# DekuBeats Video Converter
from Youtube_DL import * 
# Python code to convert video to audio 
import moviepy.editor as mp 
import random
# Insert Local Video File Path  
clip = mp.VideoFileClip(location)
filename = yt.title+".mp3"
# Insert Local Audio File Path 
audio_file = clip.audio.write_audiofile(filename)
print(audio_file)
