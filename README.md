# RedHerring Server
The server for the RedHerring project, run separately from the client   
[original repl](https://repl.it/@DashL/RedHerringServer)

## Running
**NOTE:** You probably don't want to just run the server, see the [RedHerring](https://www.github.com/dash-l/RedHerring) github repo for the full project
1. Install [poetry](https://github.com/python-poetry/poetry)
2. Run `poetry install`
3. Run the server with `poetry run python main.py`   
by default this puts the server on `0.0.0.0:5000` meaning port 5000 must be exposed to access the server externally.   
If you run the server somewhere other than the original repl, you will have to set an environment variable when running the client, see the README.md for the client for info.