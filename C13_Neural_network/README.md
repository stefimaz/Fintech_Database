![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&width=1000&height=200&section=header&text=Neural%20Network%20&fontSize=30&fontColor=black)

<!-- header is made with: https://github.com/kyechan99/capsule-render -->

[Stephane Masyn](https://www.linkedin.com/in/stephane-masyn-35b16817a/) [<img src="https://cdn2.auth0.com/docs/media/connections/linkedin.png" alt="LinkedIn -  Stephane Masyn" width=15/>](https://www.linkedin.com/in/stephane-masyn-35b16817a/)
                                 

---

### Table of Contents

* [Overview](#overview)
* [Requirements](#requirements)
* [Visualization](#visualization)
* [User Experience](#user-experience)
* [License](#license)  

---

## Overview

In this program, a model that predicts whether applicants will be successful if funded by Alphabet Soup was created. The CSV file used contains more than 34,000 organizations that have received funding from Alphabet Soup over the years to work with. With the knowledge of machine learning and neural networks the following was performed...

* Prepare the data for use on a neural network model.

* Compile and evaluate a binary classification model using a neural network.

* Optimize the neural network model.
 
---

## Requirements

This project leverages python 3.7, scikit-learn, TemsorFlow and Keras.

A [conda](https://docs.conda.io/en/latest/) environment with liabraries listed below and [Jupyter Notebook/Lab](https://jupyter.org/) are required to run the code.

The following libraries were used:

1. [TensorFlow 2.0](https://www.tensorflow.org/) - The core open source library to help you develop and train ML models.
2. [Scikit Learn](https://scikit-learn.org/stable/index.html) - Scikit Learn or Sklearn is one of the most used Python libraries for Data Science, along with others like Numpy, Pandas, Tensorflow, or Keras.


Install the following librarie(s) in your terminal...

    pip install -U scikit-learn
    pip install --upgrade tensorflow

---

## Data

The data used in this neural network model was from derived from a CSV file called applicants_data.csv.:

---

## Visualization

Uploading and reading the .csv file
![readcsv](Images/Csv_file.png)

Creating a OneHotEncoder instance
![onehotencoder](Images/One_encoder.png)

Fitting the model using 100 epochs and the training data
![fitmodel](Images/Fit_model.png)

Displaying the accuracy scores achieved by each model and comparing the results
![three_models](Images/Models.png)

Saving alternative models as an HDF5 file.
![altmodels](Images/Saved_models.png)

---

## License

MIT License

Copyright (c) 2022 Stephane Masyn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---
