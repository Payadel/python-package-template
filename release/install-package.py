import sys
import os
import glob
import subprocess

# Inputs
dist_dir = sys.argv[1]

# Search for files with the .tar.gz extension
result = glob.glob(os.path.join(dist_dir, "*.tar.gz"))

# Count number of files found
count = len(result)

# If no file or more than one file is found, print error message and exit
if count == 0:
    print(f"Error: no .tar.gz file found in dist_dir '{dist_dir}'")
    sys.exit(1)
elif count > 1:
    print(f"Error: multiple .tar.gz files found in dist_dir '{dist_dir}'")
    sys.exit(1)

# Upgrade pip package using the file found
subprocess.run(["pip", "install", "--upgrade", result[0]])
