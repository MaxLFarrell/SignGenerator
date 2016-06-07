from PIL import Image, ImageFont, ImageDraw
import uuid
import os
def textcalc(text):
    line1 = [(37, 140)]
    line2 = [(37, 160)]
    line3 = [(37, 180)]
    try:
        line1text = text[:26]
    except:
        line1text = text
        line2text = ""
        line3text = ""
    try:
        line2text = text[27:53]
    except:
        line2text = text[27:]
        line3text = ""
    try:
        line3text = text[54:]
    except:
        pass
    line1.append(line1text)
    line2.append(line2text)
    line3.append(line3text)
    return line1, line2, line3
def imbuild(text):
    if len(text) > 79:
        return "TL"
    im = Image.open("static/lennys_sign_blank.jpg").convert("RGBA")

    f = ImageFont.truetype("sign_font_tw_condensed_bold.ttf", 20)
    txt = Image.new("RGBA", (im.size[0], im.size[1]), (255, 255, 255, 0))

    d = ImageDraw.Draw(txt)
    for line in textcalc(text):
        d.text(line[0], line[1], font=f, fill = (0, 0, 0, 255))
    r = txt.rotate(5)
    out = Image.alpha_composite(im, r)
    name = str(uuid.uuid4())
    out.save("ims/" + name + ".jpg")
    return name
if (os.path.isdir("ims") != True):
    os.makedirs("ims")