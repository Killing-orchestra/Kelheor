#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import time

_SIZE_WIDTH = 666 # Ширина результирующего изображения по умолчанию
_SIZE_HEIGHT = 999 # Высота результирующего изображения по умолчанию

_SIZE_SPACE=_SIZE_WIDTH*_SIZE_HEIGHT # Площадь результирующего изображения по умолчанию 1802


def get_image(k) -> None:

	def from_k_to_bin(k: int) -> list:
		
		binary = bin(k)[2:]

		if len(binary) < _SIZE_SPACE:
			new_binary = ""
			for i in range(_SIZE_SPACE-len(binary)):
				new_binary += "0"
			binary = new_binary + binary

		lists = [[] for x in range(_SIZE_HEIGHT)]
		for x in range(_SIZE_SPACE):
			lists[x%_SIZE_HEIGHT].append(binary[x])

		lists.reverse()
		return lists

	lists = from_k_to_bin(k)

	image = Image.new("1", (_SIZE_WIDTH,_SIZE_HEIGHT), (0))
	draw = image.load()
	for y in range(_SIZE_HEIGHT):
		for x in range(_SIZE_WIDTH):
			image.putpixel(xy = ((_SIZE_WIDTH-1)-x,(_SIZE_HEIGHT-1)-y), value = (int(lists[y][x]),))
	#image.save(str(k)+".png")
	now = time.time()
	image.save("Pic"+str(now)+".png")

def main():

        #k = 0
        k=int(input("Введите k:"))
        get_image(k)
        #while k >= 0:
                #get_image(k)
                #k=k
                #print(k)

if __name__ == '__main__':
	main()
