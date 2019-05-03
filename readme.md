# Unirooms - Simplified UNIBZ free rooms search
Unirooms project provides a RESTful api for Unibz free rooms. The project is written in Python3.7. 


## Installation
We recommend you to use virtual environment to test this project or contribute to it. 
In order to use the virtual environment, make sure you have already installed the `virtualenv` package.
In case of missing `virtualenv` package, you can install it by using the following command: `sudo pip3 install virtualenv `


To run the project, you can download or clone the project.
 - [Download the project](https://github.com/Phoenix404/unirooms/archive/master.zip).
 - clone `git clone https://github.com/Phoenix404/unirooms.git` 

 
If you have downloaded the project as zip file, extract it in your working directory.

Go to the directory where you have extracted or cloned the project.
 
Run the following command to create the virtual environment in that directory
 `virtualenv ./venv `

Now, to activate the environment, you will need to run the `source venv/bin/activate` command.

To deactivate the current environment, simply run the `deactivate` command.

Unirooms project uses some third party packages. To install, those packages you can execute one of the following commands:
 - `pip install -r requirements.txt` 
 - `python -m pip install -r requirements.txt ` 

This command will read the necessary packages from requirement.txt file and install them in the project environment.

## Usage
_Assumed that you are in the root directory of project and Virtual environment is active._

### Run server
In order to start the server, execute the following command: `python3 unirooms/api_runner.py`

In output, there will be given a url i.e http://127.0.0.1:5000/. 
Open that url in your browser and *voilà*.

`/` endpoint will return the list of the endpoints that are available for this api.




