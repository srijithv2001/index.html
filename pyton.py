string=input("enter the string ");
print("string operations")
print("Menu\n1. length\n 2. Upper case\n 3. Lower case\n 4. swap case\n 5. Title\n 6. Reverse\n 7. Is Alpha\n 8. Slice\n 9. Split\n 10.Count\n 11. Exit")
while(1):
	ch=int(input("Enter input of your choice"))u
	if(ch==1):
		print("the length of the string is ",len(string))
	elif(ch==2):
		print(string.upper())
	elif(ch==3):
		print(string.lower())
	elif(ch==4):
		print(string.swapcase())
	elif(ch==5):
		print(string.title())
	elif(ch==6):
		print(string[::-1])
	elif(ch==7):
		print(string.isalpha())
	elif(ch==8):
		print(string[0:2])
	elif(ch==9):
		print(string.split())
	elif(ch==10):
		print(string.count('a'))
	elif(ch==11):
		break

