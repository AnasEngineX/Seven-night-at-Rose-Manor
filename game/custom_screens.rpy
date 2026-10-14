## custom_screens.rpy
## Layar Khusus Jurnal Investigasi dan Status Hubungan Karakter Seven Nights at Rose Manor

## =========================================================================
## SCREEN: JURNAL INVESTIGASI BUKTI (EVIDENCE NOTEBOOK)
## =========================================================================
style vscrollbar:
    unscrollable "hide"

screen evidence_journal():
    tag menu
    modal True

    add Solid("#08050bee")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1640
        ysize 940
        background "gui/ornate_modal_bg.png"
        padding (45, 36)

        vbox:
            spacing 12

            ## Header Jurnal Ornate Victorian
            hbox:
                xfill True
                vbox:
                    spacing 4
                    hbox:
                        spacing 10
                        text "✦" size 15 color "#d4af37" yalign 0.5
                        text _("JURNAL INVESTIGASI ROSE MANOR") size 32 color "#f4ede2" bold True outlines [ (2, "#0d0712", 0, 1) ]
                        text "✦" size 15 color "#d4af37" yalign 0.5
                    text _("Catatan barang bukti dan petunjuk okultisme yang telah berhasil dikumpulkan selama penyelidikan tujuh malam.") size 16 color "#b8a892"

                button:
                    background "gui/action_btn_idle.png"
                    hover_background "gui/action_btn_hover.png"
                    xsize 200
                    ysize 42
                    xalign 1.0
                    yalign 0.5
                    action [Play("sound", "audio/sfx/sfx_journal_close.wav"), Return()]
                    focus_mask True

                    hbox:
                        xalign 0.5
                        yalign 0.7
                        spacing 15
                
                        text _("Tutup Jurnal") size 15 color "#f4ede2" hover_color "#fff8e7" bold True yalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]
                

            null height 2
            add "gui/header_divider.png" xalign 0.5
            null height 4

            hbox:
                spacing 30

                ## Daftar Bukti di sebelah kiri
                frame:
                    xsize 560
                    ysize 730
                    background Frame("gui/ornate_card_bg.png", 16, 16)
                    padding (20, 20)

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 10

                            if not evidence_list:
                                text _("Belum ada bukti khusus yang tercatat dalam jurnal.") size 20 color "#7f8c8d" italic True outlines [ (1, "#0d0712", 0, 1) ]
                            else:
                                for clue_key in evidence_list:
                                    $ clue = all_clues.get(clue_key)
                                    if clue:
                                        button:
                                            xfill True
                                            action [Play("sound", "audio/sfx/sfx_clue_select.wav"), SetVariable("selected_clue_id", clue_key)]
                                            idle_background Frame("gui/ornate_card_bg.png", 14, 14)
                                            hover_background Frame("gui/ornate_card_hover.png", 14, 14)
                                            padding (16, 12)

                                            vbox:
                                                spacing 4
                                                hbox:
                                                    spacing 6
                                                    text "✦" size 11 color ("#d4af37" if selected_clue_id == clue_key else "#8a7550") yalign 0.5
                                                    text _(clue.name) size 21 color ("#f8edd9" if selected_clue_id == clue_key else "#d0c4b0") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                                hbox:
                                                    text _(clue.category) size 15 color "#e58282"
                                                    text "  •  " size 14 color "#705c48"
                                                    text _(clue.date_found) size 15 color "#d4af37"

                ## Detail Bukti di sebelah kanan
                frame:
                    xsize 970
                    ysize 730
                    background Frame("gui/ornate_card_bg.png", 16, 16)
                    padding (30, 24)

                    $ current_clue = all_clues.get(selected_clue_id)
                    if current_clue:
                        vbox:
                            spacing 12
                            hbox:
                                spacing 10
                                text "✦" size 16 color "#c59b4c" yalign 0.5
                                text _(current_clue.name) size 30 color "#f5e8d5" bold True outlines [ (1, "#0d0712", 0, 1) ]

                            hbox:
                                spacing 16
                                frame:
                                    background Solid("#2a1520dd")
                                    padding (12, 4)
                                    text _(current_clue.category) size 16 color "#f5a0a0" bold True outlines [ (1, "#0d0712", 0, 1) ]
                                frame:
                                    background Solid("#1a1a2cdd")
                                    padding (12, 4)
                                    text _(current_clue.date_found) size 16 color "#a8d8ea" bold True outlines [ (1, "#0d0712", 0, 1) ]

                            null height 2

                            hbox:
                                spacing 24
                                fixed:
                                    xsize 250
                                    ysize 250
                                    add "gui/evidence_frame_border.png" xalign 0.5 yalign 0.5 xsize 250 ysize 250
                                    if current_clue.image_path:
                                        add Transform(current_clue.image_path, size=(230, 230)) xalign 0.5 yalign 0.5
                                    else:
                                        text _("No Image") size 18 color "#7f8c8d" xalign 0.5 yalign 0.5

                                vbox:
                                    xsize 620
                                    spacing 8
                                    hbox:
                                        spacing 6
                                        text "✦" size 12 color "#c59b4c" yalign 0.5
                                        text _("Deskripsi Bukti:") size 18 color "#d4af37" bold True outlines [ (1, "#0d0712", 0, 1) ]
                                    text _(current_clue.description) size 18 color "#e4ddcf" justify True outlines [ (1, "#08050b", 0, 1) ]

                            null height 2

                            frame:
                                xfill True
                                background Frame("gui/ornate_card_bg.png", 12, 12)
                                padding (18, 14)
                                vbox:
                                    spacing 6
                                    hbox:
                                        spacing 6
                                        text "✦" size 12 color "#9b7ec2" yalign 0.5
                                        text _("Analisis & Deduksi Investigasi:") size 17 color "#c9a8e8" bold True outlines [ (1, "#0d0712", 0, 1) ]
                                    text _(current_clue.deduction_note) size 17 color "#d6d0c8" italic True justify True outlines [ (1, "#08050b", 0, 1) ]

                            null height 8

                            ## Tombol Inspeksi Visual Penuh digeser lebih ke kiri/tengah agar proporsional
                            hbox:
                                xalign 0.5
                                button:
                                    background "gui/action_btn_idle.png"
                                    hover_background "gui/action_btn_hover.png"
                                    xsize 340
                                    ysize 46
                                    action [Play("sound", "audio/sfx/sfx_page_turn.wav"), Show("evidence_showcase", clue_id=selected_clue_id, from_journal=True)]
                                    focus_mask True

                                    hbox:
                                        xalign 1
                                        yalign 0.5
                                        spacing 10
                                        text _("Inspeksi Visual Penuh") size 16 color "#f4ede2" hover_color "#fff8e7" bold True yalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]

                                
                    else:
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            text _("Pilih salah satu bukti di panel kiri untuk membaca catatan rincian.") size 22 color "#7f8c8d" italic True

