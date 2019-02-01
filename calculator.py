from tkinter import*
def iCalc(source , side):
    storeobj= Frame(source, borderwidth=4, bd=4, bg="light green")
    storeobj.pack(side=side, expand=YES, fill=BOTH)
    return storeobj
def button(source, side, text, command = None):
    storeobj=Button(source, text=text, command=command)
    storeobj.pack(side=side, expand=YES, fill=BOTH)
    return storeobj
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('calculator')


        display = StringVar()
        Entry(self, relief= RIDGE,
              textvariable=display, justify='right', bd=30, bg="orange").pack(side=TOP, expand=YES,
                    fill=BOTH)


        for clearBut in (["CE"],["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))

        for NumBut in ("789/%" , "456*#" , "123-@", "0.+!"):
            FunctionNum = iCalc(self, TOP)
            for iEquals in NumBut:
                button(FunctionNum, LEFT, iEquals,
                        lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q))
        EqualsButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualsButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>',
                                lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualsButton, LEFT, iEquals,
                    lambda storeObj=display, s=' %s '%iEquals: storeObj.set(storeObj.get()+s))


    def calc(self,display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")
             
if __name__ == '__main__':
    app().mainloop()        
