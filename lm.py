from corpus import *
import random

"""This class trains the language model and generates text."""
class LanguageModel:
    def __init__(self, n):
        self.n=n
        self.tokendict={}
        self.vocab={}

    """This method creates an n-gram for a given sequence of tokens."""
    def create_ngrams(self,sequence,m):
        ngram_list=[]
        while len(sequence)>=m:
            ngram_list.append(tuple(sequence[:m]))
            sequence=sequence[1:]
        return ngram_list
    
    """This method calculates the frequency of each token in the text
    and documents it in self.vocab."""
    def token_frequency(self,sequence):
        for token in sequence:
            if token in self.vocab:
                self.vocab[token]+=1
            else:
                self.vocab[token]=1

    """This method trains the model."""
    def train(self, token_sequences):
        for seq in token_sequences:
            temp=seq.copy()
            
            #This segment of code is for the unigram case.
            if self.n==1:        
                #The sequence is padded with None.
                temp.insert(0,None)
                temp.append(None)
                self.token_frequency(temp)

            #This segment of code is for all cases other than unigram.
            else:
                #The sequence is padded with None.
                for i in range(self.n-1):
                    temp.insert(0,None)
                    temp.append(None)
                self.token_frequency(temp)
                nglist=self.create_ngrams(temp,self.n)
                #Each n-gram is added to self.tokendict
                #and its frequency is documented.
                for ngram in nglist:
                    if ngram[:-1] in self.tokendict:
                        if ngram[-1] in self.tokendict[ngram[:-1]]:
                            self.tokendict[ngram[:-1]][ngram[-1]]+=1
                        else:
                            self.tokendict[ngram[:-1]][ngram[-1]]=1
                    else:
                        self.tokendict[ngram[:-1]]={ngram[-1]:1}

        return self.tokendict
    
    """This method calculates the next probable token 
    given a sequence of tokens."""
    def p_next(self, tokens):
        ngram_count=0
        probability_dict={}
        temp=tokens.copy()  #stores a copy of the sequence in another variable

        #This segment of code is for the unigram case.
        if self.n==1:
            for gen_word in self.vocab:
                probability_dict[gen_word]=self.vocab[gen_word]/len(self.vocab)

        #This segment of code is for all cases other than unigram.
        else:
            #The n-1 tokens sequence is padded with None.
            for i in range(self.n-1):
                temp.insert(0,None)
            tokenlist=self.create_ngrams(temp,self.n-1)
            ngram=tokenlist[-1]

            #This segment of code checks the existence of the above n-gramr
            #(n-1 tokens) against self.tokendict and
            #calculates conditional probability of the token given the n-gram
            if ngram in self.tokendict:
                for i in self.tokendict[ngram]:
                    ngram_count+=self.tokendict[ngram][i]
                for i in self.tokendict[ngram]:
                    probability_dict[i]=self.tokendict[ngram][i]/ngram_count
        return probability_dict
    
    """This method generates a random text (sequence of tokens)
    based on the calculated probabilities."""
    def generate(self):
        generated_list=[]    #Stores words generated so far
        generated_string=''  #Stores final string to be returned
        gen_word=''          #Stores newly-generated word
        while gen_word!=None:
            wordlist=self.p_next(generated_list)
            #This picks a random gen_word from the calculated 
            #probability distribution of p_next token
            gen_word=random.choices(list(wordlist.keys())
                                    ,weights=tuple(wordlist.values()),k=1)[0]
            #This creates a list of tokens.
            generated_list.append(gen_word)
        generated_string=detokenize(generated_list)
        return generated_string