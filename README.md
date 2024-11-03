# int6_miniproject9
[![Install](https://github.com/nogibjj/int6_miniproject9/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/int6_miniproject9/actions/workflows/install.yml) [![Format](https://github.com/nogibjj/int6_miniproject9/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/int6_miniproject9/actions/workflows/format.yml) [![Lint](https://github.com/nogibjj/int6_miniproject9/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/int6_miniproject9/actions/workflows/lint.yml) [![Test](https://github.com/nogibjj/int6_miniproject9/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/int6_miniproject9/actions/workflows/test.yml)

This repo contains work for mini project 9. It sets up an environment on codespaces and uses Github Actions to run a Makefile for the following: `make install`, `make format`, `make lint`, and `make test`. It loads in a dataset (from individual project 1's github repo) that contains information on Spotify sound tracks and performs some basic exploratory data analysis.

Some important components:

* `Makefile`

* `Dockerfile`

* `main.ipynb` from Colab

* A base set of libraries for devops and web

* `githubactions` 

## Purpose of project
The purpose of this project is to set up a cloud-hosted Jupyter Notebook using Google Colab and demonstrate data manipulation.

## Important files
The notebook main.ipynb is a local copy of the Google Colab notebook found [here](https://colab.research.google.com/drive/1AydzYVrV8wWAdAl0-wdQhIJ6zSEFDm0U#scrollTo=Jed1n_yrmS1K). I use the nbval plugin to test my code when running `make test`. To make sure github actions is working properly, I use a Makefile to test various parts of my code. 

## Preparation
1. Open codespaces 
2. Wait for container to be built and virtual environment to be activated with requirements.txt installed.
3. Alternatively, git clone the repository and use `make install` to run the code locally.

## Tasks Performed
Data is read from the raw github content link and saved as a csv for data processing. Tasks performed in `main.ipynb` include generating summary statistics and data visualizations for the Spotify dataset. The contents can be displayed by executing code chunks in main.ipynb.

**1. Summary Stats**   
<img width="400" alt="showing summary stats image" src=resources/working_stats.png>

**2. Side by Side Plots**   
<img width="400" alt="showing plots image" src=resources/working_plots.png>

**3. Song Track Tempo Distribution**   
<img width="400" alt="showing plots image" src=resources/working_tempo.png>

**4. Explicit Songs per Genre**   
<img width="400" alt="showing plots image" src=resources/explicit_genre.png>

**5. Top Tracks by Popularity**   
<img width="400" alt="showing plots image" src=resources/top_tracks.png>


To view the EDA code, visit the notebook [here.](/main.ipynb)
