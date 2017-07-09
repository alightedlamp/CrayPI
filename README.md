# Cratejoy Super Admin

A web interface for using the Merchant API to freely change things as necessary.

## Dev Setup

### Install requirements

#### Install Python Requirements
`pip install -r requirements`

#### Install Javascript Requirements
`bower install`

### Setup database
Make sure your local database is running and open it with
`psql postgres`

Create a new database with `CREATE DATABASE flask_template`

`python db_create.py`

`python db_migrate.py`

### Run the app
`python run.py`

### Create config
In the root directory, make a file called config.py using example_config.py as a template then replace all of the keys with your own

## Run the app
`python run.py`

## User Setup

![alt text](http://www.gtigazette.com/wp-content/uploads/2014/02/determined-fumanchu-computer-stare-l.png "working on it")