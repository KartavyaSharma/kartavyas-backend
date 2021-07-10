from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir='./spec/')

app.add_api('specification.yml')

@app.route('/')
def home():
    """
    Static kartavys-backend page, responds to the "/" route
    :return:    Static welcome template 'home.html'
    """
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)