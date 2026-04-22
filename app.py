from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
  return "Ai-Trust-Wall: System
  is Online. Secure Content Detection
  in Progress..."
  if __name__ == '__main__':
    app.run(debug=True)
