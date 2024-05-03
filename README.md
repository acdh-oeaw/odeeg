# README

## about

The ODEEG project has been funded by the go!digital programme 2016, Austria, and is connected to the wider CVA (Corpus Vasorum Antiquorum) project. Initially, the objectives of ODEEG were to: (1) Digitally document ancient Greek and Cypriot vases in 3D; (2) Ensure long-term digital preservation of the documentation; (3) Make a variety of data (e.g., 3D models, photographs, scientific illustrations, and text) available for researchers via a dedicated online database, referencing to the Beazley Archive (University of Oxford). By providing a publicly available, long-term, online archive, we aimed at creating an ideal foundation to gain further knowledge and help answering innovative scientific questions dealing with interior and exterior measurements of ancient vessels.

## install

1. clone the repo
2. create a virtual env in the root of the repo (you can put the created folder on the ignore list)
3. activate the virtual env
4. install dependencies (`pip install -r requirements.txt`)
5. adapt the `default.env` file to your needs and run `./set_env_variables.sh`
6. makemigrations and migrate `python manage.py makemigrations|migrate`
7. spin up the (dev) server: `python manage.py runserver`


## build search index

`python manage.py rebuild_index --no-input`

see django-haystack docs for more information: https://django-haystack.readthedocs.io/en/master/management_commands.html`


## Docker
### building the image

* `docker build -t odeeg:latest .`
* `docker build -t odeeg:latest --no-cache .`


### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

* `docker run -it -p 8020:8020 --rm --env-file docker.env --name odeeg odeeg:latest`

-----