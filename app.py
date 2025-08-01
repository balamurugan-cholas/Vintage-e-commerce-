from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql
import mysql.connector

app = Flask(__name__)
app.secret_key = 'thisisme'

@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
        cursor = db.cursor()

        cursor.execute("SELECT ID FROM user_details WHERE email = %s", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            print('already exist')
            flash('Username already exist', 'warning')
            return render_template('registerpage.html')
        else:
            sql = "INSERT INTO user_details (name, email, password) VALUES (%s, %s, %s)"
            val = (name, email, pwd)
            cursor.execute(sql, val)
            db.commit()
            flash('Account created sucessfull')
            return redirect('login')
    else:
        return render_template('registerpage.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
        cursor = db.cursor()
        cursor.execute("SELECT count(*) FROM user_details WHERE email = %s AND password = %s", (email,pwd))
        user = cursor.fetchone()[0]
        if user > 0:
            session['email'] = email
            flash('Login succesfull', 'success')
            return redirect(url_for('products'))
        
        elif email == 'murugan' and pwd == 'murugan':
            return redirect(url_for('dashboard'))
        
        else:
            flash('Invalid username and password', 'warning')
            return render_template('loginpage.html')
    else:
        return render_template('loginpage.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    db.commit()
    return render_template('dashboard.html', products=products)
        
@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        price = request.form['price']
        image = request.form['image']
        db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
        cursor = db.cursor()
        cursor.execute("INSERT INTO products (product_code, product_name, product_price, product_image) VALUES (%s, %s, %s, %s)", (code, name, price, image))
        db.commit()
        return redirect(url_for('add_product'))
    else:
        db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM products")
        products = mycursor.fetchall()
        return render_template('dashboard.html', products=products)

@app.route('/update-product', methods=['GET', 'POST'])
def update_product():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        price = request.form['price']
        image = request.form['image']
        db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
        cursor = db.cursor()
        cursor.execute("UPDATE products SET product_name = %s, product_price = %s, product_image = %s WHERE product_code = %s", (name, price, image, code))
        db.commit()
        return redirect(url_for('dashboard'))
    
@app.route('/delete-product/<int:code>', methods=['GET', 'POST'])
def delete_product(code):
    db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
    cursor = db.cursor()
    cursor.execute("DELETE FROM products WHERE product_code = %s", (code,))
    db.commit()
    return redirect(url_for('dashboard'))

@app.route('/products', methods=['GET', 'POST'])
def products():
    db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template('products.html', products=products)

@app.route('/cart', methods=['GET', 'POST'])
def add_to_cart():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        price = request.form['price']
        image = request.form['image']
        quantity = request.form['quantity']
        db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
        cursor = db.cursor()
        cursor.execute("INSERT INTO user_cart (product_code, product_name, product_price, product_image, product_quantity) VALUES (%s, %s, %s, %s, %s)", (code, name, price, image, quantity))
        db.commit()
        flash('Product added to cart', 'success')
        return redirect(url_for('add_to_cart'))
    else:
        db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user_cart")
        cart_items = cursor.fetchall()
        db.commit()
        cart_count = len(cart_items)
        total_price = sum(item[3] * item[5] for item in cart_items) 
        return render_template('cart.html', cart_items=cart_items, cart_count=cart_count, total_price=total_price) 

@app.route('/delete-cart/<int:code>', methods= ['GET', 'POST'])
def delete_cart(code):
    if request.method == 'POST':
        db = mysql.connector.connect(host='localhost', user='root', password='0321', database='vintage')
        cursor = db.cursor()
        cursor.execute('DELETE FROM user_cart WHERE product_code = %s', (code,))
        db.commit()
        return redirect(url_for('add_to_cart'))

if __name__ == '__main__':
    app.run(port=2000, debug=True)