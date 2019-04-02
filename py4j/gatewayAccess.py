from py4j.java_gateway import JavaGateway, GatewayParameters
import os,sys
gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25375))                   # connect to the JVM on port
JavaCalc = gateway.entry_point     # get the javacalc instance

aSEA = False#already shown error
aSES = False

cls = lambda: os.system('cls')

def mainMenu():
    while True:
        print("╠═════════╦═════════════════════════╦══════╗")
        print("║         ║Python to Java Calculator║      ║")
        print("║         ╚═════════════════════════╝      ║")
        print("║Select Your Operation                     ║")
        print("╠═══╦═════════════╗                        ║")
        print("║ 1 ║ Addition    ║                        ║")
        print("║ 2 ║ Subtraction ║                        ║")
        print("║                                          ║")
        print("║                                          ║")
        print("╚══════════════════════════════════════════╝")
        function = input("Operation: ")
        if function == "1" or function.lower() == "addition":
            addition()
        if function == "2" or function.lower() == "subtraction":
            subtraction()
        else:
            cls()
            firstNum = input("X: ")


#addition_app = gateway.entry_point               # get the AdditionApplication instance
#value = addition_app.addition(number1, number2) # call the addition method


def addition():
    global aSEA
    cls()
    if aSEA == False:
        cls()
    else:
        print("Invalid Entry! please use vaild characters")
    print("Function: Addition \n Example: 1 + 2 = 3")
    firstNum = input("X: ")
    secondNum = input("Y: ")
    try:
        if(isinstance(float(firstNum), float) and isinstance(float(secondNum), float)):
            sum = JavaCalc.addition(float(firstNum),float(secondNum))
            cls()
            print(firstNum, " + ", secondNum, " = ", sum)
            continueUsing = input("continue? (y/n): ")
            if continueUsing.lower() == "y":
                cls()
            else:
                cls()
                sys.exit()

        else:
            print("Invalid Entry! please use vaild characters")
            addition()
    except(ValueError):
        print("Invalid Entry! please use vaild characters")
        aSEA = True
        addition()
def subtraction():
    global aSES
    cls()
    if aSES == False:
        cls()
    else:
        print("Invalid Entry! please use vaild characters")
    print("Function: Subtraction \n Example: 10 - 5 = 5")
    firstNum = input("X: ")
    secondNum = input("Y: ")
    try:
        if(isinstance(float(firstNum), float) and isinstance(float(secondNum), float)):
            sum = JavaCalc.subtraction(float(firstNum),float(secondNum))
            cls()
            print(firstNum, " - ", secondNum, " = ", sum)
            continueUsing = input("continue? (y/n): ")
            if continueUsing.lower() == "y":
                cls()
            else:
                cls()
                sys.exit()

        else:
            print("Invalid Entry! please use vaild characters")
            addition()
    except(ValueError):
        print("Invalid Entry! please use vaild characters")
        aSES = True
        subtraction()


mainMenu()
