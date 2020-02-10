import sys
import spacy
import pandas as pd
try:
    nlp = spacy.load('en')
except:
    import en_core_web_sm
    nlp = en_core_web_sm.load()
with open(sys.argv[1],'r') as f:
  data=f.read().split('\n')

datass=[]

save_pd=pd.DataFrame([None]*len(data),columns=['sentence'])

for i in range(len(data)):
  sentece=data[i]
  doc=nlp(sentece)
  
  save_pd['sentence'][i]=sentece
  for tok in doc:
    if tok.pos_ not in save_pd.keys():
      save_pd[tok.pos_]=''
    if tok.dep_ not in save_pd.keys():
      save_pd[tok.dep_]=''

    save_pd[tok.pos_][i]=tok
    save_pd[tok.dep_][i]=tok
save_pd.to_csv('corpus_details.csv',index=False)
print('Resuls are saved in corpus_details.csv')