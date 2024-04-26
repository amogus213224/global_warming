from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')
#Вторая страница
@app.route('/<size>')
def lights(size):
    return render_template(
                            'eng.html', 
                            size=size
                           )


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_eng = request.form.get('button_eng')
    button_rus = request.form.get('button_rus')
    return render_template('index.html', button_eng=button_eng,
                           button_rus=button_rus)


if __name__ == "__main__":
    app.run(debug=True)