from flask import Flask, Request, render_template, request
from model import SpellCheckerModule


app = Flask(__name__)
spell_checker_module = SpellCheckerModule( )
@app.route('/')
def index():
    return render_template('index1.html')
@app.route('/spell',methods=['POST','GET'])
def spell():

    if request.method =='POST':
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)
        return render_template('index1.html',corrected_text=corrected_text)

@app.route('/grammar',methods=['POST','GET'])
def grammar():
    pass

#python main
if __name__== "__main__":
    app.run(debug=True)



