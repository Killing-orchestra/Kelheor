from PIL import Image
im = Image.open("bd.jpg")

width = im.size[0]
height = im.size[1]
k = ''

def color( c ):
  sum = c[0] + c[1] + c[2]
  if ( sum < 383 ):
    return 1
  else:
    return 0

for x in range(0, width):
  for y in reversed(range(0, height)):
    k += str( color( im.getpixel( (x,y) ) ))

#k = int(k, base = 2) * height
print("k=",k)
