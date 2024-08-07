# Heart Attack Analysis and Prediction

This repository contains the Exploratory Data Analysis (EDA) and predictive models for heart attack prediction. The goal of this analysis is to explore and understand the dataset, uncover patterns, identify anomalies, and provide insights that will guide further analysis or decision-making.

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
   - [Source](#source)
   - [Description](#description)
3. [Analysis](#analysis)
   - [Data Cleaning](#data-cleaning)
4. [Results](#results)
5. [Requirements](#requirements)
6. [Running the Analysis](#running-the-analysis)
   - [Using Manual Download](#using-manual-download)
   - [Using Docker](#using-docker)
7. [Conclusion](#conclusion)

## Introduction

Heart disease is one of the leading causes of death worldwide. Early detection and accurate prediction of heart attacks can save lives. This project aims to analyze the heart attack dataset and build predictive models to identify potential heart attack cases.

## Dataset

### Source
The dataset is sourced from Kaggle: [Heart Attack Analysis & Prediction Dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)

### Description
The dataset contains the following features:

- **AGE**: Age in years.
- **SEX**: Sex (1 = male; 0 = female).
- **CP**: Chest pain type (1 = typical angina; 2 = atypical angina; 3 = non-anginal pain; 0 = asymptomatic).
- **TRESTBPS**: Resting blood pressure (in mm Hg on admission to the hospital).
- **CHOL**: Serum cholesterol in mg/dl.
- **FBS**: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false).
- **RESTECG**: Resting electrocardiographic results (0 = normal; 1 = having ST-T wave abnormality; 2 = left ventricular hypertrophy).
- **THALACH**: Maximum heart rate achieved.
- **EXANG**: Exercise induced angina (1 = yes; 0 = no).
- **OLDPEAK**: ST depression induced by exercise relative to rest.
- **SLOPE**: The slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping).
- **CA**: Number of major vessels (0-3) colored by fluoroscopy.
- **THAL**: 1 = normal; 2 = fixed defect; 3 = reversible defect.
- **OUTPUT**: Diagnosis of heart disease (0 = < 50% diameter narrowing; 1 = > 50% diameter narrowing).

## Analysis

### Data Cleaning
The dataset was scanned for missing and duplicate values. Appropriate steps were taken to handle these issues, such as:
- Identifying and imputing or removing missing values.
- Detecting and removing duplicate records.

### Exploratory Data Analysis (EDA)
The EDA process includes:
- Statistical summary of the dataset.
- Visualization of the distribution of variables.
- Correlation analysis to identify relationships between features.

## Results
The results of the analysis and modeling include:
- Insights from the data exploration.
- Performance metrics of the predictive models.

## Requirements

Analysis was conducted using Python 3.11.9 with the following packages:
- pandas
- matplotlib
- seaborn
- scikit-learn
- xgboost
- lightgbm
- streamlit
- yprofiling
  
## Running the Analysis

### Using Manual Download

 Install the required packages:
 ```bash
   pip install -r requirements.txt
   streamlit run home.py
```
### Using Docker

```bash
  docker build --pull --rm -f "Dockerfile" -t heart-attack-analysis:latest "."
  
  docker run -p 8501:8501 heart-attack-analysis 
```

## Conclusion
This project provides an in-depth analysis of the heart attack dataset and implements predictive models to assist in early detection of heart disease.
