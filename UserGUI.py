from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
from Document import Document
from DocumentStream import DocumentStream
from Sentence import Sentence
from DocumentStreamError import DocumentStreamError
from CommandLinePlotter import CommandLinePlotter
from BasicStats import BasicStats
from MatPlotPloter import MatPlotPloter

class Ploter:
    '''
    from the web page, I learned how to use the graphic user interface in a abbreviated way. For example, how a button object
    and a input entry are connected. And the way the input are updated.
    We haven't mastered the usage of GUI, but I was introduced to the basic functionality of parameters and implementation of 
    graphing.
    '''

    def __init__(self, master):
        '''
        initialize the window of program with the buttons, labels and entries of inputs.
        '''
        self.master = master
        master.title("File Stats Plotter")

        self.total = 0
        self.entered_number = 0
        self.entered_filename = ''
    
        self.label = Label(master, text="File Stats Plotter")

        self.number_label = Label(master, text = 'TopN')
        self.filename_label = Label(master, text = 'Filename')
        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        okay = master.register(self.validate1)
        self.entry1 = Entry(master, validate='key', validatecommand=(okay, '%P'))

        self.generategraph_button = Button(master, text='Generate Graph', command = lambda:self.generate())


        self.label.grid(row=0, column=0, sticky=W)

        self.number_label.grid(row=1,columnspan = 1, sticky = W)
        self.filename_label.grid(row= 3, columnspan = 2, sticky = W)
        self.entry.grid(row =2, column=0, columnspan=1, sticky=W)
        
        
        self.entry1.grid(row =4,columnspan = 2, sticky = W)
        self.generategraph_button.grid(row=5, column=0,sticky = W+E)

    
    def validate(self, new_text):
        '''
        validate the legality of topn number input
        '''
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            print(self.entered_number)
            return True
        except ValueError:
            return False
    
    def validate1(self, new_text):
        '''
        test the validity of the filename inputed
        '''
        if not new_text: # the field is being cleared
            self.entered_filename = ''
            return True

        try:
            self.entered_filename = new_text
            print(self.entered_filename)
            return True
        except ValueError:
            return False
    
    def generate(self):
        '''
        generate the graph based on the filename and the topn inputed.
        '''
        print(self.entered_filename)
        file = Document(self.entered_filename)
        file.generateWhole()
        
        wordlist = file.wordlist
        worddict = BasicStats.createFreqMap(wordlist)
        n = self.entered_number
        topdict = BasicStats.topN(worddict,n)
        lista = [[],[]]
        for i in topdict:
            lista[0] += [i] #words
            lista[1] += [topdict[i]] #frequency
        print(lista)
        a = MatPlotPloter()
        a.scatterPlot(range(len(lista[1])), lista[1])

    
root = Tk()
my_gui = Ploter(root)
root.mainloop()
