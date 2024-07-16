# Flask Oracle Search API

This project is a Flask web server that provides a search endpoint to query an Oracle database using `cx_Oracle`. The application loads database connection settings from environment variables and exposes a `/search` endpoint that allows users to search for records in the database.

## Features

- **Search API**: Provides a `/search` endpoint to query the Oracle database.
- **Environment Configuration**: Uses `.env` file for configuration management.
- **Easy Setup**: Simple and straightforward setup process.

## Requirements

- Python 3.x
- Flask
- cx_Oracle
- Oracle Instant Client
- dotenv

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/flask-oracle-search-api.git
cd flask-oracle-search-api
```

### 2. Set Up Virtual Environment

Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project and add your Oracle database connection settings:

```
DB_USER=your_username
DB_PASS=your_password
DB_DSN=your_dsn
```

### 5. Run the Application

```sh
python app.py
```

The server will start running on `http://0.0.0.0:5000`.

## Usage

To search for records in the database, send a GET request to the `/search` endpoint with the `query` parameter.

### Example Request

```sh
curl -X GET "http://127.0.0.1:5000/search?query=John"
```

### Example Response

```json
[
    {
        "Name": "John Doe",
        "Age": 30,
        "Occupation": "Engineer"
    },
    {
        "Name": "Johnny Smith",
        "Age": 25,
        "Occupation": "Designer"
    }
]
```

## Project Structure

```
flask-oracle-search-api/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env                # Environment variables file
├── venv/               # Virtual environment
└── README.md           # Project README
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask: [Flask Documentation](https://flask.palletsprojects.com/)
- cx_Oracle: [cx_Oracle Documentation](https://oracle.github.io/python-cx_Oracle/)
- dotenv: [python-dotenv Documentation](https://saurabh-kumar.com/python-dotenv/)
