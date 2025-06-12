import os
import shutil

def remove_git_files(directory):
    print(f"Scanning: {directory}")  # Debugging print
    for root, dirs, files in os.walk(directory, topdown=True):
        print(f"Checking: {root}")  # Debugging print
        
        if '.git' in dirs:
            git_path = os.path.join(root, '.git')
            shutil.rmtree(git_path)
            print(f"Removed: {git_path}")
            
        for file in files:
            if file == '.gitignore':
                gitignore_path = os.path.join(root, file)
                os.remove(gitignore_path)
                print(f"Removed: {gitignore_path}")

downloaded_repo_path = r"C:\Users\suhas b s\Downloads\Deblring-main"
remove_git_files(downloaded_repo_path)
