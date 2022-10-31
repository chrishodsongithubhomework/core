from flask import Flask, request, Response
import json
import pprint
from actions import execute_functions

DEBUG=True

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handler():
  data = json.loads(request.data)
#  if DEBUG:
#    pp = pprint.PrettyPrinter(indent=2)
#    pp.pprint(data)

  event = request.headers.get('X-GitHub-Event', 'ping')
  if event == 'ping':
    return Response(status=200)

  if data["action"] != "created":
    return Response(status=200)

  # Do work
  print("got work to do")
  if execute_functions(data):
    return Response(status=200)
  else:
    return Response(status=500)

if __name__ == '__main__':
  app.run(debug=DEBUG, host='0.0.0.0', port=5000)
