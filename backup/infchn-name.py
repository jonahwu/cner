
import spacy

nlp1 = spacy.load(R"./content/ner_demo/training/model-best") #load the best model
doc = nlp1("誰是秦始皇?") # input sample tex
print([(ent.text, ent.label_) for ent in doc.ents])


