from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("index.html",num=1)

@app.route("/play/<int:num>")
def playwithtimes(num):
    return render_template("index.html",num=num)


@app.route("/play/<int:num>/<color>")
def playwithtimescolor(num,color):
    return render_template("index.html",num=num,color=color)

@app.errorhandler(404)
def not_found_error(error):
    return "404,Sorry! No response. Try again."
    

if __name__=="__main__": 
    app.run(debug=True)
