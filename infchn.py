
import spacy

nlp1 = spacy.load(R"./content/ner_demo/training/model-best") #load the best model
doc = nlp1("这是什么鬼三小啦") # input sample tex
print([(ent.text, ent.label_) for ent in doc.ents])
doc = nlp1("这是什么鬼三小拉拉事情啦") # input sample tex
print([(ent.text, ent.label_) for ent in doc.ents])
doc1 = nlp1("我是真的恋爱了") # input sample tex
print([(ent.text, ent.label_) for ent in doc1.ents])
doc1 = nlp1("我想永无止境的恋爱") # input sample tex
print([(ent.text, ent.label_) for ent in doc1.ents])
doc1 = nlp1("恋爱") # input sample tex
print([(ent.text, ent.label_) for ent in doc1.ents])
doc1 = nlp1("我不想只是恋爱而已") # input sample tex
print([(ent.text, ent.label_) for ent in doc1.ents])
