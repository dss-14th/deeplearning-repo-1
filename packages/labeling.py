
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import json
import math

def get_detection(file_path,json_path):
    files = os.listdir(file_path)
    file_len = len(files)
    plt.figure(figsize=(14,12))

    for i in range(1,file_len+1):
        plt.subplot(math.ceil(file_len/2),2, i)
        image = mpimg.imread(file_path + "/" + files[i-1])
        with open(json_path + '/{}.json'.format(files[i-1][:5]), 'r+') as f:
            data = json.load(f)
            coor_1 = data['mark'][0]["coordinates"][0]
            coor_2 = data['mark'][0]["coordinates"][1]
            coor_3 = data['mark'][0]["coordinates"][2]
            coor_4 = data['mark'][0]["coordinates"][3]

        plt.imshow(image)
        plt.vlines(coor_1[0], coor_1[1], coor_4[1], color='r')
        plt.vlines(coor_2[0], coor_1[1], coor_3[1], color='r')
        plt.hlines(coor_4[1], coor_4[0], coor_3[0], color='r')
        plt.hlines(coor_2[1], coor_1[0], coor_3[0], color='r')

    plt.tight_layout()    
    plt.show() 
