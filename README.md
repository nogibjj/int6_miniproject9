# int6_individual1
[![Install](https://github.com/nogibjj/int6_individual1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/int6_individual1/actions/workflows/install.yml) [![Format](https://github.com/nogibjj/int6_individual1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/int6_individual1/actions/workflows/format.yml) [![Lint](https://github.com/nogibjj/int6_individual1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/int6_individual1/actions/workflows/lint.yml) [![Test](https://github.com/nogibjj/int6_individual1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/int6_individual1/actions/workflows/test.yml)

This repo contains work for individual project 1. It sets up an environment on codespaces and uses Github Actions to run a Makefile for the following: `make install`, `make test`, `make format`, `make lint`. It loads in a dataset (from Kaggle) that contains information on Spotify sound tracks and performs some basic exploratory data analysis.

Some important components:

* `Makefile`

* `Dockerfile`

* A base set of libraries for devops and web

* `githubactions` 

## Purpose of project
The purpose of this project is to build upon mini projects 1-3 to simulate best practices of continuous integration in data science projects. 

## Important files
The file lib.py contains four main functions: 
* `read_data(df_path)`: reads in our data as a pandas dataframe
* `calc_stats(df)`: calculates summary statistics including mean, median, and standard deviation
* `create_viz(df, save)`: creates two sample plots using the data; set save=True to save as png
* `create_viz_tempo(df, save)`: creates sample plot for tempo using the data; set save=True to save as png

The file main.py contains two main functions: 
* `create_all_viz(df, save)`: creates all visualizations at once; set save=True to save as png
* `create_report(data_path)`: generates a pdf report of the data including basic summary stats and plots

These functions are tested in test_lib.py and test_main.py using pytest, and in main.ipynb using the nbval plugin. To make sure github actions is working properly, I use a Makefile to test various parts of my code. 

## Preparation
1. Open codespaces 
2. Wait for container to be built and virtual environment to be activated with requirements.txt installed.
3. Alternatively, git clone the repository and use `make install` to run the code locally.

## Check format and test errors 
1. Format code `make format` with black

    <img width="600" alt="working make format" src=resources/working_format.png>

2. Lint code `make lint` with ruff

    <img width="600" alt="working make lint" src=resources/working_lint.png>

3. Test code `make test` with pytest and nbval

    <img width="600" alt="passing test cases image" src=resources/working_test.png>


## Outputs
Summary statistics and data visualizations can be displayed by executing code chunks in main.ipynb. The `generate_and_push` target in the Makefile automates the process of generating our resources (images and pdf report) and pushing these generated files to my repository under "actions-user".

<img width="600" alt="showing summary stats image" src=resources/working_stats.png>

Data visualizations are saved to a `resources` folder by running `python test_main.py` calling `create_all_viz(df, save)`

<img width="600" alt="showing plots image" src=resources/working_plots.png>

PDF report is created by running `python test_main.py` calling `create_report(data_path)`. You can view this report [here.](/spotify_report.pdf)

## Demo Video Link
[Video Link](https://youtu.be/uJ7U-2ERJjg)
