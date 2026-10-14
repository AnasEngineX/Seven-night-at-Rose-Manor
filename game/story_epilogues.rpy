## story_epilogues.rpy
## Epilog Lengkap dan Resolusi Akhir (The Epilogues of Rose Manor)
## Naskah interaktif sastra gothic romance dan resolusi takdir

## =========================================================================
## EPILOG GOOD ENDING: CINTA DI TENGAH SEMERBAK MAWAR
## =========================================================================
label good_ending_epilogue:
    scene black
    with fade

    "Enam bulan telah berlalu sejak malam ketujuh berdarah di Rose Manor."
    "Salju tebal dan embun beku yang selama puluhan tahun menyelimuti lembah Ashwood telah meleleh seutuhnya di bawah kehangatan musim semi yang tiba tepat waktu."
    "Lereng-lereng bukit granit yang dahulu kelabu dan suram kini diselimuti oleh permadani rumput hijau segar, bunga-bunga liar berwarna keemasan, dan dedaunan pohon willow yang bertunas lebat."

    scene bg_rose_garden
    with fade

    "Di taman mawar Rose Manor, perubahan yang terjadi sungguh menakjubkan."
    "Semak-semak mawar merah kini bermekaran dengan keindahan yang alami, segar, dan sehat."
    "Duri-duri hitam purba yang beracun telah dipangkas habis, digantikan oleh kuncup-kuncup bunga mawar merah muda dan putih yang menebarkan wangi nektar manis ke seluruh penjuru pekarangan."
    "Air mancur malaikat marmer di tengah taman yang selama seabad tersumbat oleh lumut hitam kini telah diperbaiki, mengalirkan air jernih pegunungan yang gemericik menenangkan."
    "Kawanan burung gereja dan burung pipit berkicau riang di dahan-dahan pohon, menyanyikan simfoni kehidupan yang belum pernah terdengar di tanah ini."

    "Di beranda marmer yang menghadap ke arah lembah, Seraphina berdiri bersandar pada pagar batu."
    "Hari ini, ia mengenakan gaun sutra musim semi berwarna merah muda pucat dengan selendang renda putih yang berkibar lembut ditiup angin sepoi-sepoi."
    "Rambut peraknya yang panjang dibiarkan terurai bebas, berkilau keemasan disinari hangatnya cahaya matahari pagi."
    "Di dadanya, bros mawar merah delima tersemat anggun—bukan lagi sebagai wadah kutukan penghisap memori, melainkan sebagai tanda cinta abadi kami."

    show seraphina neutral with dissolve

    ser "Kau sudah selesai memeriksa surat-surat kiriman dari kota pelabuhan selatan, Guest?"

    mc "Sudah, Seraphina. Para saudagar kain sutra dan kurir pos sekarang tidak lagi ragu-ragu untuk menaiki bukit dan mengantarkan barang langsung ke depan pintu Rose Manor."
    mc "Nama Rose Manor bukan lagi momok yang menakutkan bagi penduduk kota Ashwood, melainkan kediaman bangsawan yang dihormati dan ramah."

    "Seraphina melangkah mendekatiku dengan keanggunan yang penuh kebahagiaan."
    "Ia menyandarkan kepalanya dengan manja di pundakku, melingkarkan lengannya di pinggangku, dan menatap ke arah lembah yang hijau di bawah sana."
    "Jemarinya yang hangat menyelinap di antara jemariku, menggenggam tanganku dengan erat dan penuh rasa syukur yang tak terhingga."

    show seraphina smile with dissolve

    ser "Semua keajaiban ini terjadi berkat dirimu, cintaku..."
    ser "Berkat keberanianmu untuk memelukku di depan altar kapel, di saat seluruh dunia dan akal sehat menyuruhmu untuk melarikan diri."
    ser "Setiap kali aku memetik mawar di taman ini... aku tidak lagi mencium aroma darah atau keputusasaan."
    ser "Aku hanya mencium aroma kebebasan, kehangatan, dan masa depan indah yang akan kita bangun bersama."

    mc "Kita telah merebut masa depan itu dari cengkeraman malam, Seraphina. Dan aku berjanji akan menjaganya bersamamu hingga akhir hayatku."

    "Seraphina tersenyum manis—sebuah senyuman yang begitu murni dan bahagia hingga membuat hatiku bergetar."
    "Perlahan, ia mendongakkan wajahnya dan mendaratkan sebuah kecupan lembut, hangat, dan penuh gairah di bibirku di bawah siraman cahaya mentari musim semi."

    hide seraphina with dissolve

    "Kutukan tujuh malam telah berakhir."
    "Dan cinta sejati yang mekar di Rose Manor akan terus bersemi untuk selama-lamanya."
    return

