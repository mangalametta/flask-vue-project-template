from flask import Flask, request, render_template
from flask_cors import CORS
from waitress import serve


def response(code, message, data=None):
    # code=0 for success, code=1 for fail
    return {'code': code, 'message': message, 'data': data}


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        # I changed the jinja expression delimiter from {{...}} to %%...%%
        # because it conflicts with the Vue template syntax {{}}
        variable_start_string='%%',
        variable_end_string='%%',
    ))


app = CustomFlask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/get-info-from-backend', methods=['POST'])
def direction_control():

    data = request.get_json()
    text = data['text']
    resData = text + ' ,I got you back'
    return response(0, 'success', resData)

@app.route('/test', methods=['GET'])
def test():
    return response(0, 'success', "test")


def main():

    # for develop mode
    app.run(host='0.0.0.0', port=8080, debug=True)
    # for production mode
    # serve(app,host="0.0.0.0",port=8080)


if __name__ == "__main__":
    main()
