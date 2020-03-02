# ChadevMonster
A web application to manage article submissions that are posted to /r/chadev and the Chadev slack.

[Production Site](https://google.com/)

# Previous version

More info -> [Original ChadevMonster project](https://github.com/juzten/chaDevMonster)

## Getting Started

These instructions will get you setup with the project and running on your local machine for development and testing purposes.

### Prerequisites

Note: Built using python 3.8.1 but any version of python 3.6+ should work. You can use something like Pyenv to manage python versions.

* Python 3
* Pip
* Virtualenv or similar (optional)
* PostgreSQL (v10 should work)

### Activate environment

```
source venv/bin/activate
cd chadevmonster
```

### Install python packages

```
pip install -r pip.txt
```

### Set dev environment variable
Set this environment variable in your .bashrc or .zshrc

```
export ENVIRONMENT="dev"
```

### Set config file

copy/rename config/example-dev.py to config/dev.py

### Create the database and upgrade the database with the latest migrations

```
./manage.py create_db
./manage.py db upgrade
```

### Running the script

```
python run.py
```

### Open web browser to localhost:5000

open http://localhost:5000

## VueJS Frontend located in ChadevMonsterUI

You will need to install vue and make sure you can run Vue UI priort to the next step.

```
cd ChadevMonsterUI
npm install
vue ui
```

Once in the Vue UI you will be able to select the project and run the `serve` task.

### Build frontend for deployment

Run the `build` command in Vue UI

Files for deployment will be in the `dist` folder.

