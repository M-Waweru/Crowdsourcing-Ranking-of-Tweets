# Crowdsourcing-Ranking-of-Tweets
This project is based on my Final IS Project. It entails the collection and labelling of tweet by social media users in order to identify misinformation and provide datasets for automating the process using machine learning

## Modules of the system
The project consists of two modules: The Pybossa Server and the Streamlit application.

### Pybossa Server
This is the main server that manages the crowdsourcing process from creating a project, labelling and API to send results to the Streamlit server. This module allows the user to download the task results as well for independent data analysis.

### Streamlit Server
This is an open source framework was used to create the interactive results dashboard. The dashboard gets the labelled tasks from the Pybossa API known as Enki.

Note: For more details on how to install them, please find documentation links below on how to get started.

Pybossa Server Installation links:
1.	[Installation of Pybossa] (https://docs.pybossa.com/installation/gettingstarted/)
2.	https://docs.pybossa.com/installation/guide/
3.	https://docs.pybossa.com/installation/configuration/
4.	https://docs.pybossa.com/build/pbs/ - used to install the project 
Deployment links:
1.	https://docs.pybossa.com/installation/deployment/
API for Pybossa 
1.	https://github.com/Scifabric/enki - this was used in the Streamlit application
2.	https://github.com/Scifabric/webhooks 
3.	https://docs.pybossa.com/build/webhooks/ - documentation on webhooks for real-time analysis
Streamlit Documentation
1.	https://docs.streamlit.io/en/stable/getting_started.html
