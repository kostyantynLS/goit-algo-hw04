'''
Третє завдання (не обов'язкове)

Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і 
візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. 
Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.
'''

from pathlib import Path, PurePath
from colorama import Fore, Back, Style
import sys

def recursive_scan(path_to_scan, scan_deep):
    local_path = Path(path_to_scan)
    #start scan
    for path in local_path.iterdir():
        p_path = PurePath(path)
        #check if path is directory
        if path.is_dir():
            print('| '*scan_deep,'\- ',Fore.RED + p_path.name, Style.RESET_ALL, sep="")
            recursive_scan(path, scan_deep+1)
        else:
            print('| '*scan_deep,'|- ',Fore.BLUE + p_path.name, Style.RESET_ALL, sep="")

def main():
    # checking arguments to file
    if len(sys.argv)<2:
        directory = Path(".")
    else:
        directory = sys.argv[1]
    # run scan
    try:
        recursive_scan(directory, 0)
    except Exception as e:
        print(f'exception {e} at module {sys.argv[0]}') 

if __name__ == "__main__":
    main()