default selected_clue_id = "invitation_letter"

## =========================================================================
## SCREEN: STATUS HUBUNGAN KARAKTER (RELATIONSHIP STATUS)
## =========================================================================
screen character_status():
    tag menu
    modal True

    add Solid("#08050bee")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1640
        ysize 940
        background "gui/ornate_modal_bg.png"
        padding (45, 36)

        vbox:
            spacing 14

            ## Header Status Ornate Victorian
            hbox:
                xfill True
                vbox:
                    spacing 4
                    hbox:
                        spacing 10
                        text "✦" size 15 color "#d4af37" yalign 0.5
                        text _("STATUS HUBUNGAN & KEPERCAYAAN KARAKTER") size 32 color "#f4ede2" bold True outlines [ (2, "#0d0712", 0, 1) ]
                        text "✦" size 15 color "#d4af37" yalign 0.5
                    text _("Tingkat kedekatan emosional (Affection) dan tingkat keterbukaan rahasia (Trust) para penghuni Rose Manor.") size 16 color "#b8a892"

                button:
                    background "gui/action_btn_idle.png"
                    hover_background "gui/action_btn_hover.png"
                    xsize 200
                    ysize 42
                    xalign 1.0
                    yalign 0.5
                    action [Play("sound", "audio/sfx/sfx_journal_close.wav"), Return()]
                    focus_mask True

                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 8
                        text "✦" size 11 color "#d4af37" yalign 0.5
                        text _("Kembali") size 15 color "#f4ede2" hover_color "#fff8e7" bold True yalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]
                        text "✦" size 11 color "#d4af37" yalign 0.5

            null height 2
            add "gui/header_divider.png" xalign 0.5
            null height 10

            grid 2 2:
                spacing 24
                xalign 0.5

                ## 1. Seraphina Rosewood
                frame:
                    xsize 760
                    ysize 280
                    background Frame("gui/ornate_card_bg.png", 16, 16)
                    padding (22, 18)

                    hbox:
                        spacing 20
                        yalign 0.5
                        add "gui/portraits/status_seraphina.png" yalign 0.5

                        vbox:
                            yalign 0.5
                            spacing 6
                            hbox:
                                spacing 8
                                text "✦" size 13 color "#e74c3c" yalign 0.5
                                text _("Seraphina Rosewood") size 23 color "#f4ede2" bold True outlines [ (1, "#0d0712", 0, 1) ]
                            text _("Pewaris Rose Manor • Rute Blood Rose") size 14 color "#c59b4c" italic True

                            null height 2

                            hbox:
                                spacing 10
                                text _("Kedekatan Emosional (Affection):") size 14 color "#e8dfd3"
                                text "[ser_aff] / 5" size 14 color "#d4af37" bold True
                            bar value ser_aff range 5 xsize 530 ysize 12 left_bar "gui/bar_fill.png" right_bar "gui/bar_track.png" thumb None

                            hbox:
                                spacing 10
                                text _("Tingkat Kepercayaan (Trust):") size 14 color "#e8dfd3"
                                text "[ser_trust] / 5" size 14 color "#d4af37" bold True
                            bar value ser_trust range 5 xsize 530 ysize 12 left_bar "gui/bar_fill.png" right_bar "gui/bar_track.png" thumb None

                            null height 2
                            text _("Ikatan misterius yang menuntun Anda ke rahasia terdalam mansion terkutuk ini.") size 13 color "#a89f91"

                ## 2. Evelyn Hart
                frame:
                    xsize 760
                    ysize 280
                    background Frame("gui/ornate_card_bg.png", 16, 16)
                    padding (22, 18)

                    hbox:
                        spacing 20
                        yalign 0.5
                        add "gui/portraits/status_evelyn.png" yalign 0.5

                        vbox:
                            yalign 0.5
                            spacing 7
                            hbox:
                                spacing 8
                                text "✦" size 13 color "#f39c12" yalign 0.5
                                text _("Evelyn Hart") size 23 color "#f4ede2" bold True outlines [ (1, "#0d0712", 0, 1) ]
                            text _("Kepala Pelayan • Penjaga Sumpah Abadi 1884") size 14 color "#c59b4c" italic True

                            null height 2

                            if "silver_key" in evidence_list:
                                frame:
                                    background Solid("#1b2f1fdd")
                                    padding (10, 4)
                                    text _("Kunci Perak Kapel Telah Diserahkan — Sumpah Bebas") size 14 color "#69e094" bold True outlines [ (1, "#0d0712", 0, 1) ]
                            else:
                                frame:
                                    background Solid("#2f1f1add")
                                    padding (10, 4)
                                    text _("Terikat Sumpah Darah — Menjaga Gerbang Kapel") size 14 color "#f09855" bold True outlines [ (1, "#0d0712", 0, 1) ]

                            null height 2
                            text _("Evelyn mengamati kepribadian dan ketulusan niat MC terhadap keselamatan Nona Seraphina serta rahasia leluhur keluarga.") size 13 color "#a89f91"

                ## 3. Lilith Vane
                frame:
                    xsize 760
                    ysize 280
                    background Frame("gui/ornate_card_bg.png", 16, 16)
                    padding (22, 18)

                    hbox:
                        spacing 20
                        yalign 0.5
                        add "gui/portraits/status_lilith.png" yalign 0.5

                        vbox:
                            yalign 0.5
                            spacing 7
                            hbox:
                                spacing 8
                                text "✦" size 13 color "#9b59b6" yalign 0.5
                                text _("Lilith Vane") size 23 color "#f4ede2" bold True outlines [ (1, "#0d0712", 0, 1) ]
                            text _("Roh Taman Mawar • Jiwa Terikat Musim Gugur 1892") size 14 color "#c59b4c" italic True

                            null height 2

                            if lilith_truth:
                                frame:
                                    background Solid("#1b2f1fdd")
                                    padding (10, 4)
                                    text _("Kebenaran Terungkap — Menanti Pembebasan Segel") size 14 color "#69e094" bold True outlines [ (1, "#0d0712", 0, 1) ]
                            else:
                                frame:
                                    background Solid("#2c1b30dd")
                                    padding (10, 4)
                                    text _("Misteri Kematian Masih Terselubung Kabut") size 14 color "#d18be6" bold True outlines [ (1, "#0d0712", 0, 1) ]

                            null height 2
                            text _("Korban ritual pertama keluarga Rosewood yang mencari keadilan dan pelepasan arwah dari belenggu mawar hitam.") size 13 color "#a89f91"

                ## 4. Victoria Ashbourne
                frame:
                    xsize 760
                    ysize 280
                    background Frame("gui/ornate_card_bg.png", 16, 16)
                    padding (22, 18)

                    hbox:
                        spacing 20
                        yalign 0.5
                        add "gui/portraits/status_victoria.png" yalign 0.5

                        vbox:
                            yalign 0.5
                            spacing 7
                            hbox:
                                spacing 8
                                text "✦" size 13 color "#e67e22" yalign 0.5
                                text _("Victoria Ashbourne") size 23 color "#f4ede2" bold True outlines [ (1, "#0d0712", 0, 1) ]
                            text _("Peneliti Okultisme • Tamu Sayap Timur") size 14 color "#c59b4c" italic True

                            null height 2

                            if victoria_alliance:
                                frame:
                                    background Solid("#1b2f1fdd")
                                    padding (10, 4)
                                    text _("Aliansi Penuh Terjalin — Diagram Segel Aktif") size 14 color "#69e094" bold True outlines [ (1, "#0d0712", 0, 1) ]
                            else:
                                frame:
                                    background Solid("#22232edd")
                                    padding (10, 4)
                                    text _("Skeptis & Mengawasi Secara Independen") size 14 color "#9db6d8" bold True outlines [ (1, "#0d0712", 0, 1) ]

                            null height 2
                            text _("Meneruskan buku catatan penelitian kakek buyutnya untuk membongkar anomali Rose Manor dan mengungkap artefak.") size 13 color "#a89f91"


