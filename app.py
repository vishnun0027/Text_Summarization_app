from flask import Flask, render_template, request, redirect, url_for
from Text_Summarization import Summarise_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    Text = ''
    prediction = ''
    if request.method == 'POST':
        Text = request.form['Text']
        # check Text is empty
        if Text == '':
            return redirect(url_for('index'))

        else:
            prediction = Summarise_text(Text)
    elif request.method == 'GET' and request.args.get('clear') == 'true':
        Text = ''
        prediction = ''
    return render_template('index.html',Text=Text, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
