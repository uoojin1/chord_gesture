import numpy as np
import cv2
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image

class GesturePredictionModel:
      
  def __init__(self):
    self.model = load_model('../data/saved_model/model-1.h5')
  
  def predict_gesture(self, img):
    numpy_image=np.array(img)  
    test_image=cv2.cvtColor(numpy_image, cv2.COLOR_BGR2RGB) 
    img_to_predict = image.img_to_array(test_image)
    img_to_predict = np.expand_dims(img_to_predict, axis=0)
    self.predictions = self.model.predict(img_to_predict, batch_size=1)
    print('PREDICTIONS!', np.argmax(self.predictions))

  


