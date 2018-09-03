import glob, os
from shutil import copy

src_dir = "D:/_MA/_Models, Datensaetze, etc/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/Annotations/"
dest_dir = "D:/_MA/psychic-memory/Datensatz/Prepared Data/New Classes/dog/"

for pathAndFilename in glob.iglob(os.path.join(dest_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(src_dir + title + ".xml")
    copy(src_dir + title + ".xml", dest_dir)