import easygui
#окно для выбора файла
import shutil
#для переноса файла

start_file_path=easygui.fileopenbox() #определение пути к исходному файлу
shutil.copy(start_file_path, "./music")
