import tensorflow as tf 
import tensorflowjs as tfjs

model = tf.keras.models.load_model('saved_model.pb')

tfjs.converters.save_keras_model(model, 'output/js/')