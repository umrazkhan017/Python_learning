name = input()
#taking input from user
size=len(name)
#getting length of the name
count=0



for i in range(0,size):
    if(name[i]!=name[size-i-1] and count==0 ):
        print("Not a Palindrome")
        count=1
        
            
if(count==0):
    print("It is Palindrome");



#m a d a m

#0 1 2 3 4

 m !=  m
 a !=  a
 d !=  d 
