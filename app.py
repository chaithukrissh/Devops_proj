# from flask import Flask, jsonify , render_template

# app = Flask(__name__)

# # Sample menu data (replace this with your actual menu data)
# menu_items = [
#     {
#         'id': 1,
#         'name': 'Dish 1',
#         'description': 'A delicious dish',
#         'price': 10.99
#     },
#     {
#         'id': 2,
#         'name': 'Dish 2',
#         'description': 'Another tasty dish',
#         'price': 12.99
#     }
# ]

# @app.route('/')
# def get_menu():
#     return render_template("index.html")

# if __name__ == '__main__':
#     app.run()



# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Dummy user data (replace with a proper user authentication system)
# users = [
#     {'username': 'user1', 'password': 'password1'},
#     {'username': 'user2', 'password': 'password2'},
# ]

# @app.route('/api/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')

#     # Check if the username and password match a user in the database
#     for user in users:
#         if user['username'] == username and user['password'] == password:
#             return jsonify({'message': 'Login successful'})
    
#     return jsonify({'message': 'Login failed'})

# if __name__ == '__main__':
#     app.run()





















#from flask import Flask, render_template, request, redirect, url_for
#from flask_cors import CORS
#app = Flask(__name__)
# CORS(app)
#CORS(app, origins=['http://localhost:5000/login_test'])

# Dummy user data (replace with a proper user authentication system)
#users = [
#    {'username': 'user1', 'password': 'password1'},
#    {'username': 'user2', 'password': 'password2'},
#]

#@app.route('/')
#def home():
    # Render the login.html template
#    return render_template('index.html')

#@app.route('/login', methods=['GET', 'POST'])  # Allow both GET and POST requests
#def login():
#    if request.method == 'POST':
#        # print(request.form)
#        username = request.form['username']
#        password = request.form['password']

        # print(f'Received username: {username}')
        # print(f'Received password: {password}')

        # Check if the username and password match a user in the database
 #       for user in users:
#            if user['username'] == username and user['password'] == password:
#                return 'Login successful'  # You can redirect or return a success response
##
#        return 'Login failed'  # You can handle this as needed

    # If it's a GET request (initial page load), render the login.html template
#    return render_template('index.html')

#@app.route('/login_test', methods=['POST'])
#def test():
#    print('Received POST request')
#    print(request.get_json())  # Print received data
#    return 'Test route for POST requests'
#
#if __name__ == '__main__':
#    app.run()


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In a real application, you would store user credentials securely (e.g., in a database).
# This example uses a simple dictionary for demonstration purposes.
# Replace this with your actual user authentication logic.
Admins = {
    'Chaithu': '1234',
    'Mani': '1234',
}

users = {
    'Shekhar': '5678',
    'Pavan': '5678',
}



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_for_admins', methods=['POST'])
def loginforadmins():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username and password match (replace this with your authentication logic).
    if username in Admins and Admins[username] == password:
        return  redirect(url_for('homeforadmins'))
    else:
        return redirect(url_for('homeforerrosforadmins'))
    




@app.route('/homeforadmins')
def homeforadmins():
    return render_template('admins-homepage.html')



@app.route('/homeforerrosforadmins')
def homeforerrorsforadmins():
    return f'Hello You credentials do not match with our admins database !! please check it once'


@app.route('/login_for_users', methods=['POST'])
def loginforuser():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username and password match (replace this with your authentication logic).
    if username in users and users[username] == password:
        return  redirect(url_for('homeforuser'))
    else:
        return redirect(url_for('homeforerrorforusers'))
@app.route('/homeforuser')
def homeforuser():
    return render_template('home.html')

@app.route('/homeforerroforusers')
def homeforerrorforusers():
    return f'Hello You credentials do not match with our Users database !! please contact your Admins once'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

