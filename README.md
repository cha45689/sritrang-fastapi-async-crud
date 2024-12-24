# sritrang-fastapi-async-crud
This is repository to host take home assignment interview of **STA group**

### Assignment
Create **FastAPI** application which manage "Items" asynchronously consist of **CRUD** operation

# Development Setup & How to run
1. Install python package for developement
    <br>
    pre-requisite
    - python=3.11
```bash
pip install -r dev-requirements.txt
```
2. Run server using fastapi
```bash
fastapi run app/application/main.py
```
3. Setup pre-commit hooks **(Optional)**
```bash
pre-commit install
```

# How to run using Docker
please install docker and docker compose before running the snippet in terminal
```bash
docker compose build
docker compose up
```

# API usage examples
Please use swagger to try it out or please import from file item_crud.postman_collection.json

# How to test
run test using local environment
```cli
pytest --cov=app
```

# Additional Caveat
* Do not use SQLite memory when deploy multiple worker there seem to be some kind of instability
* in case you want persist database please mount database file to docker or modify code to accept other source to your liking