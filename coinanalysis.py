import sys
import numpy as np
import matplotlib.pyplot as plt




# Load the prior and posterior distribution for bias coin from the text file
with open("bias-prior1.txt", "r") as fileN:
    prior= np.loadtxt(fileN)
prior_mean = np.mean(prior)
with open("bias-post.txt", "r") as filex:
    post = np.loadtxt(filex)
post_mean = np.mean(post)

#Plot the prior distribution of the bias coin
plt.hist(prior, bins=50, color='red', edgecolor='black', label='prior distribution')
plt.xlabel('prior distribution of a bias cion ')
plt.ylabel('Counts')
plt.title('prior Distribution for 100 cion flips (biased coin)')
plt.text(prior_mean, plt.ylim()[1]*0.5, 'mean={:.1f})'.format(prior_mean), rotation=90, color='black', fontsize=10)
plt.axvline(prior_mean , color='blue', label="Mean")
plt.legend()
#plt.savefig('plot2.png')
plt.show()


#Plot the posterior distribution of the bias coin
plt.hist(post , bins=50, color='skyblue', edgecolor='black', label='posterior distribution' )
plt.xlabel('posterior distribution of a bias coin ')
plt.ylabel('Counts')
plt.text(post_mean, plt.ylim()[1]*0.5, 'mean={:.1f})'.format(post_mean), rotation=90, color='black', fontsize=10)
plt.title('Posterior Distribution for biased coin with 100 flips')
# Plot a vertical line for the sample mean
plt.axvline(post_mean, color='red', label="Mean")
#plt.savefig('plot3.png')
plt.legend()
plt.show()

