import os


def createTrainvalTxt(baseDirDataSet):
    buffer = ''
    baseDir = baseDirDataSet+'/Images'
    for filename in os.listdir(baseDir):
        filenameOnly, file_extension = os.path.splitext(filename)
        # print (file_extension)
        s = 'Images/'+filenameOnly+'.jpg'+' '+'Labels/'+filenameOnly+'.xml\n'
        print (repr(s))
        img_file, anno = s.strip("\n").split(" ")
        print(repr(img_file), repr(anno))
        buffer+=s
    with open(baseDirDataSet+'/Structure/trainval.txt', 'w') as file:
        file.write(buffer)  
    print('Done')   
#Usage
createTrainvalTxt('/home/rishav/dataset/Dataset-ev3-tracking')