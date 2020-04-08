This project is built with the [Django framework](https://www.djangoproject.com) and Python 3.x.

## Environment Setup
### MacOS
#### Homebrew

If you don't have it already, start by [installing Homebrew](https://brew.sh). This tool makes it easy to manage development tools and keep them up-to-date.

#### pyenv
By default, MacOS comes installed with `python 2.x`. Managing multiple versions of Python can be painful and confusing, but `pyenv` can help manage this complexity.
```
brew install pyenv
```

The latest version of Python can now be installed and set as the global default.
```
pyenv install --list
pyenv install 3.8.2
pyenv global 3.8.2
pyenv version
```

`pyenv` needs to be added to the `$PATH` in order to act as the default `python` command. Add the following to `~/.bash_profile`:
```
if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi
```

Running `which python` should now point to `~/.pyenv/shims/python`.

## Running the Application
Now that the environment is setup and configured, we can run the application.

### Install Project Dependencies
Python uses `pip` to manage package dependencies. To start, let's update `pip`.
```
pip install --upgrade pip
source ~/.bash_profile
```

`pipenv` is a convenience tool that wraps `pip` and `virtualenv`, and makes it easy to create a runtime environment for our application.
```
pip install --upgrade pipenv
source ~/.bash_profile
```

Now we can use `pipenv` to download our project dependencies. From the project root folder, run
```
pipenv install
```
to download and install the dependencies indicated in `Pipfile` and `Pipfile.lock`.

### Create Configuration
This application expects a `.env` file in the root folder at runtime. An example of this file:
```
SECRET_KEY = 'your_secret_key_here'
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
SITE_URL = 'http://localhost:8000'
INIT_PASS = 'password123'
INITIALIZE = true
SEND_EMAIL = 'true'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
DEBUG = true
```
The most important field here is `INIT_PASS`, which determines the password for the default user login.

### Start the Application
#### Running for the first time
First we need to setup our database by running the Django database migrations.
```
pipenv run python manage.py migrate
```

#### Running every time
Now we can start the application, which will start a webserver, start the Django website, and run the `initialize.py` script inside a Python virtual environment.
```
pipenv run python manage.py runserver
```
Output:
```
Loading .env environment variables…
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 08, 2020 - 14:02:10
Django version 2.2.11, using settings 'wefeed.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The site should now be available at http://localhost:8000. The webserver supports live reloads, so you can make changes to the code without restarting the webserver.

## Contributing
### If you are going to modify this script then take advantage of pre-commit hooks
```shell script
pip install pre-commit
pre-commit install
```
