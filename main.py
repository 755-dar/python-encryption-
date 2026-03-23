import sys
import string
from deycript import decreyption, encrypt_message

chars = string.ascii_letters
chars_list = list(chars)


def input_to_char_list(s: str, only_letters: bool = False) -> list:
	"""Convert a string `s` into a list of characters.

	- If `only_letters` is True, only alphabetic characters are kept.
	- Otherwise every character (including spaces/punctuation) is returned.
	"""
	if only_letters:
		return [c for c in s if c.isalpha()]
	return list(s)



def main():
	q = input("do you want to encrypt or decrypt? (e/d) :")
	if q == "d":
		
		code =  input ("what do you want to decrpt? :")
		divide = input("what do you want to divide the decrpted numbers with? :")
		print("Decoded message:", decreyption(code, divide))
		
	else:# Accept a sample string from argv if provided, else prompt the user.
		if len(sys.argv) > 1:
			text = " ".join(sys.argv[1:])
		else:
			text = input("Type a message: ")
			all_chars = input_to_char_list(text)
			encryptFactor = input("what do you want to multiply the encrypted numbers with? :")
			encrypted = encrypt_message(all_chars,encryptFactor)
			#print("number to charcter", chars_list(90/encryptFactor))
			print("Encrypted message:", encrypted)
		

	
	
	
	



if __name__ == "__main__":
	main()
	




