# import flask
from flask import Flask, request, render_template, make_response, session 
app = Flask(__name__)
app.secret_key = "abcdefghijklmnopqrstuvwxyz"


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/score', methods=['GET','POST'])
def addscore():
  session['score'] += 1
  return str(session['score'])

@app.route('/game')
def gameset():
  print(request.cookies.get('score'))
  if 'score' not in session:
    session['score'] = 0
  if request.method == 'POST':
    print('im working')
    resp = make_response(render_template('game.html', score='0'))
    return resp
  return render_template('game.html', score=session['score'])

# @app.route('/score', methods=['POST'])
# def addscore():
#   intscore = int(request.cookies.get('score'))
#   intscore += 1 
#   request.cookies['score'] = str(intscore)
#   return request.cookies.get('score')

@app.route('/settings')
def setting():
  return render_template('settings.html')

@app.route('/backset', methods=['POST'])
def backsetting():
  if request.method =='POST':
    form = request.form
    response = make_response(render_template('game.html', score=session['score']))
    response.set_cookie('backcol', form['backcol'])
    response.set_cookie('gamecol', form['gamecol'])
    response.set_cookie('objecturl', form['objecturl'])
    response.set_cookie('fontcol', form['fontcol'])
    return response 

print("hello world")

app.run(host = '0.0.0.0', port = 5555)
