import numpy as np
key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789~`!@#$%^&*()-_+=[]{}|;:' ,./<>?\"\\\n\t"

key_inp = ""
K = np.array([[0,2,3],[4,5,6],[7,8,9]])
print("Note that the key is something based on which one uses to encrypt texts using this program.\nPlease enter the key (Enter any character using keyboard of exactly 9 letters to build a key): ")
key_inp = input()
ls4 = []
ls5 = []
if len(key_inp)!=9:
	print("The key is not the 9 letter long so, going with default keys...")
else:
	print("Size of key is verified to be correct length...\nVerifying it's compatibility...")
	for i in range(0, 9, 3):
		for j in range(3):
			char_location = key.find(key_inp[i+j])
			ls4.append(char_location)
		ls5.append(ls4)
		ls4 = []
	X = np.array(ls5)
	if round(np.linalg.det(X),3)==0:
		print("The given key is incompatible because Determinant of the matrix formed by it is Zero.\nWhich we can't be able to decrypt it once we encrypt. So, going with the default keys.")
	else:
		print("The given key is compatible with this mode of encryption.\nRegistering the new key entered.....")
		K = X
file = open("Key.txt", 'w')
file.write("Below is the summary of the encryption that you've used to encrypt which consist of all details including keys which should be kept private between you and sender/receiver.")
file.write("\nkeychar = ")
file.write(key)
file.write("\nkeycode = ")
file.write(key_inp)
file.close()

print("Please enter the plain text to be encrypted: ")
inp_string = input()
ls = []
ls1 = []
ls2 = []
ls3 = []
dummy=""
enc_string = ""
z=0
if len(inp_string)%3==1:
	inp_string = inp_string + "  "
elif len(inp_string)%3==2:
	inp_string = inp_string + " "
else: pass

for i in range(0,len(inp_string),3):
	for j in range(3):
		dummy += inp_string[i+j]
	ls1.append(dummy)
	dummy = ""

for i in range(len(ls1)):
	for j in range(3):
		char_location = key.find(ls1[i][j])
		ls.append(char_location)

for i in range(0,len(ls),3):
	for j in range(3):
		z = ls[i+j]
		ls2.append(z)
	ls3.append(ls2)
	ls2 = []
P = np.array(ls3)
C=[]
for i in range(len(P)):
	c = P[i].dot(K)%len(key)
	C.append(c)
C = np.array(C)
for i in range(len(C)):
	for j in range(3):
		enc_string += key[C[i][j]]
print("The encrypted string is:\n", enc_string)
