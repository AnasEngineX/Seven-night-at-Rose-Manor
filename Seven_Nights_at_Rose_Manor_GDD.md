# Seven Nights at Rose Manor
## Game Design Document (GDD) v1.0

> **Jenis dokumen:** Fondasi desain dan rencana produksi  
> **Engine:** Ren'Py  
> **Visual:** Anime 3D sinematik, dirender menjadi gambar  
> **Genre:** Gothic mystery, supernatural, romance, ecchi ringan hingga sedang  
> **Mode:** Single-player visual novel  
> **Pengembang:** Solo developer dengan bantuan AI untuk aset tertentu  
> **Bahasa target:** Bahasa Indonesia dan Inggris  
> **Status:** Konsep awal, belum menjadi spesifikasi produksi final

---

## 1. Ringkasan Konsep

### Judul
**Seven Nights at Rose Manor**

### Premis singkat
MC menerima surat misterius yang mengundangnya tinggal di Rose Manor selama tujuh malam. Mansion itu dihuni oleh Seraphina Rosewood, pewaris keluarga, serta tiga orang lain yang masing-masing menyimpan rahasia. Seiring malam berlalu, potret berubah, jam berhenti pada waktu yang sama, dan mawar merah muncul di ruangan terkunci.

MC harus mengungkap hubungan antara para penghuni, tragedi keluarga Rosewood, dan sebuah ritual yang menghapus kenangan. Pilihan pemain menentukan hubungan, bukti yang ditemukan, dan akhir cerita.

### Tiga aturan mansion
1. Jangan membuka pintu kamar di lantai tiga setelah tengah malam.
2. Jangan menjawab suara yang memanggil nama MC dari taman mawar.
3. Jangan pernah bertanya kepada penghuni mansion tentang malam kedelapan.

### Pilar desain
- **Misteri berlapis:** Setiap malam memberikan petunjuk baru.
- **Romance perlahan:** Kedekatan tumbuh melalui kepercayaan dan percakapan, bukan otomatis.
- **Pilihan bermakna:** Pilihan mengubah informasi, hubungan, dan ending.
- **Produksi terkendali:** Lingkungan dan pose digunakan kembali dengan komposisi kamera berbeda.
- **Visual sinematik:** Model 3D dirender sebagai gambar statis untuk Ren'Py.

---

## 2. Target Desain

| Elemen | Target awal |
|---|---|
| Struktur cerita | 7 malam, 3 fase cerita |
| Karakter penting | 4 karakter utama selain MC |
| Heroine utama | Seraphina Rosewood |
| Route romance | Satu route utama; karakter lain menjadi pendukung emosional dan naratif |
| Ending | Good ending, bad ending, true ending |
| Lingkungan awal | 3 lokasi untuk demo; 5–7 untuk game lengkap |
| Durasi demo | 15–30 menit |
| Durasi game penuh | Ditentukan setelah vertical slice diuji |
| Gaya visual | Anime 3D, render sinematik |
| Bahasa | Indonesia dan Inggris |
| Platform awal | PC, sesuai dukungan dan pengujian Ren'Py |

Angka di atas merupakan target perencanaan, bukan hasil produksi yang sudah teruji.

---

## 3. Genre dan Nada

### Genre
- Gothic mystery
- Supernatural
- Romance
- Ecchi ringan hingga sedang

### Nada cerita
Atmosfer misterius, elegan, intim, dan kadang menegangkan. Humor ringan dapat muncul lewat interaksi karakter, tetapi tidak boleh merusak ketegangan misteri.

### Batas konten
- Semua karakter yang terlibat dalam romance atau konten ecchi berusia 18 tahun ke atas.
- Adegan romantis harus konsensual.
- Ecchi berfungsi sebagai bagian dari perkembangan karakter dan hubungan, bukan sisipan yang tidak berkaitan dengan cerita.
- Gunakan fanservice ringan hingga sedang: pakaian tidur, situasi canggung, kedekatan emosional, atau momen privat yang tidak eksplisit.
- Hindari membuat adegan intim sebagai hadiah yang otomatis diperoleh hanya dengan menaikkan angka affection.

