from flask import Flask, render_template, request, send_file, redirect
import qrcode
from io import BytesIO
from redis import Redis

from helpers import generate_link, recursion_generate_check

app = Flask(__name__)
app.jinja_env.auto_reload = True  # Отключаем кеширование шаблонов
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Автоматическая перезагрузка шаблонов

menu = {'Main Page': 'index', 'QR-code Generator': 'qr_code_generator', 'URL-shortener': 'url_shortener'}

redis_db = Redis(host='localhost', port=6379)

@app.route('/')
def index():
    redis_db.incr('hits')
    return 'This page has been visited {} times.'.format(redis_db.get('hits'))

@app.route('/qr-code-generator', methods=['GET', 'POST'])
def qr_code_generator():
    """generates qr-codes"""
    if request.method == 'POST':
        text = request.form['text']
        img = qrcode.make(text)
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')

    current_url = request.path

    context = {
        'menu': menu,
        'current_url': current_url
    }

    return render_template('qrcodegenerator.html', **context)


@app.route('/url_shortener', methods=['GET', 'POST'])
def url_shortener():
    """Adds to Redis user's data for redirect"""

    if request.method == 'POST':
        user_link = request.form['user_link']

        if redis_db.exists(user_link):
            key = redis_db.get(user_link).decode('utf-8')

            return f'{request.host_url}{key}'

        if user_link:
            generate_path = recursion_generate_check(generate_link(), redis_db)

            redis_db.set(user_link, generate_path, ex=2592000)
            redis_db.set(generate_path, user_link, ex=2592000)
            return f'{request.host_url}{generate_path}'
        return 'bad request', 400

    current_url = request.path

    context = {
        'menu': menu,
        'current_url': current_url
    }

    return render_template('urlshortener.html', **context)


@app.route('/<string:short_url>', methods=['GET'])
def url_redirect(short_url):
    """redirect for url_shortener"""

    if redis_db.exists(short_url):
        redirect_uri = redis_db.get(short_url).decode('utf-8')
        return redirect(redirect_uri)
    if not short_url or not redis_db.exists(short_url):
        return redirect('url_shortener')



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
