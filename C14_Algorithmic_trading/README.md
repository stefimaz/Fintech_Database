![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&width=1000&height=200&section=header&text=Algorithmic%20Trading%20&fontSize=30&fontColor=black)

<!-- header is made with: https://github.com/kyechan99/capsule-render -->

                                                             
<br>
Columbia FinTech Bootcamp Assignment - Challenge from Module 14

---

### Table of Contents

* [Overview](#overview)
* [Requirements](#requirements)
* [Data](#data)
* [Visualization](#visualization)
* [Evaluation Report](#evaluation-report)
* [License](#license)

---

## Overview [Table of Contents](#table-of-contents)


The program was designed to improve the existing algorithmic trading systems and maintain the firm’s competitive advantage in the market. In order to enhance the existing trading signals with machine learning algorithms that can adapt to new data, the following was accomplished...

* Establish a Baseline Performance

* Tune the Baseline Trading Algorithm

* Evaluate a New Machine Learning Classifier

* Create an Evaluation Report

---

## Requirements

This project leverages python 3.7 and scikit-learn.

A [conda](https://docs.conda.io/en/latest/) environment with liabraries listed below and [Jupyter Notebook/Lab](https://jupyter.org/) are required to run the code.

The following library was used:

1. [Scikit Learn](https://scikit-learn.org/stable/index.html) - Scikit Learn or Sklearn is one of the most used Python libraries for Data Science, along with others like Numpy, Pandas, Tensorflow, or Keras.


Install the following librarie(s) in your terminal...

    pip install -U scikit-learn

---

## Data

The data used in this neural network model was from derived from a CSV file called emerging_markets_ohlcv.csv:

---

## Visualization

Cumulative return plot that shows the actual returns vs. the strategy returns. 

Orignial window was 3 months.
![testing report_3_mo](Images/svm_3months.png)
![cumulative_return_plot_3_mo](Images/svmfig_3months.png)
Increase trading window to 6 months
![testing report_6_mo](Images/svm_6months.png)
![cumulative_return_plot_6_mo](Images/svmfig_6months.png) 
Increase trading window to 9 months
![testing report_9_mo](Images/svm_9months.png)
![cumulative_return_plot_9_mo](Images/svmfig_9months.png)
Decrease trading window to 1 months
![testing report_1_mo](Images/svm_1month.png)
![cumulative_return_plot_1_mo](Images/svmfig_1months.png)


---

## Evaluation Report

### Alternative ML Model and Evaluate Strategy Returns

#### Step 1: Tune the training algorithm by adjusting the size of the training dataset:

Answer the following question: What impact resulted from increasing or decreasing the training window?

By increasing the window, we have a better accuracy for the 6 months period but worst for the 9 months period. we can also see that the spread between the actual and the strategy returns is wilder. Meaning that at some point in the timeframe the strategy returns are much worst and at other much better. This suggest that increasing the window period increse the risk.

But by decreasing the window to 1 month, we get a more stable strategy that keep the same accuracy. This window also shows less risk as the strategy projection always stays above the actual returns.

#### Step 2: Tune the trading algorithm by adjusting the SMA input features.

Answer the following question: What impact resulted from increasing or decreasing either or both of the SMA windows?


### Side note

so far best is adabooster with 1 month window and SMA of 4 and 50

---

### Backtesting a new model to evaluate its performance:

Using the Logistic Regression Classifier gives the better results compare to the other classifiers.
![cumulative_return_plot](Images/Logisticreg_fig.png)

Did this new model perform better or worse than the provided baseline model?

This new model performed better in the long run. But it also present more risk compare to the provided baseline model.  

Did this new model perform better or worse than your tuned trading algorithm? 

The model performed the best with the window changed to 1 month and the SMA long changed to 50 (no changed in SMA short)
 
 
---

## License

MIT

Copyright (c) 2021 Stephane Masyn

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