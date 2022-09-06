# flask-part-1
HHA 507 Assignment: Flask part 1


Create a new github repo called 'flask-part-1': 

Step 1: Inside the repo, create a basic flask app that has a 'hello world' as the main index (/), and create at least two additional pages
Step 2: Deploy flask app on GCP + Azure 

When deploying your flask application on GCP or Azure, to keep the flask app running in the background when you exit out of the remote terminal, please use this command: 


sudo nohup python3 app.py > log.txt 2>&1 &


explanation: 

    nohup => allows to run command/process or shell script that can continue running in the background after you log out from a shell.
    python3 app.py => this is how you normally start your flask app; note, if you called your python script something other then app.py, you will need to replace app.py with the name of the .py file you created 
    > log.txt => it forword the output to this file.
    2>&1 = move all the stderr to stdout.
    & = at the end of the command, allows you to run a command/process in background on the current shell.


Deliverable #1: share GitHub repo URL with me

Deliverable #2: inside repo's code, update the readme.md to contain two
URL links to your flask app deployed on GCP and Azure
