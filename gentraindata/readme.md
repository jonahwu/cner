# read me

## Todo List

quick and dirty as first priority 

1. one button process (combine each individual process from internet parser to extract keyword and formating and training and to test and output)
2. traditional chinese to simple chinese


## Processes

```
## get keyword information from internet

python lawdisk.py
## data store to ./data


## ./data to individual sentence
python tokeysentence.py
output to keytosentence.txt



## edit keywords in gt.py
python gt.py
#output to 
assets/train.json
assets/dev.json
#move assets/* to Custom_CHN_NER_Spacy3/assets




# into trainning and make sure assets folder has been updated to newest version
Custom_CHN_NER_Spacy3
cp ../gentraindata/assets/* assets/.
assets/train.json
assets/dev.json

## execute training
train.sh

## check result
...






```


