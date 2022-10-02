from googletrans import Translator
from gtts import gTTS
import os
import playsound
import time

translator = Translator()

# depending on where the yolov5 otuput is saved


# for objects
def read_position(name,x_coord,y_coord):
    x_pos=""
    y_pos=""
    if x_coord<0.5:
        x_pos= "left"
    if x_coord==0.5:
        x_pos= "middle"
    if x_coord>0.5:
        x_pos = "right"

    if y_coord<0.5:
        y_pos = "bottom"
    if y_coord==0.5:
        y_pos="middle"
    if y_coord>0.5:
        y_pos="top"
    
    sentence= "There is a " + name + " on the " + y_pos + " " + x_pos
    tts(sentence)
    time.sleep(5)
    


def tts(contents):
    results_chinese = translator.translate(contents, dest='zh-cn')
    results_malay = translator.translate(contents, dest='ms')
    results_tamil = translator.translate(contents, dest='ta')

    en = gTTS(text=contents, lang='en', slow=False)
    ch = gTTS(text=results_chinese.text, lang='zh-CN', slow=False)
    m = gTTS(text=results_malay.text, lang='ms', slow=False)
    t = gTTS(text=results_malay.text, lang='ta', slow=False)

  
    en.save("en.mp3")
    ch.save("ch.mp3")
    m.save("m.mp3")
    t.save("t.mp3")

    playsound.playsound("en.mp3")
    playsound.playsound("ch.mp3")
    playsound.playsound("m.mp3")
    playsound.playsound("t.mp3")

    os.remove("en.mp3")
    os.remove("ch.mp3")
    os.remove("m.mp3")
    os.remove("t.mp3")

##tts(contents)


# f = open('output_file.txt', 'r')
# lines = f.readlines()

# for number,line in enumerate(lines):
#     # line = f.readline()
#     object= line.strip().split("  ")
#     ##print(object)
#     n= object[0].split()
#     if len(n)==2:
#         name = n[0]
#     if len(n)>2:
#         name = n[0] +" "+ n[1]
#     x = float(object[1])
#     y=float(object[2]) 
#     width=object[3]
#     height= object[4]
#     read_position(name,x,y)
