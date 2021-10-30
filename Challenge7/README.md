# ETF Analyzer

In this Challenge assignment, I build a financial database and web application by using SQL, Python, and the Voilà library to analyze the performance of a hypothetical fintech ETF. 

---

## Technologies

This project leverages python 3.7 with the following libraries:


* [pandas](https://pandas.pydata.org/docs/) - For Pandas Documentation

* [numpy](https://numpy.org/doc/) - For numpy Documentation

* [hvplot](https://hvplot.holoviz.org/) - For hvplot Documentation

* [sqlalchemy](https://docs.sqlalchemy.org/en/14/) - For sqlalchemy Documentation

* [Voilà](https://voila.readthedocs.io/en/stable/) - For voila Documentation

---

## Installation Guide For Voila

To install Voila, open a terminal window, and complete the following steps.

1 Activate your Conda "dev" environment

2 Run the following command
```python
  conda install -c conda-forge voila
```

3 Confirm that the installation succeeded by running the following command
```python
  conda list voila
```
If Voila successfully installed, a similar terminal window as the following image shows
 [Voila install confirmation](Images/voila_install_confirm.png)

---

## Usage

To use EFT Analyser Notebook simply open the **etf_analyser.ipynb** file in Jupyter.

I also used a Python library named Voila to build interactive web applications directly from the Jupyter notebooks. 

The Voilà library works only with Jupyter notebooks on localhost.


---

## Run Voila In The terminal

Voilà accepts a path to the notebook and then generates a web app with any visualizations or output that were generated in the Jupyter notebook. The code is simple:
```shell
voila <relative-path-to-notebook>
```

this screenshot (or video) of the deployed application using Voila.

![voila localhost image](Images/Voila_record.mov)

---

## Contributors

Brought to you by Stephane Masyn

Stefimaz@gmail.com

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
