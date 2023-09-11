n=int(input()) 
s=set(map(int,input().split())) 
N=int(input()) 
for i in range (N): 
    c=input().split() 
    for i in range (1,len(c)): 
        c[i]=int(c[i]) 
        if c[0] =="pop": 
            s.pop() 
        elif c[0]=="remove": 
            s.remove(c[1]) 
        else: 
            s.discard(c[1]) 
print(len(s))