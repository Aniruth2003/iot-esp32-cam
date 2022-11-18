from flask import Flask, render_template, request, send_from_directory
from werkzeug.exceptions import RequestEntityTooLarge 
from werkzeug.utils import secure_filename
import datetime
# import Main
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = ['.png', '.jpg', '.jpeg', '.gif']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result() :
    filename=''
    try :
        file = request.files['image']
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # checking if file is uploaded or not
        if file:
            extension = os.path.splitext(filename)[1].lower()

            if extension in app.config['ALLOWED_EXTENSIONS']:
                file.save(filepath)
                
                # result = Main.predict(filepath)
                # Main.sendMessage("The Bird Name is : {}".format(result))
                # Main.sendPhoto(filepath)
                msg = 'file uploaded successfully.....!!!'
                # msg = f'The Bird name is %-30s and uploaded file is {filename}' %(result)

            else:
                msg = 'Please upload an image file. Allowed extensions are .png, .jpg, .jpeg, .gif'

        else:
            msg = 'Please Select a File'

    # catching request entity too large exception
    except RequestEntityTooLarge :
        msg = 'Failed to upload. selected file is Grater than 2MB'

    # logging the data
    with open('logs.txt','a') as f:
        now = datetime.datetime.now().strftime('%H:%M:%S %d/%m/%y')
        log = f'[{now}] {msg} \n'
        f.write(log)

    return render_template('result.html', data = msg, image=filename)

@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    files=os.listdir(app.config['UPLOAD_FOLDER'])
    images=list()

    for filename in files:
        extension = os.path.splitext(filename)[1].lower()

        if extension in app.config['ALLOWED_EXTENSIONS'] :
            images.append(filename)
    
    return render_template('gallery.html', images=images)

@app.route('/log', methods=["GET", "POST"])
def view_log():
    log = list()
    with open('logs.txt','r') as f:
        log.append(f.read())
        
    return render_template('log.html', log=log)

@app.route('/display-image/<filename>', methods=['GET', 'POST'])
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__' : 
    app.run(debug=True)