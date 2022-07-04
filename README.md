# Glints Backend Evaluation

The project is described in the Github Gist [here](https://gist.github.com/seahyc/97b154ce5bfd4f2b6e3a3a99a7b93f69)

# Run the server
Go to the root directory of the project and run the following command:
```
$ docker compose -p glints up -d
```
Wait a few seconds for the server to start and we can start digging. To check if the servers are running, run the following command:
```
$ docker ps
```
To see logs, run the following command:
```
$ docker logs -f glintsevalbackend
```

# Run ETL script
Go to the root directory of the project and run the following command:
```
$ python3 ingest.py
```

The API Documentation is available at [Postman Link](https://documenter.getpostman.com/view/12416836/UzJFxK91)