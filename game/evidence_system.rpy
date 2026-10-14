## evidence_system.rpy
## Sistem Jurnal Investigasi dan Arsip Bukti Seven Nights at Rose Manor

init python:
    class ClueItem(object):
        def __init__(self, item_id, name, description, date_found, category, image_path="", deduction_note=""):
            self.item_id = item_id
            self.name = name
            self.description = description
            self.date_found = date_found
            self.category = category
            self.image_path = image_path
            self.deduction_note = deduction_note

    ## Daftar bukti default di awal permainan
    all_clues = {
        "invitation_letter": ClueItem(
            "invitation_letter",
            "Surat Undangan Bersegel Mawar",
            "Sepucuk surat tebal dengan stempel lilin merah darah berbentuk mawar berduri. Berisi undangan tinggal selama tujuh malam di Rose Manor untuk menemukan kenangan yang hilang.",
            "Malam 1",
            "Dokumen",
            "images/clues/clue_invitation.jpg",
            "Stempel lilin merah menyembunyikan serat sutra perak. Tinta latin bertuliskan 'Sanguis et Memoria' membuktikan bahwa surat ini adalah pemicu ikatan takdir kutukan."
        ),
        "rose_brooch": ClueItem(
            "rose_brooch",
            "Bros Mawar Merah Seraphina",
            "Bros pusaka keluarga Rosewood yang tersemat di dada Seraphina. Memancarkan denyut gaib dan berfungsi sebagai wadah resonansi penampung ingatan para tamu.",
            "Malam 1",
            "Artefak",
            "images/clues/clue_rose_brooch.jpg",
            "Kristal merah delima berdenyut selaras dengan denyut jantung Seraphina. Benda ini menyerap resonansi memori dan menyimpannya sebelum dialirkan ke segel altar."
        ),
        "guestbook_1884": ClueItem(
            "guestbook_1884",
            "Buku Tamu Kuno Tahun 1884",
            "Catatan arsip tamu Rosewood dari satu abad lalu. Memuat tanda tangan 'Evelyn Hart' dengan guratan pena yang identik dengan kepala pelayan saat ini.",
            "Siang 2",
            "Dokumen",
            "images/clues/clue_guestbook.jpg",
            "Tanda tangan Evelyn pada arsip tahun 1884 membuktikan bahwa sang kepala pelayan terikat oleh sumpah darah selama seratus empat puluh dua tahun tanpa menua."
        ),
        "nocturne_score": ClueItem(
            "nocturne_score",
            "Partitur Musik Nocturne 1891",
            "Lembaran kertas musik kuno di atas piano sayap barat, digubah oleh Lilith Vane sesaat sebelum ia dikorbankan dalam ritual mawar pertama.",
            "Siang 2",
            "Peninggalan",
            "images/clues/clue_nocturne_score.jpg",
            "Notasi musik 'Nocturne in F Minor' memiliki progresi melodi yang mampu meredam amukan kabut eterik mawar di taman labirin."
        ),
        "bleeding_portrait": ClueItem(
            "bleeding_portrait",
            "Potret Berdarah Lilith Vane",
            "Lukisan cat minyak di galeri keluarga. Mawar putih yang digenggam Lilith berubah menjadi merah darah segar yang menetes saat malam tiba.",
            "Malam 2",
            "Misteri",
            "images/clues/clue_bleeding_portrait.jpg",
            "Darah yang merembes di atas kanvas adalah proyeksi rasa bersalah Lord Jonathan Rosewood yang menyegel sahabatnya sendiri hidup-hidup ke dalam mawar."
        ),
        "black_rose": ClueItem(
            "black_rose",
            "Mawar Hitam Makam Lilith",
            "Mawar supernatural yang tumbuh dari celah nisan tanpa nama Lilith di bawah pohon willow. Kelopaknya sekeras kaca kristal dan menolak membeku oleh salju.",
            "Malam 3",
            "Artefak",
            "images/clues/clue_black_rose.jpg",
            "Kelopak mawar kristal hitam ini tidak layu oleh suhu beku. Merupakan jangkar katarsis yang mampu menyerap kembali energi kehampaan jika ditancapkan di pusat segel ketujuh."
        ),
        "love_letters_1892": ClueItem(
            "love_letters_1892",
            "Surat Cinta Jonathan dan Lilith",
            "Korespondensi rahasia musim gugur 1892 yang membuktikan penyesalan mendalam Lord Jonathan Rosewood setelah mengorbankan ingatan Lilith.",
            "Siang 4",
            "Dokumen",
            "images/clues/clue_love_letters.jpg",
            "Surat-surat ini membuktikan bahwa ritual Rosewood berakar dari rasa bersalah dan pengkhianatan cinta, bukan takdir ketuhanan yang tak terhindarkan."
        ),
        "seal_diagram": ClueItem(
            "seal_diagram",
            "Diagram Segel Ketujuh Victoria",
            "Peta okultisme analitis karya Victoria Ashbourne yang membedah polaritas enam pilar mawar dan mekanisme penetralan kutukan kehampaan.",
            "Malam 4",
            "Okultisme",
            "images/clues/clue_seal_diagram.jpg",
            "Kalkulasi ilmiah Victoria membuktikan polaritas segel dapat dibalik pada dentangan ketujuh lonceng jika kunci perak dan mawar hitam digunakan bersamaan."
        ),
        "silver_locket": ClueItem(
            "silver_locket",
            "Liontin Perak Nyonya Eleanor",
            "Pusaka perak murni pemberian Seraphina di depan perapian. Berfungsi melindungi kesadaran batin dari ilusi hipnotis di dalam kapel bawah tanah.",
            "Malam 5",
            "Pusaka",
            "images/clues/clue_silver_locket.jpg",
            "Ditempa dari perak pegunungan utara dengan doa perlindungan seorang ibu. Melindungi pemakainya dari kehilangan memori dan delusi darah di ruang bawah tanah."
        ),
        "silver_key": ClueItem(
            "silver_key",
            "Kunci Perak Kapel Evelyn",
            "Kunci kuno yang tergantung di leher Evelyn selama seratus empat puluh dua tahun. Membuka gerbang utama menuju altar kapel bawah tanah.",
            "Malam 6",
            "Kunci",
            "images/clues/clue_silver_key.jpg",
            "Kunci kuno empat silinder berukir pedang ksatria dan sulur mawar. Satu-satunya kunci sah yang dapat membuka gerbang menuju Kapel Segel Ketujuh."
        )
    }

