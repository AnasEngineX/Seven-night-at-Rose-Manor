## story_night5.rpy
## Malam 5: A Fragile Promise (Ruang Duduk Pribadi dan Janji Rapuh Seraphina)
## Naskah interaktif sastra gothic mystery dan romance mendalam

label night_5:
    $ night = 5

    scene black
    with fade

    "Malam kelima tiba membawa keheningan yang memesona sekaligus menghanyutkan jiwa."
    "Badai angin dan salju yang telah menderu selama beberapa hari terakhir mendadak reda seutuhnya, seolah langit sendiri tunduk pada ketetapan gaib yang menguasai Rose Manor."
    "Di luar jendela kaca bertingkat, lapisan embun beku kristal berkilauan seperti debu berlian di atas dahan-dahan pohon willow yang membungkuk murung."
    "Bulan purnama menggantung bulat sempurna di langit malam yang bersih tanpa awan, memancarkan cahaya perak pucat yang membanjiri lorong-lorong sepi lantai dua mansion."

    "Langkah kakiku membawaku melintasi sayap utara mansion—bagian paling terisolasi dan paling mewah dari Rose Manor."
    "Di ujung koridor berkarpet merah marun yang tebal, berdiri sebuah pintu ganda dari kayu mahoni gelap berukir relief kuntum mawar mekar yang rumit."
    "Di atas meja konsol marmer putih di samping pintu, sebuah vas kristal berisi setangkai mawar merah segar yang masih berembun menebarkan aroma wangi manis yang memabukkan ke seluruh penjuru lorong."

    "Tepat ketika aku mengangkat tanganku untuk mengetuk daun pintu kayu tersebut, suara kait logam berbunyi pelan, dan pintu itu berayun terbuka dengan sendirinya ke arah dalam."

    scene bg_seraphina_room
    with fade

    "Ruang duduk pribadi Seraphina Rosewood memancarkan kehangatan dan keintiman yang jauh berbeda dari ruangan-ruangan dingin lainnya di mansion ini."
    play sound sfx_fire
    "Sebuah perapian marmer putih berukir malaikat kecil menyala dengan kobaran api kayu cendana yang harum, meliuk-liuk menari dalam nada gemeretak yang menenangkan hati."
    "Dinding-dinding ruangan dilapisi wallpaper sutra berwarna merah anggur tua dengan motif sulur mawar emas yang timbul bila disentuh jemari."
    "Sofa beludru tebal berwarna merah marun tertata anggun di dekat perapian, dikelilingi oleh rak-rak buku kecil berisi puisi-puisi romantis Prancis dan Inggris abad ke-18."
    "Di atas meja rias berbingkai cermin perak murni, sebuah kotak musik kuno berputar lambat tanpa disentuh, mengalunkan melodi balada melankolis yang menyentuh sudut terdalam sanubari."

    "Di dekat jendela berkaca lengkung yang menghadap ke arah lembah mawar, Seraphina berdiri membelakangiku."
    "Cahaya bulan perak menyelimuti siluet tubuhnya dari luar, sementara cahaya jingga perapian membelai rambutnya dari dalam ruangan."

    "Malam ini, ia tidak mengenakan gaun bangsawan resminya yang kaku dan berlapis korset besi."
    "Sebagai gantinya, ia mengenakan gaun malam sutra hitam panjang dengan renda lembut di bagian pundak dan dadanya."
    "Pundaknya yang putih mulus terekspos lembut di bawah kerah gaun yang terbuka anggun, sementara rambut peraknya yang panjang terurai bebas melewati pinggangnya tanpa sanggul atau jepit mutiara."
    "Sosoknya malam ini tampak begitu rapuh, begitu lembut, dan begitu manusiawi—seorang gadis muda yang terlepas dari segala kepalsuan status bangsawan dan bayang-bayang kutukan keluarganya."

    show seraphina night with dissolve

    "Mendengar derit halus langkah kakiku di atas karpet wol tebal, Seraphina menoleh perlahan."
    "Sepasang matanya yang merah anggur memancarkan kehangatan yang belum pernah kulihat sebelumnya—bercampur dengan keraguan, rasa malu, dan kepedihan yang teramat dalam."

    ser "Kau menepati undanganmu, Guest."
    ser "Sejujurnya... setelah semua percakapan rahasiamu dengan Lilith di taman dan Victoria di perpustakaan... aku setengah menduga kau akan membenciku dan menolak melihat wajahku lagi."

    mc "Aku telah berjanji padamu di rumah kaca semalam, Seraphina. Aku tidak akan menghakimimu berdasarkan perkataan orang lain."
    mc "Aku datang ke sini untuk mendengarkan kebenaran langsung dari bibirmu sendiri."

    "Sebuah helaan napas lega meluncur pelan dari bibir Seraphina."
    "Ia melangkah mendekat ke arah sofa perapian dengan keanggunan yang sunyi, lalu mengulurkan tangannya yang halus, memberi isyarat agar aku duduk di sampingnya."
    "Di atas meja kayu jati kecil di antara kami, sebuah botol kaca antik berisi anggur merah Rosewood telah terbuka, memancarkan aroma manis buah ceri hitam matang dan kelopak mawar."
    "Dua gelas kristal berkaki ramping telah terisi separuhnya oleh anggur berwarna merah delima pekat."

    ser "Duduklah bersamaku di dekat perapian ini, Guest."
    ser "Malam ini... untuk beberapa jam saja sebelum fajar menyingsing... aku tidak ingin menjadi Nona Rosewood sang tuan tanah terkutuk."
    ser "Aku hanya ingin menjadi Seraphina... seorang gadis kesepian yang rindu mendengar suara manusia yang tulus di dalam rumah sunyi ini."

    "Aku duduk di sampingnya di atas sofa beludru merah marun."
    "Jarak di antara kami begitu dekat hingga kehangatan tubuhnya dan aroma wangi mawar alami dari rambutnya merayapi seluruh inderaku."

    if ser_aff >= 2 and ser_trust >= 2:
        ser "Ruangan ini adalah satu-satunya tempat di mana aku merasa benar-benar bisa bernapas, Guest."
        ser "Sepuluh tahun yang lalu, di ruangan ini... ibuku, Lady Eleanor, memelukku untuk terakhir kalinya sebelum ia dibawa oleh ayahku ke dalam kapel bawah tanah."
        ser "Kala itu usiaku baru lima belas tahun. Ayahku selalu menanamkan ke dalam kepalaku bahwa keluarga Rosewood adalah penjaga gerbang suci."
        ser "Bahwa keabadian dan kemewahan yang kami nikmati adalah berkah yang harus dibayar dengan kepatuhan mutlak pada ritual tujuh malam."

        "Seraphina mengangkat gelas kristalnya, menyesap sedikit anggur merah tua itu."
        "Bibirnya yang basah merona merah segar di bawah temaram cahaya kobaran api cendana."

        ser "Namun seiring bertambahnya usiaku, aku menyadari bahwa semua perkataan ayahku adalah kebohongan yang dirancang untuk menjustifikasi keputusasaan."
        ser "Keabadian ini bukanlah berkah... melainkan sangkar besi berkarat di mana waktu berhenti berputar."
        ser "Setiap tamu yang tiba di gerbang kami dengan harapan dan impian mereka sendiri... satu per satu harus kulihat kehilangan cahaya di mata mereka ketika lonceng malam ketujuh berdentang."
        ser "Sebagian menjerit histeris memohon ampun, sebagian melarikan diri ke dalam badai hingga tubuh mereka ditemukan membeku di jurang, dan sebagian lainnya keluar dari mansion ini laksana boneka tanpa jiwa yang melupakan keluarga dan jati diri mereka."

        "Air mata bening menggenang di pelupuk matanya yang merah anggur, memantulkan nyala api perapian laksana permata delima yang basah."
        show seraphina sad with dissolve

        ser "Aku membenci ritual itu, Guest. Aku membenci diriku sendiri setiap kali harus mengenakan gaun upacara dan berdiri di depan altar berdarah itu."
        ser "Tetapi kau... sejak malam pertama kau melangkah masuk ke aula besar, caramu menatapku begitu berbeda."
        ser "Kau tidak memandangku dengan ketakutan, dan kau tidak memandangku dengan keserakahan atas kekayaan Rosewood."
        ser "Kau melihatku sebagai manusia yang terluka... bukan monster penjaga kutukan."

        menu:
            "Melangkah mendekat, merengkuh tubuhnya ke dalam pelukan hangat di depan perapian, dan menyeka air matanya":
                $ ser_aff += 3
                $ ser_trust += 2
                "Melihat pundaknya yang sedikit gemetar menahan tangis yang telah ia simpan selama bertahun-tahun, aku tidak dapat lagi menahan dorongan di dalam dadaku."
                "Aku menggeser dudukku mendekat, mengulurkan kedua tanganku, dan menarik tubuhnya yang rapuh ke dalam dekapan hangat dadaku."
                "Seraphina sempat tersentak kaku sesaat karena terkejut oleh sentuhanku yang tiba-tiba, namun hanya beberapa detik kemudian, seluruh dinding pertahanannya runtuh seutuhnya."
                "Kedua tangannya yang ramping melingkari leher dan punggungku, mencengkeram kain mantelku begitu erat seolah aku adalah satu-satunya jangkar keselamatannya di tengah amukan samudra badai."
                "Wajahnya terbenam di lekuk leherku, hembusan napasnya yang hangat dan wangi menerpa kulitku, bercampur dengan tetesan air mata hangat yang merembes ke kemejaku."

                ser "Guest... aku sangat takut..."
                ser "Aku takut kehilangan akal sehatku di dalam kegelapan rumah ini... dan aku takut kehilangan dirimu ketika malam ketujuh tiba besok lusa...!"

                mc "Kau tidak akan kehilangan akal sehatmu, Seraphina. Dan kau tidak akan kehilanganku. Aku bersumpah demi hidupku sendiri, aku tidak akan membiarkan ritual itu menelanmu atau menelan kita berdua."
                mc "Kita akan mencari jalan keluar dari sangkar ini bersama-sama. Kau pantas mendapatkan kebebasan, kau pantas melihat fajar di dunia luar tanpa rasa takut."

                "Seraphina mendongakkan kepalanya perlahan dari dadaku."
                "Wajah kami begitu dekat hingga aku bisa merasakan detak jantungnya yang berpacu kencang di balik kain gaun sutranya."
                "Ujung ibu jariku menyeka sisa air mata di pipinya yang halus bagai porselen termahal."
                "Sepasang matanya menatap bibirku sesaat, sebelum kembali menatap lurus ke dalam mataku dengan binar cinta yang membara."

                ser "Janji seorang pria di Rose Manor sering kali terhapus oleh embun pagi... Namun malam ini, untuk pertama kalinya dalam hidupku yang terkutuk ini, aku ingin mempercayai sebuah janji."
                ser "Jika memang ada fajar di luar sana... aku ingin menyambutnya bersamamu, Guest."

            "Menggenggam tangannya erat, mencium punggung tangannya dengan takzim, dan berjanji menjadi pelindungnya":
                $ ser_aff += 2
                $ ser_trust += 2
                if ser_aff >= 3:
                    $ unlock_achievement("ach_affection", "Kuncup Bunga Kasih")
                if ser_trust >= 3:
                    $ unlock_achievement("ach_trust", "Kepercayaan Sang Mawar")
                "Aku meraih kedua tangan Seraphina yang dingin ke dalam genggaman tanganku yang hangat, menautkan jemari kami dengan erat."
                "Perlahan, aku mengangkat tangan kanannya ke dekat bibirku, lalu mendaratkan sebuah kecupan lembut dan lama di atas punggung tangannya yang halus."
                "Seraphina menahan napasnya, rona merah muda merebak di kedua pipinya yang putih pucat laksana bunga mawar yang baru merekah."

                mc "Seraphina, kau telah memikul beban dosa leluhurmu terlalu lama seorang diri di ruangan dingin ini."
                mc "Izinkan aku memikul separuh dari beban itu di pundakku. Kau tidak perlu lagi menghadapi malam-malam berdarah ini sendirian."
                mc "Kita akan menembus ruang bawah tanah itu bersama-sama. Aku akan berdiri di sisimu, bukan sebagai korban, melainkan sebagai pelindungmu."

                "Seraphina tersenyum tipis—sebuah senyuman tulus yang begitu manis dan memukau hingga membuat waktu seolah berhenti berputar di sekitar kami."
                show seraphina smile with dissolve

                ser "Kau berbicara dengan keteguhan hati yang luar biasa, Guest... Keteguhan yang sudah puluhan tahun hilang dari dinding-dinding batu rumah ini."
                ser "Memilikimu di sisiku... membuatku merasa bahwa barangkali kutukan ini bukanlah akhir dari segalanya, melainkan awal dari keberanianku untuk melawan."

            "Menanyakan rahasia bros mawar merah di dadanya dan cara mematikan alirannya":
                $ evidence += 1
                $ ser_trust += 2
                mc "Seraphina, bros mawar merah yang selalu tersemat di dadamu... Victoria menduga bahwa bros itu adalah wadah penyimpan resonansi ingatan para tamu. Ceritakan padaku bagaimana cara kerjanya."
                "Seraphina menyentuh bros kristal merah di dadanya dengan tatapan mata yang dipenuhi kegetiran."

                ser "Victoria sangat cerdas... bahkan terlalu cerdas untuk kebaikannya sendiri."
                ser "Bros ini adalah artefak darah leluhur pertama Rosewood. Setiap kali seorang tamu berinteraksi denganku, ikatan emosional yang terbangun menghasilkan resonansi jiwa yang diserap oleh kristal mawar ini."
                ser "Di malam ketujuh, resonansi itu akan dialirkan ke inti segel di kapel bawah tanah untuk menutup celah dimensi kehampaan."
                ser "Jika bros ini dihancurkan secara paksa tanpa menetralkan segel terlebih dahulu, energi yang terkumpul di dalamnya akan meledak dan memusnahkan seluruh mansion beserta siapa pun yang berada di dalamnya."
                ser "Itulah sebabnya aku tidak pernah bisa begitu saja melarikan diri atau membuang bros ini. Aku terikat padanya sebagaimana ia terikat pada jiwaku."

    else:
        ser "Banyak hal di mansion ini yang berada di luar kuasaku untuk dijelaskan, Guest."
        ser "Satu-satunya hal yang bisa kukatakan adalah: berhati-hatilah dengan setiap langkah yang kau ambil."
        ser "Malam ketujuh akan menuntut kepastian dari kita semua."

        mc "Aku mengerti, Seraphina. Aku akan mempersiapkan diriku menghadapi apa pun yang menanti di depan."

    "Seraphina menarik tangannya perlahan, lalu melepaskan sebuah rantai perak tipis dari balik lehernya."
    "Di ujung rantai itu, sebuah liontin perak kuno berbentuk mawar mekar dengan ukiran daun perak halus berkilau hangat di bawah temaram cahaya api perapian."
    "Ia meletakkan liontin itu ke dalam telapak tanganku, lalu menutup jemariku dengan kedua tangannya."
    call inspect_clue("silver_locket")

    ser "Simpanlah ini baik-baik di sakumu, Guest. Ini adalah liontin peninggalan ibuku, Lady Eleanor."
    ser "Ditempa dari perak murni pegunungan utara dan diberkati dengan doa perlindungan sebelum ibuku melangkah ke kapel bawah tanah."
    ser "Liontin ini memiliki daya tolak gaib terhadap ilusi dan halusinasi darah yang memenuhi ruang bawah tanah."
    ser "Bawalah ini sebagai pelindung pikiranmu... dan sebagai tanda bahwa di mansion yang penuh dengan tipu daya dan kepalsuan ini, rasa terima kasih dan perasaanku kepadamu adalah satu-satunya hal yang murni."

    mc "Aku akan menjaganya dengan segenap jiwaku, Seraphina. Liontin ini tidak akan pernah lepas dari dadaku."

    "Seraphina menatapku dengan tatapan yang begitu hangat dan sarat makna, sebelum bangkit perlahan dari sofa beludru."
    "Lonceng kecil di atas perapian berdentang lembut dua kali, menandakan bahwa tengah malam telah lewat jauh."

    ser "Beristirahatlah malam ini, Guest. Pulihkan tenagamu di kamar tamu."
    ser "Karena besok malam... malam keenam... segel ruang bawah tanah akan mulai terbuka, dan kita harus mempersiapkan diri untuk penentuan takdir kita."

    mc "Selamat malam, Seraphina. Mimpi indah."

    ser "Selamat malam, cintaku... Semoga mimpi kita tidak tertelan oleh bayang-bayang mansion ini."

    scene bg_guest_bed_pov
    with fade

    "Aku kembali ke kamar tamuku dengan membawa liontin perak pemberian Seraphina di genggaman tanganku."
    "Merebahkan tubuhku di atas kasur berkanopi yang hangat, aku mendekap liontin perak berukir mawar itu di dadaku sambil menatap langit-langit kamar dalam temaram api perapian."
    "Logam perak itu tetap terasa hangat di kulitku, memancarkan aura ketenangan yang menepis segala hawa dingin dan ketakutan yang mengintai di balik dinding-dinding kamar."

    "Malam kelima di Rose Manor telah berakhir."
    "Bukan lagi sekadar misteri pembunuhan atau penyelidikan okultisme yang mengikatku pada rumah ini."
    "Kini, sebuah janji hati yang tulus telah terukir di antara aku dan Seraphina Rosewood."

    "Besok adalah hari keenam."
    "Waktu yang tersisa semakin menipis sebelum konfrontasi terakhir di altar kapel bawah tanah dimulai."

    jump day_6

