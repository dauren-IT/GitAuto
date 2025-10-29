import subprocess
import os
import sys

def check_syntax(file_path):
    try:
        subprocess.check_output(['python', '-m', 'py_compile', file_path])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # 1. Python файлдарын табу
    py_files = [f for f in os.listdir('.') if f.endswith('.py')]

    # 2. Синтаксистік тексеру
    all_valid = True
    for file in py_files:
        if not check_syntax(file):
            print(f"❌ Синтаксистік қате табылды: {file}")
            all_valid = False

    if not all_valid:
        print("🚫 Commit орындалмайды. Қателерді түзетіңіз.")
        sys.exit(1)

    # 3. Git командалары
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Автоматтандырылған commit'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("✅ Барлық Python файлдар дұрыс. Git push сәтті орындалды.")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git командасында қате: {e}")

if __name__ == "__main__":
    main()
