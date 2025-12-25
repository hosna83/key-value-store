# key-value-store

A lightweight in-memory key-value store built with FastAPI, allowing you to store and retrieve data via a simple API. Ready to run with Docker.

### API Endpoints:

- 📝 **POST /set** → store a key-value pair
- 🔍 **GET /get/{key}** → retrieve value by key
- 📄 **Swagger documentation** available at `/docs`
- 🚀 **Lightweight and easy to deploy with Docker**



### Run with Docker

```bash
docker build -t key-value-store .
docker run -p 8000:8000 key-value-store

Access the API: http://localhost:8000
Swagger docs: http://localhost:8000/docs

- ⚠️ **Data is stored in memory**, so it will be lost when the app stops.
- 🔑 **Keys must be non-empty strings.**
- 🔄 **Each key stores a single value**; overwriting is allowed.
- ❌ **Requests for non-existing keys return 404 Not Found.**


### Install Dependencies 

The project requires Python 3.9 and the following main packages (listed in requirements.txt):

- **FastAPI** – for building the REST API
- **Uvicorn** – for running the ASGI server
