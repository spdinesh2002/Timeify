def s_c(s,p,p2):
    while(True):
            r=random.choices(s)
            st=' '.join(map(str, r))
            ind=s.index(st)
            if p[ind]>0 and p2[ind]<=2:
                return st
            return s_c(s,p,p2)
import pandas as pd
import random
import tabulate
df=pd.read_excel(r"C:\Users\DINESH\Downloads\class.xlsx")
df2=pd.read_excel(r"C:\Users\DINESH\Downloads\subject.xlsx")
c=df["class"].unique()
s=list(df2["subject"])
p=list(df2["periods"])
w_d=5
n_o_p=7
tt=[]
for i in range(w_d):
    p2=[0,0,0,0,0,0,0]
    l=[]
    for j in range(n_o_p):
            st=s_c(s,p,p2)
            st=''.join(map(str, st))
            ind=s.index(st)
            p[ind]=p[ind]-1
            p2[ind]=p2[ind]+1
            l.append(st)
    tt.append(l)
tt
