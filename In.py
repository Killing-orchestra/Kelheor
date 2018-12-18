#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import ASCII
from siphr import Siphr
import binascii

siphr = Siphr()

def get_tally() -> None:

	def get_image() -> Image:
		name = input("Enter the file name:")
		#name="Pic.png"

		try:
			im = Image.open(name)
		except Exception:
			print("Fail!")
			exit(0)

		return im


	image = get_image()
	width, height = image.size


	#print("Все ок!")
	image = image.convert('1')

	byteset = ""
	swidth=width-1
	for x in range(swidth,-1,-1):
		for y in range(0,height):
			byte = str(image.getpixel((x,y)))
			if byte == "255":
				byteset += '1'
			else:
				byteset += '0'

	k = int(byteset,2)
	return(k)
	


def main():
	num=get_tally()
	
	print("Was the message encrypted? If it was, enter the password.")
	password = input()
	if password=="":
		crypto=False
		message=ASCII.int2message(num, crypto)
	else:
		try:
			crypto=True
			code=ASCII.int2message(num, crypto)
			code=binascii.unhexlify(code)
			password = bytearray(password,"utf8")
			message = siphr.decrypt(password, code)
			message=str(message, "utf8")
		except UnicodeDecodeError:
			print("Wrong password.")
	print(message)


if __name__ == '__main__':
	main()
