from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('birthday_card.html', recipient_name="Sheep :3")

if __name__ == '__main__':
    app.run(debug=True)