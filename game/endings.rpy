## endings.rpy
## Rute dan Adegan Akhir Mendalam Seven Nights at Rose Manor (Tiga Ending Utama dan Epilog)
## Naskah interaktif sastra gothic mystery dan romance mendalam

## =========================================================================
## GOOD ENDING: MEKARNYA BUNGA HARAPAN (The Scarlet Bond)
## =========================================================================
label good_ending:
    stop music fadeout 1.5
    scene black with fade
    play sound sfx_bell
    "Lonceng ketujuh berdentang membelah langit malam Rose Manor dengan gaung yang menggetarkan langit dan bumi..."
    "{i}TENG...!{/i}"

    "Gelombang energi crimson yang dahsyat meledak dari dalam bros mawar kristal di dada Seraphina."
    "Pusaran angin panas berbau mawar merebak kencang di seluruh penjuru kapel bawah tanah, menerbangkan ratusan kelopak bunga layu dan memadamkan lilin-lilin merah."
    "Namun di tengah pusaran badai energi yang membutakan itu, pelukan kami di atas undakan altar tidak pernah terlepas barang satu inci pun."
    "Dekapan kedua tanganku di tubuhnya, kehangatan napas yang kami bagi, dan ketulusan janji suci yang telah kuikrarkan di hadapannya menjadi perisai jiwa tak kasat mata yang menahan amukan resonansi kehampaan."

    ser "Guest... aku bisa merasakan denyut jantungmu... Aku bisa merasakan kehangatanmu...!"
    mc "Pegang aku erat-erat, Seraphina! Jangan lepaskan! Kita akan menembus malam ini bersama-sama!"

    "Perlahan namun pasti, denyut merah darah yang liar dari bros mawar di dadanya mulai melunak."
    "Warna merah pekat yang mengancam itu perlahan mencair menjadi pendaran cahaya merah muda lembut yang menyejukkan hati laksana embun fajar musim semi."
    "Akar-akar mawar hitam berduri yang membelit pilar-pilar marmer hitam merenggang, mengering, lalu luruh menjadi debu keemasan berkilauan yang melayang damai di udara kapel."
    "Getaran gempa gaib di bawah lantai marmer mereda seutuhnya, menyisakan keheningan yang agung dan menenangkan."

    scene bg_manor_hall with fade
    play music bgm_manor fadein 2.5

    "Kami melangkah perlahan menaiki undakan tangga batu, keluar dari kegelapan ruang bawah tanah kembali ke aula utama Rose Manor."
    "Di luar jendela-jendela berkubah tinggi, badai salju dan petir yang telah mencekam bukit Ashwood selama berhari-hari kini telah lenyap tanpa bekas."
    "Langit malam kelabu perlahan memudar dari hitam pekat menjadi warna biru safir yang jernih dan tenang, ditaburi jutaan bintang berkilauan yang memantul di lantai marmer aula."

    show seraphina neutral with dissolve

    "Seraphina berdiri di hadapanku di bawah temaram cahaya lampu gantung kristal aula."
    "Dengan jemari yang tenang dan tanpa getaran ketakutan lagi, ia melepaskan bros mawar merah dari bagian dada gaun upacaranya."
    "Benda itu terbaring di atas telapak tangannya—kristal mawar itu tidak lagi dingin, tidak lagi berbau darah atau memancarkan radiasi kehampaan."
    "Kini, bros itu tampak seperti permata delima biasa yang berkilau hangat dan damai."

    ser "Kutukan itu... akhirnya berhasil diredakan."
    ser "Selama ratusan tahun, para leluhurku mengira mereka harus memberi makan kehampaan di bawah tanah dengan ingatan dan jiwa para tamu karena ketakutan mereka sendiri akan kematian dan kehancuran."
    ser "Namun malam ini... kau membuktikan bahwa ikatan cinta yang tulus dan keberanian moral jauh lebih kuat daripada kutukan mana pun."
    ser "Kau tidak membiarkanku menjadi monster, Guest... Kau menyelamatkanku dari diriku sendiri."

    mc "Kau tidak pernah menjadi monster, Seraphina. Kau adalah jiwa yang terluka dan terkurung di dalam sangkar batu."
    mc "Kau tidak perlu lagi hidup dalam ketakutan akan malam kedelapan atau kedatangan para tamu yang akan kau lukai. Tujuh malam berdarah itu telah berakhir selamanya."

    "Air mata haru membasahi kedua pipi Seraphina saat sebuah senyuman tulus—senyuman termanis dan paling menawan yang pernah kulihat seumur hidupku—terukir di bibirnya."
    show seraphina smile with dissolve
    "Ia melangkah maju, melingkarkan kedua tangannya di leherku dan membenamkan wajahnya di lekuk pundakku, membiarkan helai rambut peraknya membelai pipiku."

    ser "Terima kasih, cintaku... Terima kasih karena telah mempercayaiku di saat aku sendiri hampir menyerah pada keputusasaan rumah ini."
    ser "Mulai detik ini... Rose Manor bukan lagi penjara dingin bagiku. Di mana pun kau berada, di situlah rumah dan hidupku."

    "Dari sudut koridor sayap timur, Evelyn Hart melangkah maju dengan nampan perak berisi dua cangkir teh manis beraroma melati."
    "Untuk pertama kalinya dalam seratus empat puluh dua tahun pengabdiannya, seulas senyuman tulus dan hangat terbit di wajah sang kepala pelayan."

    show evelyn smile with dissolve

    eve "Selamat datang di kehidupan yang baru, Nona Seraphina, Tuan Guest."
    eve "Malam telah berlalu, dan sarapan pagi yang hangat telah dipersiapkan di ruang makan beranda yang disinari mentari."

    "Di luar jendela kaca, untuk pertama kalinya dalam sejarah wangsa Rosewood, seberkas sinar matahari pagi yang hangat dan keemasan merayapi pucuk-pucuk menara gotik."
    "Semak-semak mawar di pekarangan mekar dengan kelopak merah segar dan keharuman murni, menyambut datangnya musim semi baru di dalam hati kami berdua."

    show rose_petals with dissolve
    $ persistent.ending_good = True
    $ unlock_achievement("ach_trust", "Kepercayaan Sang Mawar")
    $ unlock_achievement("ach_affection", "Kuncup Bunga Kasih")
    $ if (persistent.cg_first_meeting and persistent.cg_balcony_promise and persistent.cg_piano_duet and persistent.cg_ritual_climax and persistent.cg_dawn_embrace and persistent.cg_hollow_cycle): unlock_achievement("ach_collector", "Kolektor Memori Abadi")

    call good_ending_epilogue
    "[[Tamat - Good Ending: Mekarnya Bunga Harapan]"
    return

