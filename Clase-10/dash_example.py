from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)
app.layout=html.Div("hello")



if __name__ =="__main__":
    app.run_server(port=8051)


#another way
#from dash import html
#from jupyter_dash import JupyterDash
#
#app = JupyterDash(__name__)
#app.layout = html.Div("Hello")
#
#if __name__ =="__main__":
#    app.run_server(mode="inline")