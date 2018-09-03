import glob, os
import xml.etree.ElementTree
from shutil import copy

xml_dir = "D:/_MA/psychic-memory/Datensatz/Prepared Data/New Classes/dog/VOC/"
src_dir = "D:/_MA/psychic-memory/Datensatz/Prepared Data/Final Dataset/myVOC/JPEGImages/"
dest_dir = "D:/_MA/psychic-memory/Label Tools/LabelImg/data/"

for pathAndFilename in glob.iglob(os.path.join(xml_dir, "*.xml")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    tree = xml.etree.ElementTree.parse(xml_dir + title + ".xml")
    txt_outpath = xml_dir + title + ".xml"
    print(txt_outpath)
    e = tree.getroot()

    width = 0
    height = 0
    for child in e:
        if child.tag == 'size':
            width = child[0].text
            height = child[1].text
            if int(child[0].text) <= 0:
              print("Width: " + title)
            if int(child[1].text) <= 0:
                print("Height: " + title)
            if int(child[2].text) < 3:
                print("Depth: " + title)
                child[2].text = '3'
                tree.write(xml_dir + title + ".xml")
        if child.tag == 'object':
            if int(child[4][0].text) > int(width):
                print(title + ", " + width + ", " + child[4][0].text)
            if int(child[4][1].text) > int(height):
               print(title + ", " + height + ", " + child[4][1].text)
            if int(child[4][2].text) > int(width):
                print(title + ", " + width + ", " + child[4][2].text)
            if int(child[4][3].text) > int(height):
                print(title + ", " + height + ", " + child[4][3].text)
        if child.tag == "folder":
            child.text = "myVOC"
    tree.write(txt_outpath)
    #print(title)

#for pathAndFilename in glob.iglob(os.path.join(xml_dir, "*.xml")):
#    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#    print(src_dir + title + ".jpg")
#    copy(src_dir + title + ".jpg", dest_dir)
