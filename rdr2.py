import subprocess
import datetime
import os

def get_git_info():
    try:
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
        branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()
        commit_date = subprocess.check_output(['git', 'show', '-s', '--format=%ci', 'HEAD']).decode().strip()
        author_name = subprocess.check_output(['git', 'show', '-s', '--format=%an', 'HEAD']).decode().strip()
        return {
            'Commit Hash': commit_hash,
            'Branch': branch_name,
            'Commit Date': commit_date,
            'Author': author_name,
            'Generated At': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    except subprocess.CalledProcessError as e:
        print("Git ақпаратын алу кезінде қате:", e)
        return None

def write_build_info(info, filename='build_info.txt'):
    if info:
        with open(filename, 'w') as f:
            for key, value in info.items():
                f.write(f'{key}: {value}\n')
        print(f"{filename} файлына жазылды.")
    else:
        print("Ақпарат жоқ, файл жазылмады.")

if __name__ == "__main__":
    git_info = get_git_info()
    write_build_info(git_info)
