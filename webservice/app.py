from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Read sentence from config.txt
    with open('config.txt', 'r') as file:
        sentence = file.read().strip()
    return sentence

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
