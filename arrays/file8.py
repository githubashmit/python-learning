import os
if os.path.exists("new_folder"):
    os.rmdir("new_folder")
else:
    print("File doesn't exist")