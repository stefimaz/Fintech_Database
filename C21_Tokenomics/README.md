![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&width=1000&height=200&section=header&text=KaseiCoin%20Tokenomics%20And%20Crowdsale&fontSize=30&fontColor=black)

<!-- header is made with: https://github.com/kyechan99/capsule-render -->

[Stephane Masyn](https://www.linkedin.com/in/stephane-masyn-35b16817a/) [<img src="https://cdn2.auth0.com/docs/media/connections/linkedin.png" alt="LinkedIn -  Stephane Masyn" width=15/>](https://www.linkedin.com/in/stephane-masyn-35b16817a/)
                                 

---

### Table of Contents

* [Overview](#overview)
* [Requirements](#requirements)
* [Evaluation Evidence](#Evaluation-Evidence)
* [License](#license)  

---

## Overview

Creation of a fungible token that is ERC-20 compliant and that will be minted by using a Crowdsale contract from the OpenZeppelin Solidity library.

The crowdsale contract created will manage the entire crowdsale process, allowing users to send ether to the contract and in return receive KAI, or KaseiCoin tokens. The contract will mint the tokens automatically and distribute them to buyers in one transaction.

I extended the crowdsale contract to enhance its functionality. To do so, I use the following OpenZeppelin contracts:

* CappedCrowdsale: This contract allows you to cap the total amount of ether that may be raised during your crowdsale.
* TimedCrowdsale: This contract allows you to set a time limit for your crowdsale by adding an opening time and a closing time.
* RefundablePostDeliveryCrowdsale: Every time you launch a crowdsale, you set a goal amount of ether to raise. If the goal is not reached, it is common practice to refund your investors. This contract adds this capability to a crowdsale.

---

## Requirements


This project leverages Solidity 0.5.0.
The file was opened and creadted using Remix IDE. 
The remix IDE can be access here: https://remix.ethereum.org

---

## Evaluation Evidence
 
### Screenshot of the contracts compiled:
#### Kaseicoin Contract Compiled.
![Kaseicoin Compiled](Images/Kaseicoin_compile.png)

#### KaseiCoinCrowdsale Contract Compiled.
![KaseiCoinCrowdsale](Images/KaseiCrowdsale1.png)

#### KaseiCoinCrowdsaleDeployer Contract Compiled.
![KaseiCoinCrowdsaleDeployer](Images/KaseiCrowdsale2.png)
  
### KaseiCoinCrowdsale With Enhance Functionality 
![Enhance Functionality](Images/Kasei_xtra_functionality.png)
![Enhance Functionality](Images/Kasei_xtra_functionality2.png)


## Short video demonstration. 
![5 ETH to account 2](Execution_Results/10eth_to_account2.png)


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
