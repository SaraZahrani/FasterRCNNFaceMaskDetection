import os
import shutil
trainset = 'AIZOO/train/'
valset = 'AIZOO/val/'
trainpath = 'train'
valpath = 'val'
if not os.path.exists(trainpath):
    os.makedirs(trainpath + '/Annotations')
    os.makedirs(trainpath + '/JPEGImages')
if not os.path.exists(valpath):
    os.makedirs(valpath + '/Annotations')
    os.makedirs(valpath + '/JPEGImages')
i=0
j=0
f = open('./train/train.txt', 'w')
for file in sorted(os.listdir(trainset)):
    if i < 700:
        i = i + 1
        if os.path.splitext(file)[1] == '.xml':
            print(file)
            r = shutil.copy(trainset + file, os.path.join('./train/Annotations'))
            print('copy path is ' + r)
        elif os.path.splitext(file)[1] == '.png':
            print(file)
            r = shutil.copy(trainset + file, os.path.join('./train/JPEGImages'))
            print('copy path is ' + r)
            f.write(str(file) + '\n')
            print("write image in txt")
    if  j < 700:
        j = j + 1
        if os.path.splitext(file)[1] == '.xml':
            print(file)
            r = shutil.copy(trainset + file, os.path.join('./train/Annotations'))
            print('copy path is ' + r)
        elif os.path.splitext(file)[1] == '.png':
            print(file)
            r = shutil.copy(trainset + file, os.path.join('./train/JPEGImages'))
            print('copy path is ' + r)
            f.write(str(file) + '\n')
            print("write image in txt")
f.close()

i=0
j=0
f = open('./val/val.txt', 'w')
for file in sorted(os.listdir(valset)):
    if i <100:
        i=i+1
        if os.path.splitext(file)[1] == '.xml':
                print(file)
                r=shutil.copy(valset + file,os.path.join('./val/Annotations'))
                print('copy path is '+ r)
        elif os.path.splitext(file)[1] == '.png':
                print(file)
                r=shutil.copy(valset + file,os.path.join('./val/JPEGImages'))
                print('copy path is '+ r)
                f.write(str(file)+'\n')
                print("write image in txt")
    if j <100:
        j = j + 1
        if os.path.splitext(file)[1] == '.xml':
            print(file)
            r = shutil.copy(valset + file, os.path.join('./val/Annotations'))
            print('copy path is ' + r)
        elif os.path.splitext(file)[1] == '.png':
            print(file)
            r = shutil.copy(valset + file, os.path.join('./val/JPEGImages'))
            print('copy path is ' + r)
            f.write(str(file) + '\n')
            print("write image in txt")
f.close()