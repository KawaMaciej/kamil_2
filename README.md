# Exploratory Data Analysis and modeling for heart attack

## Overview

This repository contains the Exploratory Data Analysis (EDA)  and models for heart attack. The goal of this analysis is to explore and understand the dataset, uncover patterns, identify anomalies, and provide insights that will guide further analysis or decision-making.

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Analysis](#analysis)
4. [Results](#results)
5. [Requirements](#requirements)

## Introduction


## Dataset

### Source

https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset

### Description

<p style="font-family: Arials, sans-serif; font-size: 14px; color: #808080"><strong>FEATURES:</strong></p>
<ol style="font-family: Arials, sans-serif; font-size: 14px; line-height:1.5"><li><strong>AGE</strong> - age in years. </li> 
<li><strong>SEX</strong> - sex (1 = male; 0 = female).
<li><strong>CP</strong> -  chest pain type (1 = typical angina; 2 = atypical angina; 3 = non-anginal pain; 0 = asymptomatic). </li>
<li><strong>TRESTBPS</strong> - resting blood pressure (in mm Hg on admission to the hospital). </li>
<li><strong>CHOL</strong> - serum cholestoral in mg/dl.</li>
<li><strong>FBS</strong> - fasting blood sugar > 120 mg/dl (1 = true; 0 = false).</li>
<li><strong>RESTECG</strong> - resting electrocardiographic results (1 = normal; 2 = having ST-T wave abnormality; 0 = hypertrophy).</li>
<li><strong>THALACH</strong> - maximum heart rate achieved.</li>
<li><strong>EXANG</strong> - exercise induced angina (1 = yes; 0 = no).</li>
<li><strong>OLDPEAK</strong> - ST depression induced by exercise relative to rest.</li>
<li><strong>SLOPE</strong> - the slope of the peak exercise ST segment (2 = upsloping; 1 = flat; 0 = downsloping). </li>
<li><strong>CA</strong> - number of major vessels (0-3) colored by flourosopy.</li>
<li><strong>THAL</strong> - 2 = normal; 1 = fixed defect; 3 = reversable defect. </li>
<li><strong>OUTPUT</strong> - the predicted attribute - diagnosis of heart disease (angiographic disease status) (Value 0 = < diameter narrowing; Value 1 = > 50% diameter narrowing). </li> 
</ol>

## Analysis

### Data Cleaning

<p style="font-family: Arials, sans-serif; font-size: 14px; color: #808080">The dataset was scanned for missing and duplicate values. Appropriate steps were taken to handle these issues, such as:</p>
<ul>
<li> Identifying and imputing or removing missing values.</li>
<li> Detecting and removing duplicate records.</li>

</ul>


## Results


## Requirements
Analysis was made using python 3.11.9 with packages
- pandas
- matplotlib
- seaborn
- sklearn
- xgboost
- lightgbm
- steamlit

### Running the Analysis

```bash
# Using manual download
  -- pip install -r requierements.txt
  
  -- streamlit app.py

# Using Docker  
  -- docker build --pull --rm -f "Dockerfile" -t projekt1:latest "."
  
  -- docker run -p 8501:8501 projekt1 
  
