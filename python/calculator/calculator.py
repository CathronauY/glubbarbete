import tkinter as tk

calculation = ""
def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)

def evaluateCalculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        textResult.delete(1.0, "end")
        textResult.insert(1.0, calculation)
    except:
        calculation = ""
        textResult.delete(1.0, "end")
        textResult.insert(1.0, "GLUBBS det må ha gått åt helvetet asså bröl")

def clearField():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")
root.title("Calculator")
root.resizable(False, False)
textResult = tk.Text(root, width=17, height=2, font=("Arial", 24))
textResult.grid(row=1, columnspan=5)

btn1 = tk.Button(root, text="1", command=lambda:addToCalculation(1), width=5, font=("Arial", 14))
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda:addToCalculation(2), width=5, font=("Arial", 14))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda:addToCalculation(3), width=5, font=("Arial", 14))
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda:addToCalculation(4), width=5, font=("Arial", 14))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda:addToCalculation(5), width=5, font=("Arial", 14))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda:addToCalculation(6), width=5, font=("Arial", 14))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda:addToCalculation(7), width=5, font=("Arial", 14))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda:addToCalculation(8), width=5, font=("Arial", 14))
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda:addToCalculation(9), width=5, font=("Arial", 14))
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda:addToCalculation(0), width=5, font=("Arial", 14))
btn0.grid(row=5, column=2)
btnleftP = tk.Button(root, text="(", command=lambda:addToCalculation("("), width=5, font=("Arial", 14))
btnleftP.grid(row=5, column=1)
btnRightP = tk.Button(root, text=")", command=lambda:addToCalculation(")"), width=5, font=("Arial", 14))
btnRightP.grid(row=5, column=3)
btnPlus = tk.Button(root, text="+", command=lambda:addToCalculation("+"), width=5, font=("Arial", 14))
btnPlus.grid(row=2, column=4)
btnMinus = tk.Button(root, text="-", command=lambda:addToCalculation("-"), width=5, font=("Arial", 14))
btnMinus.grid(row=3, column=4)
btnMulti = tk.Button(root, text="*", command=lambda:addToCalculation("*"), width=5, font=("Arial", 14))
btnMulti.grid(row=4, column=4)
btnDivide = tk.Button(root, text="/", command=lambda:addToCalculation("/"), width=5, font=("Arial", 14))
btnDivide.grid(row=5, column=4)
btnClear = tk.Button(root, text="C", command=lambda:clearField(), width=11, font=("Arial", 14))
btnClear.grid(row=6, columnspan=2, column=1)
btnEqualizer = tk.Button(root, text="=", command=evaluateCalculation, width=11, font=("Arial", 14))
btnEqualizer.grid(row=6, columnspan=2, column=3)
root.mainloop()
