The main folder for the project code, where images, metadata and feature extraction information is stored.

Our annotation guide can be found in the documents folder.

----------
HOW TO RUN:

Download a local copy of the entire folder structure, and place any pictures and masks in .\data\images\imgs_part_1 and .\data\images\masks_part_1

Features will be saved to the features.csv in .\features   -> The current data extraction from 1082 images is saved in the features.csv currently present there.

Run all code in 01_feature_extraction.ipynb to get the features extracted and saved to the csv

Run all code in 02_train_classifiers.ipynb to get a new pickled classifier, currently set to KNearestNeighbor(5).

To evaluate the classifier, run 03_evaluate_classifier.ipynb. You have to set a new csv_path to new evaluation data in the second box to get the probabilities.


----------

REQUIRED PACKAGES:
numpy
PIL
cv2
matplotlib.pyplot
skimage
pandas
sklearn
