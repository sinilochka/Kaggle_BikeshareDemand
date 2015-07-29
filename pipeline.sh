echo "Splitting data..."
python2.7 split_data.py train.csv sub_train.csv validate.csv

echo "Features Extraction..."
python2.7 features_extraction.py sub_train.csv sub_train_features.tsv
python2.7 features_extraction.py validate.csv validate_features.tsv
python2.7 features_extraction.py test.csv test_features.tsv

echo "Learning...."
python2.7 learn_and_predict.py sub_train_features.tsv validate_features.tsv >> validate_submission.csv
python2.7 compute_quality.py validate.csv validate_submission.csv

echo "Prediction..."
python2.7 learn_and_predict.py sub_train_features.tsv test_features.tsv >> submission.csv

echo "Done"
