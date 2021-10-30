# Homework One of Computational Models
# Timothy Seifert
# JP -> Computational Models of Cog Sci

import csv
import scipy
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))
# The naive model for a bystander given as an example
# def bystander_model(N, Temperature, Altruism):
# 	return N == 1 and Temperature > 6 and Altruism > 0.5

# My model for the bystander effect
def bystander_model(N, Temperature, Altruism):
	if(N == 0 or Temperature == 0):
		return False
	# have to presume a bad input like this is possible
	if(Temperature > 120 or Altruism > 1 or Altruism < 0 or N < 0):
		return False

	# calculate the probability decrease
	temp_weighted =((1/int(Temperature))*12)
	bystander_weighted = (1-(1/int(N)))

	probability = ((1 - temp_weighted - bystander_weighted)+(.5*Altruism))
	sigmoid_var =  sigmoid(probability)
	# less than 50% probability and we will say the person was not saved
	print(sigmoid_var)

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

def main():
	print("Testing Falsifying Data")
	print(error_metric('/Users/timseifert/Desktop/CompModels/hw2_comp_models/Timothy_Seifert_falsifying_data.csv'))
	print("Testing Supporting Data")
	print(error_metric('/Users/timseifert/Desktop/CompModels/hw2_comp_models/Timothy_Seifert_supporting_data.csv'))

if __name__ == "__main__":
    main()