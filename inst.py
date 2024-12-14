import subprocess

# Создание файла requirements.txt
with open('requirements.txt', 'w') as f:
    subprocess.run(['pip', 'freeze'], stdout=f)
print("requirements.txt успешно создан.")

# Установка pylint и flake8
subprocess.run(['pip', 'install', 'pylint'])
subprocess.run(['pip', 'install', 'flake8'])
subprocess.run(['pip', 'install', 'isort'])