## =========================================================================
## BAD ENDING: SIKLUS ABADI (The Hollow Cycle)
## =========================================================================
label bad_ending:
    stop music fadeout 1.0
    scene black with fade
    play sound sfx_bell
    play music bgm_night fadein 2.0
    "Lonceng ketujuh berdentang membelah kesunyian malam dengan gema logam yang dingin, pekat, dan mematikan..."
    "{i}TENG...!{/i}"

    "Pusaran angin es membekukan seketika menyembur keluar dari retakan altar kapel bawah tanah."
    "Aura kehampaan meledak tanpa ada kendali atau penangkal yang mampu menahannya."
    "Rantai-rantai sulur mawar hitam berduri melesat cepat dari celah lantai marmer, membelenggu kedua kaki, tangan, dan tubuhku dengan cengkeraman duri beracun yang membakar darah."

    show seraphina neutral with dissolve

    "Di hadapanku, Seraphina berdiri terpaku di depan altar dengan mata membelalak ketakutan dan air mata yang mengalir deras membasahi pipinya."

    ser "Guest...! Tidak...! Maafkan aku... kumohon maafkan aku...!"
    ser "Altar ini menuntut bayarannya... Resonansi kehampaan ini terlalu lapar untuk dihentikan...!"

    "Bros mawar merah di dada Seraphina menyala laksana matahari darah yang menyilaukan dan membakar retina mataku."
    "Sebuah gaya tarik gaib yang luar biasa dahsyat menyedot rongga kepalaku, merobek dinding-dinding kesadaranku satu per satu."

    "Perlahan... ingatan hidupku mulai terkelupas bagai abu yang ditiup angin badai."
    "Wajah ayah dan ibuku... kenangan masa kecilku saat berlari di padang rumput hijau... nama kota kelahiranku... aroma masakan rumah..."
    "Semuanya tersedot ke dalam pusaran kelopak mawar merah yang berputar di depan altar."
    "Bahkan nama diriku sendiri... kini memudar menjadi hamparan kabut putih yang dingin dan hampa."

    mc "Siapa... siapa sebenarnya diriku...?"
    mc "Mengapa... mengapa aku berdiri di ruangan gelap ini...?"

    voice_unknown "Siklus mawar membutuhkan ingatan manusia yang murni untuk terus memperpanjang napasnya."
    voice_unknown "Dan malam ini... seluruh ingatan hidupmu adalah persembahan abadi berikutnya bagi fondasi Rose Manor."

    "Sosok Seraphina di hadapanku memudar perlahan menjadi siluet kabur yang buram di balik air mata."
    "Suara isak tangisnya yang memilukan terdengar semakin jauh, semakin lirih, hingga akhirnya ditelan seutuhnya oleh kegelapan abadi tanpa batas."

    "..."
    "..."
    "..."

    call bad_ending_epilogue

    scene bg_gate with fade
    "Rintik hujan es yang dingin dan menusuk pipi perlahan membangunkanku dari ketidaksadaran yang panjang."
    "Aku mendapati diriku berdiri mematung di atas jalan setapak berbatu kerikil berlumpur di pinggiran Hutan Ashwood."
    "Kabut kelabu tebal merayap di permukaan tanah basah, menyembunyikan pepohonan pinus yang meranggas kaku."

    "Di hadapanku, gerbang besi tempa raksasa bergaya gotik berdiri menjulang tinggi dan angkuh menantang langit badai."
    "Puncak-puncak menara kastil Rose Manor mencakar awan mendung di kejauhan bukit granit."

    "Di tanganku yang basah kuyup dan kaku kedinginan, sepucuk surat tebal dengan stempel lilin merah berbentuk mawar berduri tergenggam erat."

    mc "Tujuh malam di Rose Manor... Mengapa aku memegang surat undangan ini di tanganku?"
    mc "Siapa yang mengundangku ke tempat terkutuk ini... dan siapa namaku yang sebenarnya?"

    $ persistent.cg_hollow_cycle = True
    $ persistent.ending_bad = True
    $ if (persistent.cg_first_meeting and persistent.cg_balcony_promise and persistent.cg_piano_duet and persistent.cg_ritual_climax and persistent.cg_dawn_embrace and persistent.cg_hollow_cycle): unlock_achievement("ach_collector", "Kolektor Memori Abadi")
    scene cg_hollow_cycle with dissolve

    play sound sfx_creak
    "Gerbang besi kuno di depanku perlahan berderit membuka sendiri tanpa ada yang mendorongnya, mengeluarkan suara logam ngilu yang menyambut mangsa barunya."
    "Siklus tujuh malam kembali berulang dari titik nol... dalam lingkaran kutukan keabadian tanpa akhir."

    "[[Tamat - Bad Ending: Siklus Abadi]"
    return

