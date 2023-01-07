from flask import Flask, render_template
import requests
import sys
import pytrends
from pytrends.request import TrendReq
from datetime import datetime


app = Flask(__name__)


@app.route('/', methods=["GET"])

def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=G-KG1PQW1MWX"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-KG1PQW1MWX');
    </script>
    """
    return prefix_google + "Hello World"


@app.route('/logger', methods=["GET"])
def logger() :
    print('logger test')
    return 'check console' + render_template('logger.html')

@app.route('/googlerequest')
def reqGA():
    req = requests.get("https://www.google.com/")
    print(req)
    return req.cookies.get_dict()

@app.route('/GArequest')
def myreqGA():
    req = requests.get('https://analytics.google.com/analytics/web/#/a250417158p344237591')
    print(req)
    return req.text

@app.route('/chart')
def trend_charts():
    keywords=['ukraine', 'poutine', 'guerre']
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=keywords, timeframe='today 5-y', geo='FR')
    df = pytrends.interest_over_time()
    
    trend_1 = df[keywords[0]].tolist()
    trend_2 = df[keywords[1]].tolist()
    trend_3 = df[keywords[2]].tolist()
    dates = df.index.values.tolist()
    
    timestamp_in_seconds=[element/1e9 for element in dates]
    date= [datetime.fromtimestamp(element) for element in timestamp_in_seconds]
    days=[element.date() for element in date]
    months=[element.isoformat() for element in days]
    params = {
        "type": 'line',
        "data": {
            "labels": months,
            "datasets": [{
                "label": keywords[0],
                "data": trend_1,
                "borderColor": '#ffd966',
                "fill": 'false',
            },
            {
                "label": keywords[1],
                "data": trend_2,
                "borderColor": '#000000',
                "fill": 'false',
            },
            {
                "label": keywords[2],
                "data": trend_3,
                "borderColor": '#f44336',
                "fill": 'false',
            }
            ]
        }

    }
                                        
    prefix_chartjs = """
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
         <canvas id="myChart" width="1200px" height="700px"></canvas>""" + f"""
        <script>
        var ctx = document.getElementById('myChart');
        var myChart = new Chart(ctx, {params});
        </script>
        """
  
    return prefix_chartjs