---

## 4. Karakter

### 4.1 MC: The Unnamed Guest

**Peran:** Protagonis dan sudut pandang pemain.

**Presentasi visual:**
- Wajah tidak pernah diperlihatkan secara jelas.
- Gunakan sudut pandang orang pertama, tangan, lengan baju, siluet, dan pantulan kabur.
- Nama bisa dikustomisasi atau menggunakan sebutan `Guest`.
- Tidak membutuhkan model wajah penuh untuk versi awal.

**Kepribadian dasar:**
- Penasaran dan observatif.
- Dapat bersikap tegas ketika menghadapi bahaya.
- Memiliki batasan karakter agar tidak terasa sebagai protagonis kosong.

**Tujuan cerita:** Memahami alasan undangan dan menentukan nasib Rose Manor.

### 4.2 Seraphina Rosewood

**Usia:** 25 tahun  
**Peran:** Heroine utama dan pewaris mansion.  
**Route:** `Blood Rose`

**Kepribadian:** Anggun, serius, menjaga jarak, dan diam-diam kesepian.

**Tujuan:** Mempertahankan mansion dan melindungi rahasia keluarga.

**Ketakutan:** Kehilangan orang yang akhirnya ia percayai.

**Konflik:** Ia percaya tragedi keluarga hanya bisa dicegah dengan mengulang ritual lama.

**Perkembangan hubungan:** Formal dan dingin → mulai terbuka → rentan dan jujur.

**Identitas visual:** Rambut perak panjang, mata merah anggur, gaun hitam-merah, bros mawar.

**Aset penting:** Model utama, ekspresi netral/senyum/marah/sedih/terkejut, beberapa pose berdiri dan duduk, close-up sinematik.

### 4.3 Evelyn Hart

**Usia:** 23 tahun  
**Peran:** Kepala pelayan.  
**Fungsi cerita:** Menjaga akses ke ruangan dan dokumen rahasia.

**Kepribadian:** Tenang, perhatian, teliti, dan loyal.

**Rahasia:** Buku tamu lama memuat tanda tangannya dari puluhan tahun sebelum ia lahir.

**Hubungan dengan Seraphina:** Loyal, tetapi tidak selalu menyetujui keputusan majikannya.

**Identitas visual:** Rambut cokelat gelap, mata amber, seragam pelayan bergaya Victorian, kalung kunci perak.

### 4.4 Lilith Vane

**Usia saat meninggal:** 22 tahun  
**Peran:** Roh yang menghuni taman mawar.  
**Fungsi cerita:** Menghubungkan mansion masa kini dengan tragedi masa lalu.

**Kepribadian:** Jenaka, suka menguji orang, menyembunyikan kesedihan.

**Rahasia:** Ia mengingat malam ketika ritual keluarga Rosewood pertama kali gagal.

**Hubungan dengan Seraphina:** Terikat oleh janji lama yang tidak pernah ditepati.

**Identitas visual:** Rambut hitam panjang, mata violet, gaun Victorian berwarna gading, efek spektral yang halus.

### 4.5 Victoria Ashbourne

**Usia:** 27 tahun  
**Peran:** Peneliti okultisme dan tamu mansion.  
**Fungsi cerita:** Menguji bukti supernatural dan menyelidiki ritual.

**Kepribadian:** Rasional, berani, skeptis, dan sedikit sarkastis.

**Rahasia:** Keluarganya pernah terlibat dalam penyelidikan Rose Manor.

**Hubungan dengan Seraphina:** Saling curiga, tetapi harus bekerja sama.

**Identitas visual:** Rambut auburn pendek, mata keemasan, pakaian hitam bergaya Victorian, aksesori perak.

---

## 5. Hubungan Antarkarakter

### Seraphina ↔ MC
Seraphina ingin melindungi mansion, tetapi menyembunyikan kebenaran. Hubungan mereka berkembang melalui percakapan pribadi, keputusan yang jujur, dan keberanian MC untuk mempertanyakan ritual.

### Seraphina ↔ Evelyn
Evelyn setia kepada keluarga Rosewood, tetapi tidak ingin tragedi masa lalu terulang.

