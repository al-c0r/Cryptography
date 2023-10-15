char="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789~`!@#$%^&*()-_+=[]{}|;:' ,./<>?" + "\"\\\n" #Total 95 characters
print("The length of key string is ", len(char))
print("Please enter number of character(s) by which you need to be shifted: ")
m=int(input())
n=m%96
print("Please enter input string:")
input_string=input()
output_string=""
#For Encryption algorithm
for i in range(len(input_string)):
	character=input_string[i]
	location_of_char = char.find(character) #Indexing step
	if location_of_char>95-n:
		new_char = location_of_char + n - 96 #Find&Replace
	else:
		new_char = location_of_char + n
	output_string += char[new_char]
print("The encrypted text is ", output_string)
decrypt_string=""
#For Decryption algorithm
for i in range(len(output_string)):
	character= output_string[i]
	char_location = char.find(character)
	if char_location<n:
		new_char = char_location + 96 - n
	else:
		new_char = char_location - n
	decrypt_string += char[new_char]
print("The decrypted text is ", decrypt_string)

