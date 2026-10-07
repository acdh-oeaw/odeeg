# README

[![Linting](https://github.com/acdh-oeaw/odeeg/actions/workflows/lint.yaml/badge.svg)](https://github.com/acdh-oeaw/odeeg/actions/workflows/lint.yaml)
[![Test](https://github.com/acdh-oeaw/odeeg/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/odeeg/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/acdh-oeaw/odeeg/branch/main/graph/badge.svg?token=5A8LPTQ1L0)](https://codecov.io/gh/acdh-oeaw/odeeg)
[![workflows starter](https://github.com/acdh-oeaw/odeeg/actions/workflows/starter.yaml/badge.svg)](https://github.com/acdh-oeaw/odeeg/actions/workflows/starter.yaml)

## about

The ODEEG project has been funded by the go!digital programme 2016, Austria, and is connected to the wider CVA (Corpus Vasorum Antiquorum) project. Initially, the objectives of ODEEG were to: (1) Digitally document ancient Greek and Cypriot vases in 3D; (2) Ensure long-term digital preservation of the documentation; (3) Make a variety of data (e.g., 3D models, photographs, scientific illustrations, and text) available for researchers via a dedicated online database, referencing to the Beazley Archive (University of Oxford). By providing a publicly available, long-term, online archive, we aimed at creating an ideal foundation to gain further knowledge and help answering innovative scientific questions dealing with interior and exterior measurements of ancient vessels.

## install

The project uses [uv](https://docs.astral.sh/uv/).

1. clone the repo
1. makemigrations and migrate `uv run python manage.py migrate`
1. spin up the (dev) server: `uv run python manage.py runserver`

## Docker

### building the image

```bash
docker build -t odeeg:latest .
```

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

```bash
docker run -it -p 8020:8020 --network="host" --rm --env-file default.env --name odeeg odeeg:latest
```
