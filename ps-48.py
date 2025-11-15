from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
import json

# Untuk mulai buat app desktop
app = QApplication([])

# data note dummy awal
notes = {
    "Welcome!" : {
        "text" : "This is the best note taking app in the world!",
        "tags" : ["good", "instructions"]
    }
}

# untuk membuat file notes_data.json jika belum ada
# dan menuliskan data dummy ke dalamnya
with open("notes_data.json", "w") as file:
    json.dump(notes, file, ensure_ascii=False)


# setting ukuran dari layar aplikasi
notes_win = QWidget()
notes_win.setWindowTitle('Smart Notes')
notes_win.resize(900, 600)

# widget list sebagai dasar dari list notesnya nanti
list_notes = QListWidget()
list_notes_label = QLabel('List of notes')

"""
Tugas ada dibawah ini, kamu hanya boleh mengotak-atik kode dibawah ini
ya, jangan sampai mengubah kode selain yang diizinkan agar tidak terjadi error
"""


# Tugas 1
# Buat 3 button widget dengan variabel button_note_create, button_note_del , button_note_save
# gunakan widget QPushButton



# Tugas 2
"""
Widget untuk manajemen tag pada catatan: (Buat variabel berikut)
- field_tag: input teks untuk memasukkan nama tag (Pakai QLineEdit())
- field_text: area teks isi catatan (Pakai QTextEdit())
- button_add: tombol menambahkan tag ke catatan aktif (Pakai QPushButton())
- button_del: tombol menghapus tag dari catatan aktif (Pakai QPushButton())
- button_search: tombol mencari catatan berdasarkan tag (Pakai QPushButton())
- list_tags & list_tags_label: daftar semua tag yang tersedia/terpasang (Pakai QListWidget dan QLabel)
"""


# Tugas 3
"""
 - Buat variabel layout_notes sebagai QHBoxLayout
 - Buat variabel col_1 sebagai QVBoxLayout, lalu tambahkan field_text ke dalam col_1
 - Buat variabel col_2 sebagai QVBoxLayout, lalu tambahkan list_notes_label (QLabel) dan list_notes (QListWidget) ke dalam col_2
 - Buat variabel row_1 sebagai QHBoxLayout, lalu tambahkan button_note_create (QPushButton) dan button_note_del (QPushButton) ke dalam row_1
 - Buat variabel row_2 sebagai QHBoxLayout, lalu tambahkan button_note_save (QPushButton) ke dalam row_2
 - Tambahkan row_1 dan row_2 ke dalam col_2

"""



# Tugas 4
"""
- Tambahkan list_tags_label (QLabel) ke dalam col_2
- Tambahkan list_tags (QListWidget) ke dalam col_2
- Tambahkan field_tag (QLineEdit) ke dalam col_2
- Buat row_3 sebagai QHBoxLayout, lalu tambahkan button_add (QPushButton) dan button_del (QPushButton) ke dalam row_3
- Buat row_4 sebagai QHBoxLayout, lalu tambahkan button_search (QPushButton) ke dalam row_4
- Tambahkan row_3 dan row_4 ke dalam col_2
- Tambahkan col_1 ke layout_notes dengan stretch 2
- Tambahkan col_2 ke layout_notes dengan stretch 1
- Set layout_notes sebagai layout untuk notes_win

"""


# Tugas 5
"""
kode logika untuk show notes dari list note
nanti kita akan perbaiki kode ini bersama-sama sebagai latihan
"""

def show_note():
    print("tugas disini")


"""
Batas kode tugas sampai disini !!!!!!!!!!!!!!!!!!
"""

# untuk menjalankan aplikasi
list_notes.itemClicked.connect(show_note)
notes_win.show()


with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)


app.exec_()
