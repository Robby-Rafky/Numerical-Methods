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
    FFPIter = (format(FPIter,'.17g'))
    FFPX = (format(CurX,'.17g'))
    LENX = 24 -len(FCurNum)
    LENFX= 24 -len(FFxVal)
    LENFPIter= 24 -len(FFPIter)
    LENFPX= 24 -len(FFPX)
    
    print("|"+str(FCurNum)+" "*LENX+"|"+str(FFxVal)+" "*LENFX+"|"+str(FFPIter)+" "*LENFPIter+"|"+str(FFPX)+" "*LENFPX+"|")

CurNum = int(input("Enter first value ---> "))
Func = str(input("Input function e.g.(x**(1/2) + x**2 + 3*(x)+ 12) ---> "))
Iter = int(input("How many iterations would you like me to perform? ---> "))
OutAll = str(input("Do you want to output in a table format? ---> "))
Arrange= str(input("What arrangement do you want? (A => +1,*x)(B => +x)(C => +x**2,/x) --->"))
CurX = CurNum
getFunction()
if OutAll == "yes":
    print("""|	X Values         |      F(X) Values 	  | Iterated current value |    Iterated X value    |
|------------------------|------------------------|------------------------|------------------------|""")
import func
iterate = []
for i in range(1, int(Iter/2)):
    try:
        FxVal = func.function(CurNum)
        if Arrange == "B":
            FPIter = FxVal + CurNum
        elif Arrange == "A":
            FPIter = (FxVal + 1)*CurNum
        elif Arrange == "C":
            FPIter = (FxVal + CurNum**2)/CurNum
        else:
            print("You must enter A,B or C for your chosen arrangement, restart")
        if OutAll == "yes":
            TableLayout()
        CurNum = FPIter
        FxVal = func.function(CurNum)
        if Arrange == "B":
            FPIter = FxVal + CurNum
        elif Arrange == "A":
            FPIter = (FxVal + 1)*CurNum
        elif Arrange == "C":
            FPIter = (FxVal + CurNum**2)/CurNum
        else:
            print("You must enter A,B or C for your chosen arrangement, restart")
        CurX = FPIter
        if OutAll == "yes":
            TableLayout()
        CurNum = FPIter
        iterate.append(FPIter)
    except:
        print("OverFlow Error")

