# Seven Nights at Rose Manor

**Seven Nights at Rose Manor** adalah novel visual misteri gotik psikologis (psychological gothic mystery visual novel) yang dibangun menggunakan mesin **Ren'Py 8.5+** (Python 3).

---

## Informasi Versi
- **Versi Saat Ini**: `v1.0.0`
- **Status Rilis**: Rilis Lengkap Cerita & Sistem Investigasi (7 Malam Penuh, Multi Ending, Sistem Bukti & Audio Victorian)
- **Mesin Permainan**: Ren'Py 8.5.2+ (Python 3.10+)
- **Bahasa yang Didukung**: Bahasa Indonesia & English

---

## Sinopsis Cerita
Sebuah undangan misterius membawa seorang penyelidik ke Rose Manor—sebuah kastil megah terpencil bergaya Victorian yang diselimuti rahasia kelam keluarga bangsawan serta misteri okultisme masa lalu.

Badai dahsyat yang melanda memutus seluruh akses keluar dari lembah Rose Manor selama tujuh malam berturut-turut. Setiap malam membawa ketegangan baru, bisikan-bisikan tak kasat mata, dan kematian misterius yang mengguncang para penghuni manor. Di balik tatapan dingin Victoria, senyum misterius Evelyn, kewaspadaan Arthur, dan doa-doa gelap Pastor Thomas, tersimpan kebenaran kelam yang menuntut untuk diungkapkan sebelum malam ketujuh berakhir.

---

## Fitur Utama Permainan

### 1. Sistem Jurnal Investigasi & Berkas Barang Bukti (Evidence Journal)
- Mengumpulkan barang bukti, dokumen kuno, artefak okultisme, dan catatan forensik sepanjang tujuh malam.
- Dilengkapi dengan fitur **Inspeksi Visual Penuh** yang memungkinkan pemain meneliti ilustrasi barang bukti dalam resolusi tinggi beserta catatan analisis detail dan tanggal penemuan.

### 2. Sistem Hubungan & Kepercayaan Karakter (Trust & Affection System)
- Setiap pilihan dialog dan tindakan investigasi memengaruhi tingkat kepercayaan (*Trust*) serta kedekatan (*Affection*) masing-masing penghuni manor:
  - **Evelyn Rosewood**: Putri tertua keluarga yang tampak ramah namun menyimpan rahasia masa lalu.
  - **Victoria Rosewood**: Sosok bangsawan dingin dan penuh otoritas yang mencurigai setiap langkah penyelidik.
  - **Arthur Pendelton**: Pengurus setia manor yang menjaga rahasia terdalam kediaman.
  - **Pastor Thomas**: Rohaniwan yang mengetahui sejarah kelam dan ritual terlarang Rose Manor.

### 3. Percabangan Cerita & Ragam Ending (Branching Storylines)
- Keputusan pemain, barang bukti yang berhasil ditemukan, serta tingkat kepercayaan karakter menentukan nasib akhir penyelidik dan penghuni Rose Manor dalam berbagai konklusi cerita:
  - *True Ending*: Mengungkap dalang sebenarnya dan mematahkan kutukan Rose Manor.
  - *Tragic Endings*: Terjebak dalam kutukan abadi manor atau menjadi korban intrik okultisme.
  - *Escape Ending*: Melarikan diri dari manor namun meninggalkan misteri yang tak terpecahkan.

### 4. Lanskap Suara & Desain Antarmuka Victorian (Atmospheric Soundscape & UI)
- Efek suara interaktif yang dibuat khusus untuk nuansa gotik klasik: klik mekanis kuningan, gesekan halus kertas perkamen, sampul jurnal kulit, ketukan berkas investigasi, dan denting pilihan narasi.
- Komposisi musik latar atmosferik yang mengiringi pergantian waktu dari siang yang mencekam hingga malam yang penuh misteri.

### 5. Dukungan Dwi-Bahasa Penuh (Bilingual Support)
- Mendukung peralihan bahasa secara instan antara **Bahasa Indonesia** dan **English** melalui menu pengaturan (Preferences).

---

## Kontrol & Tombol Pintasan

| Tombol / Aksi | Fungsi |
|---|---|
| **Klik Kiri / Spasi / Enter** | Melanjutkan dialog dan memilih opsi |
| **Klik Kanan / Tombol Esc** | Membuka Menu Permainan / Menutup Layar Modal |
| **Scroll Roda Mouse ke Atas** | Membuka Riwayat Percakapan (History Log) |
| **Tab** | Melewati dialog yang sudah dibaca (Skip Mode) |
| **Ctrl** | Mode lewati cepat (Fast Skip) |
| **H** | Menyembunyikan antarmuka dialog (Hide Interface) |
| **S** | Mengambil tangkapan layar (Screenshot) |