## =========================================================================
## EPILOG TRUE ENDING: KEBANGKITAN DAN CAHAYA ABADI
## =========================================================================
label true_ending_epilogue:
    scene black
    with fade

    "Satu tahun setelah malam pembebasan mutlak di Kapel Bawah Tanah Rose Manor."
    "Kabar tentang runtuhnya kutukan Rose Manor telah menyebar ke seluruh penjuru negeri, mengubah lembah terpencil ini menjadi simbol kebangkitan dan perdamaian spiritual."

    scene bg_rose_garden
    with fade

    "Di sudut taman mawar yang paling tenang dan terlindung, sebuah nisan marmer putih baru berdiri dengan anggun di bawah naungan pohon willow yang rindang."
    "Di atas lempengan marmer putih yang bersih berkilau itu, terpahat sebuah tulisan prasasti bertinta emas murni:"
    "{i}'Lilith Vane (1870 - 1892)'{/i}"
    "{i}'Jiwa yang Telah Bebas dari Belenggu Duka, Diingat Selamanya sebagai Sahabat Sejati dan Pelindung Abadi Rose Manor.'{/i}"

    "Evelyn Hart melangkah anggun menyusuri jalan setapak berkerikil putih."
    "Ia tidak lagi mengenakan gaun pelayan hitam-putihnya yang kaku; hari ini, ia mengenakan gaun wol anggun berwarna biru safir seorang wanita bangsawan merdeka."
    "Wajahnya yang awet muda tampak berseri-seri dengan kehangatan manusiawi yang sejati."
    "Dengan gerakan khidmat dan penuh rasa hormat, ia meletakkan seikat bunga mawar putih segar di atas makam Lilith."

    show evelyn smile at sprite_mid_left with dissolve

    eve "Selamat pagi, Nona Lilith."
    eve "Hari ini adalah hari peringatan satu tahun pembebasan kita. Rose Manor dipenuhi oleh suara tawa, musik, dan para tamu yang datang untuk belajar sejarah."
    eve "Tuan Jonathan dan Anda... akhirnya bisa beristirahat dalam damai di surga abadi."

    "Suara langkah kaki yang mantap dan tegas terdengar dari arah gerbang taman."
    "Victoria Ashbourne melangkah mendekat dengan mantel wol modis dan membawa sebuah buku tebal bersampul kulit merah marun bertuliskan lambang Universitas Kerajaan."

    show victoria smile at sprite_mid_right with dissolve

    vic "Evelyn! Lihat apa yang baru saja diantarkan oleh kurir kereta pos dari ibu kota!"
    vic "Buku hasil penelitianku akhirnya resmi diterbitkan oleh Percetakan Akademik Kerajaan!"
    vic "Judul resminya: {i}'The Rosewood Phenomenon: How Truth and Reason Conquered the Gothic Myth'{/i}."
    vic "Buku ini membuktikan kepada seluruh komunitas ilmiah bahwa fenomena okultisme bukanlah takdir kutukan mutlak, melainkan anomali eterik yang dapat dinetralkan melalui rekonsiliasi sejarah dan pemahaman nalar yang tepat!"

    eve "Selamat atas pencapaian akademis Anda yang luar biasa, Nona Victoria. Dedikasi kakek buyut Anda akhirnya terbayar lunas dengan kehormatan tertinggi."

    "Suara denting piano yang merdu terdengar mengalun dari arah rumah kaca teras sayap selatan."
    "Seraphina dan aku melangkah keluar dari teras menuju taman mawar, menyambut Victoria dan Evelyn dengan senyuman lebar."
    "Seraphina mengenakan gaun sutra putih keperakan yang mempesona, dengan bros mawar putih kristal berkilauan di dadanya."
    "Di tangan kanannya, ia memegang lembaran partitur musik Nocturne Lilith Vane yang baru saja ia mainkan di grand piano ruang musik yang telah direnovasi."

    show evelyn smile at sprite_left with dissolve
    show seraphina dawn at sprite_center with dissolve
    show victoria smile at sprite_right with dissolve

    ser "Selamat atas bukumu, Victoria! Karyamu akan memastikan bahwa tidak ada lagi orang yang datang ke lembah ini dengan ketakutan atau niat jahat."

    vic "Terima kasih banyak, Seraphina. Namun kita semua tahu siapa pahlawan sesungguhnya dari penyelidikan ini."
    vic "Tanpa tekad bulat Tuan Guest dan cintamu yang menolak menyerah, buku ini hanyalah catatan tentang sekelompok korban berikutnya."

    "Victoria dan Evelyn pamit untuk menikmati jamuan teh sore di beranda rumah kaca bersama para sarjana tamu yang baru tiba dari ibu kota."

    hide victoria with dissolve
    hide evelyn with dissolve

    "Kini, Seraphina dan aku berdiri berdua di bawah semilir angin sepoi-sepoi pohon willow, saling menatap dengan kedalaman rasa yang tak terlukiskan oleh kata-kata."

    show seraphina smile at sprite_center with dissolve

    ser "Tujuh malam yang kita lalui setahun yang lalu... terkadang masih terasa seperti mimpi buruk yang sangat jauh, Guest."
    ser "Namun setiap detiknya adalah anugerah terbesar dalam hidupku, karena bahaya itulah yang membimbingmu melangkah ke dalam hatiku."

    mc "Dan aku tidak akan pernah melepaskan jemarimu, Seraphina. Kita telah menghalau malam tergelap, dan fajar di Rose Manor tidak akan pernah padam lagi."

    "Seraphina melingkarkan kedua tangannya di leherku, menarikku mendekat ke dalam dekapannya."
    "Di bawah langit biru cerah lembah Ashwood dan di hadapan semerbak ribuan mawar putih yang mekar damai, sebuah ciuman abadi mengunci takdir kebahagiaan kami berdua."

    hide seraphina with dissolve
    return

