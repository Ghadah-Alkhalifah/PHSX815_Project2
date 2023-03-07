import numpy as np
from scipy.stats import binom
from scipy.stats import chi2
import matplotlib.pyplot as plt



# Set up the experiment parameters
num_flips = 1000  # Number of coin flips
alpha = 6  # Alpha parameter for the beta distribution
beta = 4 # Beta parameter for the beta distribution
num_experiment = 10000  # Number of simulations to perform
seed=5555
np.random.seed(seed)

for i in range(num_experiment):
# Sample the bias coin from a beta distribution(prior distribution)
    bias_coin = np.random.beta(alpha, beta)

# Simulate flipping the coin and count the number of heads
    coin_flips = np.random.binomial(1, bias_coin, size=num_flips)
    
    num_H = np.sum(coin_flips)
    
# Compute the posterior distribution of the bias parameter
    posterior_alpha = alpha + num_H
    posterior_beta = beta + num_flips - num_H
    posterior_dist = np.random.beta(posterior_alpha, posterior_beta, size=10000)

# write text file for heads and tails
fileW=open('coinlfips.txt', "w")
C=str(coin_flips)
fileW.write(C)
fileW.close()
# read the text file 
fileR = open('coinlfips.txt', 'r')
Lines = fileR.readlines()
    
# counting 
counting_H=[]
counting_T=[]
count_accu= []
    
for line in Lines:
    counting2=line.count('1')
    counting_H.append(counting2)
    
totalH=np.sum(counting_H)
count_accu.append(totalH)
for line in Lines:
    counting1=line.count('0')
    counting_T.append(counting1)
totalT=np.sum(counting_T)
count_accu.append(totalT)

print(count_accu)
#ploting bar graph showing counts of heads and tails
category= [ 'Heads' , 'Tials']
plt.bar(category, count_accu, width=.2, bottom=None, color='g')
plt.title(f'{totalH} Heads out of {num_flips} Flips')
plt.xlabel('Outcome of a biased coin flip')
plt.ylabel('Count')
plt.grid()
#plt.savefig('plot1.pdf')
plt.show()


#Plot the posterior distribution of the bias parameter
plt.hist(posterior_dist, bins=50, color='skyblue', edgecolor='black')
plt.xlabel('Bias cion ')
plt.ylabel('Count')
plt.title('Posterior Distribution')
plt.show()


