exp = [20,35,25,10]
total = 0
for i in range(len(exp)):
    print('Month:',(i+1),'Expeses:',exp[i])
    total = total+ exp[i]

print("Total:",total)

for i in range(6):
    if i%2==0:
        continue
    else:
        print(i*i)