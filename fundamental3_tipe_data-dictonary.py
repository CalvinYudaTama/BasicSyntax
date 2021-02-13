"""
Tipe data dictonary yaitu yang menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictonary = kamus (kumpulan sebuah data)
"""

kamus_ind_eng = {'ayah': 'father', 'ibu': 'mother', 'istri': 'wife', 'anak': 'son'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['anak'])

print('\nData ini dikirimkan dari server grab, untuk memberikan info driver disekitar user')
data_dari_server_grab = {
    'Tanggal': '2020-12-10',
    'Driver-list': [{'nama': 'Eko', 'jarak': 10}, {'nama': 'Dwi', 'jarak': 100}, {'nama': 'Mamad', 'jarak': 20},
                    {'nama': 'Abdul', 'jarak': 25}]
}
print(f"tanggal hari ini : {data_dari_server_grab['Tanggal']}")
print(f"Driver yang terdekat disini yaitu {data_dari_server_grab['Driver-list']}")
print(
    f"Driver 1 {data_dari_server_grab['Driver-list'][0]['nama']} dengan jarak {data_dari_server_grab['Driver-list'][0]['jarak']} meter")
print(
    f"Driver 2 {data_dari_server_grab['Driver-list'][1]['nama']} dengan jarak {data_dari_server_grab['Driver-list'][1]['jarak']} meter")
