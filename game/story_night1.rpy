## story_night1.rpy
## Malam 1: The Invitation (Kedatangan di Rose Manor)
## Naskah interaktif sastra gothic mystery mendalam

label night_1:
    $ night = 1

    scene black
    with fade

    "Roda pedati kayu berderak keras melindas bebatuan terjal yang licin di pedalaman Ashwood."
    "Di luar jendela kereta yang basah kuyup oleh guyuran badai, pepohonan hutan tua merentangkan dahan-dahannya yang meranggas kaku."
    "Dahan-dahan hitam itu tampak menyerupai jari-jemari kurus makhluk purba yang berusaha mencengkeram langit kelam tanpa bintang."
    "Guntur bergemuruh rendah di kejauhan, menggetarkan kaca kereta yang berembun dingin dan menebarkan aroma tanah basah bercampur lumut tua."
    play sound sfx_thunder

    scene bg_carriage_interior
    with fade

    "Di dalam kabin kereta yang berguncang pelan, aku menyandarkan kepalaku pada sandaran kulit yang dingin."
    "Di tanganku, sepucuk surat bersampul perkamen tebal terasa asing dan memberatkan pikiran."
    "Kertasnya berwarna gading kusam dengan pinggiran yang sedikit menguning, menyebarkan aroma samar seperti kelopak mawar kering yang disimpan bertahun-tahun di dalam peti kayu cendana."
    "Pada bagian penutupnya, sebuah segel lilin merah darah tercetak sempurna: lambang mawar mekar yang dilingkari duri-duri tajam."

    mc "Tujuh malam di Rose Manor..."
    mc "Tanpa nama pengirim yang jelas, namun surat ini menyebut namaku dengan sangat tepat. Siapa sebenarnya yang mengenalku di tempat terpencil seperti ini?"

    "Aku meraba kembali baris-baris kalimat yang tertulis dengan tinta emas tua beraksara elegan:"
    "{i}'Kepada Tuan [mc_name] yang terhormat,{/i}"
    "{i}Tujuh malam di bawah naungan atap Rose Manor menanti kehadiran Anda.{/i}"
    "{i}Kenangan yang hilang akan dikembalikan ke tempat asalnya, atau selamanya tertidur di antara semak mawar berduri.{/i}"
    "{i}Hadirilah sebelum lonceng tengah malam berdentang, atau pintu masa lalu akan terkunci untuk selamanya.'{/i}"

    "Kalimat-kalimat itu membangkitkan rasa cemas sekaligus rasa penasaran yang tak tertahankan."
    "Sejak bertahun-tahun yang lalu, ada kekosongan ganjil di dalam ingatanku—sebuah kabut tebal yang menutupi masa kecilku sebelum aku terbangun di kota pelabuhan."
    call inspect_clue("invitation_letter")
    "Apakah Rose Manor memegang kunci dari ingatan yang hilang itu?"

    "Kereta mendadak melambat, lalu berhenti dengan hentakan pelan di atas tanah berbatu kerikil."
    "Kusir tidak mengucapkan sepatah kata pun. Dari balik tirai depan, ia hanya mengetuk dinding kayu kabin tiga kali."
    "Ketukan itu dingin dan tegas, sebuah isyarat mutlak bahwa perjalananku dengan kendaraannya telah mencapai batas akhir."

    scene bg_gate
    with dissolve

    "Ketika aku melangkah turun ke tanah basah, angin malam seketika menyusup menembus mantel tebal yang kukenakan."
    "Hujan lebat telah mereda menjadi rintik-rintik halus yang dingin bagai jarum es."
    "Kabut pekat merayap lambat di atas permukaan tanah, menelan jejak roda pedati yang segera berbalik arah dan menghilang ke dalam kegelapan hutan."

    "Di hadapanku berdiri gerbang utama Rose Manor."
    "Besi-besi hitam penopangnya menjulang tinggi ke angkasa, berkarat di beberapa sudut namun tetap memancarkan keagungan kuno yang menakutkan."
    "Sulur-sulur mawar liar melilit jeruji besi itu dengan kelebatan yang ganjil. Batang-batangnya dipenuhi duri hitam panjang yang tampak seolah sengaja diasah."
    "Di puncak lengkungan gerbang, terukir semboyan keluarga Rosewood dalam aksara latin kuno:"
    "{i}'Sanguis et Memoria in Rosa Florebunt' - Darah dan Ingatan akan Mekar di dalam Mawar.{/i}"

    "Tepat ketika ujung jariku hendak menyentuh gerendel dingin, gerbang besi itu berderit perlahan."
    play sound sfx_creak
    "Engsel-engsel kunonya berputar dengan suara gesekan logam yang memekakkan telinga, membuka celah ke dalam pekarangan tanpa ada seorang pun yang menyentuhnya dari dalam."

    mc "Menarik. Rumah ini seolah sudah mengetahui kedatanganku sebelum aku sempat mengetuknya."

    "Aku melangkah melewati pelataran berbatu kerikil kelabu."
    "Di kedua sisi jalan setapak, deretan patung malaikat marmer tanpa wajah berdiri kaku di antara semak belukar yang basah."
    "Wajah-wajah patung itu telah terkikis oleh lumut dan waktu, memberikan kesan bahwa mereka sedang mengawasi setiap derap langkahku dengan tatapan hampa."

    "Di kejauhan, siluet Rose Manor berdiri megah menembus kegelapan malam."
    "Bangunan bergaya Victorian gothic itu dibangun dari blok-blok granit hitam yang basah disinari kilatan halilintar pucat di balik awan badai."
    "Menara-menara lancipnya meruncing menembus kabut, sementara jendela-jendela tingginya memancarkan pendar cahaya lilin temaram dari balik tirai sutra gelap."
    "Sebuah menara jam tua di sayap timur berdetak lambat, gema pendulumnya terdengar berat membelah keheningan hutan."

    scene bg_manor_hall
    with fade
    play music bgm_manor fadein 2.5

    "Pintu utama kayu ek berlapis ukiran floral membuka ke sebuah aula utama yang luar biasa megah."
    "Lantai marmer hitam-putih bermotif papan catur memantulkan temaram cahaya dari lampu gantung kristal antik yang tergantung tinggi di langit-langit berkubah."
    "Puluhan lilin berkedip lembut di dalam sangkar kristal, menebarkan wangi minyak esensial, kayu manis, dan dupa mawar yang samar."

    "Di tengah ruangan, sebuah tangga marmer megah meliuk anggun menuju lantai dua, dilapisi karpet beludru merah marun yang tebal dan bersih tanpa sebutir debu pun."

    "Langkah kaki yang halus dan teratur terdengar memecah keheningan aula."
    "Dari lorong samping yang menghubungkan aula dengan sayap pelayan, seorang wanita muda melangkah mendekat dengan postur tubuh yang luar biasa tegak dan terlatih."

    "Ia mengenakan seragam pelayan bergaya Victorian berwarna biru malam pekat, dipadukan dengan celemek putih berenda kaku yang bersih tanpa cela."
    "Rambut cokelat gelapnya disanggul rapi di balik hiasan kepala pelayan, membingkai sepasang mata berwarna amber keemasan yang tenang namun tajam menatapku."
    "Di lehernya, sebuah rantai perak tipis menggantungkan sebuah kunci antik berukir rumit."

    show evelyn neutral at sprite_center with dissolve
    eve "Selamat malam, Tuan. Selamat datang di kediaman Rose Manor."
    eve "Saya Evelyn Hart, kepala pelayan di kediaman ini. Perjalanan Anda melewati hutan Ashwood tentu melelahkan di tengah cuaca buruk seperti ini."

    mc "Selamat malam, Nona Evelyn. Tempat ini cukup sulit ditemukan di tengah badai."

    eve "Mansion ini memang tidak dirancang untuk ditemukan oleh sembarang pelancong, Tuan. Hanya mereka yang menerima undangan resmi yang dapat melewati perbatasan hutan tanpa tersesat."

    "Evelyn mengulurkan kedua tangannya dengan gerakan anggun untuk menerima mantelku yang basah, lalu meletakkannya pada gantungan kayu berukir di dekat perapian."

    eve "Nona Seraphina telah menantikan kehadiran Anda sejak jam petang. Beliau secara khusus meminta saya memastikan kedatangan Anda tidak terlambat dari jadwal."

    mc "Apakah ada tamu lain yang menginap di sini selain diriku, Evelyn?"

    eve "Ada satu tamu lain yang sedang melakukan studi kepustakaan di sayap timur, Tuan. Namun untuk malam ini, fokus utama mansion adalah menyambut kedatangan Anda."

    "Sebelum aku sempat menanyakan lebih lanjut mengenai tamu tersebut, gema ketukan tumit sepatu berbunyi anggun di atas anak tangga marmer."
    "Suasana di aula mendadak berubah hening dan dingin, seolah udara hangat di dekat perapian ditarik mundur oleh kehadiran seseorang."

    "Dari balkon lantai dua, sosok yang telah lama dinantikan melangkah menuruni karpet merah dengan ketenangan seorang ratu di istana sunyinya."

    "Wanita muda itu memiliki rambut perak panjang yang berkilau laksana sutra murni di bawah temaram cahaya lilin."
    "Ia mengenakan gaun berpotongan bangsawan Victorian dengan perpaduan warna beludru hitam pekat dan sutra merah anggur yang mewah."
    "Di bagian dadanya, tepat di atas belahan gaun berenda hitam, tersemat sebuah bros mawar merah darah yang kelopaknya tampak begitu segar, seolah baru saja dipetik beberapa detik yang lalu dari tangkai mawar hidup."

    hide evelyn with dissolve
    $ persistent.cg_first_meeting = True
    scene cg_first_meeting with dissolve

    "Sepasang mata merah anggur yang dingin dan jernih menatap lurus ke arahku."
    "Tidak ada senyuman di wajahnya yang pucat dan rupawan, hanya sebuah ketenangan aristokrat yang menyembunyikan jarak yang tak terukur."

    ser "Kau akhirnya tiba."
    ser "Aku adalah Seraphina Rosewood. Pemilik sah dan penjaga tunggal Rose Manor."

    "Seraphina berhenti di anak tangga terakhir, hanya beberapa langkah di hadapanku."
    "Aroma mawar yang pekat dan dingin merebak di sekitarnya, menenggelamkan wangi lilin aula."

    menu:
        "Menjawab dengan sopan dan membungkuk hormat layaknya tamu terhormat":
            $ ser_aff += 1
            $ ser_trust += 1
            mc "Sebuah kehormatan besar bisa bertemu dengan Anda secara langsung, Nona Seraphina. Saya menghargai sambutan hangat di malam yang dingin ini."
            show seraphina smile with dissolve
            ser "Kesopanan adalah barang langka di zaman sekarang, Guest. Banyak yang menginjakkan kaki di tanah Rosewood hanya dengan tuntutan, rasa tamak, dan kesombongan."
            "Sorot mata Seraphina sedikit melembut, meski ekspresi wajahnya tetap menjaga kewibawaan yang tegas."
            ser "Kuharap kesopanan dan ketenanganmu ini akan tetap bertahan utuh hingga malam terakhir dari kunjunganmu."
            mc "Saya berusaha untuk selalu menghormati tuan rumah di mana pun saya berada."
            ser "Pilihan kata yang bijak. Kita lihat apakah tindakanmu akan sejalan dengan perkataanmu."

        "Langsung bertanya tentang alasan dan rahasia di balik surat undangan":
            $ ser_trust += 2
            mc "Terima kasih atas sambutan Anda, Nona Seraphina. Namun saya datang ke sini bukan untuk beramah-tamah tanpa tujuan. Mengapa Anda mengirimkan surat undangan ini kepada saya?"
            ser "Pertanyaan yang lugas tanpa basa-basi. Kau tidak membuang waktu untuk menuntut kejelasan."
            "Seraphina mengamati wajahku dengan tatapan menyelidik yang lebih tajam, seolah sedang mencocokkan garis wajahku dengan ingatannya sendiri."
            ser "Keberanianmu patut dihargai. Namun di Rose Manor, setiap rahasia memiliki waktu panennya masing-masing. Terlalu terburu-buru membuka pintu hanya akan memadamkan lilinmu sendiri."
            mc "Surat Anda menyebutkan tentang kenangan yang hilang. Apakah Anda mengetahui masa lalu saya?"
            ser "Masa lalu adalah benang merah yang kusut di rumah ini, Guest. Kita akan mengurainya helai demi helai, jika kau mampu bertahan."

        "Mengamati reaksinya dan memperhatikan bros mawar yang digenggamnya":
            $ evidence += 1
            $ rose_necklace_examined = True
            call inspect_clue("rose_brooch")
            "Aku memilih menahan diri untuk tidak langsung berbicara, membiarkan beberapa detik hening berlalu di antara kami."
            "Pandanganku terarah pada jemari Seraphina yang berbalut sarung tangan sutra hitam."
            "Tanpa ia sadari, ibu jarinya meraba kelopak bros mawar merah di dadanya dengan tekanan yang sedikit gemetar, seolah benda itu adalah penopang keberaniannya di hadapanku."
            ser "Tatapanmu sangat teliti dan tidak mudah dialihkan, Guest."
            ser "Observasi adalah senjata yang berbahaya di rumah ini. Berhati-hatilah agar apa yang kau perhatikan tidak balik memperhatikanmu ke dalam jurang."
            mc "Saya hanya memperhatikan bahwa bros mawar di dada Anda tampak memiliki denyut yang hidup, Nona Seraphina."
            "Seraphina tersentak kecil, lalu segera menarik tangannya dari bros tersebut dengan sikap dingin yang dipaksakan."
            ser "Itu hanyalah permata peninggalan keluarga. Tidak lebih dari sekadar perhiasan antik."

    scene bg_manor_hall with dissolve
    show seraphina neutral with dissolve

    ser "Sebelum Evelyn mengantarmu ke kamar tamu di sayap barat, ada hal yang jauh lebih penting daripada sekadar perkenalan nama."
    ser "Rose Manor bukanlah penginapan biasa. Tanah ini terikat oleh perjanjian kuno yang tidak boleh dilanggar oleh siapa pun, termasuk para tamu kehormatan."

    mc "Perjanjian kuno? Maksud Anda aturan tertentu yang mengikat tamu?"

    ser "Tepat. Ada tiga aturan mutlak yang harus kau ingat dan patuhi selama tinggal di sini. Keselamatan dan kelangsungan ingatanmu bergantung sepenuhnya pada kepatuhanmu."

    "Seraphina melangkah satu tapak lebih dekat. Nada suaranya merendah, berat dan penuh penegasan yang tidak mengizinkan perdebatan."
    show seraphina serious with dissolve

    ser "Aturan pertama: Jangan pernah membuka pintu kamar mana pun di lantai tiga setelah tengah malam tiba."
    ser "Aturan kedua: Jangan pernah menjawab suara yang memanggil namamu dari arah taman mawar."
    ser "Dan aturan ketiga: Jangan pernah bertanya kepada siapa pun di mansion ini mengenai apa yang terjadi pada malam kedelapan."

    mc "Malam kedelapan? Namun surat undangan Anda hanya mencantumkan kunjungan selama tujuh malam."

    ser "Benar. Tujuh malam adalah batas waktu yang diberikan takdir kepadamu."
    ser "Bagi mereka yang menghormati aturan, fajar akan datang membawa kepulangan. Namun bagi mereka yang melanggarnya... malam kedelapan tidak akan pernah tiba di dunia nyata."

    "Hawa dingin berdesir di punggungku mendengar perkataannya."
    "Evelyn yang berdiri di dekat pintu samping hanya menundukkan kepala perlahan, tidak membantah maupun menambahkan satu kata pun."

    eve "Kamar tamu di lantai dua sayap barat telah dipersiapkan dengan baik, Tuan. Api di perapian sudah dinyalakan dan air hangat telah disediakan."
    eve "Jika Tuan berkenan, mari saya antarkan agar Tuan dapat membersihkan diri dan beristirahat."

    ser "Istirahatlah malam ini, Guest. Besok malam, mansion ini akan mulai memperlihatkan dirinya yang sesungguhnya kepadamu."

    hide seraphina with dissolve

    "Seraphina berbalik dengan gerakan anggun gaunnya, melangkah kembali menaiki tangga marmer menuju sayap utara."
    "Hanya aroma mawar merah yang tertinggal di anak tangga marmer."

    eve "Mari lewat sini, Tuan."

    scene bg_manor_hall
    with dissolve

    "Aku mengikuti langkah Evelyn menaiki tangga marmer menuju koridor lantai dua."
    "Di sepanjang koridor panjang berpenerangan lampu minyak temaram, deretan potret leluhur keluarga Rosewood tergantung di dinding kayu ek yang gelap."
    "Ketika kami melewati persimpangan menuju tangga lantai tiga, langkah kakiku sempat tertahan."

    "Sebuah rantai besi tebal melintang menghalangi anak tangga menuju lantai tiga."
    "Sebuah gembok perak berkarat mengunci rantai tersebut, dan sebuah plakat kuningan tua tergantung di sana dengan tulisan latin yang terukir dalam:"
    "{i}'Mors memoriae est silentium' - Kematian ingatan adalah keheningan mutlak.{/i}"

    eve "Lantai tiga ditutup rapat untuk alasan privasi dan keselamatan keluarga, Tuan. Saya menyarankan Anda untuk tidak mendekati area tersebut, terutama saat malam mulai larut."

    mc "Apakah ada seseorang yang tinggal di lantai tiga, Evelyn? Atau ada sesuatu yang disimpan di sana?"

    eve "Hanya kenangan lama yang menolak untuk pergi, Tuan. Dan kenangan lama di rumah ini memiliki kebiasaan buruk menuntut harga yang teramat mahal bagi siapa pun yang membangunkannya."

    "Jawaban Evelyn diucapkan dengan nada datar dan dingin, tanpa sedikit pun keraguan atau ketakutan."

    scene bg_guest_room
    with dissolve

    "Evelyn membukakan pintu kayu jati berukir mawar di ujung lorong lantai dua."
    "Kamar tamu ini berukuran luas dan terawat luar biasa rapi."
    "Sebuah ranjang empat tiang berlapis tirai sutra gelap berdiri di sudut ruangan, sementara perapian batu bata memancarkan kehangatan kayu cedar yang berderak menenangkan."
    "Di dekat jendela tinggi yang menghadap ke luar, sebuah cermin rias oval berbingkai perak kusam memantulkan bayangan ruangan."

    show evelyn neutral at sprite_center with dissolve
    eve "Ini kunci kamar Anda, Tuan."

    "Evelyn menyerahkan sebuah kunci kuningan berukir lambang mawar ke tanganku."

    eve "Kunci pintu ini dari dalam sebelum jarum jam menunjuk angka sebelas. Dan ingat pesan Nona Seraphina: jangan hiraukan apa pun yang terdengar dari balik kaca jendela."
    eve "Selamat malam, Tuan Guest. Semoga tidur Anda tidak diganggu oleh mimpi masa lalu."

    hide evelyn with dissolve
    "Evelyn membungkuk hormat, lalu menutup pintu kamar dengan bunyi klik gerendel yang tegas."
    "Kini aku sendirian di dalam kamar tamu Rose Manor."

    play sound sfx_clock
    "Detak jarum jam dinding antik di sudut kamar berdetak ritmis dan berat, mengiringi sunyinya malam."
    "Sebelum memutuskan untuk tidur, ada waktu sejenak untuk memeriksa sudut-sudut ruangan ini dengan seksama."

