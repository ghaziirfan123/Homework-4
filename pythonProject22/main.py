# My name is Mohammad ghazi irfan and ID is 1626488

data=[]
initial=""
while(initial!="-1"):
    initial=input("")
    if(initial!="-1"):
        data.append(initial)
for i in data:
    final=[]
    end=i.split(" ")
    for i in end:
        if(len(i)>0):
            final.append(i)
    try:
        print(final[0],end="\t")
        data=int(final[1])+1
        print(data,end="\n")
    except ValueError as vError:
        print(0,end="\n")