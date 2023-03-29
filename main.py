import os
import shutil

# создаем проект
  # как создавать проект чтобы он правильно создвался на гитхаб?

# копируем файлы/папки (из папки template_for_new_project) в корень нового проекта

path_for_pycharm_folders = os.path.dirname(os.path.abspath(os.curdir))
new_project_dir_name = input("Введите название папки нового проекта: ")
folder_to = os.path.join(path_for_pycharm_folders, new_project_dir_name)
folder_from = os.path.join(os.path.abspath(os.curdir), 'template_for_new_project')

for f in os.listdir(folder_from):
    if os.path.isfile(os.path.join(folder_from, f)):
        shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, folder_user, f))
    if os.path.isdir(os.path.join(folder_from, f)):
        shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, folder_user, f))




