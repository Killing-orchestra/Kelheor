#!/usr/bin/python
# -*- coding: utf-8 -*-
import Logo
import To
import In
import Help

Logo.main()

def main():
    print("""Do you want to:
1 - Generate an image?
2 - Read message?
3 - Read the FAQ?
""")
    
    try:
        choice = int(input())
    except ValueError:
        print("!!!You must enter a number!!!")
        choice=7
        
    if choice > 3:
        print("!!!Wrong action!!!")
        main()
    else:
        if choice == 1:
            To.main()
        if choice == 2:
            In.main()
        if choice == 3:
            Help.main()
            

if __name__ == '__main__':
	main()
