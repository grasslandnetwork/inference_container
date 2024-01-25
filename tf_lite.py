# Sourced from code written by Intel
# https://www.kaggle.com/models/intel/midas/frameworks/tfLite
# License: MIT

import cv2
import tensorflow as tf
import urllib.request
import time

url, filename = ("https://github.com/intel-isl/MiDaS/releases/download/v2/dog.jpg", "dog.jpg")
urllib.request.urlretrieve(url, filename)

# input
img = cv2.imread('dog.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255.0

img_resized = tf.image.resize(img, [256,256], method='bicubic', preserve_aspect_ratio=False)
img_input = img_resized.numpy()
mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]
img_input = (img_input - mean) / std
reshape_img = img_input.reshape(1,256,256,3)
tensor = tf.convert_to_tensor(reshape_img, dtype=tf.float32)

# Download model
# https://drive.google.com/file/d/1jNHFCXl7rptGhseAPhSY8ZZXmSc3glnv/view?usp=sharing

# load model
model_path = '1.tflite'
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


# Initialize a list to store inference times
inference_times = []

# Run the inference 10 times in a loop
for _ in range(10):
    start = time.time()
    interpreter.set_tensor(input_details[0]['index'], tensor)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])
    output = output.reshape(256, 256)
    end = time.time()
    
    # Calculate this run's inference time and append to the list
    inference_times.append(end - start)

# Calculate the average inference time
average_time = sum(inference_times) / len(inference_times)

# Print the average inference time
print("Average inference time:", average_time)



# output file
prediction = cv2.resize(output, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_CUBIC)
print(" Write image to: output.png")
depth_min = prediction.min()
depth_max = prediction.max()
img_out = (255 * (prediction - depth_min) / (depth_max - depth_min)).astype("uint8")

# Using OpenCV to display the image
# cv2.imshow("Output Image", img_out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print(img_out)