## =========================================================================
## 3. LAYAR GALERI EVENT CG (Sinematik Kenangan Rose Manor)
## =========================================================================
screen cg_gallery():
    tag menu
    modal True

    add Solid("#08050bee")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1640
        ysize 940
        background "gui/ornate_modal_bg.png"
        padding (45, 36)

        vbox:
            spacing 14

            ## Header Galeri Ornate Victorian
            hbox:
                xfill True
                vbox:
                    spacing 4
                    hbox:
                        spacing 10
                        text "✦" size 15 color "#d4af37" yalign 0.5
                        text _("GALERI ILUSTRASI KENANGAN (EVENT CG)") size 32 color "#f4ede2" bold True outlines [ (2, "#0d0712", 0, 1) ]
                        text "✦" size 15 color "#d4af37" yalign 0.5
                    text _("Koleksi momen sinematik penting dan kenangan yang terabadikan selama penyelidikan tujuh malam di Rose Manor.") size 16 color "#b8a892"

                button:
                    background "gui/action_btn_idle.png"
                    hover_background "gui/action_btn_hover.png"
                    xsize 200
                    ysize 42
                    xalign 1.0
                    yalign 0.5
                    action Return()
                    focus_mask True

                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 8
                        text "✦" size 11 color "#d4af37" yalign 0.5
                        text _("Kembali") size 15 color "#f4ede2" hover_color "#fff8e7" bold True yalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]
                        text "✦" size 11 color "#d4af37" yalign 0.5

            null height 2
            add "gui/header_divider.png" xalign 0.5
            null height 8

            grid 3 2:
                spacing 24
                xalign 0.5

                ## 1. Pertemuan Pertama
                frame:
                    xsize 490
                    ysize 350
                    background Frame("gui/ornate_card_bg.png", 14, 14)
                    padding (14, 14)
                    vbox:
                        spacing 10
                        fixed:
                            xsize 368
                            ysize 210
                            xalign 0.5
                            if persistent.cg_first_meeting:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_first_meeting_thumb.jpg"
                                    hover "images/cg/thumbs/cg_first_meeting_thumb.jpg"
                                    action Show("cg_viewer", cg_path="images/cg/cg_first_meeting.jpg")
                            else:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_locked_thumb.jpg"
                                    action None
                            add "gui/cg_thumb_border.png" xalign 0.5 yalign 0.5
                        vbox:
                            xalign 0.5
                            spacing 2
                            if persistent.cg_first_meeting:
                                text _("1. Pertemuan di Aula Gotik") size 19 color "#f4ede2" bold True xalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]
                                text _("Malam 1 • Kehadiran Nona Seraphina") size 15 color "#c59b4c" xalign 0.5
                            else:
                                text _("1. ??? (Terkunci)") size 19 color "#7a6e60" bold True xalign 0.5
                                text _("Malam 1 • Belum Terbuka") size 15 color "#524638" xalign 0.5

                ## 2. Nocturne Lilith
                frame:
                    xsize 490
                    ysize 350
                    background Frame("gui/ornate_card_bg.png", 14, 14)
                    padding (14, 14)
                    vbox:
                        spacing 10
                        fixed:
                            xsize 368
                            ysize 210
                            xalign 0.5
                            if persistent.cg_piano_duet:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_piano_duet_thumb.jpg"
                                    hover "images/cg/thumbs/cg_piano_duet_thumb.jpg"
                                    action Show("cg_viewer", cg_path="images/cg/cg_piano_duet.jpg")
                            else:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_locked_thumb.jpg"
                                    action None
                            add "gui/cg_thumb_border.png" xalign 0.5 yalign 0.5
                        vbox:
                            xalign 0.5
                            spacing 2
                            if persistent.cg_piano_duet:
                                text _("2. Melodi Nocturne Lilith") size 19 color "#f4ede2" bold True xalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]
                                text _("Malam 2 • Gema Piano Ruang Musik") size 15 color "#c59b4c" xalign 0.5
                            else:
                                text _("2. ??? (Terkunci)") size 19 color "#7a6e60" bold True xalign 0.5
                                text _("Malam 2 • Belum Terbuka") size 15 color "#524638" xalign 0.5

                ## 3. Janji di Bawah Rembulan
                frame:
                    xsize 490
                    ysize 350
                    background Frame("gui/ornate_card_bg.png", 14, 14)
                    padding (14, 14)
                    vbox:
                        spacing 10
                        fixed:
                            xsize 368
                            ysize 210
                            xalign 0.5
                            if persistent.cg_balcony_promise:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_balcony_promise_thumb.jpg"
                                    hover "images/cg/thumbs/cg_balcony_promise_thumb.jpg"
                                    action Show("cg_viewer", cg_path="images/cg/cg_balcony_promise.jpg")
                            else:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_locked_thumb.jpg"
                                    action None
                            add "gui/cg_thumb_border.png" xalign 0.5 yalign 0.5
                        vbox:
                            xalign 0.5
                            spacing 2
                            if persistent.cg_balcony_promise:
                                text _("3. Janji di Menara Jam") size 19 color "#f4ede2" bold True xalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]
                                text _("Hari 5 • Di Balik Cakrawala Salju") size 15 color "#c59b4c" xalign 0.5
                            else:
                                text _("3. ??? (Terkunci)") size 19 color "#7a6e60" bold True xalign 0.5
                                text _("Hari 5 • Belum Terbuka") size 15 color "#524638" xalign 0.5

                ## 4. Altar Segel Ketujuh
                frame:
                    xsize 490
                    ysize 350
                    background Frame("gui/ornate_card_bg.png", 14, 14)
                    padding (14, 14)
                    vbox:
                        spacing 10
                        fixed:
                            xsize 368
                            ysize 210
                            xalign 0.5
                            if persistent.cg_ritual_climax:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_ritual_climax_thumb.jpg"
                                    hover "images/cg/thumbs/cg_ritual_climax_thumb.jpg"
                                    action Show("cg_viewer", cg_path="images/cg/cg_ritual_climax.jpg")
                            else:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_locked_thumb.jpg"
                                    action None
                            add "gui/cg_thumb_border.png" xalign 0.5 yalign 0.5
                        vbox:
                            xalign 0.5
                            spacing 2
                            if persistent.cg_ritual_climax:
                                text _("4. Altar Segel Ketujuh") size 19 color "#f4ede2" bold True xalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]
                                text _("Malam 7 • Klimaks Ritual Kapel") size 15 color "#c59b4c" xalign 0.5
                            else:
                                text _("4. ??? (Terkunci)") size 19 color "#7a6e60" bold True xalign 0.5
                                text _("Malam 7 • Belum Terbuka") size 15 color "#524638" xalign 0.5

                ## 5. Fajar di Rose Manor
                frame:
                    xsize 490
                    ysize 350
                    background Frame("gui/ornate_card_bg.png", 14, 14)
                    padding (14, 14)
                    vbox:
                        spacing 10
                        fixed:
                            xsize 368
                            ysize 210
                            xalign 0.5
                            if persistent.cg_dawn_embrace:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_dawn_embrace_thumb.jpg"
                                    hover "images/cg/thumbs/cg_dawn_embrace_thumb.jpg"
                                    action Show("cg_viewer", cg_path="images/cg/cg_dawn_embrace.jpg")
                            else:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_locked_thumb.jpg"
                                    action None
                            add "gui/cg_thumb_border.png" xalign 0.5 yalign 0.5
                        vbox:
                            xalign 0.5
                            spacing 2
                            if persistent.cg_dawn_embrace:
                                text _("5. Fajar di Rose Manor") size 19 color "#f4ede2" bold True xalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]
                                text _("True Ending • Mekarnya Mawar Abadi") size 15 color "#c59b4c" xalign 0.5
                            else:
                                text _("5. ??? (Terkunci)") size 19 color "#7a6e60" bold True xalign 0.5
                                text _("True Ending • Belum Terbuka") size 15 color "#524638" xalign 0.5

                ## 6. Siklus Abadi
                frame:
                    xsize 490
                    ysize 350
                    background Frame("gui/ornate_card_bg.png", 14, 14)
                    padding (14, 14)
                    vbox:
                        spacing 10
                        fixed:
                            xsize 368
                            ysize 210
                            xalign 0.5
                            if persistent.cg_hollow_cycle:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_hollow_cycle_thumb.jpg"
                                    hover "images/cg/thumbs/cg_hollow_cycle_thumb.jpg"
                                    action Show("cg_viewer", cg_path="images/cg/cg_hollow_cycle.jpg")
                            else:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.5
                                    idle "images/cg/thumbs/cg_locked_thumb.jpg"
                                    action None
                            add "gui/cg_thumb_border.png" xalign 0.5 yalign 0.5
                        vbox:
                            xalign 0.5
                            spacing 2
                            if persistent.cg_hollow_cycle:
                                text _("6. Siklus Abadi") size 19 color "#f4ede2" bold True xalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]
                                text _("Bad Ending • Gerbang Tanpa Ingatan") size 15 color "#c59b4c" xalign 0.5
                            else:
                                text _("6. ??? (Terkunci)") size 19 color "#7a6e60" bold True xalign 0.5
                                text _("Bad Ending • Belum Terbuka") size 15 color "#524638" xalign 0.5


