# README

## about

The ODEEG project has been funded by the go!digital programme 2016, Austria, and is connected to the wider CVA (Corpus Vasorum Antiquorum) project. Initially, the objectives of ODEEG were to: (1) Digitally document ancient Greek and Cypriot vases in 3D; (2) Ensure long-term digital preservation of the documentation; (3) Make a variety of data (e.g., 3D models, photographs, scientific illustrations, and text) available for researchers via a dedicated online database, referencing to the Beazley Archive (University of Oxford). By providing a publicly available, long-term, online archive, we aimed at creating an ideal foundation to gain further knowledge and help answering innovative scientific questions dealing with interior and exterior measurements of ancient vessels.

## install

The project uses [uv](https://docs.astral.sh/uv/).

1. clone the repo
1. makemigrations and migrate `uv run python manage.py migrate`
1. spin up the (dev) server: `uv run python manage.py runserver`

## Docker

### building the image

* `docker build -t odeeg:latest .`
* `docker build -t odeeg:latest --no-cache .`

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

* `docker run -it -p 8020:8020 --rm --env-file docker.env --name odeeg odeeg:latest`

-----
