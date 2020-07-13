ip=[["T","R","G","S","J"],["X","D","O","K","I"],["M"," ","V","L","N"],["W","P","A","B","E"],["U","Q","H","C","F"]]
seq="ARRBBLLO"
for r in ip:
    print("".join(r))
for i,j in enumerate(ip):
    for k,l in enumerate(j):
        if(l==" "):
            a=i
            b=k 
def ab(a,b):
    if a>0:
        ip[a][b],ip[a-1][b]=ip[a-1][b],ip[a][b]
    else:
        print("This puzzle has no final configuration")
def be(a,b):
    if a<4:
        ip[a][b],ip[a+1][b]=ip[a+1][b],ip[a][b]
    else:
        print("This puzzle has no final configuration")
def rt(a,b):
    if b<4:
        ip[a][b],ip[a][b+1]=ip[a][b+1],ip[a][b]
    else:
        print("This puzzle has no final configuration")
def lt(a,b):
    if b>0:
        ip[a][b],ip[a][b-1]=ip[a][b-1],ip[a][b]
    else:
        print("This puzzle has no final configuration")
for ch in seq:
    if ch == "A":
        ab(a,b)
        a=a-1
    if ch == "B":
        be(a,b)
        a=a+1
    if ch == "R":
        rt(a,b)
        b=b+1
    if ch == "L":
        lt(a,b)
        b=b-1
    if ch=="O":
        print("Output")
        for r in ip:
            x=" ".join(r)
            print(x)
        break
