# Iguana Group - Midway Summary

## What is our data set? (PAD-UFES-20: a skin lesion dataset composed of patient data and clinical images collected from smartphones: https://data.mendeley.com/datasets/zr7vgbcyr2/1)

The dataset we are currently working on was collected during 2018 and 2019 and there are 50 types of skin lesions that were collected during this period. Due to rarity, the dataselection was boiled down to the six most common skin lesions diagnosed at PAD: Basal Cell Carcinoma(BCC), Squamous Cell Carcinoma and Bowens disease (SCC), Artinic Keratosis (ACK), Seborrheic Keratosis (SEK), Melanoma (MEL) and Nevus (NEV). 

The six types of skin lesions can be categorized as skin cancer or skin disease:
BCC, MEL and SCC are considered to be skin cancers, whereas ACK, NEV and SEK are skin diseases. 

All the samples diagnosed as skin cancer are proved by biopsy.


## Metadata from data set
As part of the data set, a metadata .csv-file was provided. This metadata has information on the patient in each picture, with a range of additional factors, such as previous cancer history, access to water, the diameter of the lesion and a number of True/False statements regarding the lesion(Does it hurt, does it bleed, etc.)
This metadata could potentially be used alongside our masks and annotations to see if results in image recognition could match certain parameters.

## Skin lesions
Skin cancer is one of the most common types of cancer in the world and it occurs when skin cells are damaged, for example, by overexposure to ultraviolet radiation from the sun. The World Health Organization stated that one in every three cases where a person is diagnosed with cancer, it is a skin cancer. Over the past few decades, in countries like Australia, Canada or USA, the number of people diagnosed with skin cancer has been increasing at a constant rate. Over the past few years, different approaches have been proposed to deal with automated skin cancer detection.

Skin cancer can appear in a lot of different ways. There is no one way to describe how a skin cancer looks, because the symptoms can vary greatly. Some of them may include:

* itchy or painful spot
* sore that bleeds or develops a crust and is not healing 
* spot that you can feel that is scaly or red rough
* shiny bump on the top of the skin that is red or has the color of the skin 
* changes in the size, shape or color of an existing spot or a new spot on the skin
* change that looks like a scar without a well-defined border or a change that looks like a wart
* growth with a raised border and bleeding or central crust

## Types of skin cancer
# Basal cell carcinoma (BCC)
It usually (but not only) appears in areas with high sun exposure - on the neck, face, ears, arms or legs. Some pf the BCC sympotms are:
a reoccuring, not-healing or bleading sore
a patch on the skin that is rough, flat, or that looks like a scar
waxy or pearly bump on the skin

# Squamous cell carcinoma (SCC)
Similarly to BCC also usually appears in areas of high sun exposure. In some cases, especially the case for people with darker skin tones, it can also appear in different areas. Signs of SCC include:

skin lesion that are itchy or painful
a red or solid nodule
lesion with irregular borders that are crusty or scaly


## Melanoma (MEL) 
This type of cancer can appear anywhere on the body. It can develop out of some already existing moles. For  people with darker skin tones, MEL usually occurs on the soles or palms of their feet. Some of the symptoms may include:

appearance of dark lesions on the fingers and toes or the mucous membranes, like mouth, anus or vagina
changes in the appearance of a mole
growth of a brown, large spot, which often has irregular edges

### Basal Cell Carcinoma (BCC):
        Appearance: Often appears as a pearly or waxy bump, sometimes with visible blood vessels.
        Diagnosis: Typically diagnosed through a skin biopsy.

### Melanoma (MEL):
        Appearance: Usually presents as a new mole or a change in an existing mole. The ABCDE rule (Asymmetry, Border irregularity, Color variation, Diameter larger than a pencil eraser,            Evolution or change) is often used for early detection.
        Diagnosis: A biopsy is performed to confirm melanoma.

### Squamous Cell Carcinoma (SCC):
        Appearance: Often appears as a firm, red nodule or a flat sore with a scaly crust.
        Diagnosis: Confirmed through a skin biopsy.

### Actinic Keratosis (ACK):
        Characteristics: Actinic keratosis is a precancerous growth on the skin that appears as rough, scaly patches. These patches are usually caused by sun exposure and may vary in color,         such as red, pink, or flesh-toned.
        Diagnosis: Dermatologists typically diagnose actinic keratosis through a visual examination. In some cases, a biopsy may be performed to confirm the diagnosis.

### Seborrheic Keratosis (SEK):
        Characteristics: Seborrheic keratosis is a non-cancerous (benign) skin tumor that originates from cells called keratinocytes. It usually appears as waxy, scaly, or crusty growths            that can vary in color, including tan, black, or brown. They have a stuck-on appearance.
        Diagnosis: Seborrheic keratosis is usually diagnosed based on its appearance during a physical examination. In some cases, a biopsy may be performed to rule out other skin                   conditions.

### Nevus (NEV):
        Characteristics: Nevus, commonly known as a mole, is a benign growth on the skin. Moles can vary in color, size, and shape. Most moles are harmless, but changes in size, shape, or           color may warrant medical attention.
        Diagnosis: Diagnosis is typically based on visual examination. If there are concerns about the mole's characteristics, a dermatologist may recommend a biopsy for further evaluation.
  

## Data collection 
Since the dataset is compiled using smartphone cameras, it inherently provides less detailed images of skin lesions compared to dermoscopic images. Moreover, factors like camera resolution and lighting conditions further impact image quality. The dataset has already been filtered by the creators based on certain criteria during the quality selection process. This includes eliminating images with very poor resolution where lesions are unidentifiable, instances where patients could be identified (e.g., due to tattoos), and cases where lesions are entirely obscured by hair or ink markings.

However, during our process of creating masks, we encountered additional low-quality images, which we omitted. Furthermore, some pictures lacked sufficient clarity for us to accurately pinpoint the location of the lesion, leading us to skip those images as well.

## Skin canecr
Skin cancer is one of the most common types of cancer in the world. Over the past few years, different approaches have been proposed to deal with automated skin cancer detection. sun uv impact, 

## Future work

In the future we would like to implement segmentation strategies that can automate the process of annotating images. Ideally, this will be done by combing data knowledge and domain knowledge. Data knowledge is for example used, when measuring homogenous intensity or texture in an image to locate what stands out. While domain knowledge is used to further specify the task at hand. Usually domain knowledge should be discriminative, generalizable, and efficiently computable. 
A relevant segmentation strategy can be foreground segmentation, that focuses on a single object in an image, that can be used to automate the mask creation process, instead of doing it by hand. The benefits of foreground segmentation are the effectiveness of detecting the relevant lesions in the images. Also, computer-assisted analysis of medical images needs segmentation to function.  

## References
https://www.sciencedirect.com/science/article/pii/S235234092031115X
https://www.sciencedirect.com/science/article/pii/S0010482519304019?via%3Dihub

