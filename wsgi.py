from waitress import serve
from main import app as application;
if __name__ == '__main__':
    
    serve(app, host="0.0.0.0", port=8080)
    # app.run(debug=True, port=8080)