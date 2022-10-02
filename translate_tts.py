from googletrans import Translator
from gtts import gTTS
import os
import playsound

translator = Translator()

# depending on where the yolov5 otuput is saved


# for objects
def read_position(name, x_coord, y_coord, lang):
    x_pos = ""
    y_pos = ""
    if x_coord < 0.3:
        x_pos = "left"
    if 0.3 <= x_coord < 0.6:
        x_pos = "middle"
    if x_coord >= 0.6:
        x_pos = "right"

    if y_coord < 0.5:
        y_pos = "top"
    if y_coord == 0.5:
        y_pos = "middle"
    if y_coord > 0.5:
        y_pos = "bottom"

    sentence = "There is a " + (name if 'None' not in name else 'Person') + " on the " + y_pos + " " + x_pos
    tts(sentence, 0, lang)


def tts(contents, p, lang='en'):
    if not contents:
        return None
    
    if lang == "en":
        en = gTTS(text=contents, lang="en", slow=False)
        en.save(f"en{p}.mp3")
        playsound.playsound(f"en{p}.mp3")
        os.remove(f"en{p}.mp3")
    elif lang == "ch":
        results_chinese = translator.translate(contents, dest="zh-cn")
        ch = gTTS(text=results_chinese.text, lang="zh-CN", slow=False)
        ch.save("ch.mp3")
        playsound.playsound("ch.mp3")
        os.remove("ch.mp3")
    elif lang == "m":
        results_malay = translator.translate(contents, dest="ms")
        m = gTTS(text=results_malay.text, lang="ms", slow=False)
        m.save("m.mp3")
        playsound.playsound("m.mp3")
        os.remove("m.mp3")
    elif lang == "t":
        results_tamil = translator.translate(contents, dest="ta")
        t = gTTS(text=results_tamil.text, lang="ta", slow=False)
        t.save("t.mp3")
        playsound.playsound("t.mp3")
        os.remove("t.mp3")



def main(lang):
    while True:
        f = open('yolov5/runs/detect/file.txt', 'r')
        lines = f.read()

        for number,line in enumerate(lines.split('\n')):
            # line = f.readline()
            object= line.strip().split("  ")
            if len(object) > 1:
            ##print(object)
                n= object[0].split()
                if len(n)==2:
                    name = n[0]
                if len(n)>2:
                    name = n[0] +" "+ n[1]
                x = float(object[1])
                y=float(object[2]) 
                width=object[3]
                height= object[4]
                read_position(name,x,y, lang)

            


##tts(contents)

if __name__ == "__main__":
    lang = input("Enter the language (en, ch, m, t): ")
    main(lang=lang)

