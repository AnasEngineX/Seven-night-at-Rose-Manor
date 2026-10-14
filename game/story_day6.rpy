## story_day6.rpy
## Siang Hari 6: Rencana Taktis dan Bayang-Bayang Badai (The Gathering Storm)
## Naskah interaktif sastra gothic mystery mendalam

label day_6:
    scene black
    with fade

    "Fajar hari keenam terbit di balik gulungan awan badai hitam pekat yang berputar rendah di atas puncak granit bukit Ashwood."
    "Angin badai musim dingin mulai melolong ganas dari arah ngarai utara, menghantam daun-daun jendela kaca bertingkat Rose Manor dengan suara erangan panjang yang menyeramkan laksana jeritan arwah gentayangan."
    "Hawa dingin di dalam koridor-koridor batu mansion terasa semakin menusuk hingga ke sumsum tulang, seolah kehangatan api perapian marmer ditelan habis oleh gravitasi kegelapan yang merayap naik dari perut bumi."
    "Lampu-lampu gantung kristal raksasa di langit-langit aula bergoyang perlahan, butiran kristalnya berdenting halus satu sama lain akibat getaran mikro seismik gaib yang merambat di sepanjang fondasi batu mansion."

    "Di balik saku mantelku, liontin perak pemberian Seraphina semalam berdetak pelan dengan kehangatan teratur yang menenangkan debar jantungku."
    "Kata-kata tulus yang ia bisikkan di depan kobaran api perapian ruang duduknya semalam masih terpatri begitu dalam di sanubariku:"
    "{i}'Di mansion yang penuh dengan tipu daya dan kepalsuan ini, rasa terima kasih dan perasaanku kepadamu adalah satu-satunya hal yang nyata.'{/i}"

    scene bg_manor_hall
    with fade

    "Ketika aku menuruni tangga marmer menuju aula utama, Victoria Ashbourne telah berdiri menantiku di dekat meja perapian sudut aula."
    "Ia mengenakan mantel wol hitam berpotongan militer praktis, dengan sepasang kacamata perak yang memantulkan denah arsitektur kuno yang terbentang di atas meja kayu jati."
    "Di sampingnya, sebuah kompas okultisme berbahan tembaga dengan jarum magnetik berputar liar tanpa arah yang stabil, mendesis pelan oleh muatan listrik statis gaib."

    show victoria neutral with dissolve

    vic "Kau bangun tepat pada waktunya, Tuan Guest."
    vic "Waktu kita semakin sempit dan berharga. Saluran resonansi okultisme di bawah tanah telah mulai bergetar hebat sejak fajar menyingsing."

    mc "Apakah segel keenam telah mulai bereaksi terhadap kedekatan malam ketujuh, Victoria?"

    show victoria serious with dissolve

    vic "Tepat sekali. Enam pilar mawar hitam di ruang bawah tanah sedang menyerap sisa-sisa stabilitas medan eterik mansion ini dengan kecepatan eksponensial."
    vic "Malam ini adalah malam keenam—malam persiapan terakhir."
    vic "Jika kita tidak berhasil mengamankan akses ke kapel bawah tanah dan mempelajari tata letak altar inti malam ini juga, kita tidak akan memiliki peluang apa pun saat lonceng malam ketujuh berdentang besok."

    "Victoria menunjuk sebuah diagram potongan melintang di atas perkamen tua dengan pena peraknya."

    vic "Pintu masuk menuju kapel bawah tanah berada tepat di balik lorong dapur pelayan di sayap selatan. Gerbang besi berduri itu dilindungi oleh mekanisme gembok perak empat silinder milik Evelyn Hart."
    vic "Sumpah darah Rosewood melarang Evelyn membuka gerbang itu dengan tangannya sendiri, tetapi sumpah itu tidak melarangnya untuk 'kehilangan' kunci tersebut jika nurani dan logikanya tergerak oleh kebenaran."
    vic "Kekuatan moral, bukti sejarah yang autentik, dan ketulusan hati adalah satu-satunya instrumen yang mampu menembus kekakuan sumpah seratus empat puluh tahun seorang pelayan Rosewood."

    menu:
        "Mendatangi Seraphina di kapel keluarga lantai satu untuk memberinya ketenangan dan kekuatan batin":
            $ ser_aff += 2
            $ ser_trust += 2
            hide victoria with dissolve
            "Sebelum memikirkan strategi teknis lebih lanjut, langkah kakiku tergerak untuk mencari Seraphina."
            "Aku melangkah menyusuri koridor lantai satu menuju kapel doa keluarga di sayap timur."

            scene bg_chapel
            with fade

            "Di sana, di antara deretan bangku kayu jati tua yang temaram, Seraphina sedang berlutut di atas undakan marmer di depan patung malaikat berduka."
            "Kedua tangannya yang ramping saling bertaut erat di depan dadanya, sementara pundaknya bergetar halus menahan isak tangis."

            show seraphina sad with dissolve

            "Ketika aku melangkah mendekat tanpa suara, aku mendengar bisikan doanya yang lirih dan penuh kepedihan:"
            ser "{i}...Tuhan semesta alam... jika darah Rosewood harus membayar dosa ini... jangan biarkan pria itu menanggung kepedihanku... lindungilah jiwanya...{/i}"
            "Hati di dalam dadaku terenyuh mendengar doa tulusnya yang memohon keselamatanku di atas keselamatannya sendiri."
            "Aku berlutut di sampingnya di atas marmer dingin, lalu meletakkan tanganku dengan lembut di atas pundaknya."

            show seraphina surprised with dissolve

            "Seraphina tersentak kaget, mendongak menatapku dengan matanya yang merah anggur berkaca-kaca oleh genangan air mata bening."

            show seraphina sad with dissolve

            ser "Guest... kau... mengapa kau selalu datang di saat aku sedang berada di titik paling rapuh?"
            mc "Karena kau tidak boleh memikul rasa bersalah ini sendirian lagi, Seraphina. Aku mendengar doamu, dan aku bersumpah kita akan melewati kegelapan ini bersama-sama hingga fajar terbit."
            "Seraphina menyandarkan dahinya di pundakku, membiarkan kehangatan tubuh kami mengusir rasa dingin yang mencekam."

            show seraphina smile with dissolve

            ser "Bersamamu di sisiku... untuk pertama kalinya dalam hidupku, aku tidak lagi takut menghadapi malam."
            hide seraphina with dissolve

        "Menyempurnakan kalkulasi diagram pembalik segel okultisme bersama Victoria":
            $ evidence += 1
            $ victoria_alliance = True
            mc "Mari kita periksa kembali seluruh kalkulasi rumus pembalik polaritas ini, Victoria. Kita tidak boleh membuat kesalahan sedikit pun saat ritual puncak berlangsung."

            show victoria smile with dissolve

            vic "Pendekatan yang sangat tepat, disiplin, dan terukur. Aku sangat menghargai ketelitianmu di hadapan anomali mematikan seperti ini."
            "Victoria dan aku menghabiskan dua jam berikutnya di atas meja perpustakaan, meneliti setiap persamaan latin dan simbol-simbol geometri kabalistik pada diagram Sigillum Septem Foliorum."

            show victoria serious with dissolve

            vic "Jika kunci perak Evelyn dimasukkan ke rongga segel ketujuh tepat pada dentangan ketujuh lonceng, dan mawar hitam Lilith ditancapkan sebagai jangkar katarsis, seluruh aliran resonansi kutukan akan berbalik seratus delapan puluh derajat."
            vic "Alih-alih menyerap memori manusia ke dalam bros kristal mawar, kelebihan energi kehampaan akan dialirkan kembali ke perut bumi secara aman tanpa ledakan."

            show victoria smile with dissolve

            vic "Ini adalah konvergensi sempurna antara ilmu sains modern dan okultisme klasik."
            "Aku mencatat seluruh urutan aktivasi segel itu ke dalam buku jurnal sakuku dengan sangat teliti."
            hide victoria with dissolve

        "Menemui Evelyn secara pribadi untuk meminta petunjuk rahasia tentang lorong bawah tanah":
            $ evidence += 1
            $ ser_trust += 1
            hide victoria with dissolve
            "Aku melangkah menuju ruang persiapan pelayan di sayap belakang dan mendapati Evelyn sedang merapikan tempat-tempat lilin perak dengan ketenangan yang luar biasa."

            show evelyn neutral with dissolve

            mc "Evelyn, malam ini kami akan turun menembus ruang bawah tanah. Apakah ada bahaya tersembunyi atau jebakan fisik yang harus kami waspadai di lorong batu itu?"
            "Evelyn berhenti mengelap perak, lalu menatapku dengan sepasang mata ambernya yang dalam dan penuh rahasia berabad-abad."

            show evelyn serious with dissolve

            eve "Lantai batu di dekat pilar ketiga sangat licin oleh rembesan air es purba, Tuan Guest. Berhati-hatilah saat menapak agar Anda tidak terpeleset ke dalam celah retakan tanah."
            eve "Dan yang paling penting dari segalanya: apa pun ilusi suara yang Anda dengar membisikkan keputusasaan dari celah-celah dinding kubah... jangan pernah melepaskan liontin perak pemberian Nona Seraphina dari genggaman Anda."

            show evelyn smile with dissolve

            eve "Liontin itu membawa berkat cinta murni seorang ibu yang menolak kutukan Rosewood. Selama liontin itu bersamamu, jiwa Anda tidak akan tersesat di dalam kegelapan ketiadaan."
            mc "Terima kasih atas petunjuk dan perlindunganmu, Evelyn. Aku akan mengingatnya baik-baik."
            hide evelyn with dissolve

    scene bg_manor_hall
    with fade

    "Sore hari tiba dengan kecepatan yang menakutkan dan mencekam."
    "Badai salju di luar jendela melolong semakin dahsyat, menabrakkan gumpalan es ke kaca-kaca jendela dengan suara gemuruh yang menggetarkan seluruh ruangan."
    "Lonceng jam besar menara Rose Manor berdentang berat sebanyak lima kali, suaranya menggema di seluruh penjuru koridor sepi laksana lonceng pemakaman."

    "Malam keenam telah tiba."
    "Waktunya telah tiba untuk menuruni tangga batu menuju ruang bawah tanah, menghadapi Evelyn Hart, dan merebut kunci perak pembuka gerbang kapel terkutuk."

    jump night_6

