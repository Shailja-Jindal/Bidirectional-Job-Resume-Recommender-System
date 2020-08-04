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

### 1-Data_gathering_EDA 
Job_EDA.ipynb  - File to gather raw data from csv and EDA on JOBS
Resume_EDA -  File to gather raw data from csv and EDA on Resumes
fuzzy-wuzzy-logic-Resume_EDA.ipynb – To obtain similar titles based on score. We see similar titles written in different forms like Java Developer, Dev (java), Jave Deve. Etc which all should be only Java Developer. Fuzzy -wuzzy helps resolving the issue.

### 2-Preprocessing_and_Modelling
Pre-processing Jobs for modellingv1.ipynb – First iteration of Doc2Vec Model on Jobs text Data
Pre-processing Jobs for modellingv2.ipynb – Second and final iteration of Doc2Vec Model on Jobs 
Pre-processing_Resume for matchingv1.ipynb - First iteration of Doc2Vec Model on resume text Data
Pre-processing_Resume for matchingv2.ipynb - Second and final iteration of Doc2Vec Model on resume
** one can just look into v2 to understand the flow.

### 3-Matching_Sprints
Sprint1_matching_resume_to_jobs.ipynb
Sprint2_matching_resume_to_jobs-with-location-add-on.ipynb
Sprint3_matching_resume_to_jobs-with-text-add-on.ipynb
Sprint4_matching_resume_to_jobs-final.ipynb

### 4-Top_recommendations
job_output.py – Python file to run streamlit to see more intercative user interface to input resume and get top 10 jobs
center.css – Support file to help align text / images to center
load_css.py – support file for better UI
style.css – support file for color coding in streamlit
** one can focus only on job_output.py for understanding the code

### 5-Images
Contains images used / created during coding

### 6-Model
Contains the final model, so just load, and run the model (Doc2Vec model trained on 40,000 jobs with 20-D vectors and 200 epochs)

### Data  
Due to file size limitations showing samples datasets.

•	Resumes: Contains sample 15 resumes in .csv format (look and feel of dataset)

•	Jobs: Contains sample 15 jobs in .csv format (look and feel of dataset)

•	Actual datasets can be found on Kaggle:

https://www.kaggle.com/PromptCloudHQ/jobs-on-naukricom

https://www.kaggle.com/avanisiddhapura27/resume-dataset



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
