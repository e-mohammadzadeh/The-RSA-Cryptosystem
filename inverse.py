##################################################################
#############       Erfan Mohammadzadeh          #################
#############          9622473147                #################
#############            Inverse                 #################
##################################################################

import math


def check_conditions(number_a, number_n):
	answer = math.gcd(number_a, number_n)
	if answer == 1:
		inverse_answer = compute_a_inverse(number_a, number_n)
		show_results(number_a, number_n, inverse_answer)
		return inverse_answer
	else:
		print(
				"\nNOTICE !!!!\ngcd({}, {}) is equal to '{}', so we can NOT compute inverse of a ( There is no modular multiplicative inverse for this integers ).".format(
						number_a, number_n, answer))
		exit()


def compute_a_inverse(number_a, number_n):
	for index in range(0, number_n):
		if (index * number_a) % number_n == 1:
			return index



def show_results(number_a, number_n, second_answer):
	print("\nInverse of {}  in modulo {} is << {} >>.".format(number_a, number_n, second_answer))


if __name__ == "__main__":
	check_conditions()
