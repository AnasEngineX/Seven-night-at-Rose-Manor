## story_night4.rpy
## Malam 4: The Occult Guest (Perpustakaan Tua dan Rahasia Okultisme Victoria)
## Naskah interaktif sastra gothic mystery mendalam

label night_4:
    $ night = 4

    scene black
    with fade

    "Malam keempat menandai titik balik yang menentukan dalam perjalananku di Rose Manor."
    "Rintik hujan di luar jendela berubah menjadi badai angin kencang yang menghantam daun-daun jendela kaca bertingkat dengan suara gemeretak keras laksana ketukan cakar raksasa."
    "Di dalam dinding-dinding batu mansion yang menjulang tebal, suasana terasa semakin sunyi, dingin, dan tegang—seolah-olah seluruh bangunan raksasa ini sedang menahan napasnya sebelum badai kutukan yang sesungguhnya pecah menenggelamkan segalanya."

    "Sesuai dengan perkataan Seraphina semalam di taman mawar, rahasia mansion ini tidak hanya tersimpan di antara kelopak bunga, melainkan tertanam jauh di dalam catatan-catatan sejarah yang berusaha dikubur oleh para leluhur Rosewood."
    "Tujuanku malam ini adalah Perpustakaan Besar di sayap timur mansion—tempat di mana Victoria Ashbourne, sang tamu okultis yang misterius, menghabiskan sebagian besar malamnya di antara tumpukan naskah kuno."

    scene bg_library
    with fade

    "Perpustakaan Rose Manor adalah sebuah aula raksasa berkubah tinggi berarsitektur gotik murni yang dipenuhi oleh puluhan ribu jilid buku dari berbagai abad."
    "Rak-rak buku raksasa berbahan kayu mahoni gelap menjulang tinggi hingga ke langit-langit berukir lambang mawar mekar dan naga bersayap, dipenuhi barisan manuskrip tebal bersampul kulit anak sapi yang berdebu."
    "Tangga-tangga beroda dari besi tempa hitam bersandar di beberapa sudut rak tinggi, sementara karpet persia tebal bermotif floral meredam setiap getaran langkah kakiku laksana berjalan di atas lapisan lumut hutan."

    "Aroma khas kertas lapuk berusia ratusan tahun, tinta besi empedu purba, dan debu berpadu serasi dengan wangi kayu manis dari tungku perapian tembaga yang menyala hangat di sudut ruangan."
    "Di sepanjang koridor rak buku, deretan buku bertema alkimia, demonologi, filsafat mistik, dan risalah teologi abad pertengahan berbaris rapi:"
    "{i}'De Morte et Memoria', 'Ars Umbrarum et Clavicula', serta kronik keluarga bangsawan Rosewood bertarikh 1745.{/i}"

    "Di tengah perpustakaan, di atas sebuah meja baca raksasa berbahan kayu jati tua yang melengkung anggun, tumpukan buku-buku bersampul kulit berserakan di samping peta-peta topografi dan gulungan perkamen tua yang menguning."
    "Seorang wanita muda duduk bertumpu pada dagunya di depan lentera minyak kuningan yang memancarkan cahaya keemasan hangat dan stabil."

    "Ia mengenakan rompi beludru hitam berpotongan maskulin di atas kemeja putih berlengan panjang dengan manset rapi—gaya busana yang begitu praktis, modern, dan sangat tidak lazim bagi wanita bangsawan era Victoria konvensional."
    "Rambut auburn pendeknya disisir rapi ke samping dengan belahan tegas, menonjolkan garis rahangnya yang kuat dan sepasang mata tajam berwarna keemasan seperti mata burung pemangsa yang sedang mengincar buruannya."
    "Sebuah kacamata berbingkai kawat perak bertengger rapi di pangkal hidungnya, memantulkan baris-baris tulisan latin dari buku folio tebal bertinta merah di hadapannya."

    show victoria neutral with dissolve

    vic "Kau terlambat dua puluh menit dari perkiraanku, Tuan Guest."

    "Victoria Ashbourne tidak mengangkat kepalanya dari naskah kuno yang sedang dibacanya saat ia berbicara."
    "Jemari kanannya yang ramping memutar pena bulu angsa bertinta hitam dengan ketenangan dan ketepatan mekanis yang luar biasa."

    mc "Kau tahu aku akan datang ke perpustakaan malam ini, Nona Ashbourne?"

    "Victoria akhirnya mengangkat pandangannya dari buku folio tebal itu."
    "Dengan gerakan anggun dan percaya diri, ia melepaskan kacamata kawat peraknya, meletakkannya di atas meja, lalu menatapku lurus dengan sepasang mata keemasannya yang tajam menembus."

    vic "Seraphina Rosewood mungkin adalah seorang bangsawan yang dingin, anggun, dan penuh dengan rahasia gelap, tetapi gerak-gerik emosinya sangat mudah dipetakan oleh siapa pun yang memahami psikologi rasa bersalah."
    show victoria serious with dissolve
    vic "Ia tahu kau telah berbicara dengan arwah Lilith Vane di taman mawar semalam. Dan ia tahu bahwa seorang pria dengan akal sehat dan naluri bertahan hidup tidak akan berhenti sampai ia menemukan kepingan yang hilang dari teka-teki berdarah ini."
    vic "Tarik kursi itu dan duduklah, Guest. Kita memiliki banyak hal mendesak untuk dibicarakan sebelum lonceng tengah malam berdentang."

    "Aku menarik sebuah kursi berlengan berlapis beludru hijau tua dan duduk di seberang mejanya yang lebar."
    "Di atas meja baca, sebuah diagram lingkaran sihir kuno digambar dengan tinta merah pekat di atas perkamen kulit anak lembu, dikelilingi oleh angka-angka geometris dan kutipan-kutipan teks latin kuno."

    menu:
        "Menanyakan alasan Victoria menyelidiki Rose Manor dan keterlibatan keluarganya":
            $ ser_trust += 1
            $ evidence += 1
            mc "Victoria, kau jelas bukan sekadar tamu biasa yang kebetulan tersesat dalam badai salju. Apa tujuan sebenarnya dari penyelidikan keluargamu terhadap Rose Manor?"
            show victoria smile with dissolve
            "Victoria tersenyum tipis--sebuah senyuman penuh kebanggaan intelektual bercampur kepahitan masa lalu."
            show victoria serious with dissolve
            vic "Kakek buyutku, Profesor Arthur Ashbourne, adalah seorang sarjana okultisme terkemuka dari Universitas Kerajaan pada akhir abad kesembilan belas."
            vic "Pada musim gugur tahun 1892, ia diundang secara pribadi ke mansion ini oleh Lord Jonathan Rosewood untuk mendokumentasikan apa yang disebut Jonathan sebagai 'anomali temporal di lembah mawar'."
            vic "Namun apa yang ditemukan kakekku di sini bukanlah anomali ilmiah belaka, melainkan ritual pengorbanan jiwa yang keji terhadap seorang gadis bernama Lilith Vane."
            vic "Kakekku berhasil melarikan diri dari mansion ini dengan buku catatannya yang robek separuh, namun sisa hidupnya dihabiskan di dalam rumah sakit jiwa, dihantui oleh mimpi buruk tentang mawar berdarah dan jeritan di bawah tanah."
            vic "Aku datang ke sini untuk menyelesaikan apa yang gagal ia hentikan seratus tiga puluh tahun yang lalu. Aku ingin membuktikan bahwa tidak ada kutukan mistis yang tidak bisa dipatahkan oleh sains, logika, dan analisis yang tepat."
            mc "Keluargamu telah mewariskan obsesi ini selama beberapa generasi..."
            vic "Tepat sekali. Dan aku tidak berniat menjadi generasi berikutnya yang mati penasaran di dalam kuburan tak bertanda."

        "Langsung bertanya tentang cara kerja ritual penghapusan ingatan dan segel tujuh malam":
            $ evidence += 2
            mc "Lilith menyebutkan bahwa ritual mawar menghapus ingatan para tamu yang datang ke sini. Ceritakan padaku apa yang sebenarnya terjadi di kapel bawah tanah."
            vic "Pertanyaan yang langsung menusuk ke inti persoalan tanpa membuang waktu. Aku menyukai orang yang berpikir dengan efisiensi nalar."
            "Victoria menggeser diagram perkamen di atas meja ke hadapanku, menunjuk simbol-simbol geometris yang melingkari pusat diagram."
            vic "Ritual ini dikenal dalam risalah okultisme terlarang dari abad keenam belas sebagai {i}'Sigillum Septem Foliorum'{/i}—Segel Tujuh Kelopak."
            vic "Rose Manor dibangun tepat di atas persimpangan garis ley gaib yang menampung energi kehampaan dari perut bumi."
            vic "Untuk menjaga agar tanah ini tidak runtuh ke dalam dimensi ketiadaan, leluhur pertama Rosewood membuat pakta darah."
            vic "Setiap siklus tertentu, mereka membutuhkan satu jiwa tamu yang memiliki resonansi emosional yang murni untuk menyerap kelebihan energi kehampaan itu."
            vic "Enam malam pertama digunakan untuk memancing keterikatan emosi, mengikis pertahanan batin sang tamu melalui ilusi, keindahan, dan aroma mawar beracun."
            vic "Dan di malam ketujuh... seluruh ingatan hidup sang tamu akan disedot seutuhnya ke dalam inti kristal bros mawar milik Seraphina, menyisakan cangkang tubuh kosong yang dikembalikan ke dunia luar tanpa nama dan tanpa masa lalu."
            mc "Itu adalah pencurian eksistensi manusia yang teramat mengerikan..."
            vic "Tepat. Jiwamu tetap bernapas, tetapi siapa dirimu yang sesungguhnya telah dimusnahkan untuk selamanya."

        "Mempertanyakan apakah Seraphina mengetahui kebenaran kejam dari ritual berdarah ini":
            $ ser_aff += 1
            $ ser_trust += 1
            mc "Apakah Seraphina menyadari bahwa ritual yang ia jalankan ini adalah pembunuhan terhadap ingatan manusia?"
            vic "Seraphina dididik sejak kecil oleh mendiang ayahnya bahwa ritual ini adalah 'tanggung jawab suci dan berkah' untuk menjaga keseimbangan dunia."
            show victoria sad with dissolve
            vic "Gadis itu tidak memiliki niat jahat di dalam hatinya, Guest. Namun kepatuhan buta pada tradisi leluhur sering kali melahirkan kekejaman yang sama persis dengan kejahatan murni."
            vic "Ia percaya bahwa jika ritual ini dihentikan, seluruh mansion, kenangan tentang orang tuanya, dan nyawanya sendiri akan musnah seketika ditelan kehampaan."
            vic "Ketakutannya akan kematian dan rasa bersalahnya adalah rantai terkuat yang mengikatnya pada takdir berdarah ini."
            mc "Jika kita bisa membuktikan bahwa ada jalan lain untuk menutup kehampaan tanpa mengorbankan ingatan... Seraphina mungkin akan berdiri di pihak kita."
            vic "Itu adalah idealisme yang sangat mulia, Guest. Namun emosi manusia sering kali jauh lebih sulit diprediksi daripada kalkulasi okultisme."

    vic "Sekarang, Guest, kita berada pada persimpangan jalan yang sangat krusial."
    vic "Aku telah memetakan enam dari tujuh segel di ruang bawah tanah. Namun segel ketujuh—inti dari lingkaran mawar—hanya bisa ditembus dengan dua sarana mutlak."
    vic "Pertama: Mawar hitam abadi dari nisan Lilith Vane sebagai penangkal ilusi darah."
    vic "Kedua: Kunci perak kuno berukir mawar yang selalu tergantung di leher Evelyn Hart."

    mc "Kunci perak milik Evelyn? Pelayan tua itu yang memegang kunci kapel bawah tanah?"

    vic "Tepat sekali. Evelyn bukanlah manusia biasa, Guest. Kau tentu sudah menyadari kejanggalan dalam buku tamu tahun 1884, bukan?"
    vic "Ia adalah penjaga abadi sumpah Rosewood, terikat oleh darah untuk memastikan tidak ada satu pun tamu yang keluar dari sini dengan membawa ingatan mereka."

    menu:
        "Menyetujui aliansi penuh dengan Victoria untuk membongkar dan menghancurkan ritual":
            $ victoria_alliance = True
            $ evidence += 1
            call inspect_clue("seal_diagram")
            $ unlock_achievement("ach_victoria", "Aliansi Rahasia")
            mc "Aku setuju untuk bekerja sama denganmu, Victoria. Kita harus mengumpulkan seluruh bukti dan mematahkan segel ketujuh bersama-sama."
            show victoria smile with dissolve
            vic "Keputusan yang sangat rasional, berani, dan tepat sasaran. Bersama-sama, kita memiliki peluang nyata untuk mengakhiri siklus berdarah ini sekali untuk selamanya."
            "Victoria mengulurkan tangannya yang kokoh dan menggenggam tanganku erat sebagai tanda persekutuan ilmiah dan taktis."
            vic "Ambillah salinan diagram segel ketujuh ini. Simpan rapat-rapat di balik saku mantelmu."

        "Menerima kerja sama dengan syarat mutlak tidak melukai atau mengorbankan Seraphina":
            $ victoria_alliance = True
            $ ser_aff += 1
            $ ser_trust += 1
            call inspect_clue("seal_diagram")
            $ unlock_achievement("ach_victoria", "Aliansi Rahasia")
            mc "Aku akan bekerja sama denganmu, Victoria, tetapi dengan satu syarat mutlak: kita harus menyelamatkan Seraphina juga. Aku tidak akan membiarkanmu menghancurkannya demi memuaskan ambisi penelitianmu."
            "Victoria menatapku dengan sedikit binar kekaguman di balik sorot matanya yang analitis."
            show victoria surprised with dissolve
            vic "Rupanya sang pewaris Rosewood telah mencuri hatimu hanya dalam waktu empat malam saja, ya?"
            show victoria smile with dissolve
            vic "Tenang saja, Guest. Aku seorang ilmuwan, bukan pembantai. Jika kita bisa membebaskan Seraphina dari kutukan ini tanpa merusak jiwanya, itu adalah keberhasilan mutlak dari misiku."
            vic "Kita sepakat. Keselamatan Seraphina dimasukkan ke dalam parameter keberhasilan rencana kita."

        "Menolak campur tangan Victoria dan memilih mencari jalan sendiri untuk menghadapi Seraphina":
            $ ser_trust += 1
            mc "Aku menghargai informasimu, Victoria. Namun aku lebih memilih untuk menghadapi Seraphina secara langsung daripada merencanakan konspirasi di belakang punggungnya."
            vic "Keras kepala dan terlalu idealis. Sikap seperti itu sering kali menjadi batu nisan tercepat bagi para tamu yang pernah menginap di rumah ini."
            vic "Namun jika kau bersikeras... jangan katakan aku tidak pernah memperingatkanmu ketika lonceng malam ketujuh berdentang di langit malam."

    "Pintu ganda perpustakaan perlahan berderit terbuka di ujung aula."
    "Suara langkah kaki halus dan anggun terdengar mendekat di atas karpet tebal."

    "Evelyn Hart melangkah masuk ke dalam lingkaran cahaya lentera dengan membawa nampan perak berisi teko porselen dan dua cangkir teh kamomil panas yang mengepulkan asap wangi."
    "Wajahnya setenang dan sedingin patung marmer katedral, tidak menunjukkan emosi atau keterkejutan sedikit pun saat melihat kami berdua."

    show victoria serious at sprite_left with dissolve
    show evelyn serious at sprite_right with dissolve

    eve "Permisi, Nona Victoria, Tuan Guest. Saya membawakan teh kamomil hangat untuk menemani pembacaan Anda selarut ini."

    vic "Kau selalu datang di saat yang paling tepat, Evelyn. Ketepatan waktu yang sungguh mengagumkan bagi seseorang yang telah mengabdi selama lebih dari satu abad."

    show evelyn neutral at sprite_right with dissolve
    "Mata amber Evelyn melirik sekilas ke arah diagram perkamen di atas meja, lalu kembali menatap Victoria tanpa berkedip."
    show evelyn serious at sprite_right with dissolve

    eve "Tugas seorang pelayan setia adalah memastikan kenyamanan tamu, Nona Victoria. Bahkan ketika tamu tersebut... terlalu asyik mengaduk-aduk abu masa lalu yang seharusnya dibiarkan dingin dan tenang."
    eve "Nona Seraphina menitipkan pesan agar Tuan Guest tidak terlalu lelah malam ini. Besok malam, Nona Seraphina berkenan mengundang Tuan ke ruang duduk pribadinya di sayap utara."

    mc "Ruang duduk pribadi Nona Seraphina?"

    eve "Benar, Tuan. Suatu kehormatan besar yang belum pernah diberikan kepada tamu mana pun dalam sepuluh tahun terakhir."
    eve "Saya sarankan Anda mempersiapkan hati dan pikiran Anda dengan baik sebelum melangkah ke sana besok malam."

    "Evelyn meletakkan nampan teh di sudut meja baca, membungkuk hormat dengan sempurna, lalu melangkah keluar dari perpustakaan dengan keanggunan yang sunyi bagai hantu."

    hide victoria with dissolve
    hide evelyn with dissolve

    scene bg_guest_bed_pov
    with fade

    "Aku kembali ke dalam kamar tamuku di lantai dua dan merebahkan diri di atas ranjang berkanopi yang empuk."
    "Di bawah selimut beludru marun yang hangat, aku menatap langit-langit kamar dalam temaram bara api perapian."
    "Malam keempat di Rose Manor berakhir dengan persekutuan rahasia yang terjalin di balik bayang-bayang buku tua berdebu."
    "Di balik sakuku, salinan diagram segel ketujuh tersimpan rapat berdampingan dengan kelopak mawar hitam Lilith."

    "Besok malam adalah malam kelima."
    "Malam di mana Seraphina Rosewood akan membuka pintu ruang pribadinya... dan barangkali, membuka rahasia terdalam dari hatinya sendiri yang terluka."

    jump day_5

