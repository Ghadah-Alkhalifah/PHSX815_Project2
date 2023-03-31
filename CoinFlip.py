import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy.stats

# if the user includes the flag -h or --help print the options
if '-h' in sys.argv or '--help' in sys.argv:
    print ("Usage: %s [-seed number],%s [-Nflips]" % sys.argv[0])
    print
    sys.exit(1)
# Set up the experiment parameters
Nflips = 100  # Number of coin flips
alpha = 13.8  # Alpha parameter for the beta distribution
beta = 9.2  # Beta parameter for the beta distribution
seed=4444
np.random.seed(seed)

# read the user-provided seed from the command line (if there)
if '-seed' in sys.argv:
    p = sys.argv.index('-seed')
    seed = int(sys.argv[p+1])

if '-Nflips' in sys.argv:
    p = sys.argv.index('-Nflips')
    Nflips =int(sys.argv[p+1])

# Sample the bias parameter (alternative hypothises) from a beta distribution (prior distribution)
bias = np.random.beta(alpha, beta, size=Nflips)
prior_mean = np.mean(bias)

# Simulate flipping the coin and count the number of heads
coin_flips = np.random.binomial(1, bias, size=Nflips)
num_H = np.sum(coin_flips)

# Compute the posterior distribution of the bias parameter
posterior_alpha =  num_H+ alpha
posterior_beta =  Nflips +beta- num_H
posterior_dist = np.random.beta(posterior_alpha, posterior_beta, size=10000)
# Calculate the sample mean 
post_mean = np.mean(posterior_dist)


#Sample the fair coin (for null hypothysis)
p=0.5
fair_coinx = np.random.binomial(1, p, size=Nflips)
num_Hfair = np.sum(fair_coinx)

#write text file for fair coin
filez = open("faircoin.txt", "w")
np.savetxt(filez,fair_coinx, fmt='%d')
filez.close()

# write text file for prior distribution biased coin
ifile = open("bias-prior.txt", "w")
np.savetxt(ifile,bias )
ifile.close()

# write text file for posterier distribution biased coin
filex = open("bias-post.txt", "w")
np.savetxt(filex,posterior_dist)
filex.close()

#write text file for unfair
filey = open("bias.txt", "w")
np.savetxt(filey,coin_flips, fmt='%d')
filey.close()



# write text file to count heads and tails for biased coin
fileW=open('coinflips.txt', "w")
C=str(coin_flips)
fileW.write(C)
fileW.close()

# read the text file for biased coin 
fileR = open('coinflips.txt', 'r')
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
#ploting bar graph showing counts of heads and tails for biased coin
category= [ 'Heads' , 'Tials']
plt.bar(category, count_accu, width=.2, bottom=None, color='g')
plt.title(f'{totalH} Heads out of {Nflips} Flips')
plt.xlabel('Outcome of a biased coin flip')
plt.ylabel('Count')
plt.grid()
#plt.savefig('plot1.pdf')
plt.show()

    
