# Example Repository for Candidate Interviews

This repository is used as a guide to talk about important aspects of ML engineering and MLOps.

## What the Repository Does

1. Trains a machine learning model to predict the highest temperature on a given day.
2. Runs inference by taking items from an AWS SQS, generating predictions, and storing them in a Postgres database.
3. Defines a Docker image to run the prediciton.
4. Defines a `buildspec.yml` file to run a CI proces on AWS CodeBuild.

## Task

Take a few minutes to look through the various files in the repository. This repository is terrible, on purpose!

Your job is to tell us about anything you think is missing, or should be fixed/improved.

Start with looking at the repository as a whole, and then dive into the individual files.

Don't worry, you won't lose points if you don't notice or mention something. This isn't meant to be a quiz. It's meant to guid a conversation so we can understand more about your experience. If we think there's something more that could be done, we'll ask you about it so you have a chance to express your thoughts.

## Data dictionary

This is a toy dataset, taken from an online example.

Here's what the columns in `data.csv` mean.

**year**: 2016 for all data points
**month**: number for month of the year
**day**: number for day of the year
**week**: day of the week as a character string
**temp_2**: max temperature 2 days prior
**temp_1**: max temperature 1 day prior
**average**: historical average max temperature
**actual**: max temperature measurement
**friend**: your friend’s prediction, a random number between 20 below the average and 20 above the average
