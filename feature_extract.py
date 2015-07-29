from sys import argv
from utils.reader import Reader
from utils.features import FeatureExtractor, SimpleFeaturesExtractor



data_file = Reader(argv[1])
output_file = open(argv[2], 'w')

features_to_calc = [
    SimpleFeaturesExtractor,
]

for row in data_file.get_row():
    features = []
    features.append(row.datetime)
    features.append(row.count)

    for feature_to_calc in features_to_calc:
        if issubclass(feature_to_calc, FeatureExtractor):
            feature = feature_to_calc(row).compute()
            if isinstance(feature, list):
                features += feature
            else:
                features.append(feature)

    print >> output_file, "\t".join(map(str, features))
output_file.close()
