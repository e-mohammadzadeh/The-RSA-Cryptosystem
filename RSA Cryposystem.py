##################################################################
#############       Erfan Mohammadzadeh          #################
#############          9622473147                #################
#############       The RSA Cryptosystem         #################
##################################################################

import Prime_number
import inverse
import math


def get_data():
	num_p = Prime_number.get_data()
	num_g = Prime_number.get_data()
	m = int(input("Write your message that want to encrypted ? "))
	return num_p, num_g, m


def compute_encryption_exponent(num_p, num_g):
	number = (num_p - 1) * (num_g - 1)
	if (number % 2) == 0:
		for index in range(7, number // 2, 2):
			if math.gcd(index, number) == 1:
				return index
	else:
		exit()


def compute_cipher_text(n, m, e):
	return pow(m, e, n)


def compute_d_satisfying(e, p, q):
	return inverse.check_conditions(e, (p - 1) * (q - 1))


def decrypt_message(c, d, n):
	return pow(c, d, n)


if __name__ == "__main__":
	number_p, number_g, message = get_data()
	N = number_p * number_g
	print("N is : ", N)

	encryption_exponent = compute_encryption_exponent(number_p, number_g)
	print("Encryption Exponent (e) is : ", encryption_exponent)

	number_c = compute_cipher_text(N, message, encryption_exponent)
	print("Cipher text (c) is : ", number_c)

	number_d = compute_d_satisfying(encryption_exponent, number_p, number_g)
	print("number d satisfying is : ", number_d)

	decryption_message = decrypt_message(number_c, number_d, N)
	print("message after decryption is : ", decryption_message)
