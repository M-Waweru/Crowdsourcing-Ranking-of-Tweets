import streamlit as st
import enki
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit.components.v1 as components

st.title('Check BBI Report Analysis')

e = enki.Enki(api_key='c25db137-bde1-4d86-ae4b-f71e928395db', endpoint='http://waturanknews.live',                  
                project_short_name='checkBBI',
                all=1)

e.get_all()
tasks_info = {}

for t in e.tasks:
    desc = e.task_runs_df[t.id]['info'].describe()
    value_counts = e.task_runs_df[t.id]['info'].value_counts()
    analysis = dict(value_counts)
    summary = dict(desc)
    tweet_data = e.tasks[t.id -1].data
    # print(tweet_data)

    tasks_info[t.id] = analysis, summary, tweet_data

st.subheader('Completed tasks')
tasks_info.keys()

task_id = st.text_input('Enter the Task ID', '1')
st.subheader('Task ' + task_id)

task_id = int(task_id)
st.markdown('**Task ID: ** '+ str(tasks_info[task_id][2]['_id']))
st.markdown('**Task User Screen Name: ** '+ str(tasks_info[task_id][2]['user_screen_name']))
st.markdown('**Task Test: ** '+ str(tasks_info[task_id][2]['text']))
# st.markdown('**Task Url: ** '+ 'https://twitter.com/' + str(tasks_info[task_id][2]['user_screen_name']) + '/status/' + str(tasks_info[task_id][2]['_id']))

task_labels = tasks_info[task_id][0].keys()
task_values = tasks_info[task_id][0].values()

labels = task_labels
sizes = task_values
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
st.pyplot(plt)

