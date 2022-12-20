from flask import Flask, render_template
import requests
import sys
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
