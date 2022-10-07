def getFunction():
    ConvFunc = Func.replace ('x','float(x)')
    FuncPY = open("func.py",'r+')
    FuncPY.truncate()
    FuncPY.write("""def function(x):
    y="""+ConvFunc+"""
    return(y)""")
    FuncPY.close()

def TableLayout():
    FCurNum = (format(CurNum,'.13g'))
    FCurNum2 = (format(CurNum2,'.13g'))
    FFXCurNum = (format(FXCurNum,'.19g'))
    FFXCurNum2 = (format(FXCurNum2,'.19g'))
    FC = (format(BisecX,'.13g'))
    FFC = (format(BisecFX,'.19g'))
    LENX = 15 -len(FCurNum)
    LENX2= 15 -len(FCurNum2)
    LENFX= 26 -len(FFXCurNum)
    LENFX2= 26 -len(FFXCurNum2)
    LENC= 15 -len(FC)
    LENFC= 26 -len(FFC)
    print("|"+str(FCurNum)+" "*LENX+"|"+str(FCurNum2)+" "*LENX2+"|"+str(FFXCurNum)+" "*LENFX+"|"+str(FFXCurNum2)+" "*LENFX2+"|"+str(FC)+" "*LENC+"|"+str(FFC)+" "*LENFC+"|")

CurNum = int(input("Enter first value (A) ---> "))
CurNum2 = int(input("Enter second value (B) ---> "))
Func = input("""Input function e.g.(x**(1/2) + x**2 + 3*(x)+ 12) ---> """)
Iter = int(input("How many iterations would you like me to perform? ---> "))
OutAll = str(input("Do you want to output in a table format? ---> "))
getFunction()
if OutAll == "yes":
    print("""|       A       |       B       |            F(A)          |           F(B)           |       C       |           F(C)           |
|---------------|---------------|--------------------------|--------------------------|---------------|--------------------------|""")
import func
bisec = []
while Iter > 0:
    Iter -= 1
    FXCurNum = float(func.function(CurNum))
    FXCurNum2 = float(func.function(CurNum2))
    BisecX = float((CurNum + CurNum2)*(0.5))
    BisecFX = float(func.function(BisecX))
    if OutAll == "yes":
        TableLayout()
    if FXCurNum > 0 and FXCurNum2 < 0:
        if BisecFX < 0:
            CurNum2 = BisecX
        elif BisecFX > 0:
            CurNum = BisecX
    elif FXCurNum < 0 and FXCurNum2 > 0:
        if BisecFX > 0:
            CurNum2 = BisecX
        elif BisecFX < 0:
            CurNum = BisecX
    bisec.append(BisecFX)
           
   