## =========================================================================
## EPILOG BAD ENDING: RATAPAN DI DALAM KEHAMPAAN
## =========================================================================
label bad_ending_epilogue:
    scene black
    with fade

    "Di sebuah dimensi hampa tanpa batas waktu, ruang, atau cahaya..."
    "Kepingan-kepingan kristal memori melayang-layang perlahan di kegelapan abadi laksana pecahan cermin kaca yang berlumuran darah."

    "Di dalam setiap pecahan cermin memori itu, bayang-bayang masa lalu berputar tanpa suara, menertawakan ketidakberdayaanku:"
    "Senyuman lembut Seraphina saat menyeduh teh di ruang duduk pribadinya..."
    "Aroma harum mawar yang segar di rumah kaca saat jemarinya tergores duri..."
    "Lentera perak Evelyn yang menuntunku di lorong-lorong bawah tanah..."
    "Gema tawa spektral Lilith Vane di antara kabut taman labirin..."
    "Dan rumus-rumus okultisme Victoria yang tertulis dengan tinta merah di perpustakaan..."

    "Aku mengulurkan kedua tanganku ke dalam kehampaan dingin, berusaha sekuat tenaga merengkuh kepingan-kepingan ingatan yang berharga itu."
    "Namun begitu ujung jemariku menyentuhnya, kepingan-kepingan itu hancur berkeping-keping menjadi debu merah tua yang tersapu oleh badai kehampaan abadi."

    mc "Seraphina... siapa Seraphina...?"
    mc "Mengapa... mengapa dadaku terasa begitu sakit, sesak, dan hampa... seolah separuh jiwaku telah direnggut paksa...?"

    "Sebuah suara isak tangis wanita muda bergema lirih dan menyayat hati dari kejauhan dimensi yang tak terjangkau:"
    ser "{i}...Maafkan aku, Guest... Kumohon ampuni dosaku...{/i}"
    ser "{i}...Aku harus melupakan wajahmu sekali lagi demi kelangsungan rumah terkutuk ini...{/i}"
    ser "{i}...Siklus mawar ini akan terus berputar menelan jiwa... sampai fajar yang sesungguhnya sudi menyapa kita...{/i}"

    "Kesadaranku ditarik mundur dengan kecepatan yang memusingkan, jatuh semakin dalam ke dalam jurang ketiadaan..."
    "Menanti dentangan lonceng malam pertama berikutnya..."
    return

