
import random

max_error = 2
expected_ratio = 1.41*10**-1
error = 100

while(error > max_error):
    nf = random.randint(1,8)
    ni = random.randint(1,8)
    ratio = (nf**-2 - ni**-2)
    error = 100*abs((expected_ratio-ratio)/expected_ratio)

print(nf,ni,error)

