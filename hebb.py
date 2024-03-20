import numpy as np

x1=np.array([1,1,-1,-1])
x2=np.array([1,-1,1,-1])
b=np.array([1,1,1,1])

#for AND gate
# y=np.array([1,-1,-1,-1])

# for OR gate
y=np.array([1,1,1,-1])

dw1=[]
dw2=[]
db=[]

print("For AND GATE")

for i in range(0,4):
    dw1.append(x1[i]*y[i])
    dw2.append(x2[i]*y[i])
    db.append(y[i])
    
print("dw1\t dw2\t db")
for i in range(0,4):
    print(str(dw1[i])+ "\t" + str(dw2[i]) + "\t" + str(db[i]))
print("\n")

w1=w2=b0=0
w1n=[]
w2n=[]
bn=[]


for i in range(0,4):
    w1n.append(w1+dw1[i])
    w1=w1n[i]
    w2n.append(w2+dw2[i])
    w2=w2n[i]
    bn.append(b0+db[i])
    b0=bn[i]


print("w1n\t w2n\t bn")    
for i in range(0,4):
    print(str(w1n[i])+ "\t" + str(w2n[i]) + "\t" + str(bn[i]))
    