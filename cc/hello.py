from flask import Flask, render_template

from cc.db import TodoDb

app = Flask(__name__)
@app.route('/')
def index():
    db=TodoDb()
    todo=db.read_all()
    return render_template('index.html',data=todo)
if __name__=='__main__':

    app.run(debug=True);