from flask import Flask, jsonify, render_template, request, redirect, session, url_for, send_from_directory
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
import MySQLdb.cursors
import datetime
import shutil
import Main
import AWS
import os

insert_query = 'INSERT INTO users VALUES (%s, %s, %s)'
select_query = 'SELECT * FROM users WHERE user_name = %s and user_password = %s'
search_query = 'SELECT * FROM users WHERE user_name = %s'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['TEMP_FOLDER'] = 'temp/'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = ['.png', '.jpg', '.jpeg', '.gif']
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app.secret_key = 'ecs-project'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        values = (username, password)

        query.execute(select_query, values)

        user_details = query.fetchone()

        if user_details:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = user_details['user_name']
            return redirect(url_for('home'))

        else:
            msg = 'Failed. Incorrect username/password....!!'

    return render_template('login.html', data=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        query = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        values = (username, )

        query.execute(search_query, values)

        user_details = query.fetchone()

        if user_details:
            msg = 'Already an user exits with same user name'

        else:
            try:
                values = (username, password, email)

                query.execute(insert_query, values)
                msg = 'Account registered successfully'
                mysql.connection.commit()

            except MySQLdb.IntegrityError:
                msg = 'Given Email is Already in use'

    return render_template('register.html', data=msg)


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('username', None)

    return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/file-upload', methods=['GET', 'POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = ''
        try:
            file = request.files['file']
            filename = secure_filename(file.filename)
            # filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            filepath = os.path.join(app.config['TEMP_FOLDER'], filename)

            # checking if file is uploaded or not
            if file:
                extension = os.path.splitext(filename)[1].lower()
                msg = ''
                if extension in app.config['ALLOWED_EXTENSIONS']:
                    file.save(filepath)
                    if AWS.isBird(filepath):
                        result = Main.predict(filepath)
                        Main.sendMessage("A Bird is detected and Name is : {}".format(result))
                        Main.sendPhoto(filepath)
                        msg = f'The Bird name is %- 30s and uploaded file is {filename}' % (
                            result)
                        try:
                            shutil.move(filepath, app.config['UPLOAD_FOLDER'])
                            # msg = 'file uploaded successfully.....!!!'

                        except shutil.Error:
                            pass
                            # msg = 'File already exits in destination folder'

                    elif(AWS.isHuman(filepath)):
                        msg = 'A human is detected'
                        Main.sendMessage(msg)
                        Main.sendPhoto(filepath)
                        try:
                            shutil.move(filepath, app.config['UPLOAD_FOLDER'])
                        # msg = 'file uploaded successfully.....!!!
                        except shutil.Error:
                            pass
                            # msg = 'File already exits in destination folder'
                    else:
                        msg = 'An Object movement is detected'
                        Main.sendMessage(msg)
                        Main.sendPhoto(filepath)
                        try:
                            shutil.move(filepath, app.config['UPLOAD_FOLDER'])
                        except shutil.Error:
                            pass
                    resp = jsonify({'message': msg})
                    # logging the data
                    with open('logs.txt', 'a') as f:
                        now = datetime.datetime.now().strftime('%H:%M:%S %d/%m/%y')
                        log = f'[{now}]   {msg} \n'
                        f.write(log)
                    resp.status_code = 201
                    return resp
                else:
                    msg = 'Please upload an image file. Allowed extensions are .png, .jpg, .jpeg, .gif'

            else:
                msg = 'Please Select a File'

        # catching request entity too large exception
        except RequestEntityTooLarge:
            msg = 'Failed to upload. selected file is Grater than 2MB'

    else:
        resp = jsonify(
            {'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


@app.route('/result', methods=['GET', 'POST'])
def result():
    filename = ''
    try:
        file = request.files['image']
        filename = secure_filename(file.filename)
        # filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        filepath = os.path.join(app.config['TEMP_FOLDER'], filename)

        # checking if file is uploaded or not
        if file:
            extension = os.path.splitext(filename)[1].lower()

            if extension in app.config['ALLOWED_EXTENSIONS']:
                file.save(filepath)
                if AWS.isBird(filepath):
                    result = Main.predict(filepath)
                    Main.sendMessage("The Bird Name is : {}".format(result))
                    Main.sendPhoto(filepath)
                    msg = f'The Bird name is %- 30s and uploaded file is {filename}' % (
                        result)
                    try:
                        shutil.move(filepath, app.config['UPLOAD_FOLDER'])
                        # msg = 'file uploaded successfully.....!!!'

                    except shutil.Error:
                        pass
                        # msg = 'File already exits in destination folder'

                else:
                    msg = 'Uploaded image doesn\'t countian a bird'
                    Main.sendMessage(msg)
                    Main.sendPhoto(filepath)

            else:
                msg = 'Please upload an image file. Allowed extensions are .png, .jpg, .jpeg, .gif'

        else:
            msg = 'Please Select a File'

    # catching request entity too large exception
    except RequestEntityTooLarge:
        msg = 'Failed to upload. selected file is Grater than 2MB'

    # logging the data
    with open('logs.txt', 'a') as f:
        now = datetime.datetime.now().strftime('%H:%M:%S %d/%m/%y')
        log = f'[{now}]   {msg} \n'
        f.write(log)

    return render_template('result.html', data=msg, image=filename)


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    images = list()

    for filename in files:
        extension = os.path.splitext(filename)[1].lower()

        if extension in app.config['ALLOWED_EXTENSIONS']:
            images.append(filename)

    return render_template('gallery.html', images=images)


@app.route('/log', methods=["GET", "POST"])
def view_log():
    log = list()
    with open('logs.txt', 'r') as f:
        log.append(f.read())

    return render_template('log.html', log=log)


@app.route('/display-image/<filename>', methods=['GET', 'POST'])
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
