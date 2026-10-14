## story_day3.rpy
## Siang Hari 3: Rumah Kaca Mawar dan Sisi Lembut Seraphina (The Glass Greenhouse)
## Naskah interaktif sastra gothic romance dan misteri mendalam

label day_3:
    scene black
    with fade

    "Siang hari ketiga menyapa Rose Manor dengan langit kelabu yang sedikit lebih tenang."
    "Rintik hujan es yang mengguyur pekarangan sejak subuh perlahan reda, menyisakan tetesan-tetesan air jernih berkilau yang bergelantungan di dahan-dahan pohon willow yang membungkuk murung."
    "Setelah menghabiskan sarapan pagi di ruang makan yang sunyi ditemani desah langkah Evelyn, rasa penat di dalam dinding-dinding batu mansion mendorongku untuk mencari udara segar di luar ruangan."
    "Aku melangkah melewati pintu teras sayap selatan, menapaki jalan setapak berbatu marmer putih yang membelah semak-semak pekarangan belakang yang tertidur pulas."

    scene bg_conservatory
    with fade

    "Di sudut pekarangan selatan yang terlindung dari hembusan angin ngarai, sebuah rumah kaca raksasa bergaya Victorian menjulang megah di antara rerimbunan semak belukar."
    "Kerangka besi tempa berwarna hijau tua yang dipahat membentuk sulur tanaman menopang ratusan panel kaca lengkung berkubah tinggi yang diselimuti lapisan embun tipis."
    "Ketika aku mendorong pintu kaca berbingkai perunggu yang berderit halus, udara hangat dan lembap seketika menyergap wajahku—begitu kontras dengan hawa dingin menggigit di luar sana."
    "Aroma nektar mawar yang manis dan memabukkan berpadu dengan keharuman tanah gambut subur dan uap air hangat."
    "Di sepanjang lantai batu bata merah yang tertata melingkar, pipa-pipa uap kuningan kuno berdengung lembut mengalirkan panas dari ruang ketel bawah tanah, menjaga iklim tropis buatan di tengah kepungan musim dingin bukit Ashwood."

    "Di sekeliling ruangan, ribuan kuntum mawar dari puluhan varietas mekar dengan kelebatan yang luar biasa menakjubkan:"
    "Mawar merah marun sepekat darah, mawar putih gading beraroma vanila, mawar persik keemasan, dan mawar merah muda lembut yang merambat liar di tiang-tiang lengkung kubah kaca."

    "Di dekat meja pot marmer putih di tengah rumah kaca, sesosok wanita ramping sedang berdiri membelakangiku."
    "Hari ini, ia tidak mengenakan gaun upacara bangsawan dengan korset kaku yang membuatnya tampak dingin dan tak terjangkau."
    "Seraphina mengenakan gaun wol lembut berwarna hijau zamrud sederhana dengan celemek linen putih kecil terikat di pinggangnya yang ramping."
    "Rambut peraknya yang indah diikat longgar dengan pita beludru hitam, jatuh bergelombang di atas punggungnya yang anggun."
    "Di tangannya, sebuah gunting pemangkas kecil berbahan perak memotong daun-daun kering dari sekuntum mawar merah tua dengan ketelatenan dan kelembutan seorang ibu yang merawat bayinya."

    show seraphina neutral with dissolve

    ser "Bunga mawar adalah makhluk hidup yang paling jujur di dunia ini, bukan begitu?"
    ser "Mereka tidak pernah berpura-pura menyukaimu demi status atau kekayaan. Mereka hanya menuntut sedikit air yang jernih, tanah yang subur, dan ketenangan dari hiruk-pikuk dunia luar."

    "Seraphina berbicara pelan tanpa membalikkan badannya, seolah ia telah mengetahui derit langkah kakiku di atas lantai bata sejak detik pertama aku melangkah masuk."

    mc "Nona Seraphina. Saya tidak bermaksud mengganggu ketenangan Anda di tempat yang indah ini."

    "Seraphina berbalik perlahan, meletakkan gunting pangkas peraknya di atas meja pot marmer."
    "Sebuah senyuman tipis—begitu lembut, hangat, dan mempesona, jauh dari kesan angkuh yang ia tunjukkan di hadapan lukisan leluhurnya—terbit di sudut bibirnya."

    show seraphina smile with dissolve

    ser "Kau tidak mengganggu sama sekali, Guest. Justru... kedatanganmu adalah jeda yang menyenangkan."
    ser "Rumah kaca ini adalah satu-satunya sudut di Rose Manor di mana aku merasa benar-benar bisa bernapas bebas tanpa merasa dihakimi oleh mata-mata dingin para leluhur di dinding aula."
    ser "Di sini, tidak ada ritual kuno, tidak ada aturan-aturan bangsawan yang menyesakkan dada... hanya ada kehidupan hijau yang bertumbuh dengan caranya sendiri."
    ser "Dahulu, mendiang ibuku, Lady Eleanor, menghabiskan seluruh siangnya di ruangan ini. Ia mengajariku bahwa bunga mawar dapat mendengar isi hati mereka yang merasa kesepian."

    mc "Ibumu pasti seorang wanita yang sangat lembut dan penyayang."

    show seraphina sad with dissolve

    ser "Ya... terlalu lembut untuk sangkar batu yang kejam ini."

    menu:
        "Menawarkan bantuan untuk memegang keranjang pangkas dan merapikan semak mawar bersama":
            $ ser_aff += 1
            $ ser_trust += 1
            mc "Jika Anda tidak keberatan, izinkan saya membantu memegangkan keranjang potongannya, Nona Seraphina. Dua pasang tangan akan menyelesaikan pekerjaan ini lebih cepat."
            "Seraphina menatapku dengan binar geli bercampur takjub di matanya yang merah anggur."

            show seraphina smile with dissolve

            ser "Kau bangsawan yang sangat tidak lazim, Guest. Tamu-tamu lain yang pernah datang ke sini biasanya menuntut untuk dilayani oleh puluhan pelayan bertangan halus, bukan menawarkan diri memegang keranjang sampah dedaunan."
            "Ia menyerahkan sebuah keranjang anyaman rotan kecil kepadaku dengan tawa kecil yang merdu di tenggorokannya."
            ser "Peganglah di sebelah sini. Hati-hati dengan durinya; mawar jenis Crimson Rosewood ini memiliki duri melengkung yang sangat tajam dan bisa menusuk hingga ke tulang jika tidak waspada."
            "Kami menghabiskan setengah jam berikutnya memangkas ranting-ranting kering dan menyiram pot-pot mawar bersama."
            "Gerakannya begitu luwes dan tenang, sementara percakapan ringan kami tentang musim, buku-buku lama, dan kota asal kami mengalir alami tanpa kepalsuan."
            "Untuk sesaat, segala kegelapan, kutukan, dan teror Rose Manor seolah sirna tanpa bekas dari benak kami berdua."

        "Memperhatikan luka goresan duri di jemarinya, meraih tangannya, dan membalut lukanya dengan saputangan sutra":
            $ ser_aff += 2
            $ ser_trust += 1
            "Ketika Seraphina sedang memotong tangkai mawar merah marun, tangannya sedikit tersentak."
            "Setitik duri tajam menggores ujung jari telunjuknya, memunculkan butiran darah merah segar yang kontras dengan kulit tangannya yang seputih salju."
            mc "Tangan Anda terluka, Seraphina."
            "Sebelum ia sempat menyembunyikan jemarinya di balik celemeknya, aku melangkah maju mendekatinya."
            "Aku mengeluarkan saputangan sutra bersih dari saku mantelku, lalu dengan hati-hati meraih telapak tangannya yang halus dan membalut luka di jemarinya dengan lembut."
            "Kulit jemari Seraphina terasa begitu hangat, lembut, dan sedikit gemetar di dalam genggaman tanganku."
            "Napas Seraphina tercekat sesaat. Rona merah muda merebak di kedua pipinya yang putih porselen, sementara matanya membelalak menatap wajahku dari jarak yang begitu dekat."

            show seraphina surprised with dissolve

            ser "Kau... tidak perlu bersikap selembut ini kepadaku, Guest..."
            ser "Sepanjang hidupku, orang-orang di rumah ini selalu menuntutku untuk menjadi sosok pelindung yang dingin, sempurna, dan tanpa cacat kelemahan."
            mc "Bahkan seorang pemilik mansion megah sekalipun berhak untuk dirawat ketika terluka, Seraphina. Menjadi manusia berarti memiliki kerapuhan."
            "Seraphina memalingkan pandangannya sejenak ke arah semak mawar dengan senyuman yang teramat manis dan malu-malu, namun jemarinya tidak ditarik dari genggamanku."

            show seraphina smile with dissolve

            ser "Terima kasih, Guest... Saputanganmu sangat wangi dan nyaman."

        "Menanyakan misteri mengapa ribuan mawar di rumah kaca ini tetap bermekaran lebat di tengah musim dingin yang membeku":
            $ evidence += 1
            $ ser_trust += 1
            mc "Bagaimana mungkin mawar-mawar ini mampu bermekaran begitu lebat, segar, dan semerbak di tengah musim dingin beku yang membunuh semua tanaman di bukit Ashwood, Seraphina?"
            "Sorot mata Seraphina perlahan berubah menjadi lebih serius, dibayangi oleh misteri kuno yang melingkupi tanah leluhurnya."

            show seraphina serious with dissolve

            ser "Tanah di mana Rose Manor didirikan bukanlah tanah biasa, Guest. Mansion ini berdiri tepat di atas titik pertemuan urat bumi gaib yang menampung energi spiritual kuno."
            ser "Mawar-mawar Crimson Rosewood ini adalah manifestasi biologis dari resonansi energi tersebut."
            ser "Mereka hidup bukan hanya dari nutrisi tanah dan kehangatan pipa uap, melainkan dari sisa-sisa emosi, ingatan, dan kerinduan manusia yang terkubur selama berabad-abad di bawah fondasi batu rumah ini."
            ser "Semakin kuat gejolak batin dan rahasia yang terkurung di dalam dinding mansion ini... semakin merah darah kelopak mawar yang bermekaran di cabang-cabangnya."
            mc "Jadi... mawar-mawar ini memakan memori manusia?"
            ser "Alam memiliki bahasanya sendiri untuk mencatat apa yang berusaha dihapus oleh manusia dari ingatan mereka, Guest."

    "Seraphina menuangkan dua cangkir teh mawar hangat dari teko porselen kecil di atas meja pot marmer."
    "Kami duduk berdampingan di atas sebuah bangku besi tempa putih di bawah naungan pohon jeruk mini yang rindang."

    show seraphina sad with dissolve

    ser "Tahukah kau, Guest? Jauh sebelum ayahku jatuh sakit dan mewariskan tanggung jawab kutukan ini kepadaku... aku memiliki impian masa kecil yang sederhana."
    ser "Aku bermimpi ingin menjadi seorang pianis konser di gedung opera ibu kota."
    ser "Aku membayangkan diriku memainkan simfoni di bawah kilau lampu kristal megah, menyaksikan senyuman bahagia di wajah orang-orang biasa yang menikmati musikku."
    ser "Namun kematian orang tuaku dan beban nama Rosewood memaksaku mengubur impian itu di balik pintu-pintu berdebu."

    mc "Impian itu belum mati, Seraphina. Musik di dalam jiwamu masih hidup. Ketika kutukan ini berhasil kita pecahkan, kau akan melangkah keluar dari lembah ini dan memainkan melodi terindah bagi dunia luar."

    "Seraphina menatapku dalam-dalam, binar harapan dan keharuan berkilau di matanya yang merah anggur laksana embun pagi."

    show seraphina smile with dissolve

    "Tepat pada saat itu, lonceng jam menara di kejauhan berdentang tiga kali, memecah ketenangan sore yang damai."
    "Seraphina meletakkan cangkir tehnya perlahan, dan kehangatan di wajahnya mendadak berganti menjadi kehati-hatian yang dingin."

    show seraphina serious with dissolve

    ser "Matahari petang mulai terbenam di balik bukit, Guest. Malam ketiga akan segera menyelimuti pekarangan."
    ser "Dengarkan baik-baik peringatan keduaku:"
    ser "Nanti malam, jangan pernah melangkah ke dalam Taman Labirin Mawar di sayap timur setelah tengah malam berdentang."
    ser "Dan jika kau mendengar suara wanita yang memanggil namamu dari dalam kabut pekarangan... jangan pernah menjawab panggilan itu."
    ser "Aku tidak ingin melihatmu menjadi korban berikutnya dari bayang-bayang masa lalu rumah ini."

    hide seraphina with dissolve

    "Seraphina bangkit berdiri, merapikan celemeknya, dan melangkah keluar dari rumah kaca dengan langkah tergesa."
    "Aroma wangi mawar merah yang tertinggal di udara berpadu dengan hawa dingin petang yang mulai merayapi kaca-kaca jendela."

    "Malam ketiga telah tiba."
    "Malam di mana bisikan dari makam rahasia Lilith Vane menanti di tengah labirin mawar."

    jump night_3