### Seraphina ↔ Lilith
Keduanya terikat oleh janji lama. Lilith ingin dibebaskan; Seraphina takut bahwa pembebasannya akan menghancurkan mansion.

### Seraphina ↔ Victoria
Victoria menganggap Seraphina terlalu terikat pada tradisi keluarga. Seraphina menganggap Victoria gegabah.

### MC ↔ Evelyn
Evelyn membantu MC memahami rutinitas mansion dan memberikan petunjuk melalui buku tamu, kunci, serta dokumen lama.

### MC ↔ Lilith
Lilith menguji apakah MC bersedia mendengar kebenaran yang bertentangan dengan versi resmi keluarga Rosewood.

### MC ↔ Victoria
Victoria menjadi rekan investigasi. MC dapat memilih bekerja sama dengannya atau melindungi Seraphina dari penyelidikannya.

---

## 6. Misteri Utama: Ritual Mawar

Keluarga Rosewood mempertahankan mansion melalui sebuah perjanjian supernatural. Ritual itu menghapus kenangan seseorang untuk menjaga siklus mansion tetap berjalan.

Seraphina percaya ritual tersebut perlu diulang untuk mencegah tragedi. Lilith mengetahui kegagalan ritual pertama. Victoria menemukan bukti bahwa keluarga Rosewood salah memahami cara kerja ritual. Evelyn menyimpan dokumen yang menghubungkan semua petunjuk.

**Kebenaran yang direncanakan untuk true ending:** Siklus dapat dihentikan tanpa pengorbanan baru, tetapi keluarga Rosewood harus mengakui kesalahan lama dan melepaskan kendali atas kenangan yang mereka simpan.

Pastikan petunjuk tentang aturan ritual muncul sejak awal agar true ending terasa diperoleh, bukan muncul mendadak.

---

## 7. Plot Tujuh Malam

### Malam 1: The Invitation
**Lokasi:** Gerbang dan aula utama.

MC tiba di mansion, bertemu Seraphina dan Evelyn, lalu mendengar tiga aturan mansion.

**Pilihan utama:**
- Menjawab Seraphina dengan sopan.
- Bertanya langsung tentang surat.
- Mengamati reaksinya ketika surat diperlihatkan.

**Tujuan naratif:** Memperkenalkan karakter dan menanamkan kecurigaan pertama.

### Malam 2: The Locked Portrait
**Lokasi:** Galeri keluarga.

Sebuah potret berubah ketika MC meninggalkan ruangan. Evelyn mengaku tidak melihat perubahan.

**Pilihan utama:**
- Memeriksa potret.
- Memanggil Evelyn.
- Mencatat detailnya dan kembali nanti.

**Tujuan naratif:** Memperkenalkan bukti pertama dan mempertanyakan ingatan.

### Malam 3: Roses After Midnight
**Lokasi:** Taman mawar.

MC bertemu Lilith dan menemukan batu nisan tanpa nama.

**Pilihan utama:**
- Meminta Lilith menjelaskan.
- Menjaga jarak.
- Menceritakan pertemuan itu kepada Seraphina.

**Tujuan naratif:** Membuka jalur menuju sejarah ritual.

### Malam 4: The Occult Guest
**Lokasi:** Perpustakaan.

Victoria mengungkap bukti bahwa keluarga Rosewood melakukan ritual yang berkaitan dengan hilangnya kenangan.

**Pilihan utama:**
- Bekerja sama dengan Victoria.
- Melindungi Seraphina.
- Menunda keputusan dan meminta bukti tambahan.

**Tujuan naratif:** Mempertemukan dua versi kebenaran.

### Malam 5: A Fragile Promise
**Lokasi:** Kamar Seraphina atau ruang duduk.

MC dan Seraphina berbagi percakapan pribadi. Seraphina mengungkap ketakutannya kehilangan seseorang lagi.

**Pilihan utama:**
- Mendengarkan tanpa menghakimi.
- Mendesaknya untuk mengungkap seluruh rahasia.
- Menyembunyikan temuan demi menjaga kedekatan.

