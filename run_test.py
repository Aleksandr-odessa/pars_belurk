import subprocess

def run_lint():
    # Проверка main.py с помощью flake8
    print("Результаты проверки main.py с помощью flake8:")
    subprocess.run(['flake8', 'main.py'])

    # Проверка main.py с помощью pylint
    print("Результаты проверки main.py с помощью pylint:")
    subprocess.run(['pylint', 'main.py'])

    # Проверка main.py с помощью isort
    print("Результаты проверки main.py с помощью isort:")
    subprocess.run(['isort', 'main.py'])

    # Переход в директорию helpers
    print("Результаты проверки директории helpers с помощью flake8:")
    subprocess.run(['flake8', 'helpers'])

    # Проверка директории helpers с помощью pylint
    print("Результаты проверки директории helpers с помощью pylint:")
    subprocess.run(['pylint', 'helpers'])

    # Проверка директории helpers с помощью isort
    print("Результаты проверки директории helpers с помощью isort:")
    subprocess.run(['isort', 'helpers'])

    print("Проверка завершена.")

if __name__ == "__main__":
    run_lint()