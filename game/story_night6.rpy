## story_night6.rpy
## Malam 6: The Seventh Seal (Ruang Bawah Tanah dan Kunci Perak Evelyn)
## Naskah interaktif sastra gothic mystery mendalam

label night_6:
    $ night = 6

    scene black
    with fade

    "Malam keenam tiba bagaikan bayang-bayang algojo berkerudung hitam yang mendekati tiang gantungan di bawah langit kelabu pekat."
    "Udara di seluruh koridor Rose Manor terasa begitu pekat, berat, dan bermuatan listrik statis gaib yang membuat bulu kuduk meremang."
    "Cahaya lilin di tempat-tempat lilin perak di sepanjang dinding aula bergetar liar tanpa hembusan angin sedikit pun, melemparkan bayang-bayang panjang yang meliuk-liuk aneh di atas karpet marun laksana monster bertangan banyak."
    "Bahkan detak pendulum jam menara di kejauhan terdengar semakin cepat dan tidak beraturan—suara logam berat beradu ritmis yang mengumumkan bahwa waktu bagi mereka yang hidup di rumah ini semakin menipis."

    scene bg_guest_room
    with fade
    play sound sfx_fire

    "Sebelum melangkah keluar menembus dinginnya lorong menuju ruang bawah tanah, aku menyalakan lentera minyak dan menggelar seluruh barang bukti yang telah kukumpulkan di atas meja mahoni kamar tamuku."
    "Di bawah temaram cahaya api perapian dan lentera kuningan, kepingan-kepingan teka-teki yang tersebar selama lima malam terakhir kini terbentang di hadapanku."
    "Waktunya untuk menghubungkan setiap benang merah sebelum menuruni ruang bawah tanah:"

