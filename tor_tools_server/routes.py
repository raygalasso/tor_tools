from flask import current_app

app = current_app

import pandas as pd


@app.route('/echo',  methods=['GET', 'POST'])
def echo():
    return range(0,1024).join(',')


@app.route('/onions')
def onions():
    links = pd.read_json('onions.json')
    return links.to_html()
