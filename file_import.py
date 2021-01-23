import easygui
#окно для выбора файла
import shutil
#для переноса файла

start_file_path=easygui.fileopenbox() #определение пути к исходному файлу
try:
    shutil.copy(start_file_path, "./music")
except:
    print("файл не выбран")