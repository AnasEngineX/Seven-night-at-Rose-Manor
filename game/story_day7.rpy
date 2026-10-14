## story_day7.rpy
## Siang Hari 7: Ketenangan Terakhir Sebelum Badai Penentuan (The Final Calm)
## Naskah interaktif sastra gothic romance dan misteri mendalam

label day_7:
    scene black
    with fade

    "Fajar hari ketujuh merekah dalam keheningan yang luar biasa mutlak dan menakutkan."
    "Badai salju ganas yang melolong sepanjang malam mendadak lenyap tanpa bekas saat matahari terbit di balik ufuk timur."
    "Tidak ada suara desau angin, tidak ada derit cabang-cabang pohon willow tua, tidak ada suara kepakan sayap burung gagak di pekarangan."
    "Bahkan waktu itu sendiri seolah-olah membeku di atas menara-menara batu Rose Manor, menahan napasnya menyambut datangnya malam penentuan takdir."
    "Cahaya matahari pagi menyinari lembah Ashwood dengan warna perak keemasan yang dingin dan pucat, menyinari butiran-butiran es di kaca jendela laksana debu permata yang tak bernyawa."

    "Di dalam kamar tamu di lantai dua, aku berdiri menatap bayangan diriku sendiri di cermin oval berbingkai perak pudar."
    "Enam hari penuh misteri, bahaya, dan intrik telah berlalu sejak pertama kali aku menjejakkan kaki melewati gerbang besi mawar berduri."
    "Aku bukan lagi pengelana asing yang bingung, ragu-ragu, dan ketakutan oleh bayang-bayang mansion ini."
    "Hari ini, aku berdiri tegak dengan tekad membaja dan keyakinan mutlak untuk mematahkan lingkaran kutukan berdarah yang telah menelan korban jiwa dan ingatan selama lebih dari satu abad."

    "Di atas meja kayu jati di samping tempat tidurku, seluruh kepingan teka-teki telah tersusun dengan rapi dan sempurna di depan mataku:"
    "Setangkai mawar hitam abadi dari nisan Lilith Vane di taman labirin—penawar ilusi darah mawar;"
    "Liontin perak murni berukir mawar peninggalan Lady Eleanor pemberian Seraphina—pelindung jiwa dari kegelapan;"
    "Salinan diagram okultisme {i}'Sigillum Septem Foliorum'{/i} yang telah dibedah oleh Victoria Ashbourne—panduan pembalik polaritas segel;"
    "Dan Kunci Perak kuno bersumpah darah dari leher Evelyn Hart—pembuka gerbang kapel inti bawah tanah."

    scene bg_manor_hall
    with fade

    "Ketika aku melangkah menuruni tangga aula utama, ruangan luas itu bermandikan cahaya matahari siang yang dingin."
    "Di dekat perapian marmer putih, Seraphina Rosewood berdiri seorang diri, menatap lurus ke arah deretan potret para leluhurnya yang terpajang di dinding tinggi."
    "Malam ini akan menjadi malam penentuan hidupnya, namun hari ini ia tidak mengenakan gaun megah atau perhiasan bangsawan."
    "Ia mengenakan gaun hitam panjang sederhana berbahan beludru lembut tanpa renda atau korset yang kaku."
    "Wajahnya tampak begitu tenang, bersih, dan anggun, namun sepasang matanya yang merah anggur memancarkan kepasrahan yang mendalam bercampur kerinduan yang menyayat kalbu."

    show seraphina neutral with dissolve

    ser "Hari ketujuh akhirnya tiba, Guest."

    mc "Benar, Seraphina. Hari terakhir dari masa tinggal tujuh malam ini."

    "Seraphina melangkah perlahan mendekatiku. Langkah kakinya yang sunyi tidak menimbulkan suara di atas karpet marun."
    "Jemari tangannya yang halus tanpa sarung tangan menyentuh kerah mantelku dengan kelembutan yang membuat dadaku bergetar hangat."

    ser "Tahukah kau apa yang kupikirkan sepanjang malam tadi saat aku terjaga di kamarku?"

    show seraphina sad with dissolve

    ser "Aku memikirkan betapa beruntungnya aku... bahwa di antara sekian banyak orang di dunia luar yang menerima surat undangan terkutuk ini... kaulah yang melangkah melewati gerbang pekaranganku."
    ser "Setiap tamu sebelummu datang membawa keserakahan, rasa takut, atau kecurigaan."
    ser "Tetapi kau... kau datang membawa pengertian, kehangatan, dan keberanian yang tulus."
    ser "Bahkan jika malam ini adalah malam terakhir bagiku... jika takdir menuntut darahku untuk mengakhiri kutukan ini... aku tidak lagi merasa takut atau kesepian."
    ser "Untuk pertama kalinya dalam hidupku, aku merasa bahwa aku benar-benar dicintai dan dipahami sebagai Seraphina... bukan sekadar boneka pelindung Rose Manor."

    menu:
        "Merengkuh tubuhnya ke dalam pelukan erat dan berjanji bahwa malam ini adalah awal dari fajar baru":
            $ ser_aff += 3
            $ ser_trust += 2
            "Aku tidak membiarkan nada kepasrahannya menggantung di udara."
            "Aku melangkah maju, melingkarkan kedua tanganku di pinggangnya, dan menarik tubuhnya yang ramping ke dalam pelukan erat di dadaku."
            "Aku mendekapnya begitu dekat hingga ia bisa merasakan detak jantungku yang mantap, hangat, dan tak tergoyahkan."
            mc "Ini bukan akhir dari kisahmu, Seraphina. Jangan pernah mengucapkan kata-kata perpisahan."
            mc "Kita telah mengumpulkan seluruh kebenaran yang sengaja disembunyikan oleh para leluhurmu. Lilith, Evelyn, dan Victoria... semuanya berdiri di belakang kita."
            mc "Malam ini kita akan menembus kegelapan kapel bawah tanah bersama-sama, dan besok pagi... kita akan menyambut fajar pertama di taman mawar tanpa rasa takut."
            "Tubuh Seraphina bergetar pelan di dalam pelukanku, lalu kedua tangannya melingkari leherku, membalas pelukanku dengan segenap kekuatan dan cintanya."

            show seraphina smile with dissolve

            ser "Aku percaya padamu, Guest... Aku mempertaruhkan seluruh jiwa dan napasku pada janjimu."
            ser "Pimpinlah aku keluar dari kegelapan ini."

        "Memperlihatkan kunci perak kapel pemberian Evelyn untuk memberinya bukti harapan nyata":
            $ evidence += 1
            $ ser_trust += 2
            "Aku merogoh saku mantelku dan mengeluarkan kunci perak kuno berukir mawar dan pedang ksatria, lalu meletakkannya di atas telapak tangannya yang halus."
            mc "Lihatlah ini, Seraphina. Evelyn sendiri yang mempercayakan kunci kapel ini kepadaku di ruang bawah tanah semalam."
            mc "Bahkan pelayan setiamu, penjaga sumpah darah Rosewood selama seratus empat puluh tahun, percaya bahwa kita mampu menghentikan ritual ini tanpa menumpahkan darahmu!"
            "Mata Seraphina membelalak lebar dalam keterkejutan yang luar biasa."

            show seraphina surprised with dissolve

            "Jemarinya gemetar saat ia memegang logam perak dingin yang selama seabad selalu tergantung di leher Evelyn."
            ser "Kunci sumpah Evelyn... Bagaimana mungkin..."
            ser "Wanita yang paling mematuhi tradisi darah leluhur... telah melepaskan kuncinya untukmu..."
            ser "Jadi... bahkan para leluhur di alam baka telah merestui pembebasan rumah ini..."

            show seraphina smile with dissolve

            ser "Harapan ini... terasa begitu nyata dan hangat hingga membuat air mataku menetes."

        "Menegaskan kesiapan taktis dan keunggulan sains okultisme bersama Victoria":
            $ ser_trust += 2
            $ victoria_alliance = True
            mc "Seluruh persiapan telah matang sempurna, Seraphina. Victoria telah memetakan urutan pembalik polaritas segel, dan aku memegang mawar hitam makam Lilith."
            mc "Kita memiliki sains, bukti sejarah, dan kekuatan cinta yang murni. Kita tidak akan kalah dari ketakutan masa lalu."
            "Victoria melangkah keluar dari ruang perpustakaan, mengangguk mantap ke arah kami berdua dengan buku catatannya di tangan."

            show seraphina smile at sprite_mid_left with dissolve
            show victoria smile at sprite_mid_right with dissolve

            vic "Segala anomali metafisika memiliki formula penetralisirnya, Seraphina. Logika dan tekad manusia akan selalu menang melawan kutukan."
            ser "Kalian berdua luar biasa... Keberanian kalian memberi kekuatan bagi jiwaku untuk berdiri tegak di hadapan altar malam ini."
            hide victoria with dissolve

    "Evelyn melangkah masuk dari ruang makan, membawa nampan perak berisi teko teh kamomil hangat."
    "Wajahnya yang tenang memancarkan restu bisu yang khidmat bagi kami bertiga."

    show seraphina smile at sprite_mid_left with dissolve
    show evelyn smile at sprite_right with dissolve

    eve "Waktu terus bergulir, Tuan dan Nona. Senja telah mulai menyapa langit bukit Ashwood."
    eve "Matahari akan segera tenggelam di balik punggung gunung granit."

    "Cahaya keemasan di luar jendela perlahan meredup menjadi warna ungu kelabu tua yang pekat."
    "Lonceng jam besar menara Rose Manor berdentang lambat sebanyak enam kali, memecah kesunyian lembah dengan gema yang mengguncang hati."

    show seraphina smile at sprite_mid_left with dissolve

    ser "Waktunya telah tiba untuk mempersiapkan upacara terakhir di ruang bawah tanah, Guest."
    ser "Aku harus pergi ke ruang ganti untuk mengenakan gaun upacara keluarga Rosewood."
    ser "Aku akan menunggumu di depan altar kapel saat lonceng tengah malam berdentang pertama kali."
    ser "Jadilah fajar bagi kegelapanku, cintaku."

    hide seraphina with dissolve
    hide evelyn with dissolve
    hide victoria with dissolve

    "Seraphina melangkah anggun menuruni tangga menuju ruang persiapan bawah tanah, meninggalkan semerbak aroma mawar merah yang harum di udara."

    "Di luar jendela, matahari sore tenggelam seutuhnya di balik bukit Ashwood, menyisakan langit hitam pekat tanpa setitik pun bintang."
    "Malam ketujuh: Malam Mawar Terakhir telah resmi tiba di Rose Manor."
    "Saatnya melangkah ke dalam kapel bawah tanah dan memutuskan akhir dari takdir ini untuk selama-lamanya."

    jump night_7