## Layar Penampil CG Layar Penuh
screen cg_viewer(cg_path):
    modal True
    zorder 100

    button:
        action Hide("cg_viewer")
        add cg_path:
            xalign 0.5
            yalign 0.5
            xsize 1920
            ysize 1080

        frame:
            xalign 0.98
            yalign 0.03
            background Solid("#0c0712bb")
            padding (16, 8)
            hbox:
                spacing 8
                text "✦" size 12 color "#d4af37" yalign 0.5
                text _("Klik di mana saja untuk kembali") size 15 color "#e8dfd3" yalign 0.5
                text "✦" size 12 color "#d4af37" yalign 0.5


## =========================================================================
## 4. LAYAR PELACAK PENCAPAIAN & ENDING (ACHIEVEMENTS & ENDINGS TRACKER)
## =========================================================================
screen achievements_tracker():
    tag menu
    modal True

    add Solid("#08050bee")

    $ total_endings = 3
    $ unlocked_endings = (1 if persistent.ending_bad else 0) + (1 if persistent.ending_good else 0) + (1 if persistent.ending_true else 0)
    $ ending_pct = int((unlocked_endings / float(total_endings)) * 100)

    $ total_achs = 8
    $ unlocked_achs = (
        (1 if persistent.ach_invitation else 0) +
        (1 if persistent.ach_detective else 0) +
        (1 if persistent.ach_trust else 0) +
        (1 if persistent.ach_affection else 0) +
        (1 if persistent.ach_victoria else 0) +
        (1 if persistent.ach_lilith else 0) +
        (1 if persistent.ach_curse_breaker else 0) +
        (1 if persistent.ach_collector else 0)
    )
    $ ach_pct = int((unlocked_achs / float(total_achs)) * 100)

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1640
        ysize 940
        background "gui/ornate_modal_bg.png"
        padding (45, 36)

        vbox:
            spacing 14

            ## Header Pencapaian Ornate Victorian
            hbox:
                xfill True
                vbox:
                    spacing 4
                    hbox:
                        spacing 10
                        text "✦" size 15 color "#d4af37" yalign 0.5
                        text _("DAFTAR PENCAPAIAN & AKHIR KISAH") size 32 color "#f4ede2" bold True outlines [ (2, "#0d0712", 0, 1) ]
                        text "✦" size 15 color "#d4af37" yalign 0.5
                    text _("Lacak seluruh akhir kisah yang telah terbuka dan prestasi investigasi selama mengungkap rahasia Rose Manor.") size 16 color "#b8a892"

                button:
                    background "gui/action_btn_idle.png"
                    hover_background "gui/action_btn_hover.png"
                    xsize 200
                    ysize 42
                    xalign 1.0
                    yalign 0.5
                    action Return()
                    focus_mask True

                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 8
                        text "✦" size 11 color "#d4af37" yalign 0.5
                        text _("Kembali") size 15 color "#f4ede2" hover_color "#fff8e7" bold True yalign 0.5 outlines [ (1, "#0d0712", 0, 1) ]
                        text "✦" size 11 color "#d4af37" yalign 0.5

            null height 2
            add "gui/header_divider.png" xalign 0.5
            null height 6

            hbox:
                spacing 28

                ## Panel Kiri: 3 Ending Utama
                frame:
                    xsize 620
                    ysize 740
                    background Frame("gui/ornate_card_bg.png", 16, 16)
                    padding (24, 20)

                    vbox:
                        spacing 12

                        hbox:
                            spacing 8
                            text "✦" size 14 color "#d4af37" yalign 0.5
                            text _("Tiga Akhir Cerita (Endings)") size 24 color "#f4ede2" bold True outlines [ (1, "#0d0712", 0, 1) ]

                        hbox:
                            text (_("Progres: ") + str(unlocked_endings) + " / " + str(total_endings) + " (" + str(ending_pct) + "%)") size 17 color "#d4af37" bold True
                        bar value unlocked_endings range total_endings xsize 570 ysize 14 left_bar "gui/bar_fill.png" right_bar "gui/bar_track.png" thumb None

                        null height 4

                        ## Ending 1: Bad Ending
                        frame:
                            xfill True
                            ysize 175
                            background Frame("gui/ornate_card_bg.png", 12, 12)
                            padding (16, 12)
                            vbox:
                                spacing 4
                                hbox:
                                    spacing 6
                                    text "✦" size 11 color ("#e74c3c" if persistent.ending_bad else "#665545") yalign 0.5
                                    text (_("1. Bad Ending: Siklus Abadi") if persistent.ending_bad else _("1. Bad Ending: ??? (Terkunci)")) size 19 color ("#f5a0a0" if persistent.ending_bad else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                
                                if persistent.ending_bad:
                                    frame:
                                        background Solid("#2a1215dd")
                                        padding (8, 2)
                                        text _("STATUS: TERBUKA (TAMAT)") size 13 color "#e74c3c" bold True
                                    text _("Gagal mengumpulkan cukup bukti. Ingatan terhapus, dan kutukan siklus tujuh malam kembali berulang dari awal.") size 15 color "#d0c4b0"
                                else:
                                    frame:
                                        background Solid("#19131cdd")
                                        padding (8, 2)
                                        text _("STATUS: BELUM TERBUKA") size 13 color "#7a6e60"
                                    text _("Selesaikan malam ke-7 tanpa bukti penangkal ritual yang mencukupi.") size 15 color "#6b5d4f" italic True

                        ## Ending 2: Good Ending
                        frame:
                            xfill True
                            ysize 175
                            background Frame("gui/ornate_card_bg.png", 12, 12)
                            padding (16, 12)
                            vbox:
                                spacing 4
                                hbox:
                                    spacing 6
                                    text "✦" size 11 color ("#5dade2" if persistent.ending_good else "#665545") yalign 0.5
                                    text (_("2. Good Ending: Bunga Harapan") if persistent.ending_good else _("2. Good Ending: ??? (Terkunci)")) size 19 color ("#a8d8ea" if persistent.ending_good else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                
                                if persistent.ending_good:
                                    frame:
                                        background Solid("#142230dd")
                                        padding (8, 2)
                                        text _("STATUS: TERBUKA (TAMAT)") size 13 color "#5dade2" bold True
                                    text _("Kepercayaan penuh pada Seraphina meredakan keputusasaannya. Kalian berdua memilih melangkah maju bersama menyongsong fajar.") size 15 color "#d0c4b0"
                                else:
                                    frame:
                                        background Solid("#19131cdd")
                                        padding (8, 2)
                                        text _("STATUS: BELUM TERBUKA") size 13 color "#7a6e60"
                                    text _("Raih kedekatan emosional dan kepercayaan tinggi dengan Seraphina pada malam terakhir.") size 15 color "#6b5d4f" italic True

                        ## Ending 3: True Ending
                        frame:
                            xfill True
                            ysize 175
                            background Frame("gui/ornate_card_bg.png", 12, 12)
                            padding (16, 12)
                            vbox:
                                spacing 4
                                hbox:
                                    spacing 6
                                    text "✦" size 11 color ("#f1c40f" if persistent.ending_true else "#665545") yalign 0.5
                                    text (_("3. True Ending: Fajar di Rose Manor") if persistent.ending_true else _("3. True Ending: ??? (Terkunci)")) size 19 color ("#f9e79f" if persistent.ending_true else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                
                                if persistent.ending_true:
                                    frame:
                                        background Solid("#2f2712dd")
                                        padding (8, 2)
                                        text _("STATUS: TERBUKA (KEBENARAN MUTLAK)") size 13 color "#f1c40f" bold True
                                    text _("Seluruh bukti terangkai, rahasia Lilith terungkap, dan bantuan Victoria menghancurkan altar ritual selamanya.") size 15 color "#d0c4b0"
                                else:
                                    frame:
                                        background Solid("#19131cdd")
                                        padding (8, 2)
                                        text _("STATUS: BELUM TERBUKA") size 13 color "#7a6e60"
                                    text _("Kumpulkan seluruh bukti, jalin aliansi dengan Victoria, dan bebaskan arwah Lilith.") size 15 color "#6b5d4f" italic True

                ## Panel Kanan: Daftar 8 Trofi Pencapaian
                frame:
                    xsize 930
                    ysize 740
                    background Frame("gui/ornate_card_bg.png", 16, 16)
                    padding (24, 20)

                    vbox:
                        spacing 12

                        hbox:
                            spacing 8
                            text "✦" size 14 color "#d4af37" yalign 0.5
                            text _("Trofi & Prestasi Khusus (Achievements)") size 24 color "#f4ede2" bold True outlines [ (1, "#0d0712", 0, 1) ]

                        hbox:
                            text (_("Progres Pencapaian: ") + str(unlocked_achs) + " / " + str(total_achs) + " (" + str(ach_pct) + "%)") size 17 color "#d4af37" bold True
                        bar value unlocked_achs range total_achs xsize 880 ysize 14 left_bar "gui/bar_fill.png" right_bar "gui/bar_track.png" thumb None

                        null height 4

                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            xsize 880
                            ysize 600

                            vbox:
                                spacing 10

                                ## Trofi 1
                                frame:
                                    xfill True
                                    background Frame("gui/ornate_card_bg.png", 12, 12)
                                    padding (16, 12)
                                    vbox:
                                        spacing 3
                                        hbox:
                                            spacing 6
                                            text "✦" size 12 color ("#d4af37" if persistent.ach_invitation else "#665545") yalign 0.5
                                            text _("Undangan Terlarang") size 20 color ("#f4ede2" if persistent.ach_invitation else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                            null width 10
                                            text (_("TERBUKA") if persistent.ach_invitation else _("TERKUNCI")) size 13 color ("#69e094" if persistent.ach_invitation else "#e74c3c") bold True yalign 0.5
                                        text _("Menerima surat bermaterai mawar dan melangkahi gerbang Rose Manor di malam pertama.") size 16 color ("#d0c4b0" if persistent.ach_invitation else "#6b5d4f")

                                ## Trofi 2
                                frame:
                                    xfill True
                                    background Frame("gui/ornate_card_bg.png", 12, 12)
                                    padding (16, 12)
                                    vbox:
                                        spacing 3
                                        hbox:
                                            spacing 6
                                            text "✦" size 12 color ("#d4af37" if persistent.ach_detective else "#665545") yalign 0.5
                                            text _("Mata Sang Peneliti") size 20 color ("#f4ede2" if persistent.ach_detective else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                            null width 10
                                            text (_("TERBUKA") if persistent.ach_detective else _("TERKUNCI")) size 13 color ("#69e094" if persistent.ach_detective else "#e74c3c") bold True yalign 0.5
                                        text _("Menemukan sedikitnya 3 barang bukti penting selama menyelidiki mansion.") size 16 color ("#d0c4b0" if persistent.ach_detective else "#6b5d4f")

                                ## Trofi 3
                                frame:
                                    xfill True
                                    background Frame("gui/ornate_card_bg.png", 12, 12)
                                    padding (16, 12)
                                    vbox:
                                        spacing 3
                                        hbox:
                                            spacing 6
                                            text "✦" size 12 color ("#d4af37" if persistent.ach_trust else "#665545") yalign 0.5
                                            text _("Kepercayaan Sang Mawar") size 20 color ("#f4ede2" if persistent.ach_trust else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                            null width 10
                                            text (_("TERBUKA") if persistent.ach_trust else _("TERKUNCI")) size 13 color ("#69e094" if persistent.ach_trust else "#e74c3c") bold True yalign 0.5
                                        text _("Mendapatkan tingkat kepercayaan penuh (Trust >= 3) dari Seraphina Rosewood.") size 16 color ("#d0c4b0" if persistent.ach_trust else "#6b5d4f")

                                ## Trofi 4
                                frame:
                                    xfill True
                                    background Frame("gui/ornate_card_bg.png", 12, 12)
                                    padding (16, 12)
                                    vbox:
                                        spacing 3
                                        hbox:
                                            spacing 6
                                            text "✦" size 12 color ("#d4af37" if persistent.ach_affection else "#665545") yalign 0.5
                                            text _("Kuncup Bunga Kasih") size 20 color ("#f4ede2" if persistent.ach_affection else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                            null width 10
                                            text (_("TERBUKA") if persistent.ach_affection else _("TERKUNCI")) size 13 color ("#69e094" if persistent.ach_affection else "#e74c3c") bold True yalign 0.5
                                        text _("Meraih kedekatan emosional mendalam (Affection >= 3) dengan Seraphina.") size 16 color ("#d0c4b0" if persistent.ach_affection else "#6b5d4f")

                                ## Trofi 5
                                frame:
                                    xfill True
                                    background Frame("gui/ornate_card_bg.png", 12, 12)
                                    padding (16, 12)
                                    vbox:
                                        spacing 3
                                        hbox:
                                            spacing 6
                                            text "✦" size 12 color ("#d4af37" if persistent.ach_victoria else "#665545") yalign 0.5
                                            text _("Aliansi Rahasia") size 20 color ("#f4ede2" if persistent.ach_victoria else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                            null width 10
                                            text (_("TERBUKA") if persistent.ach_victoria else _("TERKUNCI")) size 13 color ("#69e094" if persistent.ach_victoria else "#e74c3c") bold True yalign 0.5
                                        text _("Membentuk aliansi penyelidikan okultisme bersama Victoria Ashbourne.") size 16 color ("#d0c4b0" if persistent.ach_victoria else "#6b5d4f")

                                ## Trofi 6
                                frame:
                                    xfill True
                                    background Frame("gui/ornate_card_bg.png", 12, 12)
                                    padding (16, 12)
                                    vbox:
                                        spacing 3
                                        hbox:
                                            spacing 6
                                            text "✦" size 12 color ("#d4af37" if persistent.ach_lilith else "#665545") yalign 0.5
                                            text _("Pembebasan Jiwa yang Hilang") size 20 color ("#f4ede2" if persistent.ach_lilith else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                            null width 10
                                            text (_("TERBUKA") if persistent.ach_lilith else _("TERKUNCI")) size 13 color ("#69e094" if persistent.ach_lilith else "#e74c3c") bold True yalign 0.5
                                        text _("Mengungkap misteri nisan tanpa nama dan kebenaran masa lalu Lilith Vane.") size 16 color ("#d0c4b0" if persistent.ach_lilith else "#6b5d4f")

                                ## Trofi 7
                                frame:
                                    xfill True
                                    background Frame("gui/ornate_card_bg.png", 12, 12)
                                    padding (16, 12)
                                    vbox:
                                        spacing 3
                                        hbox:
                                            spacing 6
                                            text "✦" size 12 color ("#d4af37" if persistent.ach_curse_breaker else "#665545") yalign 0.5
                                            text _("Pembebas Kutukan Abadi") size 20 color ("#f4ede2" if persistent.ach_curse_breaker else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                            null width 10
                                            text (_("TERBUKA") if persistent.ach_curse_breaker else _("TERKUNCI")) size 13 color ("#69e094" if persistent.ach_curse_breaker else "#e74c3c") bold True yalign 0.5
                                        text _("Menyelesaikan True Ending dan mematahkan ritual lingkaran mawar untuk selamanya.") size 16 color ("#d0c4b0" if persistent.ach_curse_breaker else "#6b5d4f")

                                ## Trofi 8
                                frame:
                                    xfill True
                                    background Frame("gui/ornate_card_bg.png", 12, 12)
                                    padding (16, 12)
                                    vbox:
                                        spacing 3
                                        hbox:
                                            spacing 6
                                            text "✦" size 12 color ("#d4af37" if persistent.ach_collector else "#665545") yalign 0.5
                                            text _("Kolektor Memori Abadi") size 20 color ("#f4ede2" if persistent.ach_collector else "#7a6e60") bold True outlines [ (1, "#0d0712", 0, 1) ]
                                            null width 10
                                            text (_("TERBUKA") if persistent.ach_collector else _("TERKUNCI")) size 13 color ("#69e094" if persistent.ach_collector else "#e74c3c") bold True yalign 0.5
                                        text _("Membuka seluruh koleksi ilustrasi Event CG di galeri kenangan.") size 16 color ("#d0c4b0" if persistent.ach_collector else "#6b5d4f")


## =========================================================================
## 5. LAYAR INVESTIGASI KAMAR INTERAKTIF (ROOM POINT-AND-CLICK INSPECTION)
## =========================================================================

## Transform Animasi Titik Sinar Investigasi (Luminous Beacon & Pulse Ring)
transform beacon_pulse:
    subpixel True
    anchor (0.5, 0.5)
    zoom 0.92 alpha 0.82
    easein 1.4 zoom 1.08 alpha 1.0
    easeout 1.4 zoom 0.92 alpha 0.82
    repeat

transform beacon_ring_expand:
    subpixel True
    anchor (0.5, 0.5)
    zoom 0.35 alpha 0.8
    easein 2.2 zoom 1.45 alpha 0.0
    repeat

transform beacon_hover_flare:
    subpixel True
    anchor (0.5, 0.5)
    easein 0.18 zoom 1.25 alpha 1.0

transform tooltip_fade:
    subpixel True
    alpha 0.0 yoffset 6
    easein 0.18 alpha 1.0 yoffset 0

screen room_inspection():
    modal True
    zorder 50

    default hovered_spot = None

    ## Header Spanduk Ornate Victorian (Tapered Filigree & Vignette)
    fixed:
        xpos 960
        ypos 24
        anchor (0.5, 0.0)
        xsize 1000
        ysize 88

        add "gui/inspect_header_banner.png" xalign 0.5 yalign 0.5

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 5

            hbox:
                xalign 0.5
                spacing 10
                text "✦" size 15 color "#c59b4c" yalign 0.5
                text _("Investigasi Kamar Tamu") size 20 bold True color "#f3c77c" yalign 0.5 outlines [ (1, "#1a0f05", 0, 1) ]
                text "✦" size 15 color "#c59b4c" yalign 0.5

            text _("Pilih sudut ruangan yang ingin Anda selidiki sebelum tidur."):
                xalign 0.5
                size 15
                italic True
                color "#d7d2c9"
                outlines [ (1, "#0a060d", 0, 1) ]

    ## -------------------------------------------------------------------------
    ## TITIK SINAR 1: Meja Tulis Mahoni (Kanan Bawah)
    ## -------------------------------------------------------------------------
    button:
        xpos 1620
        ypos 840
        anchor (0.5, 0.5)
        xsize 96
        ysize 96
        background None
        hover_background None
        action Return("inspect_desk")
        hovered SetScreenVariable("hovered_spot", "desk")
        unhovered SetScreenVariable("hovered_spot", None)

        fixed:
            xalign 0.5
            yalign 0.5
            xsize 96
            ysize 96

            add "gui/inspect_ring.png":
                xalign 0.5
                yalign 0.5
                at beacon_ring_expand

            if hovered_spot == "desk":
                add "gui/inspect_dot_hover.png":
                    xalign 0.5
                    yalign 0.5
                    at beacon_hover_flare
            else:
                add "gui/inspect_dot_idle.png":
                    xalign 0.5
                    yalign 0.5
                    at beacon_pulse

    if hovered_spot == "desk":
        frame:
            xpos 1550
            ypos 780
            anchor (1.0, 1.0)
            background Solid("#d4af3788")
            padding (1, 1)
            at tooltip_fade
            frame:
                background Solid("#0c0714f5")
                padding (18, 10)
                vbox:
                    spacing 4
                    hbox:
                        spacing 8
                        text "✦" size 15 color "#f1c40f"
                        text _("Meja Tulis Mahoni") size 20 color "#fdfefe" bold True
                    text _("Periksa laci antik") size 15 color "#e67e22"
                    text _("Klik untuk Menyelidiki") size 13 color "#85929e" italic True

    ## -------------------------------------------------------------------------
    ## TITIK SINAR 2: Perapian Marmer (Kanan Tengah)
    ## -------------------------------------------------------------------------
    button:
        xpos 1360
        ypos 690
        anchor (0.5, 0.5)
        xsize 96
        ysize 96
        background None
        hover_background None
        action Return("inspect_fireplace")
        hovered SetScreenVariable("hovered_spot", "fireplace")
        unhovered SetScreenVariable("hovered_spot", None)

        fixed:
            xalign 0.5
            yalign 0.5
            xsize 96
            ysize 96

            add "gui/inspect_ring.png":
                xalign 0.5
                yalign 0.5
                at beacon_ring_expand

            if hovered_spot == "fireplace":
                add "gui/inspect_dot_hover.png":
                    xalign 0.5
                    yalign 0.5
                    at beacon_hover_flare
            else:
                add "gui/inspect_dot_idle.png":
                    xalign 0.5
                    yalign 0.5
                    at beacon_pulse

    if hovered_spot == "fireplace":
        frame:
            xpos 1360
            ypos 620
            anchor (0.5, 1.0)
            background Solid("#e67e2288")
            padding (1, 1)
            at tooltip_fade
            frame:
                background Solid("#0c0714f5")
                padding (18, 10)
                vbox:
                    spacing 4
                    xalign 0.5
                    hbox:
                        spacing 8
                        xalign 0.5
                        text "✦" size 15 color "#e67e22"
                        text _("Perapian Marmer") size 20 color "#fdfefe" bold True
                    text _("Periksa bara api") size 15 color "#e74c3c" xalign 0.5
                    text _("Klik untuk Menyelidiki") size 13 color "#85929e" italic True xalign 0.5

    ## -------------------------------------------------------------------------
    ## TITIK SINAR 3: Cermin Kuno (Tengah Atas di atas Perapian)
    ## -------------------------------------------------------------------------
    button:
        xpos 1360
        ypos 270
        anchor (0.5, 0.5)
        xsize 96
        ysize 96
        background None
        hover_background None
        action Return("inspect_mirror")
        hovered SetScreenVariable("hovered_spot", "mirror")
        unhovered SetScreenVariable("hovered_spot", None)

        fixed:
            xalign 0.5
            yalign 0.5
            xsize 96
            ysize 96

            add "gui/inspect_ring.png":
                xalign 0.5
                yalign 0.5
                at beacon_ring_expand

            if hovered_spot == "mirror":
                add "gui/inspect_dot_hover.png":
                    xalign 0.5
                    yalign 0.5
                    at beacon_hover_flare
            else:
                add "gui/inspect_dot_idle.png":
                    xalign 0.5
                    yalign 0.5
                    at beacon_pulse

    if hovered_spot == "mirror":
        frame:
            xpos 1360
            ypos 340
            anchor (0.5, 0.0)
            background Solid("#3498db88")
            padding (1, 1)
            at tooltip_fade
            frame:
                background Solid("#0c0714f5")
                padding (18, 10)
                vbox:
                    spacing 4
                    xalign 0.5
                    hbox:
                        spacing 8
                        xalign 0.5
                        text "✦" size 15 color "#5dade2"
                        text _("Cermin Kuno") size 20 color "#fdfefe" bold True
                    text _("Tatapi pantulan diri") size 15 color "#3498db" xalign 0.5
                    text _("Klik untuk Menyelidiki") size 13 color "#85929e" italic True xalign 0.5

    ## -------------------------------------------------------------------------
    ## TITIK SINAR 4: Jendela Bersalju (Kanan Atas)
    ## -------------------------------------------------------------------------
    button:
        xpos 1730
        ypos 360
        anchor (0.5, 0.5)
        xsize 96
        ysize 96
        background None
        hover_background None
        action Return("inspect_window")
        hovered SetScreenVariable("hovered_spot", "window")
        unhovered SetScreenVariable("hovered_spot", None)

        fixed:
            xalign 0.5
            yalign 0.5
            xsize 96
            ysize 96

            add "gui/inspect_ring.png":
                xalign 0.5
                yalign 0.5
                at beacon_ring_expand

            if hovered_spot == "window":
                add "gui/inspect_dot_hover.png":
                    xalign 0.5
                    yalign 0.5
                    at beacon_hover_flare
            else:
                add "gui/inspect_dot_idle.png":
                    xalign 0.5
                    yalign 0.5
                    at beacon_pulse

    if hovered_spot == "window":
        frame:
            xpos 1660
            ypos 360
            anchor (1.0, 0.5)
            background Solid("#1abc9c88")
            padding (1, 1)
            at tooltip_fade
            frame:
                background Solid("#0c0714f5")
                padding (18, 10)
                vbox:
                    spacing 4
                    hbox:
                        spacing 8
                        text "✦" size 15 color "#48c9b0"
                        text _("Jendela Bersalju") size 20 color "#fdfefe" bold True
                    text _("Tatapi menara terkunci") size 15 color "#16a085"
                    text _("Klik untuk Menyelidiki") size 13 color "#85929e" italic True

    ## -------------------------------------------------------------------------
    ## TITIK SINAR 5: Ranjang Kanopi (Kiri Tengah - Istirahat / Selesai)
    ## -------------------------------------------------------------------------
    button:
        xpos 460
        ypos 660
        anchor (0.5, 0.5)
        xsize 96
        ysize 96
        background None
        hover_background None
        action Return("go_to_sleep")
        hovered SetScreenVariable("hovered_spot", "bed")
        unhovered SetScreenVariable("hovered_spot", None)

        fixed:
            xalign 0.5
            yalign 0.5
            xsize 96
            ysize 96

            add "gui/inspect_ring.png":
                xalign 0.5
                yalign 0.5
                at beacon_ring_expand

            if hovered_spot == "bed":
                add "gui/inspect_dot_hover.png":
                    xalign 0.5
                    yalign 0.5
                    at beacon_hover_flare
            else:
                add "gui/inspect_dot_sleep.png":
                    xalign 0.5
                    yalign 0.5
                    at beacon_pulse

    if hovered_spot == "bed":
        frame:
            xpos 460
            ypos 590
            anchor (0.5, 1.0)
            background Solid("#c0392b88")
            padding (1, 1)
            at tooltip_fade
            frame:
                background Solid("#0c0714f5")
                padding (18, 10)
                vbox:
                    spacing 4
                    xalign 0.5
                    hbox:
                        spacing 8
                        xalign 0.5
                        text "✦" size 15 color "#e74c3c"
                        text _("Ranjang Kanopi") size 20 color "#fdfefe" bold True
                    text _("Berbaring dan beristirahat") size 15 color "#f1c40f" xalign 0.5
                    text _("Klik untuk Selesai & Tidur") size 13 color "#85929e" italic True xalign 0.5

    ## -------------------------------------------------------------------------
    ## Tombol Ornate Victorian Bawah: Selesai Menyelidiki & Beristirahat
    ## -------------------------------------------------------------------------
    button:
        xpos 960
        ypos 955
        anchor (0.5, 0.5)
        xsize 480
        ysize 54
        background "gui/inspect_retire_idle.png"
        hover_background "gui/inspect_retire_hover.png"
        action Return("go_to_sleep")
        focus_mask True

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 12
            text "✦" size 13 color "#d4af37" yalign 0.5
            text _("Berbaring dan Beristirahat") size 17 color "#f4ede2" hover_color "#fff8e7" bold True yalign 0.5 outlines [ (1, "#180a10", 0, 1) ]
            text "✦" size 13 color "#d4af37" yalign 0.5


