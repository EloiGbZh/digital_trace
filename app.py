from flask import Flask

def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=344237591"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', '344237591');
    </script>
    """
    return prefix_google + "Hello World"


app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    return "Hello World"
