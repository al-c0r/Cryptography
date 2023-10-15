key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789~`!@#$%^&*()-_+=[]{}|;:' ,./<>?\"\\\n\t"
print("The length of string of key is ", len(key))
print("Please enter the encrypted string which is to be decrypted: ")
enc_string = input()
dec_string = ""
n = 1
while(n<len(key)):
	for i in range(len(enc_string)):
		char = enc_string[i]
		char_location = key.find(char)
		new_location = (char_location - n)%len(key)
		dec_string += key[new_location]
	print("The decrypted string by", n, "back-shifting is", dec_string, ".\n")
	dec_string = ""
	n = n+1
