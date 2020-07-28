import streamlit as st
import numpy as np 
import pandas as pd 
import datetime
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
# %matplotlib inline

st.title('Find best matching jobs')
"""
---- 
"""
# # Its so :fire:
# Streamlit has caching so it can store the results of the function
# st is smart enough to only re-run the function if the data file was changed

# Loading in data
@st.cache

def reading():
# reading my sorted resume csv
    resume = pd.read_csv('wip/con_resume_1.csv')

    # reading my sorted job csv
    job = pd.read_csv('wip/con_job_1.csv')

    # resume features to be matched with jobs
    r_df = resume[['resume_id','experience_range','is_grad','is_postgrad','is_doc','location',
                    'vec_1','vec_2','vec_3','vec_4','vec_5','vec_6','vec_7','vec_8','vec_9','vec_10','vec_11','vec_12',
                    'vec_13','vec_14','vec_15','vec_16','vec_17','vec_18','vec_19','vec_20']]

    return resume, job, r_df

resume, job, r_df = reading()

#My recommender system to find best jobs for a given resume
def jobs_recommender(r) :
    
    #Store the results in this DF
    matched_jobs = pd.DataFrame(columns = ["id","company","job_title","jobdescription","experience_range","location","similarity"] )
    
    r= r.to_numpy()
    r= r.reshape(1, -1)
    #Go through ALL the related jobs
    for jd in job_m['j_id'] :
        #print(f'jd is {jd}')        
        #Find the similarity of the jobs with resume
        jobs = job_m.loc[jd]
        jobs = jobs.to_numpy()
        jobs = jobs.reshape(1, -1)
        #print(f'job is {jobs}')
        #print(f'r is {r}')
        #print(f'job is {job}')
        similarity = cosine_similarity(r,jobs)
        #print(f'similarity is {similarity}')
        matched_jobs.loc[len(matched_jobs)] = [jd,
                                               related_jobs['company'][jd],
                                               related_jobs['jobtitle'][jd],
                                               related_jobs['jobdescription'][jd],
                                               related_jobs['experience_range'][jd],
                                               related_jobs['loc_name'][jd],
                                               similarity[0][0]]
        

    return matched_jobs.sort_values(by=['similarity'],ascending=False)[1:]              

# r1 contrains the only features to be matched of slected resume  13769-java

actual_name = {'java developer 1': 14, 'java developer 2': 310, 'php developer 1': 983, 'php developer 2':9934, 'python developer 1': 10303, 'python developer 2': 10940, 'oracle 1': 12330, 'oracle 2': 12884}
r_test = st.sidebar.selectbox('Choose the resume title : ', list(actual_name.keys()))
#st.text(type(r_test))
match_key= r_test.split()[0]
#st.text(match_key)
r1= r_df.loc[actual_name[r_test]]

r2= resume.loc[actual_name[r_test]]
R_title = r2['Resume_title']
R_location = r2['loc_name']
R_total_exp = r2['total_experience']
R_desc = r2['Description']
R_work_ex = r2['experience_desc']

st.markdown(f'### Resume Title: ') 
st.markdown(f'{R_title}')    
st.markdown(f'**Current location:** {R_location} **Total Experience:** {R_total_exp}')
#st.subheader(f'Experience description: {R_work_ex}')


import ast 
# for index, rows in r2.iterrows():
#     resume_desc= []
#     #pick work experience col and read it as JSON   
result_work = r2['work_experiences']
#st.subheader(result_work)
#st.subheader(type(result_work))
result_work =  ast.literal_eval(result_work)
#st.subheader(type(result_work))
#     try: result_work = eval(work)
#     except: continue
#     #read description   
for i in result_work.keys(): 
    # st.subheader(i)   
    w_title = (result_work[i][0]['wtitle:']) 
    #st.markdown(f'')       
    w_company= (result_work[i][1]['wcompany:'])
    st.markdown(f'**Work Title {i}:** {w_title}  **Company :** {w_company}') 
    w_city= (result_work[i][2]['wcity:'])
    w_state= (result_work[i][3]['wstate:'])
    w_duration= (result_work[i][4]['wduration:'])      
    w_descr= (result_work[i][5]['wdescr:'])
    st.markdown(f'**Description :** {w_descr}') 



#from pool of 22,000 jobs, selecting jobs that are releated to sql dba (resume in question)
related_jobs = job.loc[job['jobtitle'].str.contains(match_key)]
related_jobs=related_jobs.loc[related_jobs['location']==r2['location']]
#job features need to be matched with resume
job_m = related_jobs[['j_id','experience_range','is_grad','is_postgrad','is_doc','location',
                     'vec_1','vec_2','vec_3','vec_4','vec_5','vec_6','vec_7','vec_8','vec_9','vec_10','vec_11','vec_12',
                      'vec_13','vec_14','vec_15','vec_16','vec_17','vec_18','vec_19','vec_20']]
st.markdown('## Recommended jobs : ')
# call recommender by passing selected resume 
matched_jobs = jobs_recommender(r1)
matched_jobs = matched_jobs.head(10)

st.write(matched_jobs)
st.write('**Note:** Similarity Scores may round off to nearest integer value, so itcould be hard to visualize the difference. But they are displayed in ranked order.')

from PIL import Image
if match_key == 'java':
    image = Image.open('java.png')
    st.image(image, caption=(f'Suggestions for {match_key}'),
            use_column_width=True)
elif match_key == 'oracle':
    image = Image.open('oracle.png')
    st.image(image, caption=(f'Suggestions for {match_key}'),
            use_column_width=True)
elif match_key == 'php':
    image = Image.open('php.png')
    st.image(image, caption=(f'Suggestions for {match_key}'),
            use_column_width=True)
elif match_key == 'python':
    image = Image.open('python_word1.png')
    st.image(image, caption=(f'Suggestions for {match_key}'),
            use_column_width=True)


