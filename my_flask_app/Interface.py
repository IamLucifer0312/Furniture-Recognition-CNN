import os
import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model('model2.h5')

class_labels = ['Beds', 'Chairs', 'Dressers', 'Lamps', 'Sofas', 'Tables']

@app.route('/')
def home():
    return render_template("Interface.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get image path
    img_file = request.files['image']

    # Save uploaded image
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], img_file.filename)
    img_file.save(img_path)

    # Load image
    img = tf.keras.preprocessing.image.load_img(img_path, target_size = (350, 350))

    # Convert image
    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis = 0)

    # Make prediction
    pred = model.predict(img_array)

    # Get predicted class
    pred_class = np.argmax(pred[0])
    pred_label = class_labels[pred_class]

    # Prepare response
    res = {
        'prediction': pred_label,
    }

    return jsonify(res)


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug = True)