label night1_investigation_loop:
    call screen room_inspection
    $ chosen_item = _return

    if chosen_item == "inspect_desk":
        play sound sfx_creak
        "Aku melangkah mendekati meja tulis mahoni berukir mawar di sudut ruangan."
        "Laci utamanya tidak terkunci. Di dalamnya tersimpan buku catatan tamu tua berdebu dari dekade lalu."
        "Sebuah coretan pensil samar di pinggir kayu laci berbunyi: {i}'Jangan pernah mempercayai dentangan lonceng kedelapan.'{/i}"
        jump night1_investigation_loop

    elif chosen_item == "inspect_fireplace":
        play sound sfx_fire
        "Aku mendekati perapian marmer yang memancarkan kehangatan kayu cedar merah yang berderak menenangkan."
        "Bara apinya menyala stabil, mengusir dinginnya udara lembah Ashwood yang menusuk hingga ke tulang sumsum."
        "Di dekat tumpukan abu hitam, tampak secarik perkamen hangus dengan inisial 'S.R.' yang masih tersisa."
        jump night1_investigation_loop

    elif chosen_item == "inspect_mirror":
        "Aku berdiri mematung di hadapan cermin oval berbingkai perak kusam."
        "Permukaan kacanya tampak dingin dan suram, memantulkan bayangan diriku yang disinari temaram lilin."
        "Namun sekejap mata, untuk sepersekian detik... pantulan di dalam cermin seakan bergeming sesaat lebih lambat sebelum mengikuti gerakanku."
        "Hawa dingin merambati tengkukku."
        jump night1_investigation_loop

    elif chosen_item == "inspect_window":
        play sound sfx_wind
        "Aku melangkah mendekati jendela kaca besar yang berembun dingin."
        "Di luar, badai salju tipis meliuk ditiup angin malam."
        "Di kejauhan sayap barat, puncak menara lantai tiga yang terkunci tampak gelap gulita tanpa seberkas cahaya pun."
        jump night1_investigation_loop

    elif chosen_item == "go_to_sleep":
        "Rasa kantuk dan kelelahan perjalanan panjang akhirnya mendera tubuhku."
        "Aku memutuskan untuk mengakhiri pemeriksaan kamar malam ini dan bersiap istirahat."

    "Di luar jendela kaca besar yang dingin, kabut putih tebal bergulung rendah di atas pekarangan luas."
    "Di bawah cahaya bulan sabit yang memucat di balik awan mendung, terlihat hamparan taman mawar yang teramat luas."
    "Anehnya, mawar-mawar merah di taman itu tampak bermekaran segar dan lebat, menentang dinginnya musim badai yang membekukan ranting-ranting lainnya."

    "Lonceng besar di menara jam Rose Manor berdentang lambat."
    "{i}Teng... Teng... Teng...{/i}"
    "Dua belas dentangan berat mengguncang kesunyian malam, menandakan pergantian waktu menuju tengah malam."

    "Tepat ketika gema dentangan terakhir lenyap ditelan kegelapan, desiran angin lembut menyusup dari sela-sela bingkai jendela."
    "Bukan sekadar suara angin..."
    "Sebuah bisikan lirih, begitu halus dan merdu menyerupai suara tawa seorang gadis muda, berbisik memanggil namaku dari kedalaman taman mawar di bawah sana."

    voice_unknown "{i}...Guest... Mengapa kau datang begitu terlambat?...{/i}"

    "Darahku terasa membeku sejenak di dalam dada."
    "Aturan kedua terlintas jelas di benakku: {i}Jangan pernah menjawab suara yang memanggil namamu dari taman mawar.{/i}"

    menu:
        "Mengunci jendela rapat-rapat, menutup tirai tebal, dan mematuhi aturan kedua":
            $ ser_trust += 1
            "Aku segera memutar grendel kuningan pada jendela hingga terdengar bunyi kunci yang rapat."
            "Tirai beludru tebal kututup rapat, menghalangi pandangan maupun bisikan kabut malam di luar."
            "Aku duduk di dekat kehangatan perapian, menenangkan debaran jantungku yang berdegup kencang."
            mc "Tempat ini benar-benar tidak wajar. Seraphina tidak melebih-lebihkan aturan itu demi menakut-nakuti tamunya."
            "Aku membuka buku catatan kecilku dan menuliskan kejadian malam pertama dengan tangan yang perlahan kembali tenang."

        "Berdiri tenang di balik kaca jendela dan mengamati sosok bayangan di taman mawar":
            $ evidence += 1
            "Aku menahan napas dan tetap berdiri mematung di balik kaca jendela."
            "Mataku memicing menembus kabut tebal di antara semak mawar merah."
            "Di sana, di dekat sebuah batu nisan tua yang tertutup lumut, sesosok siluet bergaun putih gading melayang beberapa inci di atas tanah."
            "Cahaya violet redup tampak berpendar di sekeliling rambut hitamnya yang terurai panjang."
            "Sosok itu menoleh ke arah jendelaku, tersenyum tipis penuh rahasia sebelum memudar ke dalam kabut."
            mc "Itu bukan manusia biasa... Ada roh yang terperangkap di taman mawar itu."
            "Aku mencatat penampakan wanita bergaun gading bermata violet itu di dalam jurnal investigasiku."

    scene bg_guest_bed_pov
    with fade

    "Aku memadamkan sisa lilin di atas meja nakas dan merebahkan tubuhku yang letih di atas kasur berkanopi mewah kamar tamu."
    "Di bawah selimut beludru marun yang hangat, aku menatap langit-langit kamar dan bayangan pilar-pilar kanopi yang diterangi temaram bara api perapian."
    "Malam pertama di Rose Manor akhirnya berlalu dalam keheningan yang sarat misteri."
    "Namun satu hal yang kupahami dengan pasti: tujuh malam di mansion ini akan menjadi pertaruhan antara kebenaran masa lalu dan keselamatan nyawaku sendiri."

    jump day_2
