#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import time
from siphr import Siphr
import binascii
import ASCII

siphr = Siphr()

def validate(_SIZE_WIDTH,_SIZE_HEIGHT,_SIZE_SCALE,k):
	flag=True

	while flag:
		_SIZE_SPACE=_SIZE_WIDTH*_SIZE_HEIGHT
		ks=("1"*_SIZE_SPACE)
		kb=int(ks,2)
		if k<=kb:
			flag=False
		else:
			_SIZE_WIDTH += _SIZE_SCALE
			_SIZE_HEIGHT += _SIZE_SCALE
			
		return (_SIZE_WIDTH,_SIZE_HEIGHT)

def get_image(k: int) -> None:
	_SIZE_WIDTH = 106 # Ширина результирующего изображения по умолчанию
	_SIZE_HEIGHT = 17 # Высота результирующего изображения по умолчанию

	#_SIZE_SPACE=_SIZE_WIDTH*_SIZE_HEIGHT # Площадь результирующего изображения по умолчанию 1802
	_SIZE_SCALE=10

	_SIZE_WIDTH,_SIZE_HEIGHT=validate(_SIZE_WIDTH,_SIZE_HEIGHT,_SIZE_SCALE,k)
	_SIZE_SPACE=_SIZE_WIDTH*_SIZE_HEIGHT

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

	now = time.time()
	image.save("Pic"+str(now)+".png")
	#image.save("Pic.png")
	print("Image save as Pic"+str(now)+".png")


def main():
	message=str(input("Enter message:"))
	print("If you want to encrypt the message enter the password. Otherwise, just press the Enter")
	password = input()
	if password=="":
		crypto=False
		k=ASCII.str2int(message, crypto)
	else:
		message=bytearray(message,"utf8")
		crypto=True
		password = bytearray(password,"utf8")
		code = siphr.encrypt(password, message)
		message=str(binascii.hexlify(code)).replace("b'","").replace("'","")
		k=ASCII.str2int(message, crypto)
	get_image(k)


if __name__ == '__main__':
	main()