**Tujuan naratif:** Memperdalam romance dan menguji kejujuran.

### Malam 6: The Seventh Seal
**Lokasi:** Ruang ritual.

MC menemukan bahwa ritual menghapus kenangan untuk mempertahankan siklus supernatural.

**Pilihan utama:**
- Mengumpulkan bukti terakhir.
- Menghentikan ritual segera.
- Meminta Seraphina dan Victoria menghadapi kebenaran bersama.

**Tujuan naratif:** Menyiapkan keputusan akhir dan menguji hasil pilihan sebelumnya.

### Malam 7: The Final Rose
**Lokasi:** Kapel bawah tanah.

Seluruh petunjuk bertemu. MC harus menentukan apakah siklus akan berulang, mansion dipertahankan dengan konsekuensi tertentu, atau ritual diakhiri dengan mengakui kesalahan keluarga.

**Tujuan naratif:** Membayar semua misteri utama dan menghasilkan ending sesuai tindakan pemain.

---

## 8. Sistem Gameplay dan Variabel

### Variabel utama

| Variabel | Tipe | Rentang/awal | Fungsi |
|---|---|---|---|
| `mc_name` | String | `"Guest"` | Nama yang ditampilkan untuk MC |
| `night` | Integer | `1` | Malam cerita |
| `ser_aff` | Integer | `0` | Kedekatan dengan Seraphina |
| `ser_trust` | Integer | `0` | Kepercayaan Seraphina kepada MC |
| `evidence` | Integer | `0` | Jumlah bukti penting yang ditemukan |
| `lilith_truth` | Boolean | `False` | Apakah rahasia Lilith telah terungkap |
| `victoria_alliance` | Boolean | `False` | Apakah Victoria bekerja sama dengan MC |

### Prinsip sistem
- `ser_aff` dan `ser_trust` adalah dua hal berbeda.
- Affection membuka momen personal, tetapi trust menentukan apakah Seraphina mau mengungkap rahasia.
- `evidence` sebaiknya menghitung petunjuk utama yang berbeda, bukan jumlah klik atau pengulangan.
- Flag cerita digunakan untuk mengingat keputusan penting.
- Semua syarat ending harus diuji melalui walkthrough.

### Aturan ending awal
- **Good ending:** hubungan dengan Seraphina cukup kuat dan MC memilih mempercayainya.
- **Bad ending:** bukti tidak cukup atau MC gagal menangani konflik final; siklus berulang.
- **True ending:** bukti mencapai ambang yang ditentukan, rahasia Lilith terbuka, dan Victoria bekerja sama dengan MC.

Angka ambang awal yang dapat diuji: `ser_aff >= 3`, `ser_trust >= 3`, `evidence >= 5`, `lilith_truth == True`, dan `victoria_alliance == True`.

---

## 9. Contoh Script Ren'Py

Contoh berikut merupakan kerangka prototipe, bukan script lengkap untuk game final. Nama aset harus disesuaikan dengan file gambar yang benar-benar tersedia.

