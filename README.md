
ANN-Marks-Pred
==============

**ANN-Marks-Pred** is a machine learning project that predicts students' math marks based on various features, using an Artificial Neural Network (ANN). The project involved hyperparameter tuning to optimize the model's performance and achieve an impressive **R² score**, indicating a strong correlation between the predicted and actual marks. The model is also deployed using Streamlit to allow users to input their own data and get a prediction on their marks.

Table of Contents
-----------------

*   [About](#about)
*   [Dataset](#dataset)
*   [Model](#model)
*   [Hyperparameter Tuning](#hyperparameter-tuning)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)

About
-----

The goal of this project is to predict students' math marks using an ANN. The input features consist of factors that may influence the students' performance, The output is a continuous value representing the predicted math mark.

The model was tuned to improve accuracy and performance, and it achieved an impressive R² score, meaning that the model does an excellent job of explaining the variance in the target variable (marks).

Dataset
-------

The dataset used in this project contains various features related to students' academic performance, and it was designed for predicting math marks. The features typically include:

*   Gender (hours spent studying)
*   Test Preparation Course
*   Reading Score
*   Writing Score

The target variable is the student's predicted **Math Mark** (continuous value).

Model
-----

The model implemented in this project is an Artificial Neural Network (ANN). The architecture of the ANN includes:

*   An input layer to handle multiple features
*   One or more hidden layers with ReLU activation functions
*   An output layer with a single neuron for regression (to predict marks)

The ANN is trained using **mean squared error (MSE)** as the loss function, and **Adam optimizer** is used for optimization. The network was trained on the dataset using a regression setup.

Hyperparameter Tuning
---------------------

To optimize the model's performance, hyperparameter tuning was performed. The tuning included adjustments for the following parameters:

*   Number of hidden layers
*   Number of neurons in each layer


We used  **Random Search** techniques to explore different hyperparameter combinations and select the best model configuration. The model achieved an impressive R² score, indicating strong performance in predicting math marks.

Streamlit Deployment
--------------------

Once the model was trained and optimized, it was deployed using **Streamlit** to create an interactive web interface for users. The Streamlit app allows users to input their own features (e.g., study hours, attendance, etc.) and get a predicted math mark based on the trained ANN model.

To interact with the model on Streamlit, visit the deployed app:

[Live Streamlit App](https://ann-marks-pred-akash.streamlit.app/)


Contributing
------------

We welcome contributions to improve the project. If you would like to contribute, please fork the repository, make changes, and submit a pull request. Please make sure to:

*   Follow the existing code style
*   Write unit tests for any new features or changes
*   Update the documentation as needed

License
-------

This project is licensed under the MIT License -
