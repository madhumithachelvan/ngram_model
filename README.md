# N-Gram Model Project

The aim of the project was to design, implement, and document an n-gram language model in Python. There are three modules in this project: corpus.py, lm.py and main.py.

1.	corpus.py
This has three functions. read_file accepts the name of the file and reads the text, and calls the tokenize function to tokenize each line of text to a list. It returns a list of list of strings. tokenize accepts a string and tokenizes it using the word_tokenize function from the NLTK module.

detokenize(text) accepts a list of tokens and converts it into a string. This function also takes care of capitalization and punctuation. There are several cases listed; some check for punctuation and contractions (word starts with an apostrophe) so that they can be joined to the string with no spacing. Other cases check whether the word is at the beginning of the sentence or if it is the pronoun ‘I’ and capitalized accordingly.

2.	lm.py
This consists only of a class named LanguageModel, which has 5 methods other than __init__ within it.
The init method initializes three variables – integer n for the number accepted from the user, dictionary tokendict which stores the n-grams and their frequencies, and dictionary vocab which stores all the terms in the text and their frequencies.

The create_ngrams method creates a list of n-grams from a given sequence of tokens. The token_frequency method calculates the frequencies of each token and stores it in a dictionary. Both of these methods were created to organize the code better and make it look cleaner.

The train method accepts a list of sequences of tokens, pads each sequence with n-1 None tokens, creates n-grams from them and finally stores them in tokendict. Both unigram models and models with n>1 are accounted for in this method, in two separate cases (marked by an if-else statement). This is because the n-grams used differs with each case. With a unigram model, the n-grams used are equivalent to the terms stored in vocab, as each n-gram has only one word/term in it. The probabilities of each word are independent of the words occurring before it in the text. Therefore, this method and the other methods utilise only the dictionary vocab for the unigram model. On the other hand, the models with n>1 are stored differently in tokendict. It is a nested dictionary, with the (n-1) tokens in each n-gram making up the outer keys, and the words following these (n-1) tokens make up the inner keys.

The p_next method accepts a sequence of tokens and generates a dictionary containing all possible tokens that can come next, along with their probabilities. Here too, there are two cases for the unigram model and models with n>1, where the former uses the dictionary vocab, and the latter uses the dictionary tokendict. A copy of this sequence of tokens is stored in a variable temp so that the original sequence is not altered, and temp is padded with None tokens according to the given n. N-grams are created from this padded sequence and compared against tokendict, and if it matches, calculates their probabilities. The probability distribution is calculated within this method itself.

The generate method generates words based on the p_next function. It starts with an empty list named generated_list, which, when passed to p_next, gets padded with None tokens. This is used to create n-grams and their respective probability distributions, and generate the first token based on the last n-gram. This token is added to generated_list, which is passed to p_next, and the process repeats until the token generated is None. Each time, the probability distribution is stored in a dictionary wordlist. From each probability distribution, the generated token is chosen using the choices() function from the random module, wherein the list of words is the keys to wordlist, and the weights are the values to wordlist.

The complete generated_list is converted to a readable string with correct punctuation, capitalization and spacing using the detokenize function.

DOCUMENTATION:
The main code is divided into three menu screens:
1.	for creating an n-gram model
2.	for training the n-gram model
3.	for generating texts, and gives options to print to screen or to a file.

This was constructed such that the user can exit the program or go back to the previous screen without difficulty. These commands were also separated so that the user cannot ever generate text without training their language model at least once, as these screens are presented to the user in a certain order.

The first menu screen allows the user to choose between creating an n-gram model or exiting the program. If they choose the first option, they are prompted to input an ‘n’ number for the n-gram model. The second menu screen allows the user to choose between training the n-gram model, going back to the previous menu screen, and exiting. Choosing the first option prompts the user to input a file name, which is then used to train the model. The third menu screen allows the user to choose between generating text and printing to screen, generating text and printing to a file (which then prompts the user for number of texts to be generated and a file name), going back to the previous menu screen, and exiting. This third screen is displayed repeatedly until the user chooses to exit the program or go back to the previous menu. 

On each menu screen, the possible actions are displayed in a numbered list, and the user simply has to input a number based on that list. If the user gives a different input, an error message is displayed, followed by a display of the same menu screen.


EXTENSIONS:

The detokenize function in the corpus module accounts for spacing and punctuation, as well as for the capitalization of sentence-start words and the pronoun ‘I’. This is seen in the generated text.
