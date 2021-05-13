# Sentiment-Song-Search

## Project Report

For the project report that was submitted, refer to Report.pdf

## Data crawling

#### data_collection.ipynb

Fetches for all song data like lyrics, artist info, etc

#### Song_data_prep.ipynb

For cleaning lyrics by removing info like [Verse 1], [Intro ], [Chorus ] etc.

Upload the data_collection notebooks on Google Colab

Click on each cell and press `Shift` + `Enter` to run

## Explicit Word Rating 

Install nltk library for python

```
pip install --user -U nltk
```
Ensure the dataset named Song_data_prep-L.csv is present in the same directory as explicit_word_removal.py file 

### To run the python scrip to generate explicit ratings

```
python explicit_word_removal.py
```
## Sentiment Analysis

Run the jupyter notebooks in the sentiment analysis folder on google colab in the order
 - data_analysis_and_preprocessing.ipynb
 - sentiment_analysis_ouput_generation.ipynb


## Indexing

No installation is required, the only pre-requisite is that JDK must be set up on your machine.

### To run Solr

Run the following command to start the Solr server:

```bash
cd solr
bin/solr start
```

To check if the Solr server is running, run the following command:

```bash
cd solr
bin/solr status
```

To access the Solr admin dashboard, visit [http://localhost:8983/solr](http://localhost:8983/solr)

Now queries to the database can be made by first selecting **Core Selector > songs** and then clicking on the **Query** tab.

## Client

### Setup

We use `virtualenv` to make sure the same python libraries are being used. To install `virtualenv`, run the following command:

```shell
pip3 install virtualenv
```

Once installed, run the following command to create and activate the virtual environment:

```shell
virtualenv env
source env/bin/activate
```

You should now be inside the virtual environment and can download the required libraries:

```shell
pip install -r requirements.txt
```

### Starting the client server

Run the following command and the client will be available at http://127.0.0.1:8051:

```shell
cd client
streamlit run app.py
```
