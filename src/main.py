import os
import shutil

def main():
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

    public_path = os.path.join(PROJECT_ROOT, "public")
    static_path = os.path.join(PROJECT_ROOT, "static")

    clear_directory(public_path)
    copy_directory(static_path , public_path)
    
def clear_directory(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            os.remove(full_path)
        elif os.path.isdir(full_path):
            clear_directory(full_path)
            os.rmdir(full_path)

def copy_directory(src, dest):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        elif os.path.isdir(src_path):
            os.makedirs(dest_path, exist_ok=True)
            copy_directory(src_path, dest_path)

main()