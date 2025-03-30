from lm import *

"""global variables"""
lm=None
tok_seq=[]
option_n=0


"""This function asks for a file name from user to train model on
and then calls on the relevant functions."""
def train_model():
    trainingtext=input("Enter file name to train model on: ")
    token_sequences=read_file(trainingtext)
    lm.train(token_sequences)


"""The main code has been divided into three menu screens.
This function displays the first menu screen to user."""
def menu_1():
    option_n=input(
        """What would you like to do?
            1. Create n-gram model with n specified by you 
            2. Exit program
            Enter a number (1-2):  """)
    
    if option_n=='1':
        #This creates a new language model with a user-specified n.
        global lm
        ngram_n=input("Enter n for language model: ")
        while not ngram_n.isnumeric():
            print("Please enter a valid integer.")
            ngram_n=input("Enter n for language model: ")
        while ngram_n=='0':
            print("Cannot create n-gram model with this, please try again")
            ngram_n=input("Enter n for language model: ")
        lm=LanguageModel(int(ngram_n))
        menu_2()
    
    elif option_n=='2':
        #This exits the program.
        exit()
    
    else:
        print("Invalid input, please try again")
        menu_1()


"""This function displays the second menu screen to user."""
def menu_2():
    option_n=input(
        """What would you like to do?
            1. Train n-gram model 
            2. Go back to previous menu
            3. Exit program
            Enter a number (1-3): """)
    
    if option_n=='1':
        #This loads texts from a given file, 
        #and trains the language model on those texts.
        train_model()
        menu_3()
    
    elif option_n=='2':
        #This returns to the previous menu screen.
        menu_1()

    elif option_n=='3':
        exit()

    else:
        print("Invalid input, please try again")
        menu_2()


"""This function displays the third menu screen to user."""
def menu_3():
    continue_var='y'
    #This segment of code loops the third menu until user wants to do 
    #something else such as go back to previous menu or exit program.
    while continue_var=='y':
        option_n=input(
            """What would you like to do?
                1. Generate text and print to screen
                2. Generate multiple texts and write to file
                3. Go back to previous menu
                4. Exit program
                Enter a number (1-4): """)

        if option_n=='1':
            #This generates a text from the language model
            #and prints it to the screen
            print(lm.generate(),'\n')

        elif option_n=='2':
            text_n=''
            #This generates a user-specified number of texts from the 
            #language model, and writes them to a file.s
            text_n=input("Enter number of texts to be generated: ")
            while not text_n.isnumeric():
                print("Please enter a valid integer.")
                text_n=input("Enter number of texts to be generated: ")

            genfile=input("Enter new file name: ")
            f2=open(genfile,'w')
            for i in range(int(text_n)):
                string=lm.generate()+'\n'
                f2.write(string)
            f2.close()
    
        elif option_n=='3':
            #This returns to the previous menu screen.
            menu_2()

        elif option_n=='4':
            #This exits the program
            continue_var='n'
            exit()

        else:
            print("Invalid input, please try again")
            menu_3()


"""This is the start of the program, which displays the first menu."""
menu_1()