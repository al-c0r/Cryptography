key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789~`!@#$%^&*()-_+=[]{}|;:' ,./<>?\"\\\n\t"
print("The length of key string is", len(key))
print("Please enter no. by which you want to shift the characters: ")
n = int(input())
print("Please enter the plain text that you want to encrypt: ")
inp_string=input()
enc_string=""
for i in range(len(inp_string)):
	char = inp_string[i]
	char_location = key.find(char)
	new_location = (char_location + n)%len(key)
	enc_string += key[new_location]
print("The encrypted string is ", enc_string)
