from flask import(
  Flask,
  render_template
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
  """
  This function just response the browser URL
  localhost:5000/

  :return       The rendered template 'home.html'
  """
  return render_template('home.html')

# If we are running in stand alone application
if __name__ == '__main__':
  app.run(debug=True)