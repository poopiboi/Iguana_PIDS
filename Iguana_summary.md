# Iguana Group - Midway Summary

## What is our data set? (PAD-UFES-20: a skin lesion dataset composed of patient data and clinical images collected from smartphones: https://data.mendeley.com/datasets/zr7vgbcyr2/1)

The dataset we are currently working was collected during 2018 and 2019 and there are 50 types of skin lesions that were collected during this period. Due to rarity, the dataselection was boiled down to the six most common skin lesions diagnosed at PAD: Basal Cell Carcinoma(BCC), Squamous Cell Carcinoma and Bowens disease (SCC), Artinic Keratosis (ACK), Seborrheic Keratosis (SEK), Melanoma (MEL) and Nevus (NEV). 

The six types of skin lesions can be categorized as skin cancer or skin disease:
BCC, MEL and SCC are considered to be skin cancers, whereas ACK, NEV and SEK are skin diseases. 

All the samples diagnosed as skin cancer are proved by biopsy.


## Metadata from data set
As part of the data set, a metadata .csv-file was provided. This metadata has information on the patient in each picture, with a range of additional factors, such as previous cancer history, access to water, the diameter of the lesion and a number of True/False statements regarding the lesion(Does it hurt, does it bleed, etc.)
This metadata could potentially be used alongside our masks and annotations to see if results in image recognition could match certain parameters.


## Skin lesions
Our data set contains a total of 7 different skin lesions, abbreviated as BCC, SCC, ACK, SEK, BOD, MEL and NEV. 

## Data collection 
Since the dataset is compiled using smartphone cameras, it inherently provides less detailed images of skin lesions compared to dermoscopic images. Moreover, factors like camera resolution and lighting conditions further impact image quality. The dataset has already been filtered by the creators based on certain criteria during the quality selection process. This includes eliminating images with very poor resolution where lesions are unidentifiable, instances where patients could be identified (e.g., due to tattoos), and cases where lesions are entirely obscured by hair or ink markings.

However, during our process of creating masks, we encountered additional low-quality images, which we omitted. Furthermore, some pictures lacked sufficient clarity for us to accurately pinpoint the location of the lesion, leading us to skip those images as well.

## Skin canecr
Skin cancer is one of the most common types of cancer in the world. Over the past few years, different approaches have been proposed to deal with automated skin cancer detection. sun uv impact, 

## References
https://www.sciencedirect.com/science/article/pii/S235234092031115X
https://www.sciencedirect.com/science/article/pii/S0010482519304019?via%3Dihub





## 
