from flask import Flask
import os
import json
from init import create_app

app = create_app()

@app.route('/', methods=['GET'])
def fetch():
    return json.dumps({"success": True}), 200


if __name__ == '__main__':
    port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)
