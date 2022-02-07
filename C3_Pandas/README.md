![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&width=1000&height=200&section=header&text=Bitcoin%20Arbitrage%20&fontSize=30&fontColor=black)

<!-- header is made with: https://github.com/kyechan99/capsule-render -->

[Stephane Masyn](https://www.linkedin.com/in/stephane-masyn-35b16817a/) [<img src="https://cdn2.auth0.com/docs/media/connections/linkedin.png" alt="LinkedIn -  Stephane Masyn" width=15/>](https://www.linkedin.com/in/stephane-masyn-35b16817a/)
                                 

---

### Table of Contents

* [Overview](#overview)
* [Requirements](#requirements)
* [Visualization](#visualization)
* [License](#license)  

---

## Overview

Looking over historical data value of Bitcoin during the first three months of 2018 (January, February and March) on two different exchanges: Bitstamp and Coinbase. 


The goal is to Collect CSV data in a Jupyter notebook file.
Prepare the datasets for analysis by cleaning missing and erroneous data.
Analyze the data at a high level through summary statistics and visualizations.
Use this information to select areas for deeper analysis.
Differentiate between early in the timeframe and later in the timeframe.
Specifically, selecting time periods in which to identify arbitrage opportunities.

Analyzing data over 2 different monthy period in 2018: from January 01 to January 31 and from March 01 to March 31.
Analyzing data over 3 specific days: January 16, February 24 and March 26. 

After analyzing the data, we can see the arbitrage between Coinbase and Bitstamp was possible to be realized with a profit early on but disapeared with time.  

---

## Requirements

This project leverages python 3.7 with the following libraries:

* [condas](https://docs.conda.io/en/latest/) - For condas informations

* [Path](https://docs.python.org/3/library/pathlib.html) - For informations

* Matplotlib

To use Bitcoin arbitrage Notebook simply open the **crypto_arbitrage.ipynb** file in Jupyter.

---
## Visualisation
### Bitcoin price difference between 2 exchanges
<img width="1165" alt="Screen Shot 2022-02-04 at 3 00 45 PM" src="https://user-images.githubusercontent.com/89653430/152595754-737266b1-ee83-4898-9746-8f5911be23b1.png">

### Trades profits 
<img width="514" alt="Screen Shot 2022-02-04 at 3 02 00 PM" src="https://user-images.githubusercontent.com/89653430/152595850-7a6dd93d-e6c1-48ba-991e-e5551b0b9e47.png">



---


## License

MIT License

Copyright (c) [2021] [Stepahe_Masyn]

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
