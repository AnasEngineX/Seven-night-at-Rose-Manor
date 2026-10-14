## story_day5.rpy
## Siang Hari 5: Balkon Menara dan Impian Seraphina (The Tower Balcony)
## Naskah interaktif sastra gothic romance mendalam

label day_5:
    scene black
    with fade

    "Fajar hari kelima merekah dengan warna perak kebiruan yang luar biasa memukau di atas cakrawala Hutan Ashwood."
    "Salju tebal yang turun semalaman kini menyelimuti seluruh atap-atap lancip, menara gotik, dan patung-patung gargoyle Rose Manor, memantulkan sinar matahari pagi yang dingin bagai hamparan jutaan kristal berlian."
    "Di dalam aula utama mansion, udara pagi terasa sedikit lebih bersahabat daripada hari-hari sebelumnya."
    "Aroma roti gandum hangat yang baru keluar dari pemanggang, selai buah arbei liar yang manis asam, dan kopi kental hitam menyambut langkahku saat menuruni tangga marmer yang megah."
    "Kehangatan pagi ini terasa begitu kontras dengan kengerian diagram okultisme terlarang {i}'Sigillum Septem Foliorum'{/i} yang kuperiksa bersama Victoria di perpustakaan semalam."

    "Namun begitu kakiku menjejak lantai marmer aula, aku menyadari bahwa pagi ini ada pemandangan yang tidak lazim."
    "Bukan hanya Evelyn yang berdiri dengan celemek putihnya di dekat meja makan."

    scene bg_manor_hall
    with dissolve

    "Di dekat jendela berkaca patri tinggi yang menghadap ke pekarangan depan, berdiri Seraphina Rosewood."
    "Ia mengenakan mantel musim dingin berbahan beludru hitam pekat berpotongan anggun dengan kerah bulu rubah salju putih tebal yang membalut leher jenjangnya."
    "Rambut peraknya yang panjang disisir rapi dan berkilauan indah tertimpa seberkas sinar matahari pagi, membingkai wajah cantiknya yang seputih pualam katedral."
    "Di tangannya, ia memegang sepasang sarung tangan kulit hitam halus, sementara tatapannya terpaku pada puncak-puncak pohon pinus di kejauhan."

    show seraphina neutral with dissolve

    ser "Selamat pagi, Guest."

    mc "Selamat pagi, Seraphina. Suatu pemandangan yang sangat langka dan menyenangkan melihat sang nyonya rumah telah menyapa pagi di aula sepagi ini."

    "Seraphina menoleh ke arahku dengan senyuman tipis yang hangat, rona merah muda samar merebak di kedua pipinya yang dingin."

    show seraphina smile with dissolve

    ser "Pagi ini memiliki langit yang jernih, Guest. Kabut tebal yang biasanya mencekik lembah kita untuk sementara tersapu oleh angin utara."
    ser "Aku ingin memperlihatkan sesuatu yang istimewa kepadamu sebelum matahari terbenam dan malam kembali membawa bayang-bayang kelamnya."
    ser "Maukah kau menemaniku mendaki ke puncak menara timur?"

    mc "Tentu saja, Seraphina. Ke mana pun kau melangkah, aku akan selalu berada di sisimu."

    scene bg_balcony
    with fade
    play sound sfx_wind
    show snow_particles with dissolve

    "Kami menaiki tangga spiral batu granit yang sempit dan melingkar di dalam lambung Menara Jam Timur."
    "Undakan-undakan batunya telah aus di bagian tengahnya oleh jejak langkah para penghuni mansion selama lebih dari dua ratus tahun."
    "Setelah menaiki hampir seratus undakan batu, sebuah pintu kayu jati kecil berayun terbuka, membawa kami keluar ke sebuah balkon terbuka berlantai marmer dengan pagar pembatas batu granit berukir sulur mawar berduri."

    "Dari ketinggian puncak menara ini, pemandangan seluruh lembah Ashwood terbentang luas sejauh mata memandang, begitu agung dan mempesona hingga membuat nafasku tercekat sesaat."
    "Hutan pinus raksasa yang tertutup salju terbentang laksana lautan zamrud keperakan yang tak berujung."
    "Danau es di kaki lembah berkilau memantulkan awan-awan putih, sementara pegunungan granit yang puncaknya diselimuti gletser abadi berdiri tegak menantang langit biru pucat."
    "Angin musim dingin yang sejuk dan segar bertiup kencang di ketinggian ini, menerbangkan ujung rambut perak Seraphina dan selendang sutra hitam yang melingkari lehernya."

    $ persistent.cg_balcony_promise = True
    scene cg_balcony_promise with dissolve

    "Seraphina menyandarkan kedua tangannya yang bersarung tangan pada pagar balkon batu, menatap lurus ke arah cakrawala tak bertepi dengan sorot mata yang penuh keharuan."

    ser "Luar biasa luasnya, bukan?"
    ser "Sejak usiaku masih sangat kecil, setiap kali rasa sesak akan kewajiban keluarga Rosewood menghimpit dadaku hingga aku sulit bernapas, aku selalu melarikan diri ke puncak menara ini sendirian."
    ser "Dari sini... dunia di luar sana tampak begitu agung dan bebas... sementara Rose Manor dan segala kutukannya tampak begitu kecil dan rapuh dibandingkan dengan langit tanpa batas itu."
    ser "Namun setiap kali aku menatap ke bawah... aku teringat bahwa aku adalah tawanan dari dinding-dinding batu ini. Sebuah sangkar emas yang menuntut jiwaku sebagai harga sewa keabadian semu."

    mc "Dunia di luar sana bukan sekadar khayalan, Seraphina. Dunia itu nyata dan sedang menantimu."
    mc "Ada kota-kota pelabuhan dengan ratusan kapal berlayar di bawah terik matahari musim panas, ada pasar-pasar bunga yang riuh oleh tawa anak-anak, dan ada tempat-tempat di mana manusia bisa mencintai tanpa perlu takut ingatannya akan dicuri oleh malam."

    "Seraphina menoleh menatapku perlahan. Sepasang matanya yang merah anggur memancarkan kerinduan yang begitu menusuk kalbu, bercampur dengan kerentanan seorang wanita muda yang merindukan pelukan hangat."

    ser "Guest... katakan padaku dengan jujur..."
    ser "Jika sebuah keajaiban benar-benar terjadi... jika kutukan mawar berdarah ini berhasil kau patahkan di malam ketujuh nanti tanpa merenggut ingatan siapa pun..."
    ser "Ke mana kau akan melangkah setelah pintu gerbang Rose Manor terbuka lebar?"

    menu:
        "Menjawab bahwa aku ingin tetap tinggal di sini bersamanya untuk membangun kembali Rose Manor menjadi rumah yang penuh cinta":
            $ ser_aff += 3
            $ ser_trust += 2
            mc "Aku tidak akan melangkah ke mana-mana, Seraphina. Jika kutukan ini berakhir, aku ingin tetap tinggal di sini di sisimu."
            mc "Kita bisa membuka pintu gerbang mansion ini untuk dunia luar, membersihkan debu-debu kepedihan masa lalu, dan menanam mawar-mawar baru yang mekar murni tanpa tetesan darah."
            mc "Kita bisa menjadikan tempat ini rumah yang sesungguhnya—rumah yang dipenuhi tawa, musik piano, dan kehangatan keluarga."
            "Mata Seraphina berkaca-kaca menatapku. Bibirnya yang bergetar menahan isak haru yang mendalam."
            ser "Kau... benar-benar bersedia tinggal di lembah dingin dan terpencil ini... hanya demi diriku, Guest?"
            mc "Bukan karena dinding batunya, Seraphina, melainkan karena dirimu yang berada di dalamnya. Di mana pun kau berada, di situlah rumah tempat hatiku berlabuh."
            "Seraphina menundukkan kepalanya, menyembunyikan wajahnya yang merona merah manis di balik kerah bulu putih mantelnya yang tebal."
            ser "Kau benar-benar seorang perayu yang berbahaya, Guest... Kau telah merobohkan seluruh benteng pertahanan yang kubangun selama sepuluh tahun."

        "Mengajak Seraphina keluar meninggalkan lembah ini untuk menjelajahi lautan lepas dan dunia baru bersama":
            $ ser_aff += 2
            $ ser_trust += 2
            mc "Aku ingin membawamu keluar dari lembah berkabut ini, Seraphina. Kita akan pergi ke pesisir selatan, melihat deburan ombak lautan lepas di bawah langit biru musim panas."
            mc "Kau telah terkurung di dalam sangkar batu ini selama dua puluh lima tahun seumur hidupmu. Kau berhak merasakan hangatnya pasir pantai dan kebebasan mutlak yang belum pernah kau kecap."
            "Sebuah senyuman yang begitu cerah dan memesona terbit di wajah Seraphina, membuat kecantikan alaminya bersinar berlipat ganda laksana fajar."
            ser "Lautan lepas... Ibuku dulu sering membacakan puisi tentang layar-layar putih di atas gelombang biru."
            ser "Seumur hidupku, hal itu terdengar seperti dongeng anak-anak yang mustahil kuraih... Namun saat mendengarmu mengatakannya, aku merasa bahwa barangkali... aku memang berhak untuk bahagia."

        "Menjawab dengan realistis dan penuh kehati-hatian bahwa fokus utama kita adalah bertahan hidup di malam ketujuh":
            $ ser_trust += 2
            mc "Sebelum kita membicarakan rencana masa depan yang jauh, Seraphina, fokus utamaku adalah memastikan kita berdua selamat melewati altar bawah tanah di malam ketujuh."
            mc "Aku tidak akan membiarkan angan-angan manis membuat kewaspadaan kita melemah di hadapan bahaya yang nyata."
            ser "Jawaban yang sangat matang, rasional, dan bertanggung jawab, Guest. Kau selalu menjadi jangkar yang menenangkan di saat kepalaku mulai dipenuhi kecemasan."
            ser "Kau benar. Kita harus memenangkan pertempuran melawan kegelapan terlebih dahulu agar fajar masa depan itu benar-benar terbit."

    scene bg_balcony with dissolve
    play sound sfx_wind
    show snow_particles with dissolve
    show seraphina smile with dissolve

    "Hembusan angin utara yang bertiup kian kencang di balkon menara membuat tubuh ramping Seraphina sedikit menggigil kedinginan di balik mantel tebalnya."
    "Tanpa ragu-ragu, aku melangkah mendekat ke arahnya, membuka sebagian mantel wolku dan merapatkannya di sekeliling pundaknya, mendekap kedua tangannya yang dingin di antara telapak tanganku yang hangat."
    "Seraphina tidak menolak atau menghindar sedikit pun. Justru, ia menyandarkan kepalanya dengan lembut di dadaku, membiarkan kehangatan tubuh dan detak jantung kami menyatu di bawah langit perak."

    ser "Matahari siang mulai bergerak menuju barat, Guest. Udara dingin petang akan segera turun menyelimuti lembah."
    ser "Malam ini... adalah malam kelima."
    ser "Pintu ruang duduk pribadiku di sayap utara akan terbuka khusus untukmu."
    ser "Datanglah saat lonceng menara berdentang sembilan kali. Ada rahasia dan perasaan yang hanya bisa kubicarakan denganmu di hadapan perapian kamarku."

    mc "Aku pasti akan datang tepat waktu, Seraphina. Aku tidak akan membiarkanmu menunggu."

    hide snow_particles with dissolve
    hide seraphina with dissolve

    "Kami menuruni tangga spiral menara bersama-sama dalam keheningan yang sarat dengan ikatan batin yang kian tak terpisahkan."
    "Di puncak menara itu, sebuah janji tak terucapkan telah dipatri di antara jiwa kami."

    "Malam kelima menanti di hadapanku."
    "Malam di mana Seraphina Rosewood akan membuka pintu hatinya yang terluka."

    jump night_5

