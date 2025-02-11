# ReadyPath - URL Shortener

ReadyPath is a simple and efficient URL shortener that transforms long URLs into short, readable links like `domain.com/sophisticated-Crow`. Built with **Flask**, **MongoDB**, and containerized using **Docker** and **Docker Compose**, ReadyPath is designed to be easy to set up and use. It currently operates as an API, with the potential for a frontend interface in the future.

---

## Features
- **Short, Readable URLs**: Converts long URLs into short, human-readable links (e.g., `readyPath_domain/sophisticated-Crow`).
- **API-Based**: Accepts JSON input and returns the shortened URL in JSON format.
- **Containerized**: Easily deployable using Docker and Docker Compose.

---

## Technologies Used
- **Backend**: Flask (Python)
- **Database**: MongoDB (for URL storage) and SQLite (for token generation)
- **Containerization**: Docker and Docker Compose

---

## Getting Started

### Prerequisites
- Docker and Docker Compose installed on your machine.
- Python 3.x (if running from source).
- `pip` for installing Python dependencies.

---

### Running with Docker (Recommended)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/houndsec/readypath
   cd readypath
   ```

2. **Start the Containers**:
   Run the following command to spin up the Flask app and MongoDB containers:
   ```bash
   docker-compose up -d
   ```

3. **Access the API**:
   The Flask app will be running on `localhost:8000`. You can test the API using tools like `curl` or Postman.

---

### Running from Source

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/houndsec/readypath
   cd readypath
   ```

2. **Set Environment Variables**:
   Set the `MONGO_URI` environment variable to your MongoDB connection string:
   ```bash
   export MONGO_URI=mongodb://<MONGODB_URI_PATH>
   ```

3. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   Start the Flask development server:
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:5000`.

---

## API Usage

### Request
Send a POST request to the `/api` endpoint with the following JSON payload:
```json
{
  "url": "https://houndsec.net/"
}
```

### Response
The API will return a JSON response with the shortened URL:
```json
{
  "shortURL": "localhost:8000/sophisticated-Crow"
}
```

---

## Docker Compose File

The `docker-compose.yml` file defines two services:
1. **Flask App**: The Flask application that handles URL shortening.
2. **MongoDB**: The database used to store URLs.

```yaml
services:
  flask-app:
    build:
      context: .
    ports:
      - "8000:8000"
    depends_on:
      - mongo

  mongo:
    image: mongo:latest
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

---

## Project Structure
```
readypath/
├── app.py
├── dbms.py
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
├── utils.py
└── words.db
```

---

## Future Enhancements
- **Frontend Interface**: Add a web interface for easier interaction.
- **User Authentication**: Enable users to create accounts and manage their URLs.

---

## Contributing
Contributions are welcome! If you'd like to contribute to ReadyPath, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions or feedback, feel free to reach out:
- **Email**: mmdoha@houndsec.net 
- **GitHub**: [Monazir Muhammad Doha](https://github.com/itsmmdoha)

---

Happy shortening with ReadyPath! 🚀
