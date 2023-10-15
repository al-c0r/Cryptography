import numpy as np
key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789~`!@#$%^&*()-_+=[]{}|;:' ,./<>?\"\\\n\t"
ls1 = []
ls2 = []
K = np.array([[0,2,3],[4,5,6],[7,8,9]])
dec_string = ""

print("Note that the key is something based on which one uses to encrypt texts using this program.\nPlease enter the key (Enter any character using keyboard of exactly 9 letters to build a key: ")
key_inp = input()
ls3 = []
ls4 = []
if len(key_inp)!=9:
        print("The key is not the 9 letter long so, going with default keys...")
else:
        print("Size of key is verified to be correct length...\nVerifying it's compatibility with the algorithm....")
        for i in range(0, 9, 3):
                for j in range(3):
                        char_location = key.find(key_inp[i+j])
                        ls3.append(char_location)
                ls4.append(ls3)
                ls3 = []
        X = np.array(ls4)
        if round(np.linalg.det(X),3)==0:
                print("The given key is incompatible because Determinant of the matrix formed by the keys are found to be Zero which can't be decrypted. So, going by the default keys.")
        else:
                print("The given key is compatible with this mode of encryption so, modifying the keys....")
                K = X

def mod(x):
	for i in range(len(key)):
		if (x*1/x)%len(key)==(i*x)%len(key):
			return i
			break
		else: pass

def adj(A):
	C = [[i for i in range(3)] for j in range(3)]
	for i in range(3):
		for j in range(3):
			x = np.delete(A,[i],0)
			y = np.delete(x,[j],1)
			C[j][i]=round(((-1)**(i+j))*np.linalg.det(y), 3)
	return C

InvK = mod(round(np.linalg.det(K),3))*np.array(adj(K))
print("Please enter the encrypted Cipher-text to be decrypted: ")
enc_string = input()

for i in range(0, len(enc_string), 3):
	for j in range(3):
		char_location = key.find(enc_string[i+j])
		ls1.append(char_location)
	ls2.append(ls1)
	ls1 = []
C = np.array(ls2)
P = []

for i in range(len(C)):
	P.append(C[i].dot(InvK))

P = np.array(P)%len(key)

for i in range(len(P)):
	for j in range(3):
		new_char = int(P[i][j])
		dec_string += key[new_char]

print("The decrypted string is:\n", dec_string)