## Fungsi bantuan untuk menambah bukti
init python:
    def unlock_clue(clue_id):
        if clue_id not in evidence_list:
            evidence_list.append(clue_id)
            renpy.play("audio/sfx/sfx_page_turn.wav", channel="sound")
            renpy.notify(_("Bukti Baru Ditemukan: ") + _(all_clues[clue_id].name))
            if len(evidence_list) >= 3:
                unlock_achievement("ach_detective", "Mata Sang Peneliti")

## =========================================================================
## LAYAR MODAL SHOWCASE BUKTI VISUAL (EVIDENCE INSPECTION SHOWCASE)
## =========================================================================
screen evidence_showcase(clue_id, from_journal=False):
    modal True
    zorder 100

    $ clue = all_clues.get(clue_id)
    $ is_in_journal = from_journal or (renpy.get_screen("evidence_journal") is not None)

    if is_in_journal:
        key "game_menu" action [Play("sound", "audio/sfx/sfx_gui_click.wav"), Hide("evidence_showcase")]
    else:
        key "game_menu" action [Play("sound", "audio/sfx/sfx_journal_close.wav"), Return()]

    add Solid("#09060ced")

    if clue:
        ## Ornate Victorian Dossier Modal
        fixed:
            xalign 0.5
            yalign 0.5
            xsize 1380
            ysize 830

            add "gui/dossier_modal_bg.png" xalign 0.5 yalign 0.5

            vbox:
                xalign 0.5
                ypos 18
                xsize 1320
                spacing 10

                ## Header Bar (above the gold divider line at y=95)
                hbox:
                    xfill True
                    ysize 72
                    xpos 30

                    vbox:
                        yalign 0.5
                        spacing 2
                        text _("PENYELIDIKAN BARANG BUKTI") size 20 color "#f39c12" bold True
                        text _(clue.name) size 34 color "#ecf0f1" bold True
                    button:
                        background "gui/action_btn_idle.png"
                        hover_background "gui/action_btn_hover.png"
                        xsize 200
                        ysize 50
                        xalign 0.5
                        yalign 0.5
                        if is_in_journal:
                            action [Play("sound", "audio/sfx/sfx_gui_click.wav"), Hide("evidence_showcase")]
                        else:
                            action [Play("sound", "audio/sfx/sfx_journal_close.wav"), Return()]
                        focus_mask True

                        hbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 15
                            text _("Tutup (X)") size 16 color "#f4ede2" hover_color "#fff8e7" bold True outlines [ (1, "#0d0712", 0, 1) ]

                null height 4

                ## Content Area
                hbox:
                    spacing 30
                    xpos 30

                    ## Evidence Image with Ornate Frame
                    fixed:
                        xsize 520
                        ysize 520

                        add "gui/evidence_frame_border.png" xalign 0.5 yalign 0.5

                        if clue.image_path:
                            add Transform(clue.image_path, size=(490, 490)) xalign 0.5 yalign 0.5
                        else:
                            text _("Ilustrasi Tidak Tersedia") size 20 color "#7f8c8d" xalign 0.5 yalign 0.5

                    ## Detail Information Panel
                    vbox:
                        xsize 700
                        spacing 12

                        ## Category & Date Tags
                        hbox:
                            spacing 16
                            frame:
                                background Solid("#2a1520dd")
                                padding (14, 6)
                                hbox:
                                    spacing 6
                                    text "✦" size 12 color "#e74c3c" yalign 0.5
                                    text _(clue.category) size 17 color "#f5a0a0" bold True outlines [ (1, "#0d0712", 0, 1) ]

                            frame:
                                background Solid("#1a1a2cdd")
                                padding (14, 6)
                                hbox:
                                    spacing 6
                                    text "✦" size 12 color "#5dade2" yalign 0.5
                                    text _(clue.date_found) size 17 color "#a8d8ea" bold True outlines [ (1, "#0d0712", 0, 1) ]

                        null height 4

                        ## Observation Notes
                        hbox:
                            spacing 8
                            text "✦" size 13 color "#d4af37" yalign 0.5
                            text _("Catatan Observasi:") size 18 color "#f3c77c" bold True outlines [ (1, "#0d0712", 0, 1) ]
                        text _(clue.description) size 19 color "#e8e2d5" justify True outlines [ (1, "#08050b", 0, 1) ]

                        null height 6

                        ## Analysis & Deduction Panel
                        frame:
                            xfill True
                            background Solid("#10091500")
                            padding (0, 0)
                            vbox:
                                spacing 8
                                ## Subtle divider
                                frame:
                                    xfill True
                                    ysize 1
                                    background Solid("#c59b4c44")
                                hbox:
                                    spacing 8
                                    text "✦" size 13 color "#9b7ec2" yalign 0.5
                                    text _("Analisis & Deduksi Investigasi:") size 17 color "#c9a8e8" bold True outlines [ (1, "#0d0712", 0, 1) ]
                                text _(clue.deduction_note) size 18 color "#d6d0c8" italic True justify True outlines [ (1, "#08050b", 0, 1) ]

                null height 10

                ## Bottom Action Button (Ornate Plaque Style)
                hbox:
                    xalign 0.5
                    button:
                        background "gui/inspect_retire_idle.png"
                        hover_background "gui/inspect_retire_hover.png"
                        xsize 480
                        ysize 54
                        if is_in_journal:
                            action [Play("sound", "audio/sfx/sfx_gui_click.wav"), Hide("evidence_showcase")]
                        else:
                            action [Play("sound", "audio/sfx/sfx_journal_close.wav"), Return()]
                        focus_mask True

                        hbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 12
                            text "✦" size 13 color "#d4af37" yalign 0.5
                            if is_in_journal:
                                text _("Kembali ke Jurnal Investigasi") size 16 color "#f4ede2" hover_color "#fff8e7" bold True yalign 0.5 outlines [ (1, "#180a10", 0, 1) ]
                            else:
                                text _("Simpan ke Jurnal Investigasi") size 16 color "#f4ede2" hover_color "#fff8e7" bold True yalign 0.5 outlines [ (1, "#180a10", 0, 1) ]
                            text "✦" size 13 color "#d4af37" yalign 0.5

## Label bantuan untuk memicu showcase bukti
label inspect_clue(clue_id):
    $ unlock_clue(clue_id)
    play sound sfx_page
    call screen evidence_showcase(clue_id)
    return
