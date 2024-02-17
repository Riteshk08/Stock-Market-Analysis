# stock_market
By: Ritesh Kushwaha


# Introduction
A pipeline project for getting the stock data from yfinance, pre-processing, post processing and doing analysis on it"


## Installation guide
Please install the files in [requirements.txt](requirements.txt) for the project execution.
> **Note**: To run the main program it is necessary to install all the required packages.
This can be done with the command:


```sh
pip3 install -r requirements.txt 
```


## Using the Scraper
To use the program use the following syntax:

```sh
python3 pipeline.py
```



## Resulting directory structure
stock_market

      ├── data
      │   ├── processed      <- The final, canonical data sets for modeling.
      │   └── raw            <- The original, immutable data dump.
      │
      ├── extract            <- Folder with the necessary files files for data extraction.
      |
      ├── load               <- folder with the necessary files files for data upload.
      │
      ├── transform          <- Folder with the necessary files files for data wrangling.
      |
      |── visualize          <- Folder with the necessary files for visualization of the data
      │
      ├── pipeline.py        <- Pipeline for successful execution.
      │
      │        
      ├── requirements.txt   <- The requirements for the project execution.
      │
      ├── .gitignore         <- Files to ignore by `git`.
      │
      │
      └── README.md          <- The top-level README for developers using this project.
