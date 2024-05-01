import os
import shutil
import sys

def copy_files(source_dir, dest_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            src_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1].strip('.')
            dest_path = os.path.join(dest_dir, extension, file)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy(src_path, dest_path)
            print(f"Copied {src_path} to {dest_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 task_1.py source_dir [dest_dir]")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = "dist" if len(sys.argv) < 3 else sys.argv[2]

    try:
        copy_files(source_dir, dest_dir)
        print("Files copied successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
