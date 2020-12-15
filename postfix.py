#!/usr/bin/python
def eval_expr (string):
    zoz=[]
    zoz0=string.split()
    for i in zoz0:
        try:
            b=int(i)
        except ValueError:
            druhe=zoz.pop()
            prve=zoz.pop()
            if i=="+":
                b=prve + druhe
            elif i=="*":
                b=prve * druhe
            elif i=="/":
                b=prve / druhe
            elif i=="-":
                b=prve - druhe
        zoz.append(b)
    print(zoz[0])
