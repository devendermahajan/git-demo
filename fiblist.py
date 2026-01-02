# generate n fibonacci number using list
# initialize fib list

fib = [0,1]
terms = int(input("Enter total number to generate: "))-2
for i in range(terms):
    fib.append(fib[-1]+fib[-2])

out = ", " .join(str(e) for e in fib) 
print(out)