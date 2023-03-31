import sys
import numpy as np
import matplotlib.pyplot as plt
from MySort import MySort
import scipy.stats



# if the user includes the flag -h or --help print the options
if '-h' in sys.argv or '--help' in sys.argv:
    print ("Usage: %s [-seed number]" % sys.argv[0])
    print
    sys.exit(1)

p0=0.5
p1=0.6
Ntoss = 0  
LogLikeRatio0 = []
LogLikeRatio1 = []
LLR_min = 1e8
LLR_max = -1e8


with open("faircoin.txt", 'r') as ifile:
    Ntoss = 0  
    num_Hfair =0 
    LLR = 0
    
    for v in ifile:
        
        x=v.count('1')
        if x==1:
            num_Hfair+=1
        
        Ntoss +=1
        if int(v) >= 1:
            LLR += np.log( p1/p0 )
        else:
            LLR += np.log( (1.-p1)/(1.-p0) )
        if LLR < LLR_min:
            LLR_min = LLR
        if LLR > LLR_max:
            LLR_max = LLR
            
        LogLikeRatio0.append(LLR)
    
                    
with open("bias.txt", 'r') as xfile:
    num_H=0
    LLR = 0
    Ntoss = 0  
    for v in xfile:
        x1=v.count('1')
        if x1==1:
            num_H+=1
        Ntoss +=1
        
        if int(v) == 1:
            LLR += np.log( p1/p0 )
        else:
            LLR += np.log( (1.-p1)/(1.-p0) )
        if LLR < LLR_min:
            LLR_min = LLR
        if LLR > LLR_max:
            LLR_max = LLR
            
        LogLikeRatio1.append(LLR)
    

# Compute the chi-square statistic and p-value
expected_heads = num_Hfair
expected_tails = Ntoss - num_Hfair
observed_heads = num_H
observed_tails = Ntoss - num_H
observed=[observed_heads, observed_tails]
expected=[expected_heads, expected_tails]
chi2, pValue = scipy.stats.chisquare(observed, expected)

# Print the results of the chi-square test
if pValue <= 0.05:
    print("According to chi-square test the coin is biased (p-value = {:.10f})".format(pValue))
else:
    print("According to chi-square test the coin is fair (p-value = {:.10f})".format(pValue))

Sorter = MySort()
    
LogLikeRatio0 =  Sorter.DefaultSort(LogLikeRatio0)
LogLikeRatio1 =  Sorter.DefaultSort(LogLikeRatio1)

# Define significance level alpha
alpha = 0.05

# Calculate the likelihood ratio threshold for the 5% significance level
T = np.quantile(LogLikeRatio0, 0.95)

# Calculate the statistical power of the test
powertest= np.mean(LogLikeRatio1 > T)
# Print the results
print("Likelihood ratio threshold:", T)
print("Statistical power of log likelihood ratio test:", powertest)


title = str(Ntoss) +  " flips"

#plot
plt.figure()
plt.hist(LogLikeRatio0 ,bins=10, density=True, facecolor='b', alpha=0.9, label="assuming $\\mathbb{H}_0$")
plt.axvline(T , color='red', label='$\lambda_a$', linestyle='dashed')   
plt.hist(LogLikeRatio1, bins=10, density=True, facecolor='g', alpha=0.9, label="assuming $\\mathbb{H}_1$")
plt.legend()

plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
plt.ylabel('Probability')
plt.title(title)

betatxt = '1-Beta={:.3f}'.format(powertest)
alphatxt = f"Alpha = {alpha}"
value = alphatxt + "\n" + betatxt

# Add the text annotation to the plot
plt.text(-3.5,0.4, value)
plt.grid(True)
#plt.savefig('plot9.png')
plt.show()

