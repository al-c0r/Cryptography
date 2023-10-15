import numpy as np
key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789~`!@#$%^&*()-_+=[]{}|;:' ,./<>?\"\\\n\t"
enc_string = ""
ls1 = []
ls2 = []

print("Would you like to encrypt a readymade text file (then press '1') or are you going to create new file (then press '2')? \nElse close this program by pressing any key other than the above mentioned.")
decision = input()

if decision=='1':
	print("Please choose readymade file by entering it's file directory.")
	directory = input()
	file = open(directory, "r")
	inp_string = file.read()

elif decision=='2':
	print("Please enter the text to be encrypted: ")
	inp_string = input()

else:
	print("Please type either 1, 2 or 3 to proceed.\nShutting down the program.")
	exit()

print("To have good implementation, enter the key of the size near to plaintext but less plaintext. \nPlease enter the key: ")
inp_key = input()
i = 0

if len(inp_key)>len(inp_string):
	print("Entered long key. \nStopping the encryption process.")
	exit()
else: 
	pass

while(len(inp_key)!=len(inp_string)):
	inp_key = inp_key + inp_string[i]
	i = i+1

for i in range(len(inp_string)):
	ls1.append(key.find(inp_string[i]))
	ls2.append(key.find(inp_key[i]))

P = np.array(ls1)
K = np.array(ls2)
C = (P + K)%len(key)

for i in range(len(C)):
	enc_string += key[C[i]]

print("The encrypted text is:\n", enc_string)

file1 = open("Key", "w")
file1.write("\nArrangement of characters = ")
file1.write(key)
file1.write("\nKey entered = ")
file1.write(inp_key)
file1.write("\nKey vector: ")
for i in range(len(K)):
	file1.write(str(K[i]))
	file1.write("\t")
file1.close()

file2 = open("Encrypted Text", "w")
file2.write("\nThe encrypted text is = ")
file2.write(enc_string)
file2.close()