```renpy
define mc = Character("[mc_name]")
define ser = Character("Seraphina")
define eve = Character("Evelyn")
define lil = Character("Lilith")
define vic = Character("Victoria")

default mc_name = "Guest"
default night = 1
default ser_aff = 0
default ser_trust = 0
default evidence = 0
default lilith_truth = False
default victoria_alliance = False

label start:
    scene black
    with fade

    "Hujan menyelimuti jalan menuju Rose Manor."
    "Di tanganku, surat undangan itu terasa semakin berat."

    mc "Tujuh malam. Apa yang sebenarnya mereka inginkan dariku?"

    jump night_1

label night_1:
    $ night = 1

    scene bg_manor_hall
    with dissolve

    show seraphina neutral

    ser "Kau akhirnya tiba."

    menu:
        "Menjawab dengan sopan":
            $ ser_aff += 1
            $ ser_trust += 1
            mc "Terima kasih telah menerimaku."
            ser "Kau sangat sopan, Guest."

        "Langsung bertanya tentang surat":
            $ ser_trust += 2
            mc "Aku ingin tahu siapa yang mengirim surat itu."
            ser "Pertanyaan yang tepat. Namun, belum waktunya."

        "Mengamati reaksinya":
            $ evidence += 1
            "Seraphina menggenggam liontin mawarnya."

    jump night_2

label night_2:
    $ night = 2
    scene bg_portrait_gallery

    "Sebuah potret tampak berbeda dari yang kuingat."

    menu:
        "Memeriksa potret":
            $ evidence += 1
            "Ada nama yang tergores di belakang bingkai."

        "Memanggil Evelyn":
            eve "Tuan, tidak ada yang berubah di galeri ini."
            $ ser_trust += 1

    jump night_3

label night_3:
    $ night = 3
    scene bg_rose_garden

    lil "Kau datang juga, Guest."

    menu:
        "Meminta Lilith menjelaskan":
            $ lilith_truth = True
            $ evidence += 1
            lil "Kalau kau ingin kebenaran, carilah kapel bawah tanah."

        "Menjaga jarak":
            "Sosok itu menghilang di balik kabut."

    jump night_4

label night_4:
    $ night = 4
    scene bg_library

    vic "Aku tahu apa yang dilakukan keluarga Rosewood."

    menu:
        "Bekerja sama dengan Victoria":
            $ victoria_alliance = True
            $ evidence += 1

        "Menolak campur tangan":
            vic "Jangan menyesal ketika kebenaran ditemukan orang lain."

    jump night_5

label night_5:
    $ night = 5
    scene bg_seraphina_room

    if ser_aff >= 2 and ser_trust >= 2:
        ser "Aku belum pernah menceritakan ini kepada siapa pun."
        "Untuk pertama kalinya, Seraphina membiarkan dirinya terlihat rapuh."
        $ ser_aff += 1
    else:
        ser "Ada banyak hal yang belum kau pahami tentang rumah ini."

    jump night_6

label night_6:
    $ night = 6
    scene bg_ritual_chamber

    "Di tengah ruangan terdapat lingkaran mawar yang menghitam."

    if evidence >= 3:
        "Potongan-potongan bukti itu akhirnya membentuk pola."
    else:
        "Aku belum menemukan cukup bukti untuk memahami ritual ini."

    jump night_7

label night_7:
    $ night = 7
    scene bg_ritual_chamber

    "Malam terakhir telah tiba."

    menu:
        "Mempercayai Seraphina":
            if ser_aff >= 3 and ser_trust >= 3:
                jump good_ending
            else:
                jump bad_ending

        "Mengungkap seluruh kebenaran":
            if evidence >= 5 and lilith_truth and victoria_alliance:
                jump true_ending
            else:
                jump bad_ending

label good_ending:
    scene bg_manor_hall
    "Seraphina menggenggam tanganku."
    "Malam itu, kami memilih masa depan bersama."
    return

label bad_ending:
    scene black
    "Ketika lonceng berdentang tujuh kali, mansion kembali sunyi."
    "Aku terbangun di depan gerbang Rose Manor."
    "Surat undangan itu kembali berada di tanganku."
    return

label true_ending:
    scene bg_rose_garden
    "Untuk pertama kalinya, mawar-mawar itu mekar tanpa darah."
    "Rahasia keluarga Rosewood akhirnya terungkap."
    return
```

### Catatan implementasi
1. Buat `variables.rpy` untuk semua variabel default.
2. Buat `characters.rpy` untuk definisi karakter.
3. Pisahkan ending ke `endings.rpy` ketika proyek berkembang.
4. Hindari menambah bukti berulang untuk petunjuk yang sama.
5. Uji semua kombinasi pilihan agar ending tidak terkunci karena kesalahan logika.
6. Tambahkan screen jurnal bukti dan galeri setelah alur utama stabil.

---

## 10. Daftar Aset 3D Prioritas

### Prioritas 1: Vertical slice
Buat aset berikut terlebih dahulu:
- Aula utama mansion.
- Kamar Seraphina.
- Taman mawar.
- Model Seraphina.
- Model atau placeholder Evelyn.
- Properti surat undangan dan liontin mawar.
- 8–12 variasi ekspresi/pose.
- 3–5 CG khusus untuk demo.
- 3–4 musik latar dan 10–15 efek suara.

