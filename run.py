from app import app
from app.models import init_db

if __name__ == "__main__":
    init_db()  # Initialize the database on first run
    app.run(debug=True)
