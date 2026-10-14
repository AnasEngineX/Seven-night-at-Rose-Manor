## story_prologue.rpy
## Prolog: Undangan Bersegel Mawar (The Ashwood Crossing)
## Naskah interaktif pembuka perjalanan menuju Rose Manor

define innkeeper = Character("Pemilik Kedai", color="#a0826c")
define coachman = Character("Kusir Kereta", color="#7f8c8d")

label prologue:
    play music bgm_night fadein 2.0
    scene black
    with fade

    "Semuanya berawal dari sebuah senja yang basah oleh hujan es dan kabut kelabu di kota tua Ashwood."
    "Kota kecil di kaki lembah terpencil itu tampak suram, tua, dan seakan tertidur dalam pelukan bayang-bayang bukit granit hitam yang menjulang angkuh menantang langit."
    "Jalanan berbatu sempit digenangi air berlumpur bercampur salju mencair, memantulkan temaram cahaya lentera minyak kuning dari kedai penginapan tua {i}'The Black Crow'{/i}."
    "Angin musim dingin melolong liar di antara atap-atap seng dan cerobong bata merah yang menghitam, meniupkan bau jelaga basah, tembakau kasar, dan lumut rawa ke dalam lorong-lorong kota yang sunyi tanpa pejalan kaki."

    scene bg_tavern
    with fade

    "Di dalam kedai yang beraroma kayu ek basah, tembakau pipa, dan rebusan daging domba berempah, aku duduk sendirian di sudut perapian batu besar."
    "Di atas meja kayu ek yang penuh goresan pisau dan noda tumpahan ale, sepucuk surat bersampul perkamen tebal terbaring di samping cangkir tembaga berisi bir hitamku."
    "Segel lilin merah darah berbentuk bunga mawar mekar dengan duri-duri tajam tampak begitu mencolok di bawah pantulan lidah api perapian."
    "Tulisan tangan di atas amplop itu diukir dengan tinta besi empedu hitam yang anggun, meliuk-liuk membentuk kaligrafi bangsawan era Victoria yang sempurna."

    $ temp_name = renpy.input("Ketik nama Anda (tekan Enter untuk memakai nama bawaan 'Guest'):", default="Guest", length=20).strip()
    if temp_name:
        $ mc_name = temp_name
    else:
        $ mc_name = "Guest"

    "Nama '[mc_name]' tertera jelas di atas permukaan perkamen yang berbau wangi mawar samar."

    "Di dalam surat itu tertulis kalimat singkat yang menghantui pikiranku sejak tiba di pos pos kereta api perbatasan:"
    "{i}'Kepada Tuan [mc_name]... Hutang masa lalu yang terlupakan menanti penebusan di balik dinding-dinding Rose Manor. Datanglah sebelum musim dingin mengunci lembah selamanya, atau biarkan ingatan keluargamu musnah ditelan ketiadaan.'{/i}"

    "Lelaki tua pemilik kedai melangkah mendekat dengan celemek kain linen cokelat kotor, membawakan semangkuk sup kentang panas dan sepotong roti gandum hitam."
    "Namun begitu pandangannya jatuh ke atas segel lilin mawar merah di atas mejaku, langkahnya mendadak membeku kaku di tempat."
    "Mangkuk sup di tangannya bergetar hebat hingga kuah panasnya tumpah membasahi lantai kayu cemara."

    innkeeper "Segel lilin itu... mawar berduri keluarga Rosewood..."

    mc "Kau mengenali lambang ini, Tuan Pemilik Kedai?"

    "Lelaki tua itu menoleh ke kanan dan kiri dengan cemas, memastikan para pelanggan lain di sudut kedai tidak mendengar percakapan kami."
    "Para peminum dan pemburu di meja seberang mendadak bungkam seribu bahasa. Mereka melirik sekilas ke arah amplop surat di hadapanku dengan mata membelalak ketakutan, lalu buru-buru menundukkan kepala, berbisik-bisik panik, dan menggeser bangku kayu mereka menjauh dari mejaku."
    "Pemilik kedai membungkuk rendah ke arahku, meletakkan mangkuk sup dengan tangan yang masih gemetar hebat, lalu berbicara dengan bisikan serak yang sarat ketakutan murni."

    innkeeper "Tuan muda... jika Anda masih menghargai keselamatan nyawa, masa depan, dan kewarasan akal budi Anda... lemparkan surat itu ke dalam perapian ini sekarang juga."
    innkeeper "Jangan pernah melangkah mendekati lembah kabut Rose Manor."

    menu:
        "Menanyakan alasan mendalam mengapa seluruh penduduk kota begitu ketakutan pada Rose Manor":
            $ evidence += 1
            mc "Mengapa seluruh kota ini seolah membeku setiap kali nama Rose Manor disebut? Apa yang sebenarnya terjadi di atas bukit itu?"
            innkeeper "Lembah itu terkutuk sejak seratus lima puluh tahun yang lalu, Tuan."
            innkeeper "Setiap beberapa tahun sekali, surat undangan bersegel mawar darah itu dikirimkan ke berbagai penjuru negeri."
            innkeeper "Para pelancong terhormat, seniman berbakat, sarjana universitas, dan pemuda bangsawan datang menunggangi kereta pos dengan rasa penasaran yang membara."
            innkeeper "Dan tidak ada satu pun dari mereka yang pernah kembali seperti sedia kala!"
            innkeeper "Jika ada yang beruntung ditemukan hidup di pinggir jalan hutan Ashwood beberapa pekan kemudian... mereka ditemukan dalam keadaan linglung tanpa ingatan sedikit pun."
            innkeeper "Mereka melupakan nama orang tua mereka, melupakan wajah kekasih mereka, dan bahkan tidak tahu siapa nama mereka sendiri ketika ditanya oleh pendeta desa."
            innkeeper "Tempat itu bukan sekadar rumah bangsawan, Tuan... Orang-orang tua di lembah ini menjulukinya {i}'Makam Kenangan'{/i}."
            innkeeper "Rumah itu memakan ingatan manusia laksana binatang buas memakan daging segar!"

        "Menanyakan siapa sosok yang saat ini menguasai Rose Manor":
            $ ser_trust += 1
            mc "Siapa yang menjadi tuan tanah di Rose Manor saat ini? Surat ini ditandatangani atas nama wangsa Rosewood."
            innkeeper "Hanya seorang nona bangsawan muda bernama Nona Seraphina Rosewood... dan seorang kepala pelayan wanita yang konon tidak pernah menua."
            innkeeper "Nona Seraphina jarang sekali menampakkan dirinya di kota ini. Terakhir kali ia terlihat di pasar bunga lima tahun lalu saat musim gugur."
            innkeeper "Wajahnya cantik jelita laksana patung pualam katedral, rambutnya seputih perak murni, namun matanya... sepasang matanya merah pekat bagai anggur tua."
            innkeeper "Orang-orang mengatakan bahwa garis keturunan Rosewood terikat oleh kutukan perjanjian darah kuno yang menuntut tumbal emosi manusia pada setiap generasi."
            innkeeper "Gadis itu tidak pernah tersenyum kepada siapa pun. Di balik kecantikannya yang memikat, ada hawa kematian yang membekukan darah siapa pun yang memandangnya."

        "Menegaskan tekad membaja bahwa aku harus pergi demi mengungkap misteri masa lalu keluargaku":
            $ ser_aff += 1
            $ ser_trust += 1
            mc "Aku tidak bisa memutar balik arah, Tuan. Surat ini menyinggung masa lalu keluargaku yang sengaja dihapus dari sejarah."
            mc "Aku harus pergi ke Rose Manor untuk memahami siapa diriku yang sebenarnya dan hutang apa yang menuntut darahku."
            innkeeper "Keberanian yang membuta sering kali merupakan pintu gerbang tercepat menuju liang kubur, Tuan muda."
            innkeeper "Namun jika tekad Anda sudah sekeras batu granit purba di puncak gunung... saya hanya bisa berdoa agar malaikat menjaga jiwa Anda dari kegelapan lembah mawar."
            innkeeper "Jangan pernah meminum anggur di rumah itu, jangan pernah menyentuh mawar di taman malam mereka, dan berdoalah agar Anda masih diizinkan melihat fajar kembali."

    "Tepat ketika pemilik kedai menyelesaikan peringatannya, pintu ganda kedai terhempas terbuka lebar oleh tiupan angin badai yang menderu dahsyat."
    "Hawa dingin bersalju menyapu masuk ke dalam ruangan, memadamkan beberapa lilin di meja makan dan membuat kobaran api perapian mendesis liar."
    "Sesosok pria bertubuh kekar melangkah masuk dari kegelapan badai malam."
    "Ia mengenakan mantel kulit hitam panjang yang basah kuyup oleh salju dan topi felt bertepi lebar yang ditarik rendah hingga menutupi separuh wajahnya."
    "Sebuah syal wol tebal melilit lehernya, hanya memperlihatkan sepasang mata kelabu dingin yang tak berkedip."

    coachman "Kereta kuda terakhir menuju perbatasan Hutan Ashwood telah siap di depan pelataran."
    coachman "Penumpang yang membawa surat bersegel mawar merah... waktumu telah tiba. Naiklah sekarang juga sebelum badai menutup jalan lintas bukit."

    mc "Itu kereta jemputanku."

    "Aku mengeluarkan beberapa keping koin perak dari saku celanaku, meletakkannya di atas meja kayu di samping cangkir tembaga, lalu menyampirkan mantel tebalku ke bahu."
    "Dengan surat undangan bersegel mawar tergenggam erat di dalam sakuku, aku melangkah keluar dari kehangatan kedai, menembus terpaan badai malam yang menusuk tulang."

    scene black
    with fade

    "Di luar kedai, sebuah kereta kuda hitam beratap tinggi telah menanti di tengah jalanan berlumpur beku."
    "Dua ekor kuda jantan hitam legam mendengus keras, menghembuskan uap putih panas dari lubang hidung mereka ke dalam udara malam yang membeku."
    "Lentera minyak kuningan yang tergantung di sisi kereta berayun liar tertiup angin, melemparkan bayang-bayang patah ke permukaan lumpur jalanan."

    "Begitu aku melangkah masuk ke dalam kabin kereta dan menutup pintunya, kusir kereta mencambuk tali kekang tanpa sepatah kata pun."

    scene bg_carriage_interior
    with fade

    "Roda-roda besi berderak keras melindas bebatuan terjal, melesat menembus pekatnya malam menuju Hutan Ashwood."

    "Perjalanan melintasi hutan belantara itu terasa seperti perjalanan menembus dunia orang mati."
    "Pepohonan pinus dan willow purba berdiri rapat di kedua sisi jalan setapak yang sempit, dahan-dahan hitamnya yang membeku membungkuk rendah ke arah kereta seperti jari-jari kurus raksasa yang hendak mencakar atap kabin."
    "Tidak ada suara burung malam, tidak ada suara serangga hutan—hanya derap kuku kuda yang berdentum monoton dan derak kayu kereta yang bergoyang hebat."

    "Beberapa kali melalui jendela kaca kabin yang buram oleh embun es, aku melihat pendaran kabut ungu tipis melayang di antara batang-batang pohon tua."
    "Di tengah kabut itu, bayangan-bayangan samar menyerupai sosok manusia tampak berdiri mematung di antara pepohonan, menatap kereta kami yang melintas dengan tatapan hampa."

    "Setelah hampir dua jam perjalanan yang melelahkan menembus hutan rimba, kereta mendadak melambat hingga akhirnya berhenti total dengan suara rem besi yang memekakkan telinga."

    coachman "Turunlah, Tuan."

    "Suara serak kusir kereta terdengar dingin dari balik jendela depan kabin."

    coachman "Perjanjian melarang keretaku melintasi gerbang besi ini. Jika Anda ingin menuju Rose Manor... langkahkan kaki Anda melewati jalan setapak di hadapan Anda."

    "Aku membuka pintu kereta dan melangkah turun ke atas tanah berbatu kerikil yang diselimuti lapisan es tipis."
    "Dan tepat di hadapanku... terbentang pemandangan yang membuat napas di tenggorokanku tercekat sesaat."

    scene bg_gate
    with fade

    play sound sfx_wind
    show snow_particles with dissolve

    "Sebuah gerbang besi tempa raksasa bergaya gotik menjulang setinggi lima meter di hadapanku."
    "Besi-besi hitam gerbang itu dipahat menyerupai jalinan sulur mawar berduri yang saling membelit erat, dengan patung dua kepala gargoyle bertaring tajam yang mencengkeram lambang perisai keluarga Rosewood di puncak lengkungannya."
    "Gerbang itu berdiri setengah terbuka, mengeluarkan derit logam panjang yang ngilu saat angin malam berhembus melaluinya."
    play sound sfx_creak

    "Di balik gerbang, jalan setapak berbatu marmer putih meliuk menaiki bukit di antara semak-semak mawar liar yang kering dan menghitam."
    "Dan di puncak bukit granit kelabu itu... berdiri Rose Manor."

    "Mansion gotik raksasa itu menjulang megah sekaligus menyeramkan laksana benteng kuno yang menantang langit malam."
    play sound sfx_thunder
    with hpunch
    "Menara-menara lancip beratap batu sabak hitam mencakar awan badai kelabu, sementara jendela-jendela berkaca patri lengkung memantulkan cahaya petir yang menyambar di kejauhan langit."
    "Hanya ada satu jendela di lantai dua yang memancarkan pendaran cahaya lilin keemasan yang hangat dan temaram."

    "Di belakangku, suara pecutan cambuk terdengar keras membelah malam."
    "Kereta kuda hitam itu memutar arah dengan tergesa-gesa dan melesat pergi meninggalkan gerbang, menghilang ke dalam pekatnya kabut hutan tanpa menoleh ke belakang sedikit pun."

    "Kini, aku berdiri sendirian di depan gerbang mawar berduri."
    "Tidak ada jalan untuk kembali. Hutan Ashwood telah tertutup oleh badai di belakangku, dan satu-satunya jalan menuju kebenaran adalah melangkah melewati gerbang besi ini."

    $ unlock_achievement("ach_invitation", "Undangan Terlarang")

    "Aku menarik napas panjang, merapatkan mantel tebalku, dan melangkahkan kakiku melewati ambang gerbang Rose Manor."
    "Malam pertama... resmi dimulai."

    hide snow_particles with dissolve
    jump night_1

