from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)
app.jinja_env.auto_reload = True  # Отключаем кеширование шаблонов
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Автоматическая перезагрузка шаблонов

menu = {'Main Page': 'main', 'QR-code Generator': 'qr_code_generator', 'URL-shortener': 'url_shortener'}


@app.route('/')
def main():
    current_url = request.path

    context = {
        'menu': menu,
        'current_url': current_url
    }

    return render_template('index.html', **context)


@app.route('/qr-code-generator', methods=['GET', 'POST'])
def qr_code_generator():
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


@app.route('/url_shortener')
def url_shortener():
    current_url = request.path

    context = {
        'menu': menu,
        'current_url': current_url
    }

    return render_template('index.html', **context)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
