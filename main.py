from flask import Flask, request, render_template
from flask_cors import CORS
from waitress import serve


def response(code, message, data=None):
    # code=0 for success, code=1 for fail
    return {'code': code, 'message': message, 'data': data}


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_start_string='%%',
        variable_end_string='%%',
    ))


app = CustomFlask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)


@app.route('/')
def desktop():
    return "<p>Hello, World!</p>"
    # return render_template('desktop.html')

@app.route('/direction-control', methods=['POST'])
def direction_control():

    data = request.get_json()
    direction = data['direction']
    return response(0, direction)


def main():
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    # for develop mode
    app.run(host='0.0.0.0', port=8080, debug=True)
    # for production mode
    # serve(app,host="0.0.0.0",port=8080)


if __name__ == '__main__':
    main()