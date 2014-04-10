# Standard Library
import os
import re
# Third Party Imports
from flask import Flask, render_template, request
import requests

SECRET_KEY = os.environ['SHOW_IMAGES_KEY']
# Regex from http://stackoverflow.com/a/169631
image_url_pattern = (r'https?://(?:[a-z\-]+\.)+[a-z]{2,6}'
                     r'(?:/[^/#?]+)+\.(?:jpg|gif|png)')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    key = request.args.get('key')
    url = request.args.get('url')
    if key and url and key == SECRET_KEY:
        response = requests.get(url)
        image_urls = re.findall(image_url_pattern, response.content)
        return render_template('index.html', url=url, image_urls=image_urls)
    else:
        return 'o_O'

if __name__ == '__main__':
    app.run(debug=False)