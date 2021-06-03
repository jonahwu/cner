
import spacy

nlp1 = spacy.load(R"./content/ner_demo/training/model-best") #load the best model
doc = nlp1("Who is Vijay??") # input sample tex
print([(ent.text, ent.label_) for ent in doc.ents])

doc1 = nlp1("Who is your dog??") # input sample tex
print([(ent.text, ent.label_) for ent in doc1.ents])

doc1 = nlp1("What is your dog??") # input sample tex
print([(ent.text, ent.label_) for ent in doc1.ents])

doc1 = nlp1("I like dog and cat??") # input sample tex
print([(ent.text, ent.label_) for ent in doc1.ents])

doc1 = nlp1("I like dog and cat??") # input sample tex
print([(ent.text, ent.label_) for ent in doc1.ents])



