from flask import Blueprint, flash, Markup, redirect, render_template, url_for, send_file

from .forms import TickerForm
from .models import db, query_to_list, Site, Visit
from flask import request

import requests
import pandas as pd
from bokeh.plotting import figure, output_file, show

tickering = Blueprint("tickering", __name__)


@tickering.route("/")
def index():
    form = TickerForm()
    return render_template("EIA consumption.html",
                           site_form=form)


@tickering.route("/site", methods=("POST", ))
def get_symbol():
    form = TickerForm()
    if form.validate_on_submit():
        #site = Site()
        input = request.form['ticker']
        #db.session.add(site)
        #db.session.commit()
        flash("Added symbol")

        stock_df = get_data(input)
        plot(stock_df)
        
        return redirect("graph")

    return render_template("validation_error.html", form=form)

@tickering.route('/graph')
def plot_graph():
    return send_file('stockprice.html')


#curl "https://www.quandl.com/api/v3/datasets/EOD/FB/data.json?api_key=CSjTxPyAissHWqvzh6xg"

#_url = 'https://www.quandl.com/api/v3/datasets/EOD/FB/data.json'
_url = 'https://eodhistoricaldata.com/api/eod/'

def get_data(input):
        request = {
            'period': 'd',
            'api_token': '5d7ec51f1d4af6.29036934',
            #'SYMBOL_NAME': input
            'from': '2019-08-13',
            'to': '2019-09-13',
            'fmt': 'json'
        }

        #eod_data_json = [{'date': '2019-08-13', 'open': 185.52, 'high': 191.38, 'low': 185.37, 'close': 188.45, 'adjusted_close': 188.45, 'volume': 13577000}, {'date': '2019-08-14', 'open': 185.8, 'high': 185.99, 'low': 179.31, 'close': 179.71, 'adjusted_close': 179.71, 'volume': 18903700}, {'date': '2019-08-15', 'open': 180.95, 'high': 183.2, 'low': 180.03, 'close': 182.59, 'adjusted_close': 182.59, 'volume': 12925900}, {'date': '2019-08-16', 'open': 183.75, 'high': 185.1, 'low': 182.36, 'close': 183.7, 'adjusted_close': 183.7, 'volume': 12654600}, {'date': '2019-08-19', 'open': 186.01, 'high': 187.5, 'low': 184.85, 'close': 186.17, 'adjusted_close': 186.17, 'volume': 9691200}, {'date': '2019-08-20', 'open': 185.45, 'high': 186, 'low': 182.39, 'close': 183.81, 'adjusted_close': 183.81, 'volume': 10083400}, {'date': '2019-08-21', 'open': 185, 'high': 185.9, 'low': 183.14, 'close': 183.55, 'adjusted_close': 183.55, 'volume': 8398200}, {'date': '2019-08-22', 'open': 183.43, 'high': 184.11, 'low': 179.91, 'close': 182.04, 'adjusted_close': 182.04, 'volume': 10821400}, {'date': '2019-08-23', 'open': 180.84, 'high': 183.13, 'low': 176.66, 'close': 177.75, 'adjusted_close': 177.75, 'volume': 17323400}, {'date': '2019-08-26', 'open': 179.4, 'high': 180.5, 'low': 178.24, 'close': 180.36, 'adjusted_close': 180.36, 'volume': 8773600}, {'date': '2019-08-27', 'open': 181.93, 'high': 184.04, 'low': 181.01, 'close': 181.3, 'adjusted_close': 181.3, 'volume': 14399600}, {'date': '2019-08-28', 'open': 180.53, 'high': 181.95, 'low': 178.92, 'close': 181.76, 'adjusted_close': 181.76, 'volume': 9386100}, {'date': '2019-08-29', 'open': 183.77, 'high': 186.08, 'low': 183.47, 'close': 185.57, 'adjusted_close': 185.57, 'volume': 10128700}, {'date': '2019-08-30', 'open': 186.78, 'high': 186.8, 'low': 183.46, 'close': 185.67, 'adjusted_close': 185.67, 'volume': 10774500}, {'date': '2019-09-03', 'open': 184, 'high': 185.67, 'low': 182.11, 'close': 182.39, 'adjusted_close': 182.39, 'volume': 9779400}, {'date': '2019-09-04', 'open': 184.65, 'high': 187.75, 'low': 183.89, 'close': 187.14, 'adjusted_close': 187.14, 'volume': 11308000}, {'date': '2019-09-05', 'open': 188.53, 'high': 191.36, 'low': 187.94, 'close': 190.9, 'adjusted_close': 190.9, 'volume': 13876700}, {'date': '2019-09-06', 'open': 190.21, 'high': 190.21, 'low': 186.35, 'close': 187.49, 'adjusted_close': 187.49, 'volume': 15219500}, {'date': '2019-09-09', 'open': 187.73, 'high': 188.98, 'low': 185.85, 'close': 188.76, 'adjusted_close': 188.76, 'volume': 14722400}, {'date': '2019-09-10', 'open': 187.44, 'high': 188.1, 'low': 184.55, 'close': 186.17, 'adjusted_close': 186.17, 'volume': 15455900}, {'date': '2019-09-11', 'open': 186.46, 'high': 189.44, 'low': 186.08, 'close': 188.49, 'adjusted_close': 188.49, 'volume': 11761700}, {'date': '2019-09-12', 'open': 189.86, 'high': 190.93, 'low': 187.23, 'close': 187.47, 'adjusted_close': 187.47, 'volume': 11419800}, {'date': '2019-09-13', 'open': 187.33, 'high': 187.97, 'low': 186.54, 'close': 187.19, 'adjusted_close': 187.19, 'volume': 11297800}]

        eod_data = requests.get(_url+input.upper()+'.US', params=request)
        eod_data_json = eod_data.json()
        print('after api call:')
        print(eod_data_json)
        stock_df = pd.DataFrame()
        stock_df['closing_price'] = [db_item["close"] for db_item in eod_data_json]
        stock_df['date'] = [db_item["date"] for db_item in eod_data_json]
        stock_df['date'] = pd.to_datetime(stock_df['date'])
        #stock_df['closing_price'] = [db_item["close"] for db_item in response.json()]
        #stock_df['date'] = [db_item["date"] for db_item in response.json()]
        #stock_df['date'] = pd.to_datetime(stock_df['date'])
        #p.line(stock_df['date'], stock_df['closing_price'], color='navy', alpha=0.5)
        return stock_df

def plot(df):
    
    output_file("templates/stockprice.html")
    p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")
    p.line(df['date'], df['closing_price'], color='navy', alpha=0.5)
    show(p)
    return 