---

## Petunjuk Menjalankan Proyek dari Source Code

### Prasyarat
1. Unduh dan pasang **Ren'Py 8.5.0 atau versi yang lebih baru** dari situs resmi [Ren'Py](https://www.renpy.org/).
2. Unduh atau clone repositori ini ke komputer Anda.

### Menjalankan Melalui Ren'Py Launcher
1. Buka aplikasi **Ren'Py Launcher**.
2. Klik tombol **preferences** di pojok kanan bawah Ren'Py Launcher, lalu pastikan direktori proyek mencakup folder tempat repositori ini disimpan.
3. Pilih proyek **Seven Nights at Rose Manor** pada daftar di sisi kiri.
4. Klik **Launch Project** untuk memulai permainan.

### Melakukan Linting / Pengecekan Script
Untuk memeriksa integritas script Ren'Py tanpa membuka antarmuka grafis:
```bash
renpy.exe "path/to/Seven Nights at Rose Manor" lint
```

---

## Struktur Direktori Proyek

```
Seven Nights at Rose Manor/
├── game/
│   ├── audio/
│   │   ├── music/           # Musik latar (BGM) per lokasi dan suasana
│   │   └── sfx/             # Efek suara GUI, buku jurnal, dan atmosfer lingkungan
│   ├── gui/                 # Aset grafis antarmuka, frame bukti, dan ornate borders
│   ├── images/              # Sprite ekspresi karakter dan latar belakang adegan (BG)
│   ├── tl/                  # Berkas lokalisasi terjemahan (English)
│   ├── custom_screens.rpy   # Antarmuka Jurnal Investigasi & Status Hubungan Karakter
│   ├── evidence_system.rpy  # Logika database barang bukti dan modal inspeksi
│   ├── gui.rpy              # Pengaturan dimensi, font, dan warna antarmuka
│   ├── options.rpy          # Konfigurasi judul, versi (v1.0.0), transisi, dan audio
│   ├── screens.rpy          # Layar dialog, menu utama, quick menu, navigasi, dan pilihan
│   ├── script.rpy           # Alur pembuka dan inisialisasi permainan
│   ├── story_prologue.rpy   # Prolog kedatangan di Rose Manor
│   ├── story_day1.rpy - story_day7.rpy   # Alur cerita investigasi siang hari
│   ├── story_night1.rpy - story_night7.rpy # Alur cerita dan teror malam hari
│   └── variables.rpy        # Inisialisasi variabel status, item bukti, dan audio
├── .gitignore               # Konfigurasi pengabaian berkas cache/bytecode Ren'Py
└── README.md                # Dokumentasi utama proyek
```

---

## Rencana Pengembangan (Roadmap Versi Mendatang)

Proyek ini dirancang untuk terus berkembang dengan penambahan konten pada rilis-rilis berikutnya:

- **v1.0.0 (Rilis Saat Ini)**:
  - Cerita lengkap Prolog hingga Malam ke-7 dengan percabangan multi-ending.
  - Sistem Jurnal Investigasi & Inspeksi Visual Bukti resolusi tinggi.
  - Sistem Status Hubungan & Kepercayaan Karakter.
  - Implementasi penuh efek suara Victorian dan musik latar orisinal.
  - Lokalisasi dwi-bahasa (Bahasa Indonesia & English).

- **v1.1.0 (Rencana Rilis Berikutnya)**:
  - Mini-game deduksi penyelidikan interaktif (menghubungkan benang merah antar bukti).
  - Galeri ekstra: pembuka ilustrasi CG, pemutar musik interaktif (BGM Player), dan arsip dokumen rahasia.
  - Tambahan rute percakapan sampingan untuk mendalami latar belakang masa lalu masing-masing karakter.

- **v1.2.0 (Rencana Rilis Lanjutan)**:
  - Integrasi voice acting untuk dialog-dialog kunci.
  - Animasi visual cutscene dan efek partikel cuaca (badai dan kilat atmosferik).
  - Porting dan optimasi untuk platform Android / Mobile.

---

## Lisensi & Hak Cipta
Hak cipta skrip, cerita, dan aset visual/audio berada di bawah kepemilikan kreator Seven Nights at Rose Manor. Dikembangkan dengan perangkat lunak open-source Ren'Py.
