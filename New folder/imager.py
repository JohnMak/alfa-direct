import Image

f = open('test.csv', 'r')

lines = f.readlines()

img = Image.new("RGB", (200,201))

def getColor(color):
    if color < 64:
        color = ( color ) * 4
        return (0,color,255)
    elif color < 128:
        color = ( color - 64 ) * 4
        return (0,255,255-color)
    elif color < 192:
        color = ( color - 128 ) * 4
        return (color,255,0)
    else:
        color = ( color - 192 ) * 4
        return (255,255-color,0)

for line in lines:
    ar = line.split(',')
    color = int(128+638*4*float(ar[2]))
    img.putpixel((int(ar[0]),int(ar[1])), getColor(color))
img.save('test.jpeg', "JPEG")