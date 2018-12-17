#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

def welcome() -> None:
                print()


def get_tally() -> None:

	def get_image() -> Image:
		name = input("Введите имя изображения:")
		try:
			im = Image.open(name)
		except Exception:
			print("Неудача!")
			exit(0)

		return im


	image = get_image()
	width, height = image.size


	print("Все ок!")
	image = image.convert('1')
	image.save('result.png')

	byteset = ""
	for x in range(105,-1,-1):
		for y in range(0,17):
			byte = str(image.getpixel((x,y)))
			if byte == "255":
				byteset += '1'
			else:
				byteset += '0'

	k = int(byteset,2)*17 ##

	print("Все готово:")
	print(k)
	


def main():
    get_tally()


if __name__ == '__main__':
	main()
