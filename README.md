# Sport Management API

## Features
* CRUD for teams and players
* Support for 15,000+ records
* SQL performance optimization via indexes
* Automated Swagger UI documentation

## Tech Stack
* Python 3.x, FastAPI
* SQLAlchemy ORM
* Pydantic validation
* SQLite / PostgreSQL

## Project Structure
* `app/models.py` — Database tables and relationships
* `app/schemas.py` — Pydantic data validation
* `app/crud.py` — Database operations
* `app/main.py` — API routes and app entry point
* `schema.sql` — SQL table definitions
* `data_gen.sql` — Data generation and indexing

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
