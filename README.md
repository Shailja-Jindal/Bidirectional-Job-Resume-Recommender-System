# Bidirectional-Job-Resume-Recommender-System
## Introduction:
A must have tool for job seekers and recruiters. This project is intended to find and recommend the best fit. Job seekers can find best matching jobs to their resume and Recruiters find the best fit resumes for any job posting. Its based on Machine learning "NLP" concepts of text content match via Doc2Vec and similarity scores.
Primary feature of this recommender system is its roburst nature. It enables both Job-seekers and Recruiters to find best fit.
1.	It reads the resume features and finds the top (n) relavant jobs based on Education, Work experience, location and text content.

2.	Same code can be used to find best matching resumes for a job posting (based on Education, Work experience, location and text content).

Project involves extensive use of NLP features as in:

•	tokenization

•	lemmatization (English) 

-- Tried WordNet, spaCy, Textblob 

-- spaCy used (-PRON-) if identified pronoun 

-- Got same results with NLTK WordNet and TextBlob - chose to stick with wordNet

•	Count Vectorization

•	TF-IDF

•	entity extraction


## Model
Text data is trained on Doc2Vec Model.

Uses Cosine similarity to find the closest match and recommend top (n) matches

## Directory Structure 
https://github.com/Shailja-Jindal/Bidirectional-Job-Resume-Recommender-System/blob/master/5-Images/Directory_Structure.png

## Directory Details
### Data  
Due to file size limitations showing samples datasets.

•	Resumes: Contains sample 15 resumes in .csv format (look and feel of dataset)

•	Jobs: Contains sample 15 jobs in .csv format (look and feel of dataset)

•	Actual datasets can be found on Kaggle:

https://www.kaggle.com/PromptCloudHQ/jobs-on-naukricom

https://www.kaggle.com/avanisiddhapura27/resume-dataset

### EDA

### Stages of Recommender 

### Model 

### Final Recommender

## Resources
•	Datasets

o	https://www.kaggle.com/

o	https://www.britannica.com/

•	Lemmatization Approaches with Examples in Python

o	https://www.machinelearningplus.com/

•	Doc2Vec Tutorial and Implementation

o	https://radimrehurek.com/gensim/

o	https://towardsdatascience.com/

•	Fuzzy-Wuzzy Matching

o	https://towardsdatascience.com/

•	And shoutout to –

o	Scikit-learn documentation

o	Geekforgeeks 

o	Stackoverflow 
