# IR-Project

## Branch reference for evaluation:

baseline: Refer this branch for baseline evaluation.
mid-review: Refer this branch for Mid-Review evaluation.
main: Refer this branch for Final Project evaluation.



## Setting Up the back-end (Django): 

Step 1:Install the virtualenv package
`python3 -m pip install --user virtualenv`

Step 2: Create a virtual environment
`python3 -m venv env cd env`
`source bin/activate`

Step 3: Install the packages by using pip
`pip install django`
`pip install djangorestframework`
`python -m pip install django-cors-headers`

Step 4: Download the ‘election_analysis_backend’ folder from the Git repo and copy the folder inside the env folder created after executing the above commands

Step 5: Change directory to ‘election_analysis_backend’ folder using
`cd election_analysis_backend`

Step 6: Run the server using
`python manage.py runserver`


If you have already set up the virtual environment once the go to the folder where the environment is created and enter the following command to enter the already created virtual environment
source env/bin/activate

Then enter the ‘env’ folder using
`cd env`

Then enter the ‘election_analysis_backend’ folder using
`cd election_analysis_backend`

And run the server using
`python manage.py runserver`


## Setting Up the front-end (Reactjs):

1. Download the ‘election_analysis’ folder from git repo . Then enter the ‘election_analysis’ folder:
`cd election_analysis`
2. Run the following command
`npm install npm start`


## Setting Up the sentiment (Streamlit):

1. Download the main folder from git repo . Then enter the ‘election_analysis_sentiment’ folder:
`cd election_analysis_sentiment`
2. Install Streamlit using the following command
`pip3 install streamlit`
3. Run the following command in the terminal
`streamlit run sentiment_final.py`
4. Run the following command in another terminal
`streamlit run manipulation_final.py`
