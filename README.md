# README

## about

The ODEEG project has been funded by the go!digital programme 2016, Austria, and is connected to the wider CVA (Corpus Vasorum Antiquorum) project. Initially, the objectives of ODEEG were to: (1) Digitally document ancient Greek and Cypriot vases in 3D; (2) Ensure long-term digital preservation of the documentation; (3) Make a variety of data (e.g., 3D models, photographs, scientific illustrations, and text) available for researchers via a dedicated online database, referencing to the Beazley Archive (University of Oxford). By providing a publicly available, long-term, online archive, we aimed at creating an ideal foundation to gain further knowledge and help answering innovative scientific questions dealing with interior and exterior measurements of ancient vessels.

## install

1. clone the repo
2. create a virtual env
3. install dependencies (`pip install -r requests.txt`)
4. adapt settings file to your needs
5. makemigrations and migrate `python manage.py makemigrations|migrate --settings=odeeg.settings.dev`
6. spin up the (dev) server: `python manage.py runserver --settings=odeeg.settings.dev`
