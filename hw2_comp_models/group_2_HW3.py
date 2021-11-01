# Homework Three of Computational Models
# Timothy Seifert, Issac, and Jeff
# JP -> Computational Models of Cog Sci

import csv
from scipy.special import expit
import math
import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import fminbound


def bystander_model(N, Temperature, Altruism):
	# calculate the probability decrease
	num = np.sin((2*Altruism-.4)**2)+1
	den = 2*N + np.abs(np.tanh(.01*(Temperature-20)))*10

	prob = num/den
	# less than 50% probability and we will say the person was not saved
	return prob


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
	plt.title("LL respective to Altruism")
	plt.xlabel("Altruism")
	plt.ylabel("LL")
	plt.show()


# This is for part two of the Bonus
def find_min():
	return fminbound(alt_calc, 0, 1)

def alt_calc(Altruism):
	data =  np.genfromtxt("empirical.csv", delimiter=',', skip_header=True)
	loglik = 0
	for person in data:
		#print(bystander_model(person[1], person[0], .7), "bm")
		loglik+=np.log10(bystander_model(person[1], person[0], Altruism))
	loglik = -loglik
	return loglik
##############################

def main():
	print("falsifying data sets")
	minus_log_likelihood('group_2_falsifying_data.csv', .7)
	print("supporting data sets")
	minus_log_likelihood('group_2_supporting_data.csv', .7)
	minus_log_likelihood('empirical.csv', .7)
	plotting_increments_of_a('empirical.csv')
	print("*********Part Two Bonus**********")
	print(find_min())

if __name__ == "__main__":
    main()
