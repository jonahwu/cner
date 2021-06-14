rm ./data/*
echo "start to download data"
python lawdisk.py
echo "convert to sentence"
python tokeysentence.py
echo "formating for training data input"
python gt.py
echo "copy necessary data to Train Directory"
cp assets/*.json ../assets/.
cp assets/*.txt ../assets/.
echo "go to trainning directory"
cd ../
echo "start trainning"
bash train.sh

