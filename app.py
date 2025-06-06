from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GIPHY_API_KEY = 'JGCxj1CFfincbazSdrNYxmVPrAnVuwiN'

@app.route('/', methods=['GET', 'POST'])
def index():
    gifs = []
    if request.method == 'POST':
        query = request.form.get('query')
        url = 'https://api.giphy.com/v1/gifs/search'
        params = {
            'api_key': GIPHY_API_KEY,
            'q': query,
            'limit': 5,
            'rating': 'pg'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            gifs = [item['images']['original']['url'] for item in data['data']]
    return render_template('index.html', gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True)
