import random
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

import infrastructure


server = Flask(__name__)
Bootstrap(server)


@server.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@server.route('/online', methods=['GET'])
def online():
    lyrics = infrastructure.get_lyrics()
    return render_template('view-online.html', lyrics=lyrics)


@server.route('/top', methods=['GET'])
def top():
    lyrics = sorted(infrastructure.get_lyrics(), key=lambda lyric: -lyric.rating)
    return render_template('view-top.html', lyrics=lyrics)


@server.route('/generate', methods=['POST', 'GET'])
def generate():
    infrastructure.generate_lyric(random.randint(15, 35))
    return redirect(url_for('online'))


@server.route('/rating', methods=['POST', 'GET'])
def rating():
    is_like = request.args.get('like', default=None, type=str)
    lyric_id = request.args.get('id', default=None, type=str)
    redirect_to = request.args.get('redirect', default='/', type=str)

    if all(map(lambda arg: arg is not None, [is_like, lyric_id])):
        is_like = is_like == 'yes'
        infrastructure.rating_lyric(lyric_id, 1 if is_like else -1)

    return redirect(url_for(redirect_to))


if __name__ == '__main__':
    server.run(
        host='0.0.0.0',
        threaded=True
    )
