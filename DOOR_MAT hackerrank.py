def cen(d,w,v):
    w=w-len(d)
    w=w//2
    v=w*v
    q=v+d+v
    return q
print("Enter two odd numbers ")
s=list(map(int,input().split()[:2]))
row=s[0]
col=s[1]
i=1
while i<=row-1:
    p=i*".|."
    d=cen(p,row,'-')
    print(cen(d,col,'-'))
    i=i+2
i=row-1-1
print(cen("WELCOME",col,'-'))
while i>=1:
    p=i*".|."
    d=cen(p,row,'-')
    print(cen(d,col,'-'))
    i=i-2
        
