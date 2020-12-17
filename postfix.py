#!/usr/bin/python
def eval_expr (string, d={}):
    zoz=[]
    zoz0=string.split()
    for i in zoz0:
        try:
            b=int(i)
        except ValueError:
            if i in d:
                b=d[i]
            else: 
                druhe=zoz.pop()
                prve=zoz.pop()
            if i=="+":
                b=prve + druhe
            elif i=="*":
                b=prve * druhe
            elif i=="/":
                b=prve // druhe
            elif i=="-":
                b=prve - druhe
        zoz.append(b)
    return(zoz[0])
    
    
def znamienko (char):
    if char=="+" or char=="-" or char=="*" or char=="/" or char=="(":
        return 1
    else:
        return 0
    
def to_infix (string):
    zoz=[]
    z=string.split()
    for i in z:
        if znamienko(i)==0:
            zoz.append(i)
        else:
            druhe=zoz.pop()
            prve=zoz.pop()
            s=""
            s+="( "
            s+=prve
            s+=" "
            s+=i
            s+=" "
            s+=druhe
            s+=" )"
            zoz.append(s)
    return (zoz[0])

def to_postfix (string):
    zoz=[]
    postfix=""
    z=string.split()
    for i in z:
        if znamienko(i)==1:
            zoz.append(i)                   #zisti, ci ide o znamienko alebo "(" a prida do zoznamu znamienok
            #return(zoz)                      # kontrola zoznamu, podla vsetkeho don zapisuje spravne ale pri while sa tvari ako prazdny 
        else:
            if i==")":
                while zoz[-1] != "(":
                    postfix+=zoz.pop()      #mal by zapisat vsetky znamienka ktore boli medzi zatvorkami v opacnom poradi (teda v spravnom pre postfix)
                    postfix+=" "
                zoz.pop()                   #mal by odstranit "("
            else:
                postfix+=i                  #zapisuje cisla (a premenne)
                postfix+=" "
    return(postfix)
            
        
