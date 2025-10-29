import subprocess
import os
import sys

def check_syntax(file_path):
    try:
        subprocess.check_output(['python', '-m', 'py_compile', file_path])
        print(f"✅ Синтаксис дұрыс: {file_path}")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Синтаксистік қате табылды: {file_path}")
        return False

def main():
    # 1. Python файлдарын табу
    py_files = [f for f in os.listdir('.') if f.endswith('.py')]

    if not py_files:
        print("⚠️ Python файлдар табылмады.")
        sys.exit(1)

    # 2. Синтаксистік тексеру
    all_valid = True
    for file in py_files:
        if not check_syntax(file):
            all_valid = False

    if not all_valid:
        print("🚫 Commit орындалмайды. Қателерді түзетіңіз.")
        sys.exit(1)

    # 3. Git add
    subprocess.run(['git', 'add', '.'])

    # 4. Git commit
    commit_result = subprocess.run(['git', 'commit', '-m', 'Автоматтандырылған commit'])
    if commit_result.returncode != 0:
        print("⚠️ Commit жасау мүмкін емес: өзгеріс жоқ немесе басқа себеп.")
        sys.exit(1)

    # 5. Git push
    try:
        subprocess.run(['git', 'push'], check=True)
        print("✅ Git push сәтті орындалды.")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git push кезінде қате шықты: {e}")

if __name__ == "__main__":
    main()
    print("Push тесті")

