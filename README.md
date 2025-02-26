# Introduction:  
 
The furniture industry has seen a significant shift towards online shopping in the past few years.   
However, traditional online furniture shopping often relies on text-based search functions, which can limit 
users. This implies that users might struggle to convey the precise type or style of furniture they seek, 
hindering their ability to browse product categories effectively and discover relevant items. This project is 
focused on addressing the challenge of developing machine learning that can recognize images for an e-commerce furniture store, thus improving the customer experience.  

# To run the file:

This project is done on Google Colab, so you should run Task1_Part1 and Task2_Part2 there for the best experience
# Dataset Description:


## Source: https://drive.google.com/drive/folders/1n2vwJ3mO6RYtLDakFYyJywg7ika8JCb?usp=drive_link (Splitted_Data and TestData)  
• Size: 2.32 GB  
o Total Images: 90,084 images.  
Breakdown by Category: Beds: 6,578 images; Chairs: 22,053 images; Dressers: 7,871 images;   
Lamps: 32,402 images; Sofas: 4,080 images; Tables: 17,100 images  
  
## Features:   
o Image Categories: beds, chairs, dressers, lamps, sofas, tables  
o Interior Styles: Asian, Beach, Contemporary, Craftsman, Eclectic, Farmhouse, 
Industrial, Media, Midcentury, Modern, Rustic, Scandinavian, Southwestern, Traditional, 
Transitional, Tropical, and Victorian.  
  
## Constraint:    
a. Imbalance in Category Distribution: Models may develop a bias towards more 
frequently presented categories due to varying numbers of images across categories.   
b. Label Noise and Error: Any inaccuracies in labeling or categorization of the images can 
lead to incorrect learning, where the model might learn from wrong examples.  
c. Similarity in Style: Some furniture may possess a similar style to different categories of
furniture (e.g., that one cursed sofa that looks exactly like a bed). This could result in 
confusion when performing task 2.   
  
# Preprocessing Steps:  
To efficiently manage and process the extensive dataset, the preprocessing procedure is systematically 
executed through the DataPrep.ipynb notebook, encompassing the following four steps:  

1. Extract Data: The dataset is extracted from Funiture_Data.zip into Splitted_Data.  
2. Define Splitting Logic: The split_dataset function is defined to handle the splitting of data into 
training (60%), validation (20%), and test sets (20%). It creates the necessary directories (train, 
val, test) and ensures a random distribution of images across the splits. In all tasks, the image is 
rescaled to 1. /255, while in the first and third task, data augmentation is applied to create varies 
in the training process.  
3. Specify Parameters: Parameters for input/output directories and split ratios are set.  
4. Execute Splitting: The dataset is splitted according to the specified parameters by calling the 
split_dataset function.  

# Model Training:

## Parameter tuning:  
### CNN: 
• Method: The model is manually trained through multiple combinations of parameters in a small 
epoch number, the final performance of each training is displayed on a graph. The best 
combination that provided the highest accuracy, and the least overfitting is chosen.    
• Best hyperparameter: learning_rate = 0.001, dropout = 0.3, batch_size = 64  

## Training process:   
We defined constants for image size, batch size, number of classes, and epochs, 
and set paths for training, validation, and test data. Data augmentation is applied to the training 
set to enhance model generalization. The CNN model consists of three convolutional layers with 
ReLU activation and max pooling, followed by a flattening layer and two dense layers, with the 
final layer using SoftMax activation for classification. The model is compiled with the Adam 
optimizer and categorical cross-entropy loss. It is then trained for a specified number of epochs 
using the training and validation generators, evaluated on the test set, and finally saved.   

# Performance Evaluation:  
Models/Metrics - Accuracy - Loss:  
CNN - 0.918660581111908 - 0.260753810405731  

# Conclusion:  
To test the capacity of each model when meeting an alien dataset, we will use 6 images for each 
category. These datas were not used during the training or validation phase.  
  
CNN: Result: Accuracy: 92.4% Precision: 91.8% Recall: 92.6% F1-Score: 92.2%
The model showed excellent generalization to new, unseen images, maintaining high accuracy and 
balanced precision and recall across all six furniture categories (beds, chairs, dressers, lamps, sofas, 
tables). The performance metrics indicate that the model can reliably classify furniture images, making 
it suitable for real-world applications in the e-commerce furniture store.  
