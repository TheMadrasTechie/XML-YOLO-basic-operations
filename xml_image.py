from bs4 import BeautifulSoup
import cv2
import os
def remove_items(test_list, item):
     
    res = [i for i in test_list if i != item]
 
    return res
def xml_img(xml_path):
    with open('Anotation-20230129T150901Z-001//Anotation//Anotation xml//'+xml_path, 'r') as f:
        data = f.read()


    Bs_data = BeautifulSoup(data, "xml")

    filename = Bs_data.find_all('filename')



    p = Bs_data.find_all('name')
    class_name = []
    for x in p:
        class_name.append(str(x))
    class_name =remove_items(class_name,"<name>rotation</name>")


    p = Bs_data.find_all('xmin')    
    xmin = []
    for x in p:
        xmin.append(str(x))


    p = Bs_data.find_all('xmax')
    xmax = []
    for x in p:
        xmax.append(str(x))


    p = Bs_data.find_all('ymin')
    ymin = []
    for x in p:
        ymin.append(str(x))
    

    p = Bs_data.find_all('ymax')
    ymax = []
    for x in p:
        ymax.append(str(x))


    filename = str(str(filename).replace('<filename>','').replace('</filename>','').replace('[','').replace(']','').replace(')','').replace('(','').replace('Image%20',''))
    
    img = cv2.imread("Anotation-20230129T150901Z-001//Anotation//Original Image//"+filename)    
    for i in range(len(class_name)):
        name = class_name[i].replace('<name>','').replace('</name>','')
        x1 = int(float(xmin[i].replace('<xmin>','').replace('</xmin>','')))
        x2 = int(float(xmax[i].replace('<xmax>','').replace('</xmax>','')))
        y1 = int(float(ymin[i].replace('<ymin>','').replace('</ymin>','')))
        y2 = int(float(ymax[i].replace('<ymax>','').replace('</ymax>','')))    
        cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(img,name, (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, .3, (255,0,0))
    cv2.imwrite("annotated_images//"+filename,img)


path = "D://python//upwork project//vibu//Anotation-20230129T150901Z-001//Anotation//Anotation xml"
dir_list = os.listdir(path)    
for i in range (len(dir_list)):
    print(dir_list[i])
    xml_img(dir_list[i])