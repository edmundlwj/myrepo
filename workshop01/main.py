from flask import Flask, render_template
import os, random

IMAGE_FOLDER = os.path.join('static')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

def random_sentence():
    sentences = ["Logic will get you from A to B. Imagination will take you everywhere.", "There are 10 kinds of people. Those who know binary and those who dont.", "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.", "It\'s not that I'm so smart, it\'s just that I stay with problems longer.", "It is pitch dark. You are likely to be eaten by a grue."]
    return str(random.choice(sentences))

@app.route("/")
def index():
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'kisspng-fortune-cookie-biscuits-chocolate-chip-cookie-chin.jpg')
        r_sentence = random_sentence()
        return render_template('index.html', user_image=full_filename, sentence=r_sentence)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
