# IR-Project


# Setting Up the back-end (Django): 

Step 1:Install the virtualenv package
python3 -m pip install --user virtualenv

Step 2: Create a virtual environment
python3 -m venv env cd env
source bin/activate

Step 3: Install the packages by using pip
pip install django
pip install djangorestframework
python -m pip install django-cors-headers

Once done, download the ‘election_analysis_backend’ folder from Git repo and copy the folder inside the env folder created after executing the above commands

Then change directory to ‘election_analysis_backend’ folder using
cd election_analysis_backend

Finally run the server using
python manage.py runserver


If you have already set up the virtual environment once the go to the folder where the environment is created and enter the following command to enter the already created virtual environment
source env/bin/activate

Then enter the ‘env’ folder using
cd env

Then enter the ‘election_analysis_backend’ folder using
cd election_analysis_backend

And run the server using
python manage.py runserver


# Setting Up the front-end (Reactjs):

1. Download the ‘election_analysis’ folder from git repo . Then enter the ‘election_analysis’ folder:
cd election_analysis
2. Run the following command
npm install npm start