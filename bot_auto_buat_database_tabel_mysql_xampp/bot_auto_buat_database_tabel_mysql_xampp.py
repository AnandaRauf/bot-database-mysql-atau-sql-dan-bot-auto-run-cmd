import mysql.connector

print("==========================================================================================\n")
namaaplikasi = "Bot database\n"
versi = "Version 1.0\n"
devby = "Ananda Rauf Maududi\n"
print(namaaplikasi)
print(versi)
print("Developed by:",devby)
print("==========================================================================================\n")

def MenuBotDatabase():
    print("Pilih nomor yang ada didalam menu :")
    print
    print("1.ConnectDatabase")
    print("2.CreateDatabase")
    print("3.CreateTableDatabase")
    
def ConnectDatabase():
    dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="db_bot")
    if dbcon.is_connected():
        print("Database berhasil dihubungkan ^-^\n")
def CreateDatabse():
    dbcon = mysql.connector.connect(host="localhost",user="root",passwd="")
    createdb = dbcon.cursor()
    createdb.execute("CREATE DATABASE db_bot")
    print("Database berhasil dibuat ^-^\n")
def CreateTableDatabase():
    dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="db_bot")
    createtable = dbcon.cursor()
    sql = "CREATE TABLE test_table_bot(bot_id INT(100) AUTO_INCREMENT PRIMARY KEY,namabot TEXT)"
    createtable.execute(sql)
    print("Tabel berhasil dibuat\n")
    print("Selamat datang di Bot Database ^-^\n")
MenuBotDatabase()
pilih = int(input("Masukan nomor pilihan dalam menu bot :"))
if pilih == 1:
        ConnectDatabase()
elif pilih==2:
        CreateDatabse()
elif pilih==3:
        CreateTableDatabase()
else:
        exit