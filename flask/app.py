from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
        <h1>Hello, World!</h1>
        <a href="/form"><button>Go to Form</button></a>
    """)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        try:
            age = int(age)
            return f"<p>Hello, {name}! You are {age} years old.</p><a href='/'>Back to Home</a>"
        except ValueError:
            return "<p>Invalid age input. Please enter a number.</p><a href='/form'>Try Again</a>"
    return render_template_string("""
        <h2>Enter Your Info</h2>
        <form method="post">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br><br>
            <input type="submit" value="Submit">
        </form>
        <br>
        <a href="/"><button>Back to Home</button></a>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
