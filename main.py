import subprocess

print("Pilih menu:")
print("1. Enkripsi File")
print("2. Dekripsi File")
print("3. Keluar")

pilihan = input("Masukkan pilihan (1/2/3): ")

if pilihan == '1':
    input_file = input("Masukkan nama file yang ingin dienkripsi: ")
    output_file = input("Masukkan nama file output untuk hasil enkripsi: ")
    password = input("Masukkan password untuk enkripsi: ")

    try:
        # Perintah OpenSSL untuk enkripsi dengan AES-256-CBC
        command = [
            'openssl', 'enc', '-aes-256-cbc', 
            '-in', input_file, 
            '-out', output_file, 
            '-pbkdf2',  # Menggunakan PBKDF2 untuk derivasi kunci
            '-pass', f'pass:{password}'  # Menyediakan password untuk enkripsi
        ]
        
        # Menjalankan perintah
        subprocess.run(command, check=True)
        print(f"File berhasil dienkripsi dan disimpan di: {output_file}")
    
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan saat enkripsi: {e}")
    except Exception as e:
        print(f"Kesalahan umum: {e}")

elif pilihan == '2':
    input_file = input("Masukkan nama file yang ingin didekripsi: ")
    output_file = input("Masukkan nama file output untuk hasil dekripsi: ")
    password = input("Masukkan password untuk dekripsi: ")

    try:
        # Perintah OpenSSL untuk dekripsi dengan AES-256-CBC
        command = [
            'openssl', 'enc', '-aes-256-cbc', '-d',  # Opsi '-d' untuk dekripsi
            '-in', input_file, 
            '-out', output_file, 
            '-pbkdf2',  # Menggunakan PBKDF2 untuk derivasi kunci
            '-pass', f'pass:{password}'  # Menyediakan password untuk dekripsi
        ]
        
        # Menjalankan perintah
        subprocess.run(command, check=True)
        print(f"File berhasil didekripsi dan disimpan di: {output_file}")
    
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan saat dekripsi: {e}")
    except Exception as e:
        print(f"Kesalahan umum: {e}")

elif pilihan == '3':
    print("Keluar dari program.")
else:
    print("Pilihan tidak valid. Silakan pilih lagi.")
