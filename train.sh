# init config with zh(chinese)
rm ./content -rf
rm ./corpus -rf
 python -m spacy init config --lang zh --pipeline ner ./content/ner_demo/configs/config.cfg --force
 # convert chinses corpus from json to .spacy
 mkdir corpus
 python scripts/convert.py zh assets/train.json corpus/train.spacy
 python scripts/convert.py zh assets/dev.json corpus/dev.spacy
 
 # copy to a running directory setting by user
 mkdir ./content/ner_demo/corpus
 mkdir ./content/ner_demo/training
 cp corpus/train.spacy ./content/ner_demo/corpus/ -rf
 cp corpus/dev.spacy ./content/ner_demo/corpus/ -rf
 
 # start training chinese corpus
 sleep 2
 echo "start training"
 python -m spacy train ./content/ner_demo/configs/config.cfg --output ./content/ner_demo/training/ --paths.train ./content/ner_demo/corpus/train.spacy --paths.dev ./content/ner_demo/corpus/dev.spacy --training.eval_frequency 20 --training.max_steps 300
sleep 3

echo "start inference"
python infchn.py
