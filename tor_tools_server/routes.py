from flask import current_app

app = current_app

import pandas as pd


@app.route('/echo',  methods=['GET', 'POST'])
def echo():
    return range(0,1024).join(',')


