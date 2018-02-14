# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# isPhoneNumber.py
# ABS: 238
# Say you want to find a phone number in a string. You know the pattern: three numbers, a hyphen, three numbers, a hyphen, and four numbers. Here’s an example: 415-555-4242.
# first you do the non regex way which is long
# then you use regex

def isPhoneNumber(text):
	if len(text) != 12:
		return False

	for i in range(0,3):
		if not text[i].isdecimal():
			return False

	if text[3] != '-':
		return False

	for i in range(4,7):
		if not text[i].isdecimal():
			return False

	if text[7] != '-':
		return False

	for i in range(8,12):
		if not text[i].isdecimal():
			return False

	return True

# print('415-555-4242 is a phone number: ')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number: ')
# print(isPhoneNumber('Moshi moshi'))

message = "Call me at 415-555-1011 tomorrow.  415-555-9999 is my office."

for i in range(len(message)):
	chunk = message[i:i+12] # where 12 is the length of the phone number and [i:i+12] means from position i to i+12 is the chunk
	if isPhoneNumber(chunk):
		print('Phone number found: ' + chunk)

print('Done')

