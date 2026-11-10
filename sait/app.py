from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Обязательно добавьте doctype и закрывающие теги
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>типо сайт</title>
    </head>
    <body>
        <h1>Эмик</h1>
        <p>я тебя хочу</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)