import os

def obidji(rootdir):
     for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.html'):
                print(os.path.join(subdir, file))