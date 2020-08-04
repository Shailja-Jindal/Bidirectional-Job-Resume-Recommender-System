import streamlit as st
from PIL import Image
# image = Image.open('title_page.png')
# st.image(image,width = 600)
st.markdown("<h1 style='text-align: center; color: Blue;'>Bidirectional Job-Resume Recommender</h1>", unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center; image</h1>", unsafe_allow_html=True)
#st.markdown('# Bidirectional Job-Resume Recommender')
#"""
##---- 
#"""
import numpy as np 
import pandas as pd 
import datetime
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
# %matplotlib inline
import streamlit as st
from load_css import local_css
local_css("style.css")
from PIL import Image

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

actual_name = {'java developer - Maharashtra': 14, 'java developer - Haryana ': 310, 'php developer - Delhi': 983, 'php developer - Karnataka':9934, 'python developer -Karnataka': 10303, 'python developer - Tamil Nadu': 10940, 'oracle - Maharashtra': 12330, 'oracle - Tamil Nadu ': 12884}
r_test = st.sidebar.selectbox('Pick a resume from Drop-down : ', list(actual_name.keys()))
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
image = Image.open('cv_pic.png')
#image = image.resize((100, 100))
#st.image(image,width = 200)
t = f"<div><span class='bold'><span class='highlight blue'>Selected Resume Title  : </span></span>   <span class='highlight blue'>{R_title} </span> </div>"
with open("center.css") as f: 
    st.markdown(t.format(f.read()), unsafe_allow_html=True)
"""


"""
#st.markdown(f'{R_title}')  
loc_ex =  f"<div><span class='bold'>Location: </span><span class='highlight red'>{R_location}</span><span class='bold'>Total Experience: </span><span class='highlight red'>{R_total_exp}</span></div>" 
#st.markdown(f'**Current location:** {R_location} \t **Total Experience:** {R_total_exp}')
st.markdown(loc_ex, unsafe_allow_html=True)
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
#for i in result_work.keys(): 
# st.subheader(i)   
w_title = (result_work[0][0]['wtitle:']) 
#st.markdown(f'')       
w_company= (result_work[0][1]['wcompany:'])
t_com = f"<div><span class='bold'>Current Work Title : </span><span class='highlight red'>{w_title}</span><span class='bold'>Company : </span><span class='highlight red'>{w_company}</span></div>"
w_city= (result_work[0][2]['wcity:'])
w_state= (result_work[0][3]['wstate:'])
w_duration= (result_work[0][4]['wduration:'])      
w_descr= (result_work[0][5]['wdescr:'])
#des = f"<div><span class='bold'>Description :  </span>{w_descr}</div>" 
des = f"<div><span class='bold'>Description :  </span>{R_desc}</div>" 
#st.markdown(f'**Current Work Title :** {w_title}  **Company :** {w_company}')
st.markdown(t_com,unsafe_allow_html=True)
st.markdown(des,unsafe_allow_html=True)
#st.markdown(f'**Description :** {w_descr}') 



#from pool of 34,000 jobs, selecting jobs that are releated to sql dba (resume in question)
related_jobs = job.loc[job['jobtitle'].str.contains(match_key)]
related_jobs=related_jobs.loc[related_jobs['location']==r2['location']]
#job features need to be matched with resume
job_m = related_jobs[['j_id','experience_range','is_grad','is_postgrad','is_doc','location',
                     'vec_1','vec_2','vec_3','vec_4','vec_5','vec_6','vec_7','vec_8','vec_9','vec_10','vec_11','vec_12',
                      'vec_13','vec_14','vec_15','vec_16','vec_17','vec_18','vec_19','vec_20']]
# """
# *************************************************
# """
st.markdown('# System Recommended Top 10 Jobs : ')
image = Image.open('jobs.png')
st.image(image, width = 200) #, use_column_width=True)
st.write('Recommendation is based on cosine similarity of multiple factors like skills, location, experience, education, description, title etc ')
# call recommender by passing selected resume 
matched_jobs = jobs_recommender(r1)
matched_jobs = matched_jobs.head(10)

st.write(matched_jobs)
st.write('**Note:** Similarity Scores may round off to nearest integer value, so itcould be hard to visualize the difference. But they are displayed in ranked order.')
"""
*************************************************

"""
# st.markdown('# Phrases suggestions in word-cloud ')
# st.write('WordCloud pulls words, pairs from all related jobs to form a cloud')
# from PIL import Image
# if match_key == 'java':
#     image = Image.open('java.png')
#     st.image(image, caption=(f'Suggestions for {match_key}'),
#             use_column_width=True)
# elif match_key == 'oracle':
#     image = Image.open('oracle.png')
#     st.image(image, caption=(f'Suggestions for {match_key}'),
#             use_column_width=True)
# elif match_key == 'php':
#     image = Image.open('php.png')
#     st.image(image, caption=(f'Suggestions for {match_key}'),
#             use_column_width=True)
# elif match_key == 'python':
#     image = Image.open('python_word1.png')
#     st.image(image, caption=(f'Suggestions for {match_key}'),
#             use_column_width=True)


