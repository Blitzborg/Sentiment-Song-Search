# Sentiment-Song-Search

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