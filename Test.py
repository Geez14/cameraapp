# import datetime
# a = datetime.datetime.now().strftime("%d_%m_%Y_%H:%M:%S") # %D = date
# print(a)
import re
def sanitize(filename):
    filename = re.sub(r'[^\w\s.-]*',"", filename).strip().lower()
    filename = re.sub(r'[-\s]+',"_", filename)
    filename = re.sub(r'(\.)+',".", filename)
    return filename
print(sanitize("fuck^$-  %#  ,,,@.apk.txt"))