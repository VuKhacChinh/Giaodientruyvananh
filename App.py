from flask import Flask, render_template, request
from Model.model import model as md
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('test.html')

@app.route('/api', methods=['POST','GET'])
def testCV():
    if(request.method=='POST'):
        image_path = request.form.get('image_path');
        data = md(image_path);
        result = ""
        for dt in data:
            result = result + dt + " "
        return result
if(__name__=='__main__'): app.run()