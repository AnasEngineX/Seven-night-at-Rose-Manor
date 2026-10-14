## story_night7.rpy
## Malam 7: The Final Rose (Kapel Bawah Tanah dan Klimaks Tujuh Malam)
## Naskah interaktif sastra gothic mystery dan romance mendalam

label night_7:
    $ night = 7

    scene black
    with fade

    "Malam ketujuh."
    "Malam terakhir di Rose Manor akhirnya tiba, membawa serta beban takdir yang telah tertimbun selama lebih dari satu abad."
    "Di luar dinding-dinding batu mansion yang menjulang dingin, seluruh alam semesta seolah-olah menahan napas dalam keheningan yang mencekam dan membekukan nadi."
    "Badai angin yang mengamuk sepanjang pekan mendadak lenyap tanpa bekas, meninggalkan atmosfer yang sunyi senyap—kesunyian yang lebih mengerikan daripada gemuruh petir terhebat."
    "Embun beku di dahan-dahan pohon willow menghitam di bawah kegelapan langit yang pekat tanpa setitik pun bintang, sementara kabut tebal merayap naik dari lembah mawar, mengepung Rose Manor laksana dinding penjara gaib."

    "Di dalam dadaku, detak jantungku berdegup kencang, suaranya menggema di dalam rongga tengkorakku seperti ketukan palu algojo."
    "Malam ini bukanlah malam untuk keraguan atau ketakutan."
    "Setiap langkah yang kuambil sejak menjejakkan kaki pertama kali di desa Ashwood telah membimbingku ke titik ini."

    "Di balik saku mantelku, seluruh bukti dan artefak yang kukumpulkan selama enam malam saling memancarkan getaran resonansi hangat yang beradu sengit dengan hawa dingin mansion:"
    "Mawar hitam abadi dari makam Lilith Vane di taman labirin;"
    "Liontin perak murni berukir mawar peninggalan Lady Eleanor yang diserahkan Seraphina;"
    "Diagram okultisme Sigillum Septem Foliorum yang dianalisis oleh Victoria Ashbourne;"
    "Serta Kunci Perak kuno milik Evelyn Hart yang telah menjaga gerbang kapel selama seratus empat puluh dua tahun."

    scene bg_manor_hall
    with fade

    "Aku melangkah melewati aula utama Rose Manor."
    "Lilin-lilin pada tempat lilin gantung raksasa tidak lagi menyala dengan cahaya kuning keemasan, melainkan berpendar dalam nyala api kemerahan yang temaram dan bergetar hebat."
    "Lukisan-lukisan leluhur Rosewood di sepanjang dinding seakan menundukkan kepala mereka dalam kebisuan yang khidmat, seolah menyaksikan barisan kematian seorang martir."

    "Di ambang pintu lorong pelayan di sayap selatan, gerbang besi tebal menuju ruang bawah tanah telah menganga lebar."
    "Dari kedalaman tanah, aroma dupa belerang purba, kemenyan hitam, dan wangi mawar merah yang begitu manis hingga memualkan menguar pekat ke udara."

    scene bg_ritual_chamber
    with fade
    play music bgm_ritual fadein 2.0

    "Aku melangkah menuruni undakan batu granit yang curam, memasuki perut bumi yang lembap dan dingin."
    "Di ujung lorong melingkar, gerbang besi berukir mawar berduri kini telah terbuka seutuhnya berkat kunci perak Evelyn."
    "Di baliknya terbentang Kapel Kuno Bawah Tanah—jantung sesungguhnya dari segala kutukan dan keabadian semu keluarga Rosewood."

    "Aula kapel itu memiliki kubah gotik raksasa yang disangga oleh pilar-pilar batu marmer hitam berkilap."
    "Ratusan lilin merah menyala di sepanjang ceruk-ceruk dinding dan undakan altar, meneteskan lilin merah kental yang menyerupai darah beku ke atas lantai batu."
    "Di lantai tengah kapel, terukir sebuah lingkaran segel raksasa dengan tujuh cabang mawar yang memancarkan pendaran cahaya merah tua berdenyut."
    "Akar-akar mawar gaib berwarna hitam legam menjalar keluar dari celah-celah retakan lantai marmer, berdenyut seirama dengan degup jantung raksasa yang terkubur di bawah tanah."

    "Dan tepat di hadapan altar marmer utama... berdiri Seraphina Rosewood."

    "Malam ini, ia mengenakan gaun upacara keluarga Rosewood yang paling megah dan paling mengerikan yang pernah kulihat:"
    "Beludru hitam pekat berhiaskan sulaman benang perak dan benang merah darah yang meliuk membentuk motif sulur berduri di seluruh kelim gaunnya."
    "Korsetnya yang ketat menonjolkan kerapuhan tubuhnya yang ramping, sementara jubah sutra panjangnya menyapu lantai altar laksana genangan malam abadi."
    "Rambut peraknya dibiarkan terurai bebas, berkilau pucat di bawah pantulan nyala lilin merah."
    "Dan di dadanya, bros mawar merah kristal menyala terang benderang—memancarkan aura merah tua yang menyilaukan dan berdenyut semakin cepat seiring mendekatnya waktu tengah malam."

    $ persistent.cg_ritual_climax = True
    scene cg_ritual_climax with dissolve

    "Di kedua tangannya yang gemetar berbalut sarung tangan sutra hitam, Seraphina memegang sebuah belati upacara bertatahkan batu delima darah."
    "Air mata bening mengalir di pipinya yang pucat pasi bagai pualam beku, memecah kesunyian dengan isak napas yang tertahan."

    ser "Kau benar-benar datang, Guest..."
    ser "Kupikir... aku setengah berharap kau melarikan diri ke dalam badai salju semalam, menunggangi kereta pos pertama dan tidak pernah menoleh ke belakang lagi."
    ser "Mengapa kau harus begitu keras kepala? Mengapa kau harus kembali ke tempat yang hanya menjanjikan kehancuran bagi jiwamu?!"

    mc "Karena aku menolak untuk melarikan diri, Seraphina. Aku telah berjanji padamu di depan perapian ruang dudukmu semalam."
    mc "Aku berjanji bahwa kau tidak akan menanggung kutukan ini seorang diri lagi. Dan aku tidak akan pernah meninggalkanmu di dalam kegelapan ini."

    "Mata merah anggur Seraphina bergetar hebat saat mendengar suaraku."
    "Ia melangkah mundur satu jengkal, menempelkan punggungnya pada pilar altar marmer."

    ser "Kau tidak mengerti betapa kejamnya kebenaran di tempat ini, Guest!"
    ser "Keluarga Rosewood tidak diberkahi oleh keabadian... kami dikutuk oleh rasa lapar entitas kehampaan yang terkubur di bawah kapel ini!"
    ser "Jika ritual ini tidak diselesaikan sebelum lonceng tengah malam berdentang tujuh kali... energi kehampaan akan meledak dari dalam segel!"
    ser "Seluruh tanah ini akan runtuh ke dalam jurang ketiadaan... kenangan orang tuaku, arwah para leluhurku, dan seluruh tubuh kita berdua akan musnah tanpa sisa!"
    ser "Hanya ada satu cara untuk meredakan rasa lapar kehampaan itu: mempersembahkan resonansi kenangan hidup dari seorang tamu yang murni ke dalam bros darah ini!"

    "Seraphina mengangkat belati perak itu dengan tangan yang gemetar hebat, mengarahkannya ke dadanya sendiri."

    ser "Selama sepuluh tahun, aku menyaksikan para tamu melupakan nama mereka dan berjalan keluar dari mansion ini sebagai cangkang kosong..."
    ser "Namun denganmu... aku tidak sanggup melakukannya. Setiap tawa yang kita bagi di rumah kaca, setiap percakapan kita di balkon menara... semuanya telah berakar di hatiku!"
    ser "Jika aku mengambil kenanganmu, aku akan membunuh jiwa pria yang kucintai... Namun jika aku membiarkan ritual ini gagal, kita berdua akan hancur lebur!"

    scene bg_ritual_chamber with dissolve
    show rose_petals with dissolve
    show seraphina mourning at sprite_center with dissolve

    "Langkah kaki tergesa yang bergema di tangga kapel memecah ketegangan."
    "Victoria Ashbourne melangkah cepat ke dalam ruangan dengan buku catatan okultismenya terbuka, diikuti oleh Evelyn Hart yang membawa lentera perak kuno."

    show victoria serious at sprite_left with dissolve
    show evelyn serious at sprite_right with dissolve

    vic "Turunkan belati itu, Seraphina! Jangan biarkan kebohongan ayahmu membunuhmu malam ini!"
    vic "Aku telah membedah seluruh catatan Profesor Arthur Ashbourne dan manuskrip terlarang Rosewood abad ke-18!"
    vic "Kehampaan di bawah tanah ini tidak membutuhkan tumbal ingatan manusia! Kehampaan ini tercipta karena kakek buyutmu, Jonathan Rosewood, mengkhianati Lilith Vane dan menyegel jiwanya hidup-hidup di dalam mawar darah demi keserakahannya sendiri!"
    vic "Ingatan para tamu yang kau serap selama ini hanyalah obat bius sementara yang memperpanjang siklus dendam Lilith!"

    show evelyn sad at sprite_right with dissolve

    eve "Dengarkan Nona Victoria, Nona Seraphina... Tolong dengarkan kami."
    eve "Saya telah berdiri di sisi altar ini selama seratus empat puluh dua tahun. Saya melihat Lord Jonathan meninggal dalam penyesalan yang membakar, dan saya melihat Lady Eleanor menangis darah sebelum ajal menjemputnya."
    eve "Keluarga Anda tidak perlu membayar utang darah itu selamanya. Kutukan ini bisa diakhiri... jika Anda berani melepaskan ketakutan Anda dan mempercayai orang-orang yang berdiri di hadapan Anda."

    "Seraphina menatap kami bergantian dengan sorot mata yang dipenuhi kebingungan dan kepedihan yang luar biasa mendalam."

    show seraphina surprised at sprite_center with dissolve

    "Di dadanya, bros mawar merah mulai berdengung nyaring, memancarkan gelombang kejut gaib yang mengguncang kapel."

    "Dan tepat pada saat itu, lonceng menara Rose Manor mulai berdentang keras di kejauhan langit malam:"

    play sound sfx_bell
    "{i}TENG...!{/i}"
    with vpunch

    "Dentangan pertama."
    "Tanah kapel bergetar hebat. Retakan-retakan di lantai marmer hitam melebar, memancarkan asap merah berbau belerang yang mencekik tenggorokan."

    play sound sfx_bell
    "{i}TENG...!{/i}"
    with hpunch

    "Dentangan kedua."
    "Lilin-lilin merah di dinding padam bergantian, menyisakan bayang-bayang hitam raksasa yang menari-nari liar di dinding kubah kapel."

    play sound sfx_bell
    "{i}TENG...!{/i}"
    with vpunch

    "Dentangan ketiga."
    "Sulur-sulur mawar berduri hitam merayap naik dengan cepat dari lantai, membelit pilar-pilar batu granit dan altar marmer."

    play sound sfx_bell
    "{i}TENG...!{/i}"
    with hpunch

    "Dentangan keempat."
    "Bisikan ribuan suara tanpa wujud memenuhi udara kapel—ratapan lirih dari puluhan tamu masa lalu yang kehilangan jati diri mereka di ruangan ini bergema laksana paduan suara keputusasaan."

    show seraphina serious at sprite_center with dissolve

    ser "Guest...! Loncengnya terus berdentang! Waktu kita hampir habis!"
    ser "Katakan padaku... apa yang harus kulakukan?! Apa pilihan kita di hadapan takdir ini?!"

    play sound sfx_bell
    "{i}TENG...!{/i}"
    with vpunch

    "Dentangan kelima."
    "Aura merah darah dari bros mawar Seraphina membubung tinggi ke langit-langit kubah, membentuk pusaran kelopak mawar berdarah yang berputar kencang."

    play sound sfx_bell
    "{i}TENG...!{/i}"
    with hpunch

    "Dentangan keenam."
    "Dunia di sekitar kami serasa membeku di ambang jurang kehancuran. Tinggal satu dentangan terakhir sebelum segel ketujuh terkunci selamanya atau pecah menelan segalanya."

    menu:
        "Mempercayai ketulusan cinta Seraphina, melangkah maju menaiki altar, dan merengkuh tubuhnya ke dalam pelukan hangat":
            "Aku tidak mempedulikan belati perak di tangan Seraphina ataupun pusaran angin dingin yang merobek udara kapel."
            "Dengan langkah mantap dan tanpa ragu, aku menaiki undakan marmer hitam altar dan melangkah langsung ke hadapan sang pewaris Rosewood."
            "Aku mengulurkan kedua tanganku, meraih pergelangan tangannya yang gemetar, dan menarik tubuhnya yang rapuh ke dalam dekapan dadaku."

            mc "Aku percaya padamu seutuhnya, Seraphina. Bahkan jika seluruh kenangan di dunia ini harus terhapus, satu hal yang tidak akan pernah hilang adalah perasaanku kepadamu."
            mc "Kutukan ini tidak akan memisahkan kita. Jika kau harus menghadapi kegelapan, maka kita akan menghadapinya bersama-sama sebagai satu jiwa!"

            "Mata Seraphina terbelalak menatapku dari jarak yang begitu dekat."

            show seraphina surprised at sprite_center with dissolve

            "Jemarinya melemas, dan belati upacara perak terlepas dari genggamannya, berdenting nyaring saat jatuh membentur lantai batu."
            "Kedua tangannya melingkar erat di leherku, air matanya membasahi pundak mantelku saat ia membenamkan wajahnya di dadaku."

            show seraphina sad at sprite_center with dissolve

            ser "Guest... oh Tuhan, Guest...!"
            ser "Aku tidak ingin kehilanganmu... Aku ingin hidup... Aku ingin melihat dunia luar bersamamu...!"

            "Bros mawar merah di dadanya bersinar dengan cahaya crimson yang luar biasa menyilaukan."
            "Gelombang energi mawar darah membungkus tubuh kami berdua dalam kepompong cahaya merah muda yang hangat, menahan amukan pusaran kehampaan."

            show seraphina smile at sprite_center with dissolve

            play sound sfx_bell
            "{i}TENG...!{/i}"
            "Dentangan ketujuh berdentang, membelah keheningan dengan resonansi akhir."

            if ser_aff >= 3 and ser_trust >= 3:
                "Kehangatan cinta dan kepercayaan mutlak yang kami bagi beresonansi melawan energi dingin kutukan, mengubah arus kehampaan menjadi denyut kehidupan yang murni."
                jump good_ending
            else:
                "Namun ikatan di antara kami belum cukup kuat untuk menahan dahsyatnya pusaran kehampaan yang telah menumpuk selama ratusan tahun..."
                jump bad_ending

        "Mengangkat seluruh bukti, menancapkan mawar hitam Lilith ke inti segel, dan mematahkan ritual selamanya":
            "Aku melangkah maju dengan keyakinan membaja ke tengah lingkaran segel altar."
            "Dari dalam mantelku, aku mengeluarkan mawar hitam abadi dari makam Lilith, kunci perak Evelyn, dan diagram okultisme Victoria."

            mc "Ritual berdarah ini berakhir malam ini juga, Seraphina! Hentikan pengorbanan ini!"
            mc "Lilith Vane tidak pernah menginginkan kematianmu atau darah para tamu! Arwahnya hanya terperangkap dalam kesedihan dan pengkhianatan masa lalu!"

            "Aku menoleh ke arah Victoria dan Evelyn."
            mc "Victoria, aktifkan polaritas pilar! Evelyn, putar segel peraknya!"

            show victoria serious at sprite_left with dissolve

            vic "Dipahami! Aliran resonansi dialihkan ke fondasi bumi!"

            show evelyn serious at sprite_right with dissolve

            eve "Atas nama sumpah darah seratus empat puluh tahun... lepaskanlah belenggu ini!"

            "Cahaya ungu keperakan yang agung mendadak meledak di tengah kapel, mengusir kabut merah darah yang pekat."
            "Di samping altar marmer, sosok Lilith Vane mewujud secara utuh—bukan lagi sebagai bayangan hantu yang meratap di taman mawar, melainkan sebagai wanita bangsawan anggun bergaun putih dengan senyuman penuh kedamaian."

            show lilith smile at sprite_mid_left with dissolve

            "Lilith melangkah lembut ke arah Seraphina dan meletakkan tangannya yang bercahaya ke atas pundak Seraphina."

            lil "Cucu Jonathan... kau telah memikul dosa yang bukan milikmu terlalu lama."
            lil "Aku memaafkan Jonathan... dan aku membebaskanmu dari sangkar mawar ini."

            show seraphina surprised at sprite_center with dissolve

            "Aku menancapkan tangkai mawar hitam Lilith tepat ke rongga segel ketujuh di tengah altar batu, lalu memasukkan Kunci Perak Evelyn ke pusat lingkaran dan memutarnya sekuat tenaga!"
            "{i}KLIK...!{/i}"

            play sound sfx_bell
            "{i}TENG...!{/i}"
            "Dentangan ketujuh berdentang menggelegar di seluruh penjuru langit Rose Manor!"

            if evidence >= 5 and lilith_truth and victoria_alliance:
                play sound sfx_break
                "Simbol-simbol segel berdarah pecah berkeping-keping menjadi debu kristal keemasan yang berhamburan ke udara, melenyapkan kutukan Rose Manor untuk selamanya."
                jump true_ending
            else:
                "Namun salah satu kepingan bukti penting masih belum terhubung dengan sempurna, membuat segel tidak stabil dan meledak tanpa kendali..."
                jump bad_ending

        "Ragu-ragu, terdiam membeku karena ketakutan saat melihat amukan energi gaib":
            "Lututku lemas dan tubuhku terasa kaku membeku laksana batu nisan."
            "Pemandangan amukan pusaran merah darah, bisikan arwah, dan pendaran mata Seraphina membuat akal sehatku lumpuh seketika."
            "Aku tidak mampu melangkah, tidak mampu berbicara, dan hanya bisa berdiri terpaku menyaksikan kehancuran yang tak terelakkan."

            show seraphina surprised at sprite_center with dissolve

            ser "Guest...?! Tidak... tolong, jangan diam saja...!"

            play sound sfx_bell
            "{i}TENG...!{/i}"
            "Dentangan ketujuh lonceng menara berdentang mematikan."
            "Energi kehampaan yang tak terkendali meledak dari dalam lantai altar, menelan seluruh ruangan dalam gelombang kegelapan pekat."

            jump bad_ending

