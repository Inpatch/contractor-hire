

from web import create_app



# Create the Flask application soem
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    