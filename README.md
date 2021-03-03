# Sentiment-Song-Search

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

Now queries to the database can be made by first selecting __Core Selector > songs__ and then clicking on the __Query__ tab.

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

Run the following command and the client will be available at http://127.0.0.1:8000:

```shell
python client/manage.py run server
```