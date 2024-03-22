# and  str1[i] != divisor[:1]
def gcdOfStrings( str1: str, str2: str) -> str:
    i =0
    divisor =''
    length1 = len(str1)
    length2 = len(str2)
    while i<len(str1) and i<len(str2):
        if(str1[i]==str2[i] and  str1[i] != divisor[:1] ):
            divisor = divisor+str1[i]
            i+=1
        else:
            break
    if(length1>i):
        answer = (str1.replace(divisor,'',1))
        if(answer in divisor or divisor in answer):
            return(divisor)
        else:
            return("")
    elif(length2>i):
        answer = (str2.replace(divisor,'',1))
        if(answer in divisor or divisor in answer):
            return(divisor)
        else:
            return("")
    
name1 = "ABCDEF"
name2 = "ABC"
# name1 = "ABCABC"
# name2 = "ABC"
# name1 ="TAUXXTAUXXTAUXXTAUXXTAUXX"
# name2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# name1="ABABAB"
# name2="ABAB"

# print(gcdOfStrings(name1,name2))

def gcb( str1: str, str2: str) -> str:

    length1 = len(str1)
    length2 = len(str2)
    if str1 + str2 != str2 + str1:
        return " "
    while length2:
        length1,length2 = length2, length1 % length2
    return(str1[:length1])




candies=[2,3,5,1,3]
extraCandies=3

def kidsWithCandies( candies, extraCandies) -> [bool]:
    result = []
    max_number  = max(candies)
    for candy in candies:
        if candy + extraCandies >=max_number:
            result.append(True)
        else:
            result.append(False)
    return(result)

# print(kidsWithCandies(candies,extraCandies))
arr=[1,0,0,0,1]
num =2
def canPlaceFlowers( flowerbed, n):
    numsFree = 0
    i=0
    while i < len(flowerbed):
        if flowerbed[i]==0 and flowerbed[i+1]==0:
            numsFree+=1
            i+=2
        else:
            i+=1
    if numsFree <=n:
        return True
    else:
        return False

# print(canPlaceFlowers(arr,2))
    
def canPlaceFlowers(flowerbed, n):
    nums_free = 0
    i =0
    while i< len(flowerbed):
        if  len(flowerbed) <=1:
            if flowerbed[i] == 0:
                nums_free+=1
                i+=1
            else:
                return False  
        elif flowerbed[i] ==0  and i<1 and flowerbed[i+1]==0 and flowerbed[i+2]:
            flowerbed[i] =1
            nums_free +=1
            i+=2
        elif  i==len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1]==0:
            flowerbed[i]=1
            nums_free +=1
        elif flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
            flowerbed[i]=1
            nums_free +=1
            i+=2
        else:
            i+=1
        
    if nums_free >=n:
        return True
    else:
        return False

# bed=[0,1,0,0,0,0,0]
# n=2
# bed=  [1,0,0,0,0,1]
# n = 2
# bed  = [1,0,0,0,1]
# n = 1
# bed  = [1,0,0,0,1]
# n = 2
# bed =[1,0,0,0,1,0,0]
# n=2
# bed=[0]
# n=1
bed =[1]
n=1
# print(canPlaceFlowers(bed,n))

h = "S".lower()
# print(h)






def reverseVowels(s):
        left = 0
        right = len(s)-1
        leftArr =[]
        rightArr=[]



