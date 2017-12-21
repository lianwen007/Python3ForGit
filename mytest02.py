"""
120/(1+r)+120/(1+r)^2+120/(1+r)^3+120/(1+r)^4+120/(1+r)^5
+120/(1+r)^6+120/(1+r)^7+120/(1+r)^8+120/(1+r)^9+1560/(1+r)^10=2500  
"""


nums=[1,2,3,4,5,6,7,8,9,10]
#x=input("input the num:")
snums0=0
"""for num in nums:
    x=float(x)
    if num <10:
        snums1=120/(1+x)**num
        snums0+=snums1
    else:
        snums2=1560/(1+x)**num
print(snums0+snums2)
"""        
        
for y in range(10000):
    for z in range(10000):
        if z!=0:
            p=float(y/z)
            for num in nums:
                x=float(p)
                if num <10:
                    snums1=120/(1+p)**num
                    snums0+=snums1
                else:
                    snums2=1560/(1+p)**num
            if snums0+snums2==2500:
                print(str(p)+','+str(y)+','+str(z))
                break

#print(snums0+snums2)