# Infinity
### Purpose
The project aim to mine data from different news websites that client request. Right now only one website supported. New websites will be added in the future.

### How to build & Run

#### Virtal Env (Optional*)
Create a virtual environment `venv` module can be used.\
`python -m venv /path/to/new/virtual/environment`\
\
More information about [venv](https://docs.python.org/3/library/venv.html)

#### Packages
Required packages is given in requirements format.
Run `pip install requirements.txt` command to install required packages.

#### Environment Variables
To use environment variables create a file with name `.env` and copy contents from `.env.sample` and paste 

#### Running
To run application ``
- Windows
    - `python -m flask run` or `python app.py`
- Linux/MacOS
    - `python -m flask run` or `python app.py` 


### Build & Run with Docker
Follow [```Environment Variables```](https://github.com/AliHadiOzturk/infinity1/tree/prod#environment-variables) steps before using docker. 

#### MacOS & Linux
```app.sh``` can be use for building & starting and stoping docker container.

To use ```app.sh```:\
Run ```sh app.sh``` in the terminal and select desired action

#### Windows
To run with docker in windows use ```app.bat``` script file.
Run ```app.bat``` in the command line and select desired action

### Test

#### Postman
[Postman Collection](https://api.postman.com/collections/6250379-b76db229-bfcc-4992-ba7b-395808d1001e?access_key=PMAT-01H5K44RVW2SBA0Q3BPSGNXJNK) can be use to test the app.
Before use of postman collection create environment and add variable name `host` and value with `http://localhost:5000/api`\
Dont fotget to select environment from right top corner of postman
