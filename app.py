import os
from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'vitamin_model.h5')
model = load_model(MODEL_PATH)

class_names = ['vitamin_a', 'vitamin_b', 'vitamin_c', 'vitamin_d', 'vitamin_e']

def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(128,128))
    x = image.img_to_array(img)/255.
    x = np.expand_dims(x, axis=0)
    return x

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if not file: return redirect(url_for('index'))
        upload_dir = os.path.join('static','uploads')
        os.makedirs(upload_dir, exist_ok=True)
        save_path = os.path.join(upload_dir, file.filename)
        file.save(save_path)

        img = prepare_image(save_path)
        preds = model.predict(img)[0]
        label = class_names[int(np.argmax(preds))]
        prob  = f"{float(np.max(preds))*100:.2f}%"
        return render_template('output.html', filename=file.filename, predicted=label, probability=prob)
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
