
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import json
import math

def json2mxl(json_pathes):
    datas = []
    json_coordinates_df = pd.DataFrame()        

    for each in json_pathes:
        files = sorted(glob.glob(each+"/*"))
        for file in files:
            with open(file) as f:
                data = json.load(f)
                co_ls = data['mark'][0]['coordinates']
                x_min = min([each[0] for each in co_ls])
                x_max = max([each[0] for each in co_ls])
                y_min = min([each[1] for each in co_ls])
                y_max = max([each[1] for each in co_ls])
                upper_folder = file.split('/')[3]
                lower_folder = file.split('/')[6]
                file_name = file.split('/')[7]
                file_name_whole = file.split('/')[3]+file.split('/')[6]+file.split('/')[7]
                label = data['mark'][0]['label']
                truncated_str = label['Truncated']
                occluded_str = label['Occluded']
                category = label['Category']

            data = ({'category':category,'upper_folder': upper_folder, 'lower_folder': lower_folder, 'file_name': file_name, 'file_name_whole': file_name_whole, 'label':label, 'truncated_str':truncated_str, 'occluded_str':occluded_str, 'x_min': x_min, 'x_max': x_max, 'y_min': y_min, 'y_max': y_max})
            datas.append(data)
    json_coordinates_df = pd.DataFrame(datas)
    return json_coordinates_df

def get_detection(file_path,json_path):
    files = os.listdir(file_path)
    file_len = len(files)
    plt.figure(figsize=(14,12))

    for file in files:
        plt.subplot(math.ceil(file_len/2),2, files.index(file)+1)
        image = mpimg.imread(file_path + "/" + file)
        with open(json_path + '/{}.json'.format(file[:5]), 'r+') as f:
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
