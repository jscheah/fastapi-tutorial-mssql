# fastapi-tutorial-mssql
The FastAPI SQL database tutorial modified to use `mssql+pyodbc`.

Proof-of-concept that using FastAPI with mssql does *not* require
aioodbc and `async def` for path operation functions.

### How to run:

Create database backend
```bash
docker pull mcr.microsoft.com/mssql/server:2017-latest

docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Password_123" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-latest

```

Download and unzip to database folder
https://excelbianalytics.com/wp/wp-content/uploads/2020/09/5m-Sales-Records.zip

Load testing
```bash
docker pull grafana/k6

docker run --rm -i grafana/k6 run --vus 1 --duration 1s - <loadtesting/script.js

```

To launch uvicorn:
```bash
uvicorn sql_app.main:app --reload
```

Then load the fancy interactive docs page at

http://localhost:8000/docs

Details at

https://fastapi.tiangolo.com/tutorial/

and

https://fastapi.tiangolo.com/tutorial/sql-databases/

GitHub discussion:

https://github.com/sqlalchemy/sqlalchemy/issues/6521

Notes:

- You may need to tweak `SQLALCHEMY_DATABASE_URL` in database.py to connect
to your SQL Server instance.