## =========================================================================
## TRUE ENDING: FAJAR DI ROSE MANOR (The Bloom of Eternal Dawn)
## =========================================================================
label true_ending:
    stop music fadeout 1.0
    scene black with fade
    play sound sfx_bell
    play sound sfx_break
    "Dentangan lonceng ketujuh berdentang menggelegar bersamaan dengan suara retakan kristal purba yang memekakkan telinga..."
    "{i}TENG...! KRAAAK...!{/i}"

    "Tangkai mawar hitam abadi dari nisan Lilith Vane yang kutancapkan tepat ke pusat rongga segel ketujuh bereaksi secara instan terhadap putaran Kunci Perak Evelyn."
    "Cahaya ungu keperakan yang luar biasa agung dan terang benderang meledak dari tengah altar batu marmer hitam."
    "Pilar cahaya suci itu menembus kubah kapel bawah tanah, membubung tinggi ke angkasa malam laksana pedang perak yang membelah kegelapan langit badai."

    "Energi darah dan resonansi kehampaan yang selama lebih dari satu abad membelenggu dan menghisap kehidupan di Rose Manor ditarik mundur secara paksa ke dalam kelopak mawar hitam."
    "Warna hitam pekat kelopak mawar itu perlahan terkelupas dan luruh, berganti menjadi warna putih salju yang suci, murni, dan berpendar cemerlang tanpa noda setitik pun!"

    scene bg_rose_garden with fade
    play music bgm_dawn fadein 3.0

    "Gelombang kejut cahaya murni menyapu seluruh pekarangan dan lorong-lorong Rose Manor."
    "Kabut beracun yang selama seratus empat puluh tahun mengurung taman labirin mawar tersapu bersih oleh hembusan angin segar pegunungan yang harum dan menyejukkan."

    "Di tengah taman mawar, tepat di dekat batu nisan marmer kuno yang kini terbebas dari lumut hitam, sosok Lilith Vane berdiri mewujud secara sempurna."
    "Gaun sutra gadingnya berkilau cemerlang di bawah pancaran semburat fajar pertama."
    "Sepasang mata violetnya menatap Seraphina dan diriku dengan kedamaian abadi yang tak terhingga."

    show lilith smile with dissolve

    lil "Seratus tiga puluh tahun aku tertidur dalam duka, pengkhianatan, dan dilupakan oleh dunia fana..."
    lil "Namun malam ini, kebenaran telah membebaskanku. Janji cinta dan penyesalan keluarga Rosewood akhirnya ditebus lunas oleh keberanian kalian."
    lil "Terima kasih, Guest... Terima kasih, Seraphina. Hiduplah dalam cahaya fajar yang sesungguhnya."

    hide lilith with dissolve

    "Sosok Lilith tersenyum manis dengan tatapan penuh berkah, lalu tubuhnya perlahan berubah menjadi ribuan butiran cahaya ungu keemasan yang menari-nari naik menuju langit biru fajar sebelum menghilang damai ke alam baka."

    show victoria smile with dissolve
    vic "Luar biasa... Sungguh fenomena ilmiah dan metafisika yang menakjubkan!"
    vic "Resonansi anomali ini ternetralkan seutuhnya tanpa meninggalkan residu kehampaan di bawah fondasi tanah!"
    vic "Catatan ekspedisi kakekku akhirnya menemukan bab penutupnya yang paling mulia dan sempurna."

    "Victoria menutup buku catatannya dengan senyum kepuasan intelektual yang mendalam, lalu menepuk pundakku dengan penuh rasa hormat."

    "Di samping kami, Evelyn Hart menatap kedua telapak tangannya dengan tatapan takjub dan haru."
    "Rantai perak sumpah darah yang membeban lehernya selama lebih dari satu abad telah hancur menjadi debu perak yang diterbangkan angin fajar."

    show evelyn smile with dissolve

    eve "Sumpah darah itu... telah lunas. Saya bebas dari belenggu ratusan tahun ini."
    eve "Namun jika Nona Seraphina dan Tuan Guest berkenan mengizinkan... saya tetap ingin mengabdi di kediaman ini sebagai manusia merdeka yang memiliki pilihannya sendiri."

    show seraphina dawn with dissolve

    "Seraphina melangkah mendekatiku di antara semak-semak mawar merah yang kini bermekaran dengan keharuman yang segar, alami, dan bebas dari racun ilusi."
    "Rambut peraknya yang panjang berkilau keemasan disinari fajar pertama yang menembus cakrawala bukit Ashwood."
    "Di dadanya, bros mawar merah kristal telah bertransformasi seutuhnya menjadi kuntum mawar putih perak yang mekar abadi—lambang pembebasan, kemurnian cinta, dan awal dari era baru."

    ser "Fajar... fajar yang sesungguhnya akhirnya menyinari Rose Manor."
    ser "Seluruh kenangan masa laluku kini utuh, dan tidak ada lagi jiwa yang harus dikorbankan untuk mempertahankan rumah ini."

    mc "Kutukan itu telah hancur selamanya, Seraphina. Masa depan Rose Manor kini sepenuhnya berada di tangan kita."

    show rose_petals with dissolve
    $ persistent.cg_dawn_embrace = True
    $ persistent.ending_true = True
    $ unlock_achievement("ach_curse_breaker", "Pembebas Kutukan Abadi")
    $ unlock_achievement("ach_trust", "Kepercayaan Sang Mawar")
    $ unlock_achievement("ach_affection", "Kuncup Bunga Kasih")
    $ if (persistent.cg_first_meeting and persistent.cg_balcony_promise and persistent.cg_piano_duet and persistent.cg_ritual_climax and persistent.cg_dawn_embrace and persistent.cg_hollow_cycle): unlock_achievement("ach_collector", "Kolektor Memori Abadi")
    scene cg_dawn_embrace with dissolve

    "Seraphina menatapku dengan sepasang matanya yang merah anggur, kini memancarkan kehangatan cinta yang membara dan damai."
    "Jari-jarinya yang lembut menyelinap di antara jemariku, menautkan tangan kami erat di bawah siraman cahaya mentari pagi yang hangat."

    ser "Bukan hanya masa depan mansion ini, cintaku... tetapi masa depan hidup kita berdua."
    ser "Tujuh malam telah berakhir. Dan hari ini... adalah awal dari selamanya."

    call true_ending_epilogue
    "[[Tamat - True Ending: Fajar di Rose Manor]"
    return

