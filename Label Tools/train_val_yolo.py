import glob, os

# Directory where the data will reside, relative to 'darknet.exe'
img_dir = 'D:/_MA/psychic-memory/Datensatz/Prepared Data/Final Dataset/myVOC/JPEGImages/'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')
#file_imagelist = open('imagelist.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
#print(current_dir)
for pathAndFilename in glob.iglob(os.path.join(img_dir, "*.jpg")):
    print(pathAndFilename)
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    # print(title)
    #file_imagelist.write(title + "\n")

    if counter == index_test:
        counter = 1
        file_test.write('data/obj/' + title + '.jpg' + "\n")
    else:
        file_train.write('data/obj/' + title + '.jpg' + "\n")
        counter = counter + 1