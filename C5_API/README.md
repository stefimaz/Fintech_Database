# Financial Planning with APIs and Simulations

In this challenge, I have created two financial analysis tools in a single Jupyter notebook:

Part 1: A financial planner for emergencies. The members will be able to use this tool to visualize their current savings. The members can then determine if they have enough reserves for an emergency fund.

Part 2: A financial planner for retirement. This tool will forecast the performance of their retirement portfolio in 30 years. To do this, the tool will make an Alpaca API call via the Alpaca SDK to get historical price data for use in Monte Carlo simulations.

---

## Technologies

This project leverages python 3.7, APIs (Application Programming Interface) and SDK (Software Development Kits) to access current data.

Go to the homepage for Quandl at: https://www.quandl.com/ 
    (This is where you will acquire the QUANDL API Key)

GO to the homepage for ALPACA API Keys at: https://app.alpaca.markets/signup 
    (This is where you will acquire the ALPACA API Key and ALPACA SECRET KEY)

Once you acquire the API Keys, create and store the Keys in a .env file in Jupyter Lab with the following... 
    QUANDL_API_KEY = “Your Quandl API Key Here”
    ALPACA_API_KEY = “Your ALPACA API Key Here”
    ALPACA_SECRET_KEY = “Your ALPACA Secret Key Here”

Go to your terminal or git bash and run conda activate dev to activate your conda dev environment. 
You will then install the following librarie(s) and module(s) to run in Python codes creatd.

conda install -c anaconda requests
    (Helps you access data via APIs)
conda install -c jmcmurray json 
    (Puts the response from an API into a human-readable format)
pip install python-dotenv
    (Read key-value pairs from an environment file (.env) and add them as environment variables)
pip install alpaca-trade-api
    (Alpaca is an API for stock trading. With the Alpaca SDK, you can interact with the Alpaca API)

## Usage

Go to the Anaconda Prompt to launch JupyterLab by typing Jupyter Lab. To use this application simply clone the repository and run the financial_planning_tools.ipynb in you Jupyter Lab Notebook.

---

## Sample Visualizations

![image](https://user-images.githubusercontent.com/87351302/139186246-1c03fc0a-328c-4624-80b1-5e21e1dc29c9.png)
![image](https://user-images.githubusercontent.com/87351302/139185981-6c867552-8321-42ae-97a1-8143b3b25504.png)
![image](https://user-images.githubusercontent.com/87351302/139186087-63d0f6b0-d6ec-4ecc-b12e-9ad8c733399f.png)

---

## Contributors


[Stephane Masyn](https://www.linkedin.com/in/stephane-masyn-35b16817a/) [<img src="https://cdn2.auth0.com/docs/media/connections/linkedin.png" alt="LinkedIn -  Stephane Masyn" width=15/>](https://www.linkedin.com/in/stephane-masyn-35b16817a/)


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
