# Homework One of Computational Models
# Timothy Seifert
# JP -> Computational Models of Cog Sci

import csv
from scipy.special import expit
import math
import numpy as np

# The naive model for a bystander given as an example
# def bystander_model(N, Temperature, Altruism):
# 	return N == 1 and Temperature > 6 and Altruism > 0.5

# My model for the bystander effect
def bystander_model(N, Temperature, Altruism):
	# calculate the probability decrease
	temp_weighted =(1/int(Temperature**2 + 1))
	bystander_weighted = (1/int(N+1))

	probability = (1 - temp_weighted - bystander_weighted)+(.5*Altruism)
	sigmoid_var =  expit(probability)
	# less than 50% probability and we will say the person was not saved
	print(sigmoid_var, "sig")
	return max(sigmoid_var,.001)

# Utilizes the total rows as the error metric
def error_metric(filename):
	print(filename)
	with open(filename, 'r') as csvfile:
		reader = csv.reader((csvfile))
		error_val = 0
		next(reader)
		for row in reader:
			amb_temp = int(row[0])
			n_ppl = int(row[1])
			bst_mode = bystander_model(n_ppl, amb_temp, .7)
	# 		row_Val = row[2]
	# 		truth_val = bool(int(row_Val))
	# 		if( bst_mode != truth_val):
	# 			error_val += 1
	# return error_val

def minus_log_likelihood(filename): 
	data =  np.genfromtxt(filename, delimiter=',', skip_header=True)
	loglik = 0
	for person in data:
		#print(bystander_model(person[1], person[0], .7), "bm")
		loglik+=np.log10(bystander_model(person[1], person[0], .7))
	loglik = -loglik
	print(loglik)

def main():
	#print("Testing Falsifying Data")
	minus_log_likelihood('Timothy_Seifert_falsifying_data.csv')
	#print("Testing Supporting Data")
	#print(error_metric('Timothy_Seifert_supporting_data.csv'))
	minus_log_likelihood('Timothy_Seifert_supporting_data.csv')
	minus_log_likelihood('empirical.csv')

if __name__ == "__main__":
    main()