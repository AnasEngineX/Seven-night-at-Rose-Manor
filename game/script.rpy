## script.rpy
## Titik Masuk Utama dan Konfigurasi Visual Seven Nights at Rose Manor

## Definisi Visual Latar Belakang (Resolusi Penuh 1920x1080)
image bg_gate = "images/bg_gate.jpg"
image bg_manor_hall = "images/bg_manor_hall.jpg"
image bg_guest_room = "images/bg_guest_room.jpg"
image bg_guest_bed_pov = "images/bg_guest_bed_pov.jpg"
image bg_portrait_gallery = "images/bg_portrait_gallery.jpg"
image bg_rose_garden = "images/bg_rose_garden.jpg"
image bg_library = "images/bg_library.jpg"
image bg_seraphina_room = "images/bg_seraphina_room.jpg"
image bg_ritual_chamber = "images/bg_ritual_chamber.jpg"
image bg_music_room = "images/bg_music_room.jpg"
image bg_conservatory = "images/bg_conservatory.jpg"
image bg_balcony = "images/bg_balcony.jpg"
image bg_tavern = "images/bg_tavern.jpg"
image bg_carriage_interior = "images/bg_carriage_interior.jpg"
image bg_chapel = "images/bg_chapel.jpg"

## Definisi Partikel Atmosfer Sinematik (Gothic Visual Effects)
image snow_particles = SnowBlossom("images/particles/snowflake.png", count=45, border=50, xspeed=(-35, 35), yspeed=(90, 180), start=2.0, fast=True)
image rose_petals = SnowBlossom("images/particles/rose_petal.png", count=25, border=50, xspeed=(-45, 45), yspeed=(75, 150), start=1.5, fast=True)

## Definisi Event CG Sinematik (Resolusi Penuh 1920x1080)
image cg_first_meeting = "images/cg/cg_first_meeting.jpg"
image cg_balcony_promise = "images/cg/cg_balcony_promise.jpg"
image cg_piano_duet = "images/cg/cg_piano_duet.jpg"
image cg_ritual_climax = "images/cg/cg_ritual_climax.jpg"
image cg_dawn_embrace = "images/cg/cg_dawn_embrace.jpg"
image cg_hollow_cycle = "images/cg/cg_hollow_cycle.jpg"

## Definisi Transform Posisi Layar Karakter (Mencegah Sprite Saling Menimpa)
transform sprite_left:
    xalign 0.18
    yalign 1.0
    zoom 0.85

transform sprite_center:
    xalign 0.5
    yalign 1.0
    zoom 0.85

transform sprite_right:
    xalign 0.82
    yalign 1.0
    zoom 0.85

transform sprite_mid_left:
    xalign 0.32
    yalign 1.0
    zoom 0.85

transform sprite_mid_right:
    xalign 0.68
    yalign 1.0
    zoom 0.85

## Definisi Visual Karakter (Sprite Transparan Tanpa Latar Belakang)
## Variasi Ekspresi dan Busana Seraphina
image seraphina neutral = Transform("images/seraphina_neutral.png", yalign=1.0, zoom=0.85)
image seraphina smile = Transform("images/seraphina_smile.png", yalign=1.0, zoom=0.85)
image seraphina sad = Transform("images/seraphina_sad.png", yalign=1.0, zoom=0.85)
image seraphina serious = Transform("images/seraphina_serious.png", yalign=1.0, zoom=0.85)
image seraphina angry = Transform("images/seraphina_serious.png", yalign=1.0, zoom=0.85)
image seraphina surprised = Transform("images/seraphina_surprised.png", yalign=1.0, zoom=0.85)

## Variasi Busana Khusus Seraphina
image seraphina gothic = Transform("images/seraphina_gothic.png", yalign=1.0, zoom=0.85)
image seraphina night = Transform("images/seraphina_night.png", yalign=1.0, zoom=0.85)
image seraphina nightgown = Transform("images/seraphina_night.png", yalign=1.0, zoom=0.85)
image seraphina mourning = Transform("images/seraphina_mourning.png", yalign=1.0, zoom=0.85)
image seraphina dawn = Transform("images/seraphina_dawn.png", yalign=1.0, zoom=0.85)
image seraphina pure = Transform("images/seraphina_dawn.png", yalign=1.0, zoom=0.85)

## Variasi Ekspresi Karakter Pendukung
## Evelyn Hart
image evelyn neutral = Transform("images/evelyn_neutral.png", yalign=1.0, zoom=0.85)
image evelyn smile = Transform("images/evelyn_smile.png", yalign=1.0, zoom=0.85)
image evelyn serious = Transform("images/evelyn_serious.png", yalign=1.0, zoom=0.85)
image evelyn sad = Transform("images/evelyn_serious.png", yalign=1.0, zoom=0.85)
image evelyn surprised = Transform("images/evelyn_surprised.png", yalign=1.0, zoom=0.85)

## Victoria Ashbourne
image victoria neutral = Transform("images/victoria_neutral.png", yalign=1.0, zoom=0.85)
image victoria smile = Transform("images/victoria_smile.png", yalign=1.0, zoom=0.85)
image victoria serious = Transform("images/victoria_serious.png", yalign=1.0, zoom=0.85)
image victoria sad = Transform("images/victoria_sad.png", yalign=1.0, zoom=0.85)
image victoria surprised = Transform("images/victoria_surprised.png", yalign=1.0, zoom=0.85)

## Lilith Vane
image lilith neutral = Transform("images/lilith_neutral.png", yalign=1.0, zoom=0.85)
image lilith smile = Transform("images/lilith_smile.png", yalign=1.0, zoom=0.85)
image lilith sad = Transform("images/lilith_sad.png", yalign=1.0, zoom=0.85)
image lilith surprised = Transform("images/lilith_surprised.png", yalign=1.0, zoom=0.85)

## Label Permainan Dimulai
label start:
    $ mc_name = "Guest"
    $ night = 1
    $ ser_aff = 0
    $ ser_trust = 0
    $ evidence = 0
    $ lilith_truth = False
    $ victoria_alliance = False

    jump prologue
