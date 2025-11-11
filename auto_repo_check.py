import os
import sys

def run_git_command(command):
    try:
        result = os.popen(command).read().strip()
        return result
    except Exception as e:
        print(f"Қате: {command} командасы орындалмады.\n{e}")
        return None

def check_syntax(file_path):
    result = os.system(f"python -m py_compile {file_path}")
    if result == 0:
        print(f"✅ Синтаксис дұрыс: {file_path}")
        return True
    else:
        print(f"❌ Синтаксистік қате табылды: {file_path}")
        return False

def get_status():
    print("\n📄 Git статус:")
    output = run_git_command("git status --short")
    print(output if output else "Өзгеріс жоқ.")

def get_diff():
    print("\n🔍 Өзгерістер айырмашылығы:")
    output = run_git_command("git diff")
    print(output if output else "Айырмашылықтар жоқ.")

def get_log():
    print("\n📜 Соңғы коммиттер:")
    output = run_git_command("git log --oneline -n 5")
    print(output if output else "Коммиттер жоқ.")

def main():
    print("🔧 Репозиторийді автоматты тексеру басталды...")

    get_status()
    get_diff()

    print("\n🧪 Python файлдарын тексеру:")
    py_files = [f for f in os.listdir('.') if f.endswith('.py')]
    if not py_files:
        print("⚠️ Python файлдар табылмады.")
        sys.exit(1)

    all_valid = True
    for file in py_files:
        if not check_syntax(file):
            all_valid = False

    if not all_valid:
        print("\n🚫 Commit орындалмайды. Қателерді түзетіңіз.")
        sys.exit(1)

    print("\n✅ Барлығы дұрыс. Commit және push басталады...")
    os.system("git add .")
    commit_result = os.system('git commit -m "Автоматты commit"')
    if commit_result != 0:
        print("⚠️ Commit жасау мүмкін емес. Өзгеріс жоқ немесе басқа себеп.")
        sys.exit(1)

    push_result = os.system("git push")
    if push_result == 0:
        print("✅ Git push сәтті орындалды.")
    else:
        print("⚠️ Git push кезінде қате шықты.")

    get_log()

if __name__ == "__main__":
    main()
