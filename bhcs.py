class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
a =100
i=1
Z2=0
D1=1
D2=1
D3=1
C1=1
C2=1
C3=1
PD1=1
PC1=1
SD1=1
SC1=1
d1n=1
d2n=1
d3n=1
c1n=1
c2n=1
c3n=1
pdn=1
pcn=1
sdn=1
scn=1
dd1=0
dd2=0
dd3=0
cc1=0
cc2=0
cc3=0
d1p=0
d2p=0
d3p=0
c1p=0
c2p=0
c3p=0
d1s=0
d2s=0
d3s=0
c1s=0
c2s=0
c3s=0
prevd =''
prevc =''
scnd=''
scnc=''
INV2=0
OUT2=0
PRF =0
count2 =0
def DC103(n =100):
  if n not in range(0,37 ) and n not in (100,200):
      print("Out of range")
  else:
    global i
    global Z2
    n1=1*i
    n2=2*i
    n3=3*i
    n4=4*i
    n5=5*i
    n6=7*i
    n7=10*i
    n8=15*i
    n9=20*i
    n10=30*i
    global a
    global D1
    global D2
    global D3
    global C1
    global C2
    global C3
    global PD1
    global PC1
    global SD1
    global SC1
    global d1n
    global d2n
    global d3n
    global c1n
    global c2n
    global c3n
    global pdn
    global pcn
    global sdn
    global scn
    global dd1
    global dd2
    global dd3
    global cc1
    global cc2
    global cc3
    global d1p
    global d2p
    global d3p
    global c1p
    global c2p
    global c3p
    global d1s
    global d2s
    global d3s
    global c1s
    global c2s
    global c3s
    global prevd
    global prevc
    global scnd
    global scnc
    global scnd
    global INV2
    global OUT2
    global PRF
    global count2
    #INV2 +=eval("n"+str((D1)))*d1n+eval("n"+str((D2)))*d2n+eval("n"+str((D3)))*d3n+eval("n"+str((C1)))*c1n+eval("n"+str((C2)))*c2n+eval("n"+str((C3)))*c3n
    INV2 +=dd1+dd2+dd3+cc1+cc2+cc3
    if n == 100:
      Z =0
      a =100
      D1 =1
      D2 =1
      D3 =1
      C1 =1
      C2 =1
      C3 =1
      PD1=1
      PC1=1
      SD1=1
      SC1=1
      d1n=1
      d2n=1
      d3n=1
      c1n=1
      c2n=1
      c3n=1
      pdn=1
      pcn=1
      sdn=1
      scn=1
      dd1=0
      dd2=0
      dd3=0
      cc1=0
      cc2=0
      cc3=0
      d1p=0
      d2p=0
      d3p=0
      c1p=0
      c2p=0
      c3p=0
      d1s=0
      d2s=0
      d3s=0
      c1s=0
      c2s=0
      c3s=0
      f100=2
      prevd=''
      prevc=''
      scnd=''
      scnc=''
      INV2=0
      OUT2=0
      count2=0
    elif n == 200:
      Z =0
      D1 =1
      D2 =1
      D3 =1
      C1 =1
      C2 =1
      C3 =1
      PD1=1
      PC1=1
      SD1=1
      SC1=1
      d1n=1
      d2n=1
      d3n=1
      c1n=1
      c2n=1
      c3n=1
      pdn=1
      pcn=1
      sdn=1
      scn=1
      dd1=0
      dd2=0
      dd3=0
      cc1=0
      cc2=0
      cc3=0
      d1p=0
      d2p=0
      d3p=0
      c1p=0
      c2p=0
      c3p=0
      d1s=0
      d2s=0
      d3s=0
      c1s=0
      c2s=0
      c3s=0
      f100=2
      prevd=''
      prevc=''
      scnd=''
      scnc=''
      INV2=0
      OUT2=0
      count2=0
      DC103(a)
    elif n == 0:
      D1 +=1
      if D1 >10:
          D1=1
          d1n = 0
      D2 +=1
      if D2 >10:
          D2=1
          d2n = 0
      D3 +=1
      if D3 >10:
          D3=1
          d3n = 0
      C1 +=1
      if C1 >10:
          C1=1
          c1n = 0
      C2 +=1
      if C2 >10:
          C2=1
          c2n = 0
      C3 +=1
      if C3 >10:
          C3=1
          c3n = 0
    else:
      if n in range(1,13):
        if d1n ==1:
            #OUT2 +=(eval("n"+str((D1)))*d1n)*3
            OUT2 += dd1*3
        D1=1
        D2 +=1
        D3 +=1
        if D2 >10:
          D2=1
          d2n  =0
        if D3 >10:
          D3=1
          d3n  =0
        d1p =1
        d2p =0
        d3p =0
        if scnd == 'dp1':
            SD1 =1
        elif scnd !='' : SD1 +=1
        if SD1 >10: sdn =0
        if prevd =='dp1' or count2 ==0:
            PD1=1
        else:
            PD1 +=1
            scnd = prevd
            if prevd =='dp2':
              d1s=0
              d2s=1
              d3s=0
            if prevd =='dp3':
              d1s=0
              d2s=0
              d3s=1
        if PD1 >10: pdn =0
        prevd ='dp1'
      elif n in range(13,25):
        if d2n ==1:
            #OUT2 +=(eval("n"+str((D2)))*d2n)*3
            OUT2 += dd2*3
        D2=1
        D1 +=1
        D3 +=1
        if D1 >10:
          D1=1
          d1n  =0
        if D3 >10:
          D3=1
          d3n  =0
        d1p =0
        d2p =1
        d3p =0
        if scnd == 'dp2':
            SD1 =1
        elif scnd !='' : SD1 +=1
        if SD1 >10: sdn =0
        if prevd =='dp2' or count2 ==0:
            PD1=1
        else:
            PD1 +=1
            scnd = prevd
            if prevd =='dp1':
              d1s=1
              d2s=0
              d3s=0
            if prevd =='dp3':
              d1s=0
              d2s=0
              d3s=1
        if PD1 >10: pdn =0
        prevd ='dp2'
      elif n in range(25,37):
        if d3n ==1:
            #OUT2 +=(eval("n"+str((D3)))*d3n)*3
            OUT2 += dd3*3
        D3=1
        D1 +=1
        D2 +=1
        if D2 >10:
          D2=1
          d2n  =0
        if D1 >10:
          D1=1
          d1n  =0
        d1p =0
        d2p =0
        d3p =1
        if scnd == 'dp3':
            SD1 =1
        elif scnd !='' : SD1 +=1
        if SD1 >10: sdn =0
        if prevd =='dp3' or count2 ==0:
            PD1=1
        else:
            PD1 +=1
            scnd = prevd
            if prevd =='dp1':
              d1s=1
              d2s=0
              d3s=0
            if prevd =='dp2':
              d1s=0
              d2s=1
              d3s=0
        if PD1 >10: pdn =0
        prevd ='dp3'
      if n in (1,4,7,10,13,16,19,22,25,28,31,34):
        if c1n ==1:
            #OUT2 +=(eval("n"+str((C1)))*c1n)*3
            OUT2 += cc1*3
        C1=1
        C2 +=1
        C3 +=1
        if C2 >10:
          C2=1
          c2n  =0
        if C3 >10:
          C3=1
          c3n  =0
        c1p =1
        c2p =0
        c3p =0
        if scnc == 'dc1':
            SC1 =1
        elif scnc !='' : SC1 +=1
        if SC1 >10: scn =0
        if prevc =='dc1' or count2 ==0:
            PC1=1
        else:
            PC1 +=1
            scnc =prevc
            if prevc =='dc2':
              c1s=0
              c2s=1
              c3s=0
            if prevc =='dc3':
              c1s=0
              c2s=0
              c3s=1
        if PC1 >10: pcn =0
        prevc ='dc1'
      elif n in (2,5,8,11,14,17,20,23,26,29,32,35):
        if c2n ==1:
            #OUT2 +=(eval("n"+str((C2)))*c2n)*3
            OUT2 += cc2*3
        C2=1
        C1 +=1
        C3 +=1
        if C1 >10:
          C21=1
          c1n  =0
        if C3 >10:
          C3=1
          c3n  =0
        c1p =0
        c2p =1
        c3p =0
        if scnc == 'dc2':
            SC1 =1
        elif scnc !='' : SC1 +=1
        if SC1 >10: scn =0
        if prevc =='dc2' or count2 ==0:
            PC1=1
        else:
            PC1 +=1
            scnc =prevc
            if prevc =='dc1':
              c1s=1
              c2s=0
              c3s=0
            if prevc =='dc3':
              c1s=0
              c2s=0
              c3s=1
        if PC1 >10: pcn =0
        prevc ='dc2'
      elif n >0 and n % 3 ==0:
        if c3n ==1 :
            #OUT2 +=(eval("n"+str((C3)))*c3n)*3
            OUT2 += cc3*3
        C3=1
        C1 +=1
        C2 +=1
        if C2 >10:
          C2=1
          c2n  =0
        if C1 >10:
          C1=1
          c1n  =0
        c1p =0
        c2p =0
        c3p =1
        if scnc == 'dc3':
            SC1 =1
        elif scnc !='' : SC1 +=1
        if SC1 >10: scn =0
        if prevc =='dc3' or count2 ==0:
            PC1=1
        else:
            PC1 +=1
            scnc =prevc
            if prevc =='dc1':
              c1s=1
              c2s=0
              c3s=0
            if prevc =='dc2':
              c1s=0
              c2s=1
              c3s=0
        if PC1 >10: pcn =0
        prevc ='dc3'
      a = n
      count2 +=1
    if d1n ==0 or d2n ==0 or d3n ==0 or c1n ==0 or c2n ==0 or c3n ==0 or pdn==0 or pcn==0 :
        if D1 <=3:d1n=0
        if D2 <=3:d2n=0
        if D3 <=3:d3n=0
        if C1 <=3:c1n=0
        if C2 <=3:c2n=0
        if C3 <=3:c3n=0
        if PD1 <=3:pdn=0
        if PC1 <=3:pcn=0
        if SD1 <=3:sdn=0
        if SC1 <=3:scn=0
    d1 =int(eval("n"+str((D1)))*d1n + eval("n"+str((PD1)))*d1p*pdn + eval("n"+str((SD1)))*d1s*sdn)
    d2 =int(eval("n"+str((D2)))*d2n + eval("n"+str((PD1)))*d2p*pdn + eval("n"+str((SD1)))*d2s*sdn)
    d3 =int(eval("n"+str((D3)))*d3n + eval("n"+str((PD1)))*d3p*pdn + eval("n"+str((SD1)))*d3s*sdn)
    c1=int(eval("n"+str((C1)))*c1n  + eval("n"+str((PC1)))*c1p*pcn + eval("n"+str((SC1)))*c1s*scn)
    c2=int(eval("n"+str((C2)))*c2n  + eval("n"+str((PC1)))*c2p*pcn + eval("n"+str((SC1)))*c2s*scn)
    c3=int(eval("n"+str((C3)))*c3n  + eval("n"+str((PC1)))*c3p*pcn + eval("n"+str((SC1)))*c3s*scn)
    dd1 =d1 -min(d1,d2,d3)
    dd2 =d2 -min(d1,d2,d3)
    dd3 =d3 -min(d1,d2,d3)
    cc1 =c1 -min(c1,c2,c3)
    cc2 =c2 -min(c1,c2,c3)
    cc3 =c3 -min(c1,c2,c3)
    res =''
    #Z2 =int((dd1+dd2+dd3+cc1+cc2+cc3)/30)+zlmt((dd1+dd2+dd3+cc1+cc2+cc3)%30/30)
    if d1n==0 and d2n==0 and d3n==0 and c1n==0 and c2n==0 and c3n==0 and pdn==0 and pcn==0:
      PRF +=OUT2-INV2
      DC103(200)
    elif OUT2-INV2 >=1 and count2 >1 :
      PRF +=OUT2-INV2
      DC103(200)
    elif (OUT2-INV2 < 0 or n!=100) and (count2 >1):
      if dd1>0: print("Done - "+color.BOLD +str(dd1)+color.END )
      else:print("Done - ")
      print()
      if dd2>0:print("Dtwo - "+color.RED +str(dd2)+color.END )
      else:print("Dtwo - ")
      print()
      if dd3>0:print("D3tre - "+color.BOLD +str(dd3)+color.END)
      else:print("Dtre - ")
      print()
      res +="   Cone - "+color.RED +str(cc1)+color.END if cc1>0 else "   Cone - "
      res +=" ,Ctwo - "+color.BOLD +str(cc2)+color.END if cc2>0 else " ,Ctwo - "
      res +=" ,Ctre - "+color.RED +str(cc3)+color.END if cc3>0 else " ,Ctre - "
      print(res)
      #print("Zero- "+str(Z2))
      print(color.RED +str(int(OUT2-INV2))+color.END)
