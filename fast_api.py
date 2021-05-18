from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.route('/login')
# def login():
#     auth = request.authorization

#     if auth and auth.password == 'password':
#         token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=15)}, app.config['SECRET_KEY'])

#         return jsonify({'token' : token})

#     return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})