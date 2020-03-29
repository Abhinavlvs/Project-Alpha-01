import gzip as gz
import shutil
import os

lst = (os.listdir(r'F:\Test\gcp'))

# for file in lst:
#     with open(r"F:\Test\gcp\{file}".format(file=file), 'rb') as fin:
#
#         with gz.open(r"F:\Test\gcp\{nfile}.gz".format(nfile=file), 'wb') as fout:
#             fout.write(fin.read())


with gz.open(r'F:\Test\gcp\inventories_test.txt.gz', 'rb') as f:
    # print(f.readlines())
    data = (f.read())
    print(data)
    with open('oooo.txt','wb') as fr:
        # for e in f.readlines():
        # for e in data:
        #     print(e)
        fr.write(data)
        # with open('out.txt', 'wb') as ft:
    #     ft.write(data)
    # with open('out.txt', 'r') as fr:
    #     print(fr.read())

# with
