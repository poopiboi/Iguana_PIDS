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
Our data set contains a total of 7 different skin lesions, abbreviated as BCC, SCC, ACK, SEK, BOD, MEL and NEV, whereas BOD and SCC are combined as SCC. 

###Basal Cell Carcinoma (BCC):
        Appearance: Often appears as a pearly or waxy bump, sometimes with visible blood vessels.
        Diagnosis: Typically diagnosed through a skin biopsy.

###Melanoma (MEL):
        Appearance: Usually presents as a new mole or a change in an existing mole. The ABCDE rule (Asymmetry, Border irregularity, Color variation, Diameter larger than a pencil eraser,            Evolution or change) is often used for early detection.
        Diagnosis: A biopsy is performed to confirm melanoma.

###Squamous Cell Carcinoma (SCC):
        Appearance: Often appears as a firm, red nodule or a flat sore with a scaly crust.
        Diagnosis: Confirmed through a skin biopsy.

###Actinic Keratosis (ACK):
        Characteristics: Actinic keratosis is a precancerous growth on the skin that appears as rough, scaly patches. These patches are usually caused by sun exposure and may vary in color,         such as red, pink, or flesh-toned.
        Diagnosis: Dermatologists typically diagnose actinic keratosis through a visual examination. In some cases, a biopsy may be performed to confirm the diagnosis.

###Seborrheic Keratosis (SEK):
        Characteristics: Seborrheic keratosis is a non-cancerous (benign) skin tumor that originates from cells called keratinocytes. It usually appears as waxy, scaly, or crusty growths            that can vary in color, including tan, black, or brown. They have a stuck-on appearance.
        Diagnosis: Seborrheic keratosis is usually diagnosed based on its appearance during a physical examination. In some cases, a biopsy may be performed to rule out other skin                   conditions.

###Nevus (NEV):
        Characteristics: Nevus, commonly known as a mole, is a benign growth on the skin. Moles can vary in color, size, and shape. Most moles are harmless, but changes in size, shape, or           color may warrant medical attention.
        Diagnosis: Diagnosis is typically based on visual examination. If there are concerns about the mole's characteristics, a dermatologist may recommend a biopsy for further evaluation.
  

## Data collection 
Since the dataset is compiled using smartphone cameras, it inherently provides less detailed images of skin lesions compared to dermoscopic images. Moreover, factors like camera resolution and lighting conditions further impact image quality. The dataset has already been filtered by the creators based on certain criteria during the quality selection process. This includes eliminating images with very poor resolution where lesions are unidentifiable, instances where patients could be identified (e.g., due to tattoos), and cases where lesions are entirely obscured by hair or ink markings.

However, during our process of creating masks, we encountered additional low-quality images, which we omitted. Furthermore, some pictures lacked sufficient clarity for us to accurately pinpoint the location of the lesion, leading us to skip those images as well.

## Skin canecr
Skin cancer is one of the most common types of cancer in the world. Over the past few years, different approaches have been proposed to deal with automated skin cancer detection. sun uv impact, 

## References
https://www.sciencedirect.com/science/article/pii/S235234092031115X
https://www.sciencedirect.com/science/article/pii/S0010482519304019?via%3Dihub





## 
