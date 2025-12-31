# Sport Management System

This project is a comprehensive Sport Management System featuring a FastAPI web interface and a structured SQL database.

## Features
* **REST API**: Built with FastAPI for high performance.
* **Database Schema**: Structured SQL tables for Teams, Players, and Matches.
* **Data Generation**: SQL scripts to populate the database with 15,000 player records for testing.
* **Performance**: Database indexing implemented to speed up queries by salary and position.

## Project Structure
* `app/`: Contains the FastAPI application logic (main, models, schemas, crud, database).
* `schema.sql`: The database blueprint including table relationships and constraints.
* `data_gen.sql`: SQL script for bulk data generation.

## Setup and Execution
1. Install requirements:
   pip install fastapi uvicorn sqlalchemy
2. Initialize database:
   The application uses SQLite and will automatically create the database on first run.
3. Start the server:
   uvicorn app.main:app --reload
4. API Documentation:
   Access http://127.0.0.1:8000/docs for interactive testing.
