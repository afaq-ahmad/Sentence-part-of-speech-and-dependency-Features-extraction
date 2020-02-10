# Sentence-part-of-speech-and-dependency-Features-extraction
The code will take input of text files and find the Sentence part of speech and dependency Features extraction and save them in the csv file.

### 1.Make directory in which we can place our code and files:
    mkdir corpus

### 2. Installing packages:
    sudo apt install python3-pip 
    pip3 install -U spacy
    python3 -m spacy download en_core_web_sm
    pip3 install pandas

### 3. Running the code:
    Place the code and input text file in corpus directory.
    Python3 code.py input_text_file
    python3 code.py sample_sentenses.txt
		
### 4. Details about the outputs text features in csv:

	
LABEL | DESCRIPTION
:--- | :---
acl	|clausal modifier of noun (adjectival clause)
acomp|	adjectival complement
advcl|	adverbial clause modifier
advmod|	adverbial modifier
agent|	agent
amod|	adjectival modifier
appos|	appositional modifier
attr|	attribute
aux|	auxiliary
auxpass|	auxiliary (passive)
case|	case marking
cc|	coordinating conjunction
ccomp|	clausal complement
compound|	compound
conj|	conjunct
cop|	copula
csubj|	clausal subject
csubjpass|	clausal subject (passive)
dative|	dative
dep|	unclassified dependent
det|	determiner
dobj|	direct object
expl|	expletive
intj|	interjection
mark|	marker
meta|	meta modifier
neg|	negation modifier
nn|	noun compound modifier
nounmod|	modifier of nominal
npmod|	noun phrase as adverbial modifier
nsubj|	nominal subject
nsubjpass|	nominal subject (passive)
nummod|	numeric modifier
oprd|	object predicate
obj|	object
obl|	oblique nominal
parataxis|	parataxis
pcomp|	complement of preposition
pobj|	object of preposition
poss|	possession modifier
preconj|	pre-correlative conjunction
prep|	prepositional modifier
prt|	particle
punct|	punctuation
quantmod|	modifier of quantifier
relcl|	relative clause modifier
root|	root
xcomp|	open clausal complement
