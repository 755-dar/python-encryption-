import string

chars_list = list(string.ascii_letters)

def decreyption(code_str, divide=1):
	"""Decode a '*'-separated numeric string into text.

	Args:
		code_str (str): numbers separated by '*', e.g. '0*26*52'
		divide (int|str): value to divide each number by (default 1)

	Returns:
		str: decoded message
	"""
	if not code_str:
		return ""
	takeoutstars = [int(x) for x in code_str.split("*") if x != '']
	div = int(divide)
	decoded = []
	for n in takeoutstars:
		idx = int(n / div)
		if 0 <= idx < len(chars_list):
			decoded.append(chars_list[idx])
		else:
			if idx == 26:
				decoded.append(' ')
			else:
				decoded.append('?')
	return ''.join(decoded)

def encrypt_message(message: str, encryptFactor: str) -> str:
	encryotedNumbers = []
	for x in message:
		indexs = chars_list.index(x)
		print(str(indexs))
		encryotedNumbers.append(str(indexs * int(encryptFactor)))
	#print("Encrypted numbers:", "".join(encryotedNumbers))
	print(encryotedNumbers)
	return "*".join(encryotedNumbers)

if __name__ == '__main__':
	code = input("what do you want to decrpt? :")
	divide = input("what do you want to divide the decrpted numbers with? :")
	print("Decoded message:", decreyption(code, divide))