label night6_investigation_desk:
    menu:
        "Menganalisis Dokumen Sejarah (Surat Undangan & Buku Tamu 1884)":
            call inspect_clue("invitation_letter")
            call inspect_clue("guestbook_1884")
            "Surat undangan yang membawaku ke mansion ini dan buku tamu tahun 1884 membuktikan bahwa Evelyn Hart telah menjaga siklus ini selama lebih dari satu abad."
            "Para tamu diundang bukan karena kebetulan, melainkan karena resonansi ingatan mereka dibutuhkan untuk memperpanjang napas Rose Manor."
            jump night6_investigation_desk

        "Menghubungkan Tragedi Lilith Vane (Partitur Nocturne & Surat Cinta 1892)":
            call inspect_clue("nocturne_score")
            call inspect_clue("love_letters_1892")
            "Partitur musik Lilith dan surat penyesalan Jonathan membuktikan bahwa kutukan ini lahir dari keputusasaan cinta dan pengorbanan yang dipaksakan."
            "Lilith tidak ingin membalas dendam dengan menumpahkan darah Seraphina—arwahnya hanya merindukan kebenaran dan pengampunan atas sumpah darah masa lalu."
            jump night6_investigation_desk

        "Meneliti Pusaka Mistis Mawar (Bros Mawar Seraphina & Mawar Hitam Lilith)":
            call inspect_clue("rose_brooch")
            call inspect_clue("black_rose")
            "Bros mawar merah Seraphina bertindak sebagai wadah penampung energi memori, sementara mawar hitam makam Lilith adalah jangkar katarsis."
            "Jika mawar hitam ditancapkan tepat ke pusat segel di hadapan altar, kelebihan resonansi dapat diserap kembali tanpa menghancurkan jiwa Seraphina."
            jump night6_investigation_desk

        "Mempelajari Rencana Pembalikan Segel (Diagram Okultisme Victoria & Liontin Eleanor)":
            call inspect_clue("seal_diagram")
            call inspect_clue("silver_locket")
            "Diagram Victoria memetakan aliran polaritas enam pilar mawar, sementara liontin perak pemberian Seraphina akan menjadi perisai batinku dari ilusi kehampaan."
            "Kunci terakhir yang masih belum ada di tanganku adalah mekanisme pembuka gerbang kapel inti: Kunci Perak kuno milik Evelyn Hart."
            jump night6_investigation_desk

        "Menyimpulkan Seluruh Deduksi dan Bersiap Turun ke Ruang Bawah Tanah":
            $ evidence += 1
            "Seluruh benang merah penyelidikan kini telah tersusun utuh di kepalaku."
            "Aku memasukkan kembali artefak-artefak dan dokumen penting ke balik mantel tebalku, lalu melangkah keluar kamar."

    scene bg_manor_hall
    with dissolve

    "Aku melangkah menuruni tangga aula utama dalam kegelapan pekat, berhati-hati agar tidak menimbulkan suara decit di atas anak-tangga kayu ek."
    "Di sayap selatan mansion, tepat di balik lorong dapur pelayan yang remang-remang, terdapat sebuah pintu ganda berbahan kayu ek tebal yang dilapisi pelat besi berkarat."
    "Pintu itu—yang selama lima hari terakhir selalu terkunci rapat dengan rantai gembok kuno—malam ini tampak sedikit renggang, meninggalkan celah selebar dua jari tangan."

    "Dari celah pintu itu, mengalir keluar hawa dingin yang menusuk hingga ke sumsum tulang, bercampur dengan aroma tajam dupa belerang purba, lumut tanah basah, dan wangi mawar kering yang telah membusuk."

    scene bg_ritual_chamber
    with fade
    play music bgm_ritual fadein 2.5
    show rose_petals with dissolve

    "Aku melangkah melewati ambang pintu dan menuruni undakan batu granit yang curam dan melingkar menuju perut bumi."
    "Dinding-dinding lorong bawah tanah terbuat dari susunan batu granit hitam kasar peninggalan abad pertengahan, basah oleh tetesan air rembesan tanah dan ditumbuhi lumut kelabu yang licin."
    "Suara tetesan air dari langit-langit kubah batu bergema ritmis di dalam kesunyian yang membatu:"
    "{i}Tik... Tik... Tik...{/i}"

    "Di ujung tangga melingkar, lorong sempit itu mendadak terbuka ke sebuah aula bawah tanah berkubah raksasa yang menakjubkan sekaligus mengerikan."
    "Fondasi arsitektur ruangan ini tampaknya berasal dari reruntuhan kapel ksatria kuno berabad-abad sebelum Rose Manor dibangun di atasnya."
    "Enam pilar batu marmer hitam berdiri kokoh mengelilingi sebuah lingkaran segel raksasa yang diukir di tengah lantai marmer bertatahkan simbol-simbol alkimia latin."
    "Di atas setiap pilar, sebuah cawan perak berisi bunga mawar merah yang telah layu menghitam memancarkan asap tipis berwarna ungu keemasan yang berbau manis menusuk hidung."
    "Garis-garis ukiran segel di lantai berdenyut redup dengan cahaya keunguan yang suram, memancarkan gravitasi gaib yang membuat setiap tarikan napas terasa sesak dan berat."

    "Di ujung lingkaran segel, tepat di depan gerbang besi raksasa berpahat sulur mawar berduri yang memisahkan aula ini dari kapel inti, berdiri sesosok wanita bertubuh tegap."
    "Sebuah lentera minyak bertengger di atas peti batu di sampingnya, sementara wanita itu sibuk memeriksa mekanisme gembok gerbang dengan kaca pembesar perak dan jangka ukur besi."

    vic "Langkah kakimu terlalu berat untuk seorang pencuri malam, Guest."

    "Victoria Ashbourne tidak menoleh saat berbicara. Jemarinya yang ramping dan terampil terus mencatat angka-angka koordinat okultisme ke dalam buku catatannya yang bersampul kulit hitam tebal."

    mc "Victoria. Aku tidak menyangka kau sudah berada di sini mendahuluiku."

    show victoria neutral with dissolve
    "Victoria berbalik perlahan, merapikan letak kacamatanya dengan senyuman tipis yang tajam namun dipenuhi kepuasan intelektual."
    "Meskipun lingkaran hitam tebal di bawah matanya menunjukkan bahwa ia belum memejamkan mata selama puluhan jam, tatapan matanya tetap tajam laksana elang pemburu."

    vic "Aku menghabiskan seluruh siang tadi membedah rancangan saluran drainase bawah tanah manor dari arsip yayasan tahun 1780."
    vic "Saluran pembuangan air hujan di sudut perpustakaan terhubung langsung dengan rongga kubah ruangan ini. Bagi seorang peneliti yang bertekad, lorong sempit berdebu bukanlah rintangan yang berarti."

    "Victoria melangkah mendekati lingkaran enam pilar batu dan memberi isyarat padaku untuk melihat lebih dekat."

    vic "Perhatikan susunan enam pilar ini, Guest. Ini adalah manifestasi fisik dari enam malam pertama ritual."
    vic "Setiap malam seorang tamu tidur di Rose Manor, resonansi emosional dan ingatannya diserap oleh mansion melalui makanan, teh, aroma mawar, dan kontak emosional dengan sang nyonya rumah."
    vic "Enam pilar ini telah terisi penuh oleh energimu. Lihat bagaimana kelopak mawarnya telah menghitam sempurna dan memancarkan radiasi kehampaan."
    show victoria serious with dissolve
    vic "Tinggal satu pilar terakhir: Segel Ketujuh yang berada tepat di tengah altar kapel di balik gerbang besi berduri ini."

    mc "Dan gerbang besi ini... apakah kau berhasil membukanya?"

    "Victoria menghela napas pendek dan menggelengkan kepalanya dengan sedikit rasa frustrasi yang langka."

    vic "Mekanisme penguncian gerbang ini adalah karya pandai besi alkimia abad ke-17. Menggunakan empat lapis silinder perak yang digerakkan oleh resonansi darah Rosewood."
    vic "Tidak ada linggis, bahan peledak, atau teknik membobol kunci konvensional yang bisa menggeser kaitnya tanpa memicu runtuhnya seluruh kubah kapel."
    vic "Hanya ada satu kunci yang sah di dunia ini yang dapat membuka gerbang ini dengan aman."

    mc "Kunci perak berukir mawar kuno yang selalu tergantung di leher Evelyn Hart..."

    "Tepat ketika kata-kata itu selesai kuucapkan, sebuah suara langkah kaki yang tenang dan sangat teratur bergema dari arah undakan tangga batu."
    "Cahaya lentera kuningan yang stabil menyapu bayang-bayang pilar marmer hitam."

    show victoria serious at sprite_left with dissolve
    show evelyn neutral at sprite_right with dissolve
    "Evelyn Hart melangkah keluar dari kegelapan lorong dengan keanggunan seorang kepala pelayan bangsawan yang sempurna."
    "Seragam gaun panjang berwarna biru tua dan celemek putihnya tampak begitu rapi tanpa setitik pun noda debu, seolah ia baru saja melangkah keluar dari ruang perjamuan teh sore hari."
    "Di tangan kanannya, ia memegang lentera minyak kuningan yang apinya menyala stabil tanpa bergetar."
    show evelyn serious at sprite_right with dissolve
    "Wajahnya tampak sedingin patung marmer katedral, namun sepasang matanya yang berwarna amber menatap kami berdua dengan ketajaman yang membuat Victoria menegang waspada."

    eve "Tamu yang bijaksana dan berpendidikan seharusnya menikmati istirahat malam mereka di atas kasur berbusa empuk kamar tamu pada malam keenam, Tuan Guest, Nona Victoria."
    eve "Ruang bawah tanah ini bukanlah tempat yang pantas dikunjungi oleh mereka yang masih menghargai keutuhan akal sehat dan memori kehidupan mereka."

    show victoria serious at sprite_left with dissolve
    "Victoria melangkah maju setengah jengkal, menatap Evelyn dengan sorot mata menantang."

    vic "Berhentilah bersandiwara, Evelyn. Sandiwara pelayan setia yang polos ini sudah basi seratus tahun yang lalu."
    vic "Aku telah membaca catatan sensus desa Ashwood tahun 1884. Nama Evelyn Hart telah tercatat sebagai kepala pelayan Rose Manor bahkan sebelum kakek buyutku lahir ke dunia ini!"
    vic "Berapa banyak pria dan wanita yang telah kau layani dengan teh manis beracunmu sebelum kau mengantar mereka ke gerbang pembantaian ingatan ini?!"

    "Evelyn tidak menunjukkan kemarahan, keterkejutan, atau ketakutan sedikit pun atas tuduhan tajam Victoria."
    "Ia hanya berdiri tegak dalam keheningan sesaat, lalu menghembuskan napas panjang—sebuah desahan yang begitu berat, begitu lelah, dan begitu penuh dengan kepedihan berabad-abad yang tak terkatakan."

    show evelyn sad at sprite_right with dissolve
    eve "Seratus empat puluh dua tahun, Nona Victoria."
    eve "Tepat seratus empat puluh dua tahun saya berdiri di atas lantai batu dingin ini, menjaga dinding-dinding mansion yang terkutuk ini agar tidak roboh menimpa dunia fana."
    eve "Apakah Anda mengira saya menikmati melihat para tuan dan nyonya Rosewood mati muda dalam keputusasaan?"
    eve "Saya melihat Lady Margaret menangis darah di taman mawar hingga kedua matanya buta karena rasa bersalah."
    eve "Saya melihat Lord Jonathan Rosewood menembak kepalanya sendiri di ruang kerja setelah menyadari bahwa perjanjian darahnya telah merenggut nyawa Lilith Vane selamanya."
    eve "Dan kini... saya harus menyaksikan Nona Seraphina menanggung seluruh dosa terkutuk itu di pundaknya yang rapuh, terperangkap di antara kewajiban leluhur dan kerinduan hatinya sendiri untuk menjadi manusia biasa."

    mc "Jika kau merasakan kepedihan itu, Evelyn... jika kau benar-benar menyayangi Seraphina seperti putrimu sendiri... mengapa kau tidak menghentikan semua ini?!"
    mc "Mengapa kau membiarkan siklus berdarah ini terus berulang?!"

    "Mata amber Evelyn beralih menatapku, dan untuk pertama kalinya sejak malam pertama kedatanganku, aku melihat lapisan emosi manusia yang begitu nyata di balik tatapannya yang dingin."

    eve "Karena saya terikat oleh sumpah darah, Tuan Guest."
    eve "Ketika saya bersumpah setia kepada keluarga Rosewood pada tahun 1884, darah saya menyatu dengan fondasi batu mansion ini."
    eve "Jika saya melanggar sumpah itu secara sembarangan, energi kehampaan yang terkunci di dalam kapel akan meledak seketika dan memusnahkan Nona Seraphina sebelum fajar menyingsing."
    eve "Sumpah darah melarang saya menyerahkan kunci kapel ini kepada siapa pun... kecuali kepada seseorang yang dapat membuktikan bahwa ia memiliki sarana, pengetahuan, dan ketulusan hati untuk mematahkan segel ketujuh tanpa menumpahkan darah Nona Seraphina."
    eve "Tunjukkan kepada saya, Tuan Guest... Apakah Anda benar-benar penyelamat yang telah dinantikan oleh mansion ini selama satu abad, ataukah Anda hanyalah korban berikutnya yang akan dilupakan oleh sejarah?"

    menu:
        "Memperlihatkan liontin perak Seraphina dan mawar hitam makam Lilith":
            $ evidence += 2
            $ ser_trust += 2
            mc "Evelyn, lihatlah apa yang kubawa bersamaku."
            "Aku melangkah maju dan membuka telapak tanganku di hadapan lentera minyak Evelyn."
            "Di tanganku, liontin perak Lady Eleanor berkilau hangat di samping setangkai mawar hitam abadi yang berembun es dari makam Lilith."
            mc "Seraphina sendiri yang mempercayakan liontin ibunya kepadaku semalam. Ia tidak lagi memandangku sebagai kurban, melainkan sebagai tumpuan harapannya."
            mc "Dan ini adalah mawar hitam dari makam Lilith Vane. Lilith sendiri yang berbicara kepadaku di taman mawar semalam—ia tidak menginginkan darah Seraphina! Lilith hanya menginginkan pengakuan dan pembebasan atas sumpah darahnya!"

            show evelyn surprised at sprite_right with dissolve
            "Mata Evelyn terbelalak lebar. Tangannya yang biasanya kokoh tampak gemetar hebat saat jemarinya menyentuh kelopak mawar hitam dan ukiran perak liontin."
            eve "Liontin Nyonya Eleanor... dan mawar Nona Lilith..."
            eve "Nona Seraphina tidak pernah membiarkan siapa pun menyentuh liontin itu sejak hari pemakaman ibunya... bahkan ayahnya sendiri dilarang mendekatinya."
            eve "Anda benar-benar telah memenangkan hatinya, Guest... dan Anda telah membawa kedamaian bagi arwah yang paling terluka di rumah ini."

        "Meyakinkan Evelyn dengan diagram okultisme Victoria dan rencana pengalihan energi":
            $ evidence += 1
            $ victoria_alliance = True
            mc "Kami memiliki rencana ilmiah yang matang, Evelyn. Victoria telah memetakan seluruh aliran resonansi enam pilar ini."
            vic "Evelyn, lihat diagram Sigillum Septem Foliorum ini. Kami tidak berniat menghancurkan segel dengan kekerasan."
            vic "Jika kunci perak digunakan tepat pada dentangan ketujuh lonceng tengah malam, polaritas pilar mawar dapat dibalik, mengalirkan kelebihan energi kehampaan kembali ke perut bumi tanpa membutuhkan tumbal memori manusia."
            eve "Penelitian Anda sangat teliti, Nona Victoria... Jauh lebih matang dan terukur daripada usaha kakek buyut Anda yang ceroboh."
            eve "Barangkali... nalar dan sains zaman baru ini memang akhirnya mampu memecahkan rantai sihir kuno yang telah membelenggu kami."

        "Bersumpah demi nyawa sendiri untuk melindungi Seraphina hingga tetes darah terakhir":
            $ ser_aff += 2
            $ ser_trust += 1
            mc "Aku tidak peduli dengan kekayaan, keabadian, atau nama besar Rosewood, Evelyn."
            mc "Aku bersumpah demi nyawa dan jiwaku sendiri: jika ritual di dalam kapel itu menuntut bayaran, biar aku yang menanggung seluruh hukumannya. Aku tidak akan membiarkan sehelai rambut pun dari kepala Seraphina terluka!"
            "Evelyn menatapku lurus ke dalam mataku, mencari setitik pun keraguan atau kebohongan di wajahku."
            show evelyn smile at sprite_right with dissolve
            "Setelah beberapa detik keheningan yang menegangkan, seulas senyuman tipis yang hangat terbit di bibir wanita tua itu untuk pertama kalinya."
            eve "Keberanian yang tulus dan tanpa pamrih... Sudah teramat lama sejak seorang pria berani berdiri di hadapan kematian dengan ketulusan seperti itu demi seorang wanita Rosewood."
            eve "Nona Seraphina berhak mendapatkan seseorang yang mencintainya dengan tulus, bukan sekadar memanfaatkannya."

    "Evelyn perlahan mengangkat kedua tangannya ke lehernya."
    "Dengan gerakan yang penuh kekhidmatan, ia melepaskan rantai perak kuno yang telah membeban lehernya selama lebih dari satu abad."
    "Di ujung rantai itu, sebuah kunci perak antik sepanjang telapak tangan, berukir relief kuntum mawar yang dibelit pedang ksatria, berkilauan megah di bawah cahaya api lentera."

    eve "Sumpah darah melarang saya membuka gerbang ini dengan tangan saya sendiri."
    eve "Namun... sumpah darah itu tidak melarang saya untuk menjatuhkan kunci ini ke tangan orang yang dipercaya oleh takdir."

    "Evelyn meletakkan kunci perak itu ke dalam telapak tanganku, lalu menggenggam jemariku erat-erat dengan kedua tangannya yang dingin."
    call inspect_clue("silver_key")

    eve "Peganglah kunci ini, Tuan Guest. Kunci ini akan membuka gerbang kapel inti di malam ketujuh besok."
    eve "Tetapi dengarkan baik-baik peringatan terakhir saya:"
    eve "Besok malam, begitu lonceng tengah malam berdentang pertama kali, Anda hanya memiliki waktu hingga dentangan ketujuh untuk membalikkan segel mawar."
    eve "Jika Anda terlambat, atau jika tekad Anda goyah di hadapan altar... seluruh kenangan Anda akan musnah, dan Nona Seraphina akan terkunci selamanya di dalam malam tanpa fajar."
    show evelyn neutral at sprite_right with dissolve
    eve "Selamatkanlah Nona Seraphina... dan bebaskanlah rumah ini dari penderitaan panjang ini."

    mc "Aku berjanji, Evelyn. Atas nama seluruh kenangan yang kupiliki, aku akan menyelesaikan ini."

    "Tiba-tiba, semilir angin dingin beraroma kelopak mawar bertiup pelan di celah gerbang kapel."
    "Di antara bayang-bayang pilar batu yang gelap, sesosok siluet putih berpendar lembut—Lilith Vane—muncul sejenak, menganggukkan kepalanya dengan senyuman damai ke arah kami sebelum memudar menjadi butiran cahaya perak."

    hide rose_petals with dissolve
    hide victoria with dissolve
    hide evelyn with dissolve

    scene bg_guest_bed_pov
    with fade

    "Aku kembali ke dalam kamar tamuku di lantai dua saat langit di luar jendela mulai memancarkan semburat fajar kelabu dingin."
    "Merebahkan tubuhku di atas kasur berkanopi yang empuk di bawah selimut beludru marun yang hangat, aku menatap langit-langit kayu berukir di atas kepalaku."
    "Kunci perak pemberian Evelyn tergenggam erat di dalam telapak tanganku, memancarkan hawa dingin logam yang mengingatkanku pada takdir malam ketujuh yang kian dekat."
    "Di atas meja kayu jati, kunci perak kapel bawah tanah tergeletak berdampingan dengan liontin perak Seraphina, mawar hitam Lilith, dan diagram segel Victoria."

    "Enam malam penuh misteri, bahaya, dan intrik telah kulalui."
    "Seluruh kepingan teka-teki kini telah berada di tanganku."

    "Besok malam adalah malam ketujuh."
    "Malam di mana takdir Rose Manor, kebebasan Seraphina, dan keutuhan jiwaku sendiri akan diputuskan untuk selama-lamanya."

    jump day_7