### Prioritas 2: Produksi inti
- Galeri potret.
- Perpustakaan.
- Ruang ritual/kapel bawah tanah.
- Model Lilith dengan efek spektral.
- Model Victoria.
- Buku tamu, kunci lantai tiga, batu nisan, dan artefak ritual.
- Variasi pencahayaan: malam, candlelight, badai, dan cahaya bulan.

### Prioritas 3: Polish
- CG ending.
- Ekspresi tambahan.
- Efek kabut, partikel, dan perubahan potret.
- Galeri CG dan replay.
- Logo, key art, trailer, serta screenshot toko.

### Strategi penggunaan ulang
- Buat satu model karakter dan gunakan kembali dengan ekspresi, pose, framing, dan pencahayaan berbeda.
- Render latar dalam beberapa kondisi pencahayaan daripada membuat ulang seluruh lingkungan.
- Gunakan properti 3D yang sama sebagai petunjuk di beberapa adegan.
- Simpan file sumber Blender terpisah dari hasil render.
- Pastikan lisensi aset pihak ketiga mengizinkan penggunaan komersial.

---

## 11. Pipeline Visual dan Teknologi

### Blender
Gunakan Blender untuk:
- Pemodelan dan pengaturan karakter.
- Pembuatan lingkungan gothic.
- Material, pencahayaan, kamera, dan render.
- Rendering variasi ekspresi dan pose.
- Pembuatan CG sinematik.

### Ren'Py
Gunakan Ren'Py untuk:
- Dialog dan pilihan.
- Variabel relationship dan flag misteri.
- Perpindahan malam dan route.
- Ending.
- Jurnal bukti, galeri, pengaturan, dan penyimpanan.

### AI-assisted workflow
AI dapat membantu:
- Referensi konsep karakter dan lingkungan.
- Eksplorasi komposisi gambar.
- Draf dialog dan terjemahan awal.
- Ide efek suara atau musik, jika alat yang digunakan mengizinkan penggunaan komersial.
- Materi pemasaran awal.

Semua aset AI dan pihak ketiga perlu diperiksa kualitas, konsistensi, serta ketentuan lisensinya. Jangan menganggap setiap hasil generator otomatis aman untuk penggunaan komersial.

---

## 12. Struktur Folder Proyek

```text
game/
├── script.rpy
├── characters.rpy
├── variables.rpy
├── endings.rpy
├── screens.rpy
├── options.rpy
├── images/
│   ├── backgrounds/
│   ├── characters/
│   │   ├── seraphina/
│   │   ├── evelyn/
│   │   ├── lilith/
│   │   └── victoria/
│   ├── cg/
│   └── props/
├── audio/
│   ├── music/
│   └── sfx/
└── tl/
    ├── indonesian/
    └── english/
```

Gunakan penamaan file yang konsisten. Contoh:
- `bg_manor_hall_night.png`
- `bg_rose_garden_moonlight.png`
- `seraphina_neutral.png`
- `seraphina_sad.png`
- `cg_seraphina_promise.png`

Nama di script harus sesuai dengan nama aset yang tersedia.

---

## 13. Bahasa Indonesia dan Inggris

- Gunakan sistem terjemahan Ren'Py sejak awal.
- Jangan menanam teks penting ke dalam gambar.
- Pisahkan teks UI dari narasi jika memungkinkan.
- Uji panjang teks bahasa Inggris agar tidak memotong kotak dialog.
- Lakukan proofreading manusia untuk dialog emosional, idiom, dan istilah misteri.

Struktur direktori terjemahan mengikuti konfigurasi bahasa yang dibuat melalui tool terjemahan Ren'Py. Nama direktori harus cocok dengan bahasa yang diaktifkan di proyek.

---

## 14. Roadmap Produksi

### Tahap 1: Pre-production
- [ ] Finalisasi outline tujuh malam.
- [ ] Finalisasi rahasia utama dan aturan ritual.
- [ ] Buat diagram branching.
- [ ] Tetapkan palet warna dan standar render.
- [ ] Buat desain final Seraphina.

