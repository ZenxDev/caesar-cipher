import os,sys

def encrypt(text):
	result = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + 23-65) % 26 + 65)
		else:
			result += chr((ord(char) + 23-97) % 26 + 97)
	return result

def decrypt(text):
	result = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + (-23)-65) % 26 + 65)
		else :
			result += chr((ord(char) + (-23)-97) % 26 + 97)
	return result

try :
	import pyfiglet
except ImportError :
	os.system("pkg update && pkg upgrade && pip install pyfiglet")

#Interface
def banner():
	os.system("clear")
	print ("")
	print ("""	 \033[31m____          ____
        |  _ \ _   _  |  _ \ _   _                  | |_) | | | | | |_) | | | |
        |  __/| |_| |_|  __/| |_| |                 |_|    \__, (_)_|    \__, |
               |___/         |___/""")
	print ("          \033[30mCaesar Cipher Example\n	    Coded By \033[1;32mZenxDev\033[30m")

def menu():
	print ("")
	print ("[ 1 ] Encrypt")
	print ("[ 2 ] Decrypt")
	print ("[ x ] Exit")

def inEncrypt():
	print ("")
	fail = input("Text : ")
	result = encrypt(fail)
	print ("Done Encrypted!\n" + "Result : " + result)
	
def inDecrypt():
	print ("")
	fail = input("Text : ")
	result = decrypt(fail)
	print ("Done Decrypted!\n" + "Result : " + result)

if __name__ == "__main__":
	banner()
	menu()
	choose = input("@file\py.py >> ")
	if choose == "1":
		inEncrypt()
	elif choose == "2":
		inDecrypt()
	elif choose == "x" or choose == "X":
		os.system("clear")
		sys.exit()