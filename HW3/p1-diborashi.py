def returnDir(x):
    z=[x[i].rstrip().split(",") for i in range(len(x))]
    return([z[i][2] for i in range(len(x))])
f=open('imdb-top-casts.csv','r',encoding='utf-8')
x=[]
for xy in f:
    x.append(xy)
Directors=returnDir(x)
uniqD=set(Directors)
NumD=[sum([1 for ii in range(len(Directors)) if jj==Directors[ii]]) for jj in uniqD]
sortIdx=[i[0] for i in sorted(enumerate(NumD), key=lambda x:x[1])]
sortD=[list(uniqD)[ii] for ii in sortIdx]
sortNum=sorted(NumD)
print("Directors with most movies \n")
print([list(reversed(sortD))[0:4],list(reversed(sortNum))[0:5]])
###Q2
from numpy import genfromtxt
def returnmovdirects(x):
    z=[x[i].rstrip().split(",") for i in range(len(x))]
    return [[z[i][0] for i in range(len(x))],[z[i][2] for i in range(len(x))]]
def returnMov(x):
    z=[x[i].rstrip().split(",") for i in range(len(x))]
    return([z[i][1] for i in range(len(x))])
f=open('imdb-top-casts.csv','r',encoding='utf-8')
x=[]
for xy in f:
    x.append(xy)
MovDir=returnmovdirects(x)
f=open('imdb-top-grossing.csv','r',encoding='utf-8')
x=[]
for xy in f:
    x.append(xy)
Movs=returnMov(x)
Directors=[[MovDir[1][jj] for jj in range(len(MovDir[0])) if MovDir[0][jj]==ii] for ii in Movs]
Directors=sum(Directors,[])
uniqD=set(Directors)
NumD=[sum([1 for ii in range(len(Directors)) if jj==Directors[ii]]) for jj in uniqD]
sortIdx=[i[0] for i in sorted(enumerate(NumD), key=lambda x:x[1])]
sortD=[list(uniqD)[ii] for ii in sortIdx]
sortNum=sorted(NumD)
print("Directors with most movies in top grossing \n")
print([list(reversed(sortD))[0:5],list(reversed(sortNum))[0:5]])
###Q3
def returnRatMovs(x):
    z=[x[i].rstrip().split(",") for i in range(len(x))]
    return [[z[i+1][1] for i in range(len(x)-1)],[z[i+1][-1] for i in range(len(x)-1)]]
def returnMovAct(x):
   z=[x[i].rstrip().split(",") for i in range(len(x))]
   return [[z[i][0] for i in range(len(x))],[z[i][4] for i in range(len(x))]]
f=open('imdb-top-rated.csv','r',encoding='utf-8')
x=[]
for xy in f:
    x.append(xy)
MovRat=returnRatMovs(x)
f=open('imdb-top-casts.csv','r',encoding='utf-8')
x=[]
for xy in f:
    x.append(xy)
MovAct=returnMovAct(x)
TopAct=sum([[MovAct[1][jj] for jj in range(len(MovAct[1])) if MovAct[0][jj]==ii] for ii in MovRat[0]],[])
print("Actors with most movie Credits \n")
print(TopAct[0:5],MovRat[1][0:6])
###4
def returnGrossMovs(x):
    z=[x[i].rstrip().split(",") for i in range(len(x))]
    return [[z[i+1][1] for i in range(len(x)-1)],[z[i+1][-1] for i in range(len(x)-1)]]
def returnAllActs(x):
    z=[x[i].rstrip().split(",") for i in range(len(x))]
    ##print(z)
    return [[z[j][i] for i in [0,3,4,5,6,7]] for j in range(len(x))]
f=open('imdb-top-grossing.csv','r',encoding='utf-8')
x=[]
for xy in f:
    x.append(xy)
AllGross=returnGrossMovs(x)    
f=open('imdb-top-casts.csv','r',encoding='utf-8')
x=[]
for xy in f:
    x.append(xy)   
AllActs=returnAllActs(x)
movieCredsActs=[[[AllActs[ii][1], AllActs[ii][2],  AllActs[ii][3],  AllActs[ii][4],  AllActs[ii][5]]for ii in range(len(AllActs)) if AllActs[ii][0]==jj]for jj in AllGross[0]]
movieCredsActs=sum(movieCredsActs,[])
UniqAs=list(set(sum(movieCredsActs,[])))  #finding Unique Actors in the list of lists
Earnings=[[[float(AllGross[1][jj])*16/31, float(AllGross[1][jj])*8/31,  float(AllGross[1][jj])*4/31, float(AllGross[1][jj])*2/31,  float(AllGross[1][jj])/31]for ii in range(len(AllActs)) if AllActs[ii][0]==AllGross[0][jj]]for jj in range(len(AllGross[1]))]
Earnings=sum(Earnings,[]) #this gives a list of list in earnings Datastructure smilar to the movieCreds
#the code below creates a list of list of earnings for each Unique Actors for different movies they acted in
SumEarns=[[sum([float(Earnings[xx][yy])]) for xx in range(len(movieCredsActs)) for yy in range(len(movieCredsActs[0])) if ii==movieCredsActs[xx][yy]] for ii in UniqAs]
SumEarns=[sum(SumEarns[i])for i in range(len(SumEarns))] #summing the lists of lists up to get the total earning for each actor
sortIdx=[i[0] for i in sorted(enumerate(SumEarns), key=lambda x:x[1])]
sortActs=[list(UniqAs)[ii] for ii in sortIdx]
SortEarns=sorted(SumEarns)
print("Actors with most Earning \n")
print(list(reversed(sortActs))[0:4],list(reversed(SortEarns))[0:4])
##Bonus
#for this we use Earnings and movieCredsActs variables from last problem
import itertools as it
pairedEarnings=[list(it.combinations(ii,2)) for ii in Earnings]
pairedActs=[list(it.combinations(ii,2)) for ii in movieCredsActs]
uniqPairs=list(set(sum(pairedActs,[])))
b = []
seen = set()
for t in uniqPairs:
    s = tuple(sorted(t))
    if s not in seen:
        seen.add(s)
        b.append(s)
#b doesn't contain repeated orders of movie actors so it doesn't have [(x,y) (y,x)]... unlike uniqPairs
#uniqPairedEarns=[[pairedEarnings[ii][xx] for ii in range(len(pairedActs)) for xx in range(len(pairedActs[0]) if (jj==pairedActs[ii][xx]) or (jj[0]==pairedActs[ii][xx][1] and jj[1]==pairedActs[ii][xx][0])] for jj in b]
uniqPairedEarns=[[sum(pairedEarnings[ii][xx]) for ii in range( len(pairedActs)) for xx in range(len(pairedActs[0])) if (jj==pairedActs[ii][xx]) or (jj[0]==pairedActs[ii][xx][1] and jj[1]==pairedActs[ii][xx][0])] for jj in b]
uniqPairedEarns=[sum(i) for i in uniqPairedEarns]
sortIdx=[i[0] for i in sorted(enumerate(uniqPairedEarns), key=lambda x:x[1])]
sortActpairs=[list(b)[ii] for ii in sortIdx]
sortedpairEarns=sorted(uniqPairedEarns)
print("Top 10 pairs with most Earnings \n")
print(list(reversed(sortActpairs))[0:9], list(reversed(sortedpairEarns))[0:9])


1 Comment