### Tahap 2: Vertical slice
- [ ] Buat aula, kamar Seraphina, dan taman mawar.
- [ ] Buat model Seraphina dan placeholder Evelyn.
- [ ] Implementasikan malam pertama.
- [ ] Buat satu pilihan yang berdampak.
- [ ] Uji render di dalam Ren'Py.
- [ ] Uji resolusi, ukuran file, dan performa.

### Tahap 3: Produksi inti
- [ ] Tambahkan malam 2–4.
- [ ] Tambahkan sistem evidence.
- [ ] Tambahkan hubungan dan flag cerita.
- [ ] Produksi model Lilith dan Victoria.
- [ ] Uji seluruh cabang yang tersedia.

### Tahap 4: Penyelesaian
- [ ] Selesaikan malam 5–7.
- [ ] Implementasikan tiga ending.
- [ ] Tambahkan jurnal bukti dan galeri.
- [ ] Tambahkan bahasa Inggris.
- [ ] Uji semua jalur dari awal sampai ending.
- [ ] Siapkan demo, trailer, screenshot, dan halaman toko.

Jangan menentukan tanggal rilis sebelum vertical slice selesai dan kecepatan produksi aset dapat diperkirakan.

---

## 15. Strategi Demo dan Penjualan

1. Buat demo 15–30 menit yang memperlihatkan mansion, Seraphina, aturan supernatural, dan satu cliffhanger.
2. Tampilkan identitas visual yang konsisten: hitam, merah mawar, ungu gelap, cahaya lilin, dan kabut.
3. Jelaskan dengan jelas bahwa game ini merupakan gothic mystery dengan romance bercabang.
4. Gunakan screenshot yang benar-benar berasal dari game.
5. Uji demo dengan pemain dan catat bagian yang membingungkan atau membosankan.
6. Tentukan harga setelah ruang lingkup, kualitas, durasi, dan biaya produksi lebih jelas.
7. Periksa kebijakan platform, klasifikasi usia, dan ketentuan konten sebelum publikasi.

Konsep yang menarik tidak menjamin keuntungan. Demo yang selesai dan diuji merupakan cara yang lebih aman untuk mengukur minat pemain sebelum memperbesar proyek.

---

## 16. Risiko Produksi

| Risiko | Mitigasi |
|---|---|
| Terlalu banyak aset 3D | Batasi lokasi dan gunakan ulang model serta pencahayaan |
| Cerita bercabang membengkak | Gunakan satu misteri utama dan route yang berbagi adegan inti |
| Inkonistensi karakter dari AI | Buat model referensi tetap dan panduan visual |
| Bug ending | Uji kombinasi variabel dengan walkthrough |
| Terjemahan tidak konsisten | Buat glosarium nama, istilah, dan gaya bahasa |
| Proyek terlalu lama | Prioritaskan vertical slice sebelum konten lengkap |
| Masalah lisensi | Catat sumber dan lisensi semua aset eksternal |

---

## 17. Keputusan yang Belum Dikunci

Hal-hal berikut perlu diputuskan sebelum produksi penuh:
- Resolusi render final dan target spesifikasi PC.
- Apakah nama MC bisa dikustomisasi.
- Jumlah pasti CG untuk game penuh.
- Apakah route karakter pendukung akan berupa subplot non-romantis atau romance singkat.
- Harga dan platform distribusi.
- Detail klasifikasi usia dan kebijakan konten platform.

---

## 18. Langkah Berikutnya

**Tugas pertama:** selesaikan vertical slice malam pertama.

Urutan kerja:
1. Buat folder proyek Ren'Py.
2. Implementasikan dialog kedatangan.
3. Buat satu latar aula dan satu render Seraphina.
4. Implementasikan tiga pilihan pertama.
5. Pastikan variabel berubah dengan benar.
6. Jalankan game dan uji setiap pilihan.
7. Baru setelah itu mulai memproduksi lokasi berikutnya.

**Prinsip utama:** selesaikan satu bagian kecil yang dapat dimainkan sebelum memperbesar cakupan game.
