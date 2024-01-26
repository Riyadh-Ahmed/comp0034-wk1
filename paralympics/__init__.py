from flask import Flask, render_template_string, request

app = Flask(__name__)

html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World App</title>
</head>
<body>
    <h1>Welcome to the Hello World App!</h1>
    <form method="post">
        <label for="user_name">Enter your name:</label>
        <input type="text" id="user_name" name="user_name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # Get the user's name from the submitted form
        user_name = request.form['user_name']
        return f'Hello {user_name}! welcome to the paralympics app'

    # Render the HTML form for GET requests
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)