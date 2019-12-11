import os
from keras.models import load_model
import numpy as np
from PIL import Image
import cv2
#import matlab
#import matlab.engine

model = load_model("poles_and_nonpoles.h5")
model.summary()

def get_inputs(src=[]):
    pre_x = []
    for s in src:
        input = cv2.imread(s)
        input = cv2.resize(input, (150, 150))
        input = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)
        pre_x.append(input)
    pre_x = np.array(pre_x) / 255.0
    return pre_x

predict_dir = 'C:\\Users\18367\Desktop\boston_test1'

test = os.listdir(predict_dir)

images = []


for testpath in test:
    for fn in os.listdir(os.path.join(predict_dir, testpath)):
        if fn.endswith('jpg'):
            fd = os.path.join(predict_dir, testpath, fn)
            images.append(fd)
pre_x = get_inputs(images)
pre_y = model.predict(pre_x)
judge = [0]*len(pre_y)
for i in range(len(pre_y)):
    if pre_y[i] > 0.90000:
        judge[i] = 1;
    else:
        judge[i] = 0;

docu = open('boston_test.txt','w')
np.set_printoptions(formatter={'float': '{: 0.5f}'.format})
for i in range(len(pre_y)):
    # print(images[i])
    print(images[i][62:82] + "_" + str(judge[i]),file = docu)
    # print(images[i][62:82] + "_" + str(judge[i]))

# eng = matlab.engine.start_matlab()
# eng.map_test(nargout = 0)

