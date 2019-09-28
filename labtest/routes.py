from labtest import app
from flask import (
    jsonify
)

@app.route('/')
def index():
   return jsonify({
       "message": "Welcome to the Labtest Api"
   })

