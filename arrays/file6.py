import os
if os.path.exists("dummy.txt"):
    os.remove("dummy.txt")
else:
    print("File doesn't exist")