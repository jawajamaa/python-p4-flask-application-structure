from flask import Flask
# from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

    # resp = make_response('<h1>Welcome to my page!</h1>', 200)
    # print(resp)

    # return resp
    

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
