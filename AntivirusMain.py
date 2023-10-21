import os
import hashlib
import glob

def is_file_infected(directory_path):
    max_file_size = 1024 # Максимальный размер файла (в байтах)
    if os.path.getsize(directory_path) > max_file_size:
        return True

    suspicious_patterns = ["eval(", "exec(", "os.system("]
    with open(directory_path, "r") as file:
        content = file.read()
        for pattern in suspicious_patterns:
            if pattern in content:
                return True
            return False

    if is_file_infected(directory_path):
        print(f"Файл {directory_path} заражен вирусом или подозрительным содержимым.")
    else:
        print(f"Файл {directory_path} чистый.")

def search_file(filename, directory_path):
    for root, dirs, files in os.walk(directory_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def Name_Scan_File():
    if result:
        found_result = result
        print("Обнаружен потенциальный вирус в директори:", result)
        os.remove(found_result)
    else:
        print("Вирус не найден")

def Signature_Scan_File(file_path):
    # Открываем файл для чтения в бинарном режиме
    try:
        with open(file_path, "rb") as file:
            # Читаем содержимое файла
            content = file.read()
            # Вычисляем хеш сигнатуры файла
            file_hash = hashlib.md5(content).hexdigest()
            if file_hash in virus_signature_database:
                print(f"Обнаружен вирус в файле: {file_path}")
                os.remove(file_path)

    except PermissionError:
        print(f"Ошибка открытия папки {directory_path}: нет доступа")
    
def scan_directory(directory_path):
    # Обход всех файлов и поддиректорий в указанной директории
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            Signature_Scan_File(file_path)

directory_path = input("Вставте сюда директорию поиска: ")
filename = "Virus.exe" or "Virus.dll" or "Trojan.exe" or "Trojan.dll" or "virus.exe" or "virus.dll" or "trojan.exe" or "trojan.dll"
result = search_file(filename, directory_path)

virus_signature_database = [
"6926186a4ef5b87efaaee99f77d3d2b4",
"4f59bfa8062757b4c1b19f332bd69b65",
"1cbb672e44fafd129ae99fcf532857e5",
"0x05036c84c18aa0e6f5d2d39561c0b24e", 
"0x4a0a3627073b23c1c92caf55137cf03e", 
"0x13c5a7f2bed6ee783a8e5452df84a586",
"0xeaca8fc61e3e1b4e7be098e3516d3c1f",
"50654e3feea9a7f5001b256e25e6e738",
"ae7e486a5d679c4b35f2f6b2d2e95a84",
"b6e694ceb75b91c9cb5ac532693bf8c2",
"f48a3e4bc471c2ca0ac9463fe058d9db",
"06972afb8e64539f5fddcdae84f97f42",
"a30972e5a0bfaee9e1108d25a7064497",
"c17d4df5c7f1c1a1995d25728ef82ddb",
"e06cb868635c3ff506609ff05e8cf336",
"e789e2d4eac53712b5f1444b04622a53",
"8b5a008a3aecb43d8e99ecef38d0c6cb",
"65b8ed4c0f816dc8ad8a4337f3bc9683",
"7456c3ef2f15d31f9123f486e64dab6a"
]

# Сканирование директории
is_file_infected(directory_path)
scan_directory(directory_path)
Name_Scan_File()
