from flask import Flask, render_template, request
import os

# Serve static files (images) from project root so existing images in RPG/ are available at /static/<name>
project_root = os.path.dirname(__file__)
app = Flask(__name__, template_folder=project_root, static_folder=project_root)


@app.route('/')
def index():
    # server-side list of available images (kept in project root so available at /static/<name>)
    images = [
        'dm-blok-a.png','dm-blok-b.png','dm-blok-c.png',
        'dm-chodba-a.png','dm-chodba-b.png','dm-krizovatka-a.png',
        'dm-krizovatka-b.png','dm-krizovatka-c.png','dm-start.png',
        'dm-souboj-a.png','dm-konec.png','player.png'
    ]

    rows = 6
    cols = 8

    return render_template('base.html', images=images, rows=rows, cols=cols)




@app.route('/next')
def next_page():
    # read the selected main image from query parameter 'main'
    main = request.args.get('main', 'dm-start.png')
    return render_template('next.html', main=main)


if __name__ == '__main__':
    app.run(debug=True)