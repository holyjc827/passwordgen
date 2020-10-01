import random, string

def generate():
	rand = random.SystemRandom()
	length = int(input("how many digits do you want your password to be? "))
	specialChar = input("Do you want one or more special characters in your password? (Y/N) ")
	if specialChar == "Y":
		alphabet = string.ascii_letters + string.digits + string.punctuation
		password = str().join(rand.choice(alphabet) for _ in range(length))
	elif specialChar == "N":
		alphabet = string.ascii_letters + string.digits
		password = str().join(rand.choice(alphabet) for _ in range(length))
	else:
		print("Please type either Y or N (case-sensitive).")
	return password

password = generate()
print(password)
