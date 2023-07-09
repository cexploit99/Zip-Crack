import zipfile
print("===========================================")
print("          Welcome to Tools Zip-Crack        ")
print("               By Owner Cx99               ")
print("===========================================")

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except:
        return False

def crack_zip(zip_file, password_list):
    for password in password_list:
        if extract_zip(zip_file, password):
            print("Password ditemukan:", password)
            return
    print("Password tidak ditemukan.")

def read_password_file(file_path):
    with open(file_path, 'r') as file:
        password_list = file.read().splitlines()
    return password_list

def main():
    zip_file_path = input("Masukkan jalur file ZIP: ")
    password_file_path = input("Masukkan jalur file password.txt: ")

    password_list = read_password_file(password_file_path)

    try:
        zip_file = zipfile.ZipFile(zip_file_path)
        crack_zip(zip_file, password_list)
        zip_file.close()
    except zipfile.BadZipFile:
        print("File ZIP tidak valid.")
    except FileNotFoundError:
        print("File tidak ditemukan.")

if __name__ == '__main__':
    main()