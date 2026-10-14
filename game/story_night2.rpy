## story_night2.rpy
## Malam 2: The Locked Portrait (Galeri Keluarga dan Rahasia Kanvas Berdarah)
## Naskah interaktif sastra gothic mystery mendalam

label night_2:
    $ night = 2

    scene black
    with fade

    "Matahari sore akhirnya tenggelam seutuhnya di balik punggung bukit granit Ashwood."
    "Langit kelabu yang suram berganti menjadi kegelapan malam kedua yang pekat dan dingin."
    "Di luar jendela kaca berkisi, angin pegunungan bertiup semakin kencang, menggoyangkan pucuk-pucuk pohon pinus purba dengan suara desau panjang laksana bisikan ribuan arwah."
    "Nasihat Victoria Ashbourne di ruang musik siang tadi masih terngiang jelas di kepalaku:"
    "{i}'Perhatikan baik-baik setiap lukisan di Galeri Keluarga sayap timur nanti malam. Lukisan-lukisan di rumah ini memiliki kebiasaan ganjil untuk menceritakan apa yang sengaja dihapus dari buku sejarah.'{/i}"

    "Sebelum melangkah ke galeri lantai dua, aku melintasi aula utama yang temaram."
    "Di atas sebuah meja konsol mahoni di bawah tangga besar, sebuah buku tamu tua berbalut kulit lembu hitam dengan sudut-sudut kuningan berukir tergeletak di samping tempat lilin kuningan."
    "Evelyn sedang berada di dapur pelayan, memberiku kesempatan langka untuk memeriksa catatan arsip tersebut tanpa pengawasan."

    menu:
        "Memeriksa lembaran-lembaran awal buku tamu kuno di atas meja mahoni":
            $ evidence += 1
            $ evelyn_secret_noticed = True
            call inspect_clue("guestbook_1884")
            "Aku melangkah mendekati meja mahoni dengan langkah tanpa suara, membuka jilid tebal buku tamu kuno tersebut."
            "Aroma kertas lapuk dan tinta kering seketika menyeruak ke udara."
            "Jemariku membalik lembaran-lembaran perkamen yang menguning rapuh, menelusuri nama-nama tamu yang pernah menginap di Rose Manor puluhan tahun yang lalu."
            "Tinta hitam di halaman-halaman awal bertarikh musim gugur tahun 1884."
            "Dan tepat di sudut bawah halaman bertahun 1884 tersebut, sebuah tanda tangan tertulis dengan tinta emas tua yang sedikit pudar:"
            "{i}'Evelyn Hart - Disaksikan dengan kesetiaan abadi kepada wangsa Rosewood.'{/i}"
            "Lekukan huruf 'E', kemiringan aksara, dan bentuk tarikan garis tanda tangannya persis sama dengan tulisan tangan Evelyn saat ini!"
            "Jantungku berdegup kencang di dalam rongga dadaku."
            "Jika catatan resmi ini ditulis pada tahun 1884... lebih dari seratus tahun yang lalu... bagaimana mungkin wanita yang melayaniku sarapan tadi pagi masih tampak seperti gadis berusia dua puluh tahunan?!"
            "Evelyn Hart jelas bukan manusia biasa yang tunduk pada hukum alam."

        "Mengabaikan buku tamu dan bergegas menuju tangga sayap timur":
            $ ser_trust += 1
            "Aku memutuskan untuk tidak membuang waktu dengan buku tamu."
            "Prioritas utamaku malam ini adalah menyelidiki Galeri Potret Keluarga yang telah ditunjukkan oleh Victoria."

    scene bg_portrait_gallery
    with fade

    "Malam kedua resmi menyelimuti koridor sayap timur lantai dua."
    "Tempat-tempat lilin kuningan di dinding telah dinyalakan, memancarkan cahaya kuning temaram yang bergetar tertiup hawa dingin celah jendela."
    "Lorong ini adalah Galeri Potret Leluhur Rosewood—sebuah koridor panjang berlantai kayu ek yang dipelitur mengilap bagai cermin gelap."
    "Di kedua sisi dinding, puluhan lukisan cat minyak dalam bingkai kayu jati berlapis emas berjejer rapi, memancarkan keangkuhan dan kemurungan aristokratik yang membeku."

    "Langkah kakiku bergema pelan saat menyusuri barisan kanvas kuno tersebut."
    "Wajah-wajah para bangsawan di dalam lukisan menatapku dengan sorot mata kaku yang seolah hidup:"
    "Lord Alistair Rosewood, sang pendiri mansion pada abad ke-18, digambarkan dengan jubah beludru hitam berkerah bulu serigala dan pedang ksatria berhulu permata delima darah."
    "Di sampingnya, tergantung potret Lady Margaret Rosewood, seorang wanita bergaun sutra ungu tua dengan tatapan mata kosong dan sedih, seolah meratapi kematian anak-anaknya."
    "Setiap kanvas memancarkan hawa dingin yang ganjil, seolah jiwa-jiwa yang dilukis di dalamnya terperangkap abadi di balik lapisan pernis minyak."

    "Tiba-tiba, langkah kakiku terhenti kaku di depan sebuah kanvas raksasa di ujung lorong galeri."
    "Lukisan itu memiliki bingkai yang jauh lebih rumit daripada lukisan lainnya—diukir dengan motif sulur mawar berduri yang melilit tengkorak burung merpati."
    "Lukisan tersebut menggambarkan seorang wanita muda berparas jelita dengan gaun Victorian sutra berwarna gading yang anggun."
    "Rambut hitam legamnya terurai panjang bergelombang di atas bahunya yang ramping, sementara sepasang matanya yang berwarna violet memancarkan tatapan melankolis yang begitu memikat sekaligus menghancurkan hati."
    "Di tangannya yang lentik, wanita itu memegang erat sekuntum bunga mawar putih bersih yang mekar sempurna."

    mc "Mata violet itu... gaun sutra gading itu..."
    mc "Sosok ini adalah wanita yang kulihat melayang di antara kabut pekarangan semalam... Lilith Vane!"

    "Aku melangkah maju mendekati lukisan itu untuk membaca plakat tembaga berukir di bawah bingkainya."
    "Di sana tertera nama sederhana tanpa gelar kebangsawanan:"
    "{i}'Lilith - Jiwa yang Terikat pada Musim Gugur 1892.'{/i}"

    "Ketika aku berbalik sejenak untuk memeriksa lukisan potret keluarga di dinding seberang, sebuah suara gesekan halus dan basah terdengar dari arah kanvas di belakangku."
    "{i}Srrrt... Srrrt... Srrrt...{/i}"
    "Suara itu terdengar persis seperti ujung kuas basah yang sedang digoreskan dengan kasar di atas kain kanvas yang tegang!"

    "Bulu kudukku meremang seketika. Aku segera membalikkan badanku kembali menghadap lukisan Lilith."
    "Dan apa yang kulihat membuat darah di seluruh tubuhku seakan membeku seketika."

    "Mawar putih yang digenggam oleh Lilith di dalam lukisan... tidak lagi berwarna putih!"
    "Kelopak-kelopak bunganya kini telah berubah menjadi merah darah pekat yang mengerikan!"
    "Dan dari ujung tangkai mawar itu... cairan merah kental menyerupai darah segar merembes keluar dari permukaan kanvas, menetes pelan ke bingkai kayu bagian bawah!"
    "Bahkan sudut bibir wanita berambut hitam di dalam lukisan itu tampak melengkung sedikit, membentuk seringai pedih penuh penderitaan yang sebelumnya sama sekali tidak ada!"

    menu:
        "Memeriksa bingkai kayu dan celah di belakang lukisan secara teliti":
            $ evidence += 1
            $ inspected_portrait = True
            call inspect_clue("bleeding_portrait")
            "Mengabaikan hawa dingin yang menusuk ujung jemariku, aku melangkah maju dan meraba tepian bingkai kayu berukir rumit tersebut."
            "Di balik sudut kanan atas bingkai, kayu dinding terasa memiliki rongga sempit."
            "Ada goresan tulisan latin yang dipahat secara terburu-buru dengan benda tajam di kayu dinding belakang kanvas:"
            "{i}'Non omnes qui moriuntur requiescunt. Custos memoriae sanguinem poscit.'{/i}"
            "{i}(Tidak semua yang mati beristirahat dengan damai. Penjaga ingatan menuntut darah.){/i}"
            "Selain itu, ada goresan angka tujuh romawi: {i}VII{/i} yang dilingkari lambang mawar berduri."
            mc "Penjaga ingatan menuntut darah... Apakah ritual Rosewood benar-benar memakan korban jiwa manusia?"
            "Aku mengeluarkan buku catatanku dan menyalin tulisan latin serta simbol tersebut dengan teliti."

        "Menyentuh permukaan cat minyak pada kelopak mawar berdarah":
            $ evidence += 1
            $ inspected_portrait = True
            call inspect_clue("bleeding_portrait")
            "Aku mengangkat tanganku perlahan, mendekatkan ujung jariku ke permukaan kelopak mawar merah yang baru saja berubah warna di atas kanvas."
            "Cairan merah pada bagian mawar itu terasa basah, hangat, dan berdenyut halus!"
            "Aroma minyak biji rami segar bercampur bau logam tembaga khas darah manusia menempel di ujung jariku."
            mc "Cairan ini... adalah darah manusia sungguhan! Lukisan ini terhubung langsung dengan jiwa yang terperangkap!"
            "Setetes noda merah meresap ke dalam kulit jariku, memancarkan hawa dingin yang menusuk hingga ke pergelangan tangan sebelum kuseka dengan saputangan."

        "Berteriak memanggil Evelyn untuk meminta penjelasan segera atas fenomena ini":
            $ ser_trust += 1
            mc "Evelyn! Apakah kau ada di sekitar galeri ini?!"
            "Suaraku bergema memantul di dinding-dinding lorong galeri yang sunyi."
            "Hanya dalam hitungan detik, langkah kaki Evelyn terdengar mendekat dari ujung persimpangan lorong."

    "Evelyn Hart melangkah keluar dari bayang-bayang pilar koridor, wajahnya tetap menunjukkan ketenangan mutlak seorang pelayan bangsawan."

    show evelyn neutral with dissolve

    eve "Tuan memanggil saya? Ada yang mengganggu kenyamanan Anda di Galeri Keluarga?"

    show evelyn serious with dissolve

    mc "Evelyn, lihat lukisan ini dengan matamu sendiri! Mawar di tangan Lilith... mawar ini berwarna putih tadi sore, sekarang warnanya merah darah dan meneteskan cairan segar!"

    "Evelyn melangkah perlahan ke depan lukisan, menatap kanvas itu dengan sorot mata amber yang tak bergeming sedikit pun."

    eve "Mawar di tangan Nona Lilith selalu berwarna merah anggur, Tuan Guest. Sejak lukisan ini dibuat lebih dari seratus tahun yang lalu, tidak pernah ada catatan bahwa warnanya putih."
    eve "Pencahayaan lilin di lorong ini sering kali memperdaya mata mereka yang belum terbiasa dengan kegelapan Rose Manor."

    mc "Kau berusaha menutup-nutupi kebenaran, Evelyn. Aku melihat perubahannya dengan mata kepalaku sendiri beberapa detik yang lalu!"

    show evelyn surprised with dissolve
    "Untuk pertama kalinya, sebersit riak halus kekhawatiran melintas di pupil mata Evelyn sebelum ia kembali menguasai dirinya."
    show evelyn serious at sprite_right with dissolve

    eve "Tuan Guest... ada hal-hal di rumah ini yang jika Anda paksakan untuk dilihat sebelum waktunya, hanya akan mengundang bahaya yang mematikan bagi jiwa Anda sendiri."
    eve "Nona Seraphina sangat menjaga ketenangan galeri ini. Saya sarankan Anda kembali ke kamar tamu."

    "Suara langkah kaki halus lain terdengar menuruni tangga sayap barat."
    "Sosok bergaun hitam-merah melangkah masuk ke dalam koridor galeri dengan keanggunan yang dingin dan menawan."

    show seraphina serious at sprite_left with dissolve

    ser "Ada keributan apa di galeri leluhurku selarut ini, Evelyn?"

    eve "Nona Seraphina. Tuan Guest sedang mengagumi lukisan di sayap timur sebelum beristirahat."

    ser "Begitukah?"

    "Seraphina melangkah mendekatiku. Rambut peraknya yang panjang terurai indah di atas pundaknya, berkilau pucat di bawah temaram lentera dinding."
    "Matanya yang merah anggur melirik sekilas ke arah lukisan Lilith, lalu kembali menatap tepat ke dalam mataku."

    ser "Kau tampak gelisah, Guest. Udara malam kedua ini terasa lebih dingin dari biasanya, bukan?"

    menu:
        "Menceritakan keanehan lukisan Lilith secara jujur dan terbuka kepada Seraphina":
            $ ser_trust += 1
            mc "Seraphina, lukisan Lilith ini berubah di depan mataku sendiri. Aku melihat mawar di tangannya ternoda darah segar."
            show seraphina sad at sprite_left with dissolve
            "Seraphina terdiam sejenak. Sorot matanya menatap lukisan Lilith dengan rasa sakit yang mendalam yang berusaha ia sembunyikan di balik topeng kebangsawanannya."
            ser "Lilith adalah sahabat keluarga Rosewood di masa lalu... Kadang-kadang, kenangan duka menolak untuk tetap diam di tempat peristirahatannya."
            show seraphina neutral at sprite_left with dissolve
            ser "Kejujuranmu untuk menceritakan hal ini secara langsung kepadaku patut kuhargai, Guest. Setidaknya kau tidak menyembunyikan rasa takutmu di balik kebohongan."
            $ ser_aff += 1
            mc "Apakah Lilith benar-benar terkubur di taman mawar pekarangan?"
            ser "Pertanyaan itu melanggar batas aturan, Guest. Namun... jangan biarkan rasa penasaranmu menelan akal sehatmu."

        "Menutupi kecurigaan dan berbicara dengan nada lembut menenangkan":
            $ ser_aff += 1
            mc "Tidak ada apa-apa, Seraphina. Evelyn benar, barangkali mataku hanya lelah oleh bayang-bayang lilin."
            mc "Saya hanya tidak menyangka Anda masih terjaga selarut ini."
            ser "Malam hari adalah satu-satunya waktu di mana mansion ini terasa benar-benar milikku, Guest."
            ser "Di siang hari, rumah ini terasa seperti monumen batu yang mati. Namun di malam hari... ia bernapas bersama setiap rahasia yang terkurung di dalamnya."
            show seraphina smile at sprite_left with dissolve
            "Seraphina menatapku dengan sedikit rasa penasaran di sudut bibirnya."
            ser "Kau pria yang sangat tenang. Kebanyakan tamu sebelumnya sudah berteriak histeris sejak malam pertama."
            mc "Mungkin karena saya percaya bahwa Anda tidak berniat mencelakai saya tanpa alasan."
            show seraphina surprised at sprite_left with dissolve
            "Seraphina terdiam, memalingkan wajahnya sejenak dengan rona merah tipis di pipinya."

        "Mendesak Seraphina tentang siapa sebenarnya Lilith Vane":
            $ evidence += 1
            $ ser_trust += 1
            mc "Siapa Lilith Vane sebenarnya, Seraphina? Mengapa namanya terukir di nisan taman mawar dan lukisannya tampak hidup di sini?"
            show seraphina surprised at sprite_left with dissolve
            "Mendengar nama Lilith disebut dengan begitu tegas, Seraphina tersentak kecil. Jemarinya mencengkeram kain gaunnya erat-erat."
            show seraphina serious at sprite_left with dissolve
            ser "Kau terlalu banyak mencari tahu, Guest. Dan rasa ingin tahu di rumah ini selalu berujung pada hilangnya ingatan."
            show seraphina sad at sprite_left with dissolve
            ser "Lilith... adalah janji yang gagal dipenuhi oleh kakek buyutku. Hanya itu yang boleh kau ketahui untuk saat ini."
            show seraphina serious at sprite_left with dissolve
            ser "Jika kau terus mendesak, pintu-pintu di mansion ini akan menutup untukmu lebih cepat dari yang kau duga."

    ser "Malam semakin larut. Evelyn, pastikan gerendel pintu galeri dikunci rapat setelah Tuan Guest kembali ke kamarnya."

    hide seraphina with dissolve
    hide evelyn with dissolve

    "Seraphina berbalik dan menghilang ke dalam bayang-bayang lorong lantai atas, diikuti oleh langkah hening Evelyn."
    "Aroma mawar merah yang tertinggal di udara terasa lebih berat malam ini, seolah mengandung duka yang tak terucapkan."

    scene bg_guest_room
    with fade

    "Aku kembali ke dalam kamar tamu di lantai dua."
    "Setelah memastikan pintu terkunci rapat dengan kunci kuningan berukir mawar, aku duduk di dekat perapian yang menyala hangat."

    "Di luar jendela, badai salju tipis bercampur hujan mulai turun menyelimuti taman mawar."
    "Tepat ketika jarum jam menara berdentang dua belas kali menandakan tengah malam..."

    "{i}Kreeek... Tap... Tap... Tap...{/i}"

    "Dari langit-langit di atas kepalaku, terdengar suara langkah kaki halus yang melangkah mondar-mandir di lantai tiga!"
    "Suara langkah itu terdengar lambat dan teratur, seolah seseorang sedang berjalan dalam tidur di ruangan yang seharusnya dirantai dan dikunci rapat."

    mc "Lantai tiga... Padahal tangga menuju ke sana dirantai besi dan digembok..."
    mc "Siapa yang berjalan di atas sana setelah tengah malam?"

    "Aturan pertama kembali berdengung di telingaku:"
    "{i}Jangan pernah membuka pintu kamar mana pun di lantai tiga setelah tengah malam tiba.{/i}"

    menu:
        "Tetap berada di dalam kamar, mengamati langit-langit hingga suara langkah kaki mereda":
            $ ser_trust += 1
            "Aku mengepalkan tinjuku dan memutuskan untuk tetap bertahan di kursi perapian."
            "Mematuhi aturan pertama adalah keputusan paling bijak untuk saat ini. Menantang bahaya tanpa persiapan hanya akan membuatku celaka."
            "Setelah hampir setengah jam berlalu, suara langkah kaki di lantai tiga perlahan memudar dan lenyap ditelan deru angin malam."
            mc "Malam kedua telah berakhir. Aku harus lebih waspada di malam ketiga besok."

        "Membuka pintu kamar tamu sedikit untuk mengintip ke arah tangga lantai tiga":
            $ evidence += 1
            $ third_floor_rule_broken = True
            "Rasa ingin tahu yang membara mendorongku untuk melangkah mendekati pintu kamar."
            "Dengan sangat hati-hati, aku memutar kunci dan membuka daun pintu hanya selebar beberapa inci."
            "Koridor lantai dua gelap gulita, hanya disinari sisa bara api dari lampu dinding yang hampir padam."
            "Di ujung tangga menuju lantai tiga, rantai besi yang melintang tampak bergetar pelan."
            "Di balik bayang-bayang anak tangga paling atas, aku melihat sekelebat ujung kain gaun beludru hitam terseret perlahan sebelum menghilang ke dalam kegelapan."
            mc "Seseorang baru saja naik ke lantai tiga... dan gaun itu sangat mirip dengan gaun yang dikenakan Seraphina!"

    scene bg_guest_bed_pov
    with fade

    "Aku kembali ke ranjangku, menarik selimut beludru tebal, dan menatap ke arah langit-langit berukir dalam keheningan temaram perapian."
    "Malam kedua di Rose Manor berakhir dengan kecurigaan yang semakin menebal."
    "Potret Lilith yang berdarah, catatan tahun 1884 milik Evelyn, dan misteri langkah kaki di lantai tiga..."
    "Kepingan-kepingan teka-teki itu mulai membentuk lingkaran bahaya yang mengancam jiwaku."

    jump day_3

