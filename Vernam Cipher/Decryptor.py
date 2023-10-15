import numpy as np
key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789~`!@#$%^&*()-_+=[]{}|;:' ,./<>?\"\\\n\t"
dec_string = ""
ls1 = []
ls2 = []

print("To input encrypted text from readymade text press 1 or press 2 to type it to input it.")
decision = input()

if decision=='1':
	print("Enter the directory of the encrypted text.")
	directory = input()
	file = open(directory, "r")
	enc_string = file.read()
elif decision=='2':
	print("Please enter the text which you wanted to decrypt it:")
	enc_string = input()

print("Press 1 to input key from ready made or 2 to type.")
decision = input()

if decision=='1':
	print("Enter the directory of the key.")
	directory1 = input()
	file1 = open(directory1, "r")
	inp_key = file1.read()
elif decision=='2':
	print("Please enter the key generated from Vernam Ciphering mechanism:")
	inp_key = input()

print("Verifying the key...")
if len(inp_key)!=len(enc_string):
	print("The given key is incompatible as it's size is either larger or smaller than encrypted text. \nTerminating the encryption process.")
	exit()
else:
	print("The key is verified. \nProceeding the encryption process...")

for i in range(len(enc_string)):
	ls1.append(key.find(enc_string[i]))
	ls2.append(key.find(inp_key[i]))

C = np.array(ls1)
K = np.array(ls2)
P = (C - K)%len(key)

for i in range(len(P)):
	dec_string += key[P[i]]

print("The decrypted string is:\n", dec_string)
