## story_day2.rpy
## Siang Hari 2: Gema Melodi di Ruang Musik (The Echoing Melody)
## Naskah interaktif sastra gothic mystery mendalam

label day_2:
    scene black
    with fade

    "Cahaya fajar yang pucat dan dingin menyusup perlahan melalui celah tirai beludru tebal kamar tamu di lantai dua."
    "Bahkan di siang hari yang seharusnya cerah, Rose Manor seolah-olah menolak untuk disinari oleh kehangatan sinar matahari."
    "Lapisan kabut tebal berwarna kelabu tua tetap menggantung rendah dan membatu di atas puncak-puncak pohon pinus Hutan Ashwood, menyaring cahaya siang menjadi temaram yang murung, lembap, dan dingin."
    "Detik-detik pendulum jam dinding kuno di atas perapian berdetak lambat dan monoton di dalam keheningan kamar:"
    "{i}Tik... Tok... Tik... Tok...{/i}"

    scene bg_manor_hall
    with dissolve

    "Ketika aku melangkah keluar dari kamar dan menuruni tangga marmer melengkung menuju aula utama, kesunyian mansion ini terasa begitu megah sekaligus menekan dada."
    "Lantai marmer hitam-putih bermotif papan catur tampak bersih berkilap bagai cermin air yang tenang, memantulkan bayangan lampu gantung kristal raksasa yang tergantung tinggi di langit-langit kubah berukir malaikat berduka."
    "Di atas meja panjang dari kayu ek gelap di ruang perjamuan, sebuah taplak meja renda putih tersaji dengan rapi."
    "Sebuah cangkir porselen putih tipis mengepulkan uap harum teh hitam yang dicampur dengan kelopak mawar kering, ditemani sepiring roti gandum panggang yang hangat, madu hutan, dan mentega segar."

    "Evelyn Hart muncul dari ambang pintu lorong pelayan di sayap selatan, melangkah tanpa menimbulkan suara derit sedikit pun di atas karpet marun, laksana bayangan yang meluncur di atas lantai."

    show evelyn neutral with dissolve

    eve "Selamat pagi, Tuan Guest. Saya harap kamar tamu cukup nyaman untuk mengistirahatkan pikiran dan raga Anda setelah malam pertama yang panjang."

    mc "Selamat pagi, Evelyn. Kamar itu sangat hangat dan mewah, terima kasih. Namun keheningan mansion ini di siang hari... terasa sangat ganjil bagi bangunan sebesar ini. Di mana para pelayan lainnya?"

    "Evelyn meletakkan teko perak di samping cangkirku dengan gerakan yang sangat terlatih dan khidmat."
    "Wajahnya tetap setenang dan sedingin patung marmer katedral kuno."

    eve "Rose Manor telah berdiri selama lebih dari dua abad, Tuan. Sebuah rumah tua seperti ini belajar untuk menyimpan suaranya sendiri di balik dinding-dinding batu granit yang tebal."
    eve "Tidak ada pelayan lain di sini selain saya. Keluarga bangsawan Rosewood menghargai privasi dan kesunyian di atas segalanya."
    eve "Di tempat yang sunyi, pikiran seseorang dapat mendengar apa yang tak mampu diucapkan oleh kata-kata... Namun berhati-hatilah, Tuan. Terkadang kesunyian juga mampu memantulkan gema yang berbahaya bagi mereka yang berpikiran bimbang."

    mc "Gema yang berbahaya? Apa maksudmu, Evelyn?"

    show evelyn serious with dissolve

    eve "Masa lalu tidak pernah benar-benar mati di bawah atap ini, Tuan. Ia hanya menunggu saat yang tepat untuk dipanggil kembali oleh mereka yang memiliki rasa penasaran berlebih."

    show evelyn smile with dissolve

    eve "Nikmatilah sarapan Anda selagi hangat. Nona Seraphina sedang beristirahat di kamarnya dan berpesan agar Anda merasa bebas menjelajahi sayap barat mansion."

    hide evelyn with dissolve

    "Setelah menikmati sarapan sederhana dan teh mawar hangat yang menyegarkan tubuhku dari sisa hawa dingin malam, aku memutuskan untuk tidak mengurung diri di kamar tamu."
    "Rasa ingin tahu yang membara mendorongku untuk mulai menyelidiki denah dan sejarah rumah misterius ini."
    "Aku melangkah menyusuri koridor panjang di sayap barat lantai dasar yang dipenuhi pintu-pintu kayu mahoni berukir sulur tanaman dan patung-patung dada pualam tokoh-tokoh kuno yang berdebu."

    scene bg_music_room
    with fade

    "Di ujung koridor sayap barat, sebuah pintu ganda kayu mahoni berukir motif daun akantus dan harpa berdiri setengah terbuka."
    "Aku melangkah masuk ke dalam Ruang Musik lama Rose Manor."
    "Ruangan itu tampak luas, berdebu, dan seakan telah ditinggalkan selama puluhan tahun tanpa pernah disentuh kehidupan."
    "Lantai kayu parketnya yang gelap dipenuhi bercak-bercak noda lilin tua, sementara tirai sutra merah anggur yang tebal menutupi jendela-jendela tinggi, hanya menyisakan celah sempit bagi seberkas cahaya kelabu untuk menerobos masuk."

    "Di sudut ruangan, sebuah biola tua terbaring di dalam kotak beludru hitam yang terbuka separuh, senar-senarnya telah putus dan berkarat termakan usia."
    "Sebuah harpa berlapis emas berdiri kusam di dekat perapian batu yang padam, dengan senar-senar yang kendur."
    "Dan tepat di tengah ruangan, di atas karpet beludru merah pudar, berdiri sebuah grand piano hitam antik berkaki lengkung yang terawat dengan sangat aneh di antara debu sekelilingnya."

    "Anehnya, tepat saat ujung sepatuku menginjak lantai kayu parket ruangan ini, tuts-tuts gading gajah pada grand piano tersebut bergerak turun sendiri dengan gerakan yang sangat lembut dan ritmis!"
    play music bgm_nocturne fadein 1.5
    "{i}Ting... Ting... Tong... Tong...{/i}"
    "Serangkaian nada minor yang sangat melankolis, indah, dan menyayat hati mengalun di udara dingin ruangan yang berdebu."
    "Melodi itu terdengar seolah dimainkan oleh sepasang jemari lentik tak kasat mata yang dipenuhi kerinduan mendalam dan rasa sakit yang tak terkatakan."

    mc "Piano itu... memainkan melodi sendiri tanpa ada seorang pun di dekatnya."

    "Getaran dawai piano beresonansi di dalam dadaku, membangkitkan rasa duka yang aneh dan asing, seolah melodi itu meratapi sebuah perpisahan yang abadi."

    menu:
        "Mendekati grand piano dan memeriksa lembaran partitur kuno di atas penyangga tuts":
            $ evidence += 1
            call inspect_clue("nocturne_score")
            $ persistent.cg_piano_duet = True
            scene cg_piano_duet with dissolve
            "Aku memberanikan diri melangkah mendekati grand piano hitam tersebut dengan langkah perlahan."
            "Nada-nada melankolis itu mendadak berhenti tepat saat bayanganku jatuh di atas tuts-tuts gadingnya yang dingin membeku."
            "Di atas penyangga partitur kayu jati berukir, selembar kertas musik kuno yang rapuh, menguning, dan bernoda bercak kecokelatan terpasang di sana."
            "Di sudut kanan atas kertas partitur bergaris paranada tersebut, sebuah nama dan judul tertulis dengan tinta ungu pudar yang meliuk anggun:"
            "{i}'Lilith Vane - Nocturne untuk Malam yang Dingin, Musim Gugur 1891.'{/i}"
            "Di bagian bawah halaman partitur, ada sebuah catatan tangan yang ditulis tergesa-gesa dengan pensil karbon:"
            "{i}'Tidurlah, wahai jiwaku yang letih, sebelum mawar darah mekar kembali dan mencuri ingatan cinta kita.'{/i}"
            mc "Lilith Vane lagi... Gadis ini meninggalkan jejak jiwanya di setiap sudut mansion ini sebelum ia menghilang."
            play sound sfx_page
            "Aku mengeluarkan buku catatanku dan menyalin judul partitur, tahun pembuatan, serta baris puisi terakhir tersebut dengan teliti."

        "Berbalik waspada dan mengamati setiap sudut bayang-bayang di balik tirai sutra":
            $ ser_trust += 1
            "Naluriku berteriak waspada. Aku segera membalikkan badan, memunggungi piano, dan menatap tajam ke arah bayang-bayang tirai jendela yang bergoyang pelan."
            "Tidak ada sosok kasat mata yang berdiri di sana, namun suhu udara di dekat tirai jendela mendadak turun drastis hingga embun napasku mengepul putih pekat di udara."
            "Sebuah hawa dingin yang lembut membelai pipiku laksana belaian jemari wanita yang dingin dan tak berdaya."
            mc "Siapa pun engkau yang memainkan melodi itu... aku tahu kau berada di sini, dan aku tidak bermaksud mengganggu ketenanganmu."
            "Rasa hormat yang tulus pada keheningan jiwa-jiwa masa lalu membuatku menundukkan kepala sejenak, membiarkan kehadiran gaib itu mereda dengan sendirinya ke dalam keheningan dinding batu."

        "Mencoba melangkah maju dan menekan satu tuts piano untuk membalas nada minor tersebut":
            $ evidence += 1
            $ ser_trust += 1
            "Didorong oleh dorongan empati yang kuat, aku melangkah maju ke depan piano dan dengan sangat hati-hati menekan satu tuts gading nada C minor."
            play sound sfx_piano
            "{i}Denggg...{/i}"
            "Gema nada itu berdenting panjang dan khidmat di dalam ruangan berdebu, bergetar menyentuh dawai-dawai tembaga di dalam rongga kayu piano."
            "Dari dalam badan piano, getaran senar menghasilkan resonansi harmonik yang aneh—menyerupai bisikan suara wanita yang begitu lembut dan lirih di telingaku:"
            "{i}...Terima kasih... karena telah sudi mendengar tangisanku...{/i}"
            "Bulu kuduk di sekujur tubuhku meremang seketika, namun sebuah rasa tenang yang damai menyelimuti dadaku, seolah arwah yang terjebak di ruangan ini merasa diakui keberadaannya."

    scene bg_music_room with dissolve

    "Ketika aku berbalik dan melangkah keluar dari Ruang Musik kembali ke lorong sayap barat, seorang wanita muda berambut auburn pendek berpapasan denganku di ambang pintu."
    "Victoria Ashbourne berdiri tegak dengan setumpuk buku tua bersampul kulit tebal di dekapannya."
    "Dari balik kacamata berbingkai kawat peraknya, sepasang mata keemasannya menatapku dengan kilatan analitis yang tajam dan penuh rasa ingin tahu."

    show victoria neutral with dissolve

    vic "Melodi Nocturne C minor karya Lilith Vane... Rupanya kau juga telah mendengar gema akustik masa lalu rumah ini di siang hari bolong, Tuan Guest."

    mc "Kau... Nona Victoria Ashbourne, bukan? Tamu lain yang disebutkan oleh Evelyn."

    vic "Tepat. Victoria Ashbourne, peneliti independen sejarah sosial dan fenomena metafisika."

    show victoria smile with dissolve

    vic "Senang melihatmu masih memiliki akal sehat yang tajam dan utuh setelah melewati malam pertamamu di bawah atap terkutuk ini."
    vic "Banyak tamu sebelummu sudah mulai menunjukkan gejala delirium, paranoia, dan delusi indrawi sejak hari kedua karena paparan medan resonansi psikis yang dipancarkan oleh arsitektur Rose Manor."

    mc "Medan resonansi psikis? Apakah kau percaya bahwa melodi piano tadi hanyalah halusinasi?"

    show victoria serious with dissolve

    vic "Halusinasi adalah istilah primitif yang digunakan oleh orang-orang yang malas mencari penjelasan ilmiah, Guest."
    vic "Apa yang kau dengar tadi adalah resonansi memori—jejak energi emosional berfrekuensi tinggi yang tertinggal pada bahan padat seperti kayu dan senar piano setelah peristiwa traumatis terjadi."
    vic "Lilith Vane adalah pianis berbakat yang hidup di sini pada akhir abad kesembilan belas. Rasa sakit dari kematiannya begitu hebat hingga mengkristal menjadi rekaman abadi di ruangan ini."

    show victoria smile with dissolve

    vic "Saran dariku untuk penyelidikanmu hari ini: perhatikan baik-baik setiap lukisan di Galeri Keluarga sayap timur nanti malam."
    vic "Lukisan-lukisan di rumah ini memiliki kebiasaan ganjil untuk menceritakan apa yang sengaja dihapus dari buku-buku sejarah keluarga."

    "Victoria mengangguk singkat dengan senyuman tipis penuh arti, lalu melangkah melewatiku menuju tangga sayap timur dengan langkah tegas."

    hide victoria with dissolve

    scene bg_manor_hall
    with fade

    "Sore hari perlahan turun menyelimuti Rose Manor."
    "Kabut kelabu tebal di luar jendela mulai menggelap, berganti menjadi bayang-bayang malam kedua yang dingin dan sunyi."
    "Peringatan Victoria tentang galeri lukisan keluarga terngiang-ngiang di kepalaku."

    "Waktunya telah tiba untuk bersiap memasuki Galeri Potret Keluarga Rosewood di lantai tiga."

    jump night_2

