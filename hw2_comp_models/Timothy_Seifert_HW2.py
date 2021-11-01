# Homework Three of Computational Models
# Timothy Seifert, Issac, and Jeff
# JP -> Computational Models of Cog Sci

import csv
from scipy.special import expit
import math
import numpy as np
import matplotlib.pyplot as plt

# Our probability bystander model is shown below
def bystander_model(N, Temperature, Altruism):
	# calculate the probability decrease
	temp_weighted =(1/int(Temperature**2 + 1))
	bystander_weighted = (1/int(N+1))

	probability = (1 - temp_weighted - bystander_weighted)+(.5*Altruism)
	sigmoid_var =  expit(probability)
	# less than 50% probability and we will say the person was not saved
	print(sigmoid_var, "sig")
	return max(sigmoid_var,.001)


# def error_metric(filename):
# 	print(filename)
# 	with open(filename, 'r') as csvfile:
# 		reader = csv.reader((csvfile))
# 		error_val = 0
# 		next(reader)
# 		for row in reader:
# 			amb_temp = int(row[0])
# 			n_ppl = int(row[1])
# 			bystander_model(n_ppl, amb_temp, .7)

def minus_log_likelihood(filename, altruism): 
	data =  np.genfromtxt(filename, delimiter=',', skip_header=True)
	loglik = 0
	for person in data:
		#print(bystander_model(person[1], person[0], .7), "bm")
		loglik+=np.log10(bystander_model(person[1], person[0], altruism))
	loglik = -loglik
	print(loglik)
	return loglik

def plotting_increments_of_a(filename):

	x = list()
	y = list()
	# create a list that increments altruism up to one
	nums = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
	for num in nums:
		x.append(minus_log_likelihood(filename, num))
		y.append(num)
	plt.scatter(y, x)
	plt.show()

def main():
	#print("Testing Falsifying Data")
	minus_log_likelihood('/Users/timseifert/Desktop/CompModels/hw2_comp_models/Timothy_Seifert_falsifying_data.csv', .7)
	#print("Testing Supporting Data")
	#print(error_metric('Timothy_Seifert_supporting_data.csv'))
	minus_log_likelihood('/Users/timseifert/Desktop/CompModels/hw2_comp_models/Timothy_Seifert_supporting_data.csv', .7)
	minus_log_likelihood('/Users/timseifert/Desktop/CompModels/hw2_comp_models/empirical.csv', .7)
	plotting_increments_of_a('/Users/timseifert/Desktop/CompModels/hw2_comp_models/empirical.csv')

if __name__ == "__main__":
    main()
