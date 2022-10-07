def getFunction():
    ConvFunc = Func.replace ('x','float(x)')
    FuncPY = open("func.py",'r+')
    FuncPY.truncate()
    FuncPY.write("""def function(x):
    y="""+ConvFunc+"""
    return(y)""")
    FuncPY.close()

def TableLayout():
    FCurNum = (format(CurNum,'.17g'))
    FFxVal = (format(FxVal,'.17g'))
    FCenDiff = (format(CenDiff,'.17g'))
    FNewIter = (format(NewIter,'.17g'))
    LENX = 24 -len(FCurNum)
    LENFX= 24 -len(FFxVal)
    LENDiff= 24 -len(FCenDiff)
    LENNew= 24 -len(FNewIter)
    
    print("|"+str(FCurNum)+" "*LENX+"|"+str(FFxVal)+" "*LENFX+"|"+str(FCenDiff)+" "*LENDiff+"|"+str(FNewIter)+" "*LENNew+"|")

CurNum = int(input("Enter first value ---> "))
Func = str(input("""Input function e.g.(x**(1/2) + x**2 + 3*(x)+ 12) ---> """))
Iter = int(input("How many iterations would you like me to perform? ---> "))
OutAll = str(input("Do you want to output in a table format? ---> "))
getFunction()
if OutAll == "yes":
    print("""|	X Values         |      F(X) Values 	  |     dy/dx Value 	   |   NewtonRaphson Value  |
|------------------------|------------------------|------------------------|------------------------|""")
import func
rappo = []
for i in range(1, Iter):
    try:   
        FxVal = func.function(CurNum)
        FxFwrVal = func.function(CurNum+0.0000000001)
        FxBacVal = func.function(CurNum-0.0000000001)
        CenDiff = (FxFwrVal-FxBacVal)/(0.0000000002)
        NewIter = CurNum - FxVal/CenDiff
        if OutAll == "yes":
            TableLayout()
        CurNum = NewIter
        rappo.append(FxVal)
    except:
        print("Overflow Error")

