# Language Detection

This repository contains a Python script for training a language detection model using the Multinomial Naive Bayes algorithm. The goal is to predict the language of given text samples.

## Notebook

1. **Importing Libraries**: The script starts by importing necessary libraries such as pandas, numpy, seaborn, and scikit-learn. These libraries are essential for data manipulation, visualization, and machine learning.

2. **Exploratory Data Analysis (EDA)**: The dataset is loaded from a CSV file named "Language Detection.csv". The script then performs EDA by checking for null values and visualizing the distribution of data for each language using a pie chart.

3. **Data Cleaning and Transformation**: The `textclean` function is defined to preprocess the textual data. It converts text to lowercase, removes special characters, and strips any leading/trailing spaces. The target variable (language) is encoded using label encoding. The text data is transformed using a CountVectorizer and a TfidfTransformer.

4. **Primary Model Training**: The Multinomial Naive Bayes model is trained on the preprocessed data. The training set is split into training and testing subsets. The model is then fit to the training data.

5. **Model Pipeline Creation**: In this step we will make a class to create a pipeline with our custome text cleaning. Pipeline will consist of four steps

* Text Clean
* Count Vectorizer
* TfIdf Transformer
* Multinomialdb(Naive Bayes)

With the end of project we were able to achive following results
 ![image](/resources/results.png)

 ![image](/resources/model.png)

## Streamlit application

To run this streamlit application enter the below command

```bash
streamlit run app.py
```

## Usage

To use this code, follow these steps:

1. Install the required libraries `pip install requirements.txt`
2. Load your own dataset or modify the existing one.
3. Run the script to train the language detection model.
4. Evaluate the model's performance using classification metrics.
5. You can also tryout the streamlit app

Feel free to customize and extend this code for your specific use case!
