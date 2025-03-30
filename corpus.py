import string
import nltk

"""This function accepts the name of the file to be used for training
and calls on the tokenize function to create a list of list of strings."""
def read_file(filename):
    tok_seq=[]
    f1=open(filename,'r')
    line=f1.readline()
    while line!='':
        tok_seq.append(tokenize(line))
        line=f1.readline()
    f1.close()
    return tok_seq

"""This function accepts a string of text and returns a list of strings."""
def tokenize(text):
    tokens=nltk.word_tokenize(text.lower())
    return tokens
            

"""This function detokenizes the text and generates a string 
with correct spacing and capitalization."""
def detokenize(tokens):
    generated_string=''         
    for i in range(len(tokens)):
        if tokens[i]!=None:
            #This checks if the current token is the first word 
            #in the sentence or the pronoun 'I' and capitalizes it.
            if generated_string=='':
                tokens[i]=tokens[i].capitalize()
                generated_string+=tokens[i]
            
            #This checks if the current token is the pronoun 'I'
            #and capitalizes it.
            elif tokens[i]=='i':
                tokens[i]=tokens[i].capitalize()
                generated_string+=' '+tokens[i]

            #This checks if the previous token is an ending punctuation
            #and capitalizes the current token accordingly.
            elif tokens[i-1] in {'.','!','?'}:
                tokens[i]=tokens[i].capitalize()
                generated_string+=' '+tokens[i]

            #This checks if the current token is a punctuation
            #and attaches it to the string without spacing.
            elif tokens[i] in string.punctuation:
                generated_string+=tokens[i]
        
            #This checks if the current token is part of a contraction
            #and attaches it to the string without spacing.
            elif tokens[i][0]=="'" and tokens[i][-1]!="'":
                generated_string+=tokens[i]

            else:
                generated_string+=' '+tokens[i]

    return generated_string