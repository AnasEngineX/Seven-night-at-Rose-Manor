## variables.rpy
## Inisialisasi variabel status dan progres Seven Nights at Rose Manor

## Identitas MC dan Waktu
default mc_name = "Guest"
default night = 1

## Parameter Hubungan Karakter
default ser_aff = 0
default ser_trust = 0

## Parameter Investigasi dan Bukti
default evidence = 0
default evidence_list = []

## Flag Kejadian dan Keputusan Cerita
default lilith_truth = False
default victoria_alliance = False
default inspected_portrait = False
default evelyn_secret_noticed = False
default rose_necklace_examined = False
default third_floor_rule_broken = False

## Pelacak Buka Kunci Galeri CG (Persistent)
default persistent.cg_first_meeting = False
default persistent.cg_balcony_promise = False
default persistent.cg_piano_duet = False
default persistent.cg_ritual_climax = False
default persistent.cg_dawn_embrace = False
default persistent.cg_hollow_cycle = False

## Pelacak Ending Terbuka (Persistent)
default persistent.ending_bad = False
default persistent.ending_good = False
default persistent.ending_true = False

## Pelacak Pencapaian / Prestasi (Persistent Achievements)
default persistent.ach_invitation = False      # Tiba di Rose Manor
default persistent.ach_detective = False       # Mengumpulkan >= 5 bukti
default persistent.ach_trust = False           # Kepercayaan Seraphina >= 3
default persistent.ach_affection = False       # Afeksi Seraphina >= 3
default persistent.ach_victoria = False        # Aliansi Victoria
default persistent.ach_lilith = False          # Kebenaran Lilith
default persistent.ach_curse_breaker = False   # Menyelesaikan True Ending
default persistent.ach_collector = False       # Membuka seluruh CG

init python:
    def unlock_achievement(ach_id, title):
        if not getattr(persistent, ach_id, False):
            setattr(persistent, ach_id, True)
            renpy.notify("Pencapaian Terbuka: " + title)

## Definisi Aset Audio (Musik Latar BGM & Efek Suara SFX)
define audio.bgm_manor = "audio/music/bgm_manor_hall.wav"
define audio.bgm_night = "audio/music/bgm_night_mystery.wav"
define audio.bgm_nocturne = "audio/music/bgm_lilith_nocturne.wav"
define audio.bgm_ritual = "audio/music/bgm_ritual_tension.wav"
define audio.bgm_dawn = "audio/music/bgm_dawn_liberation.wav"

define audio.sfx_bell = "audio/sfx/sfx_bell_chime.wav"
define audio.sfx_thunder = "audio/sfx/sfx_thunder.wav"
define audio.sfx_piano = "audio/sfx/sfx_piano_key.wav"
define audio.sfx_creak = "audio/sfx/sfx_door_creak.wav"
define audio.sfx_page = "audio/sfx/sfx_page_turn.wav"
define audio.sfx_break = "audio/sfx/sfx_crystal_break.wav"
define audio.sfx_clock = "audio/sfx/sfx_clock_tick.wav"
define audio.sfx_wind = "audio/sfx/sfx_wind_howl.wav"
define audio.sfx_fire = "audio/sfx/sfx_fire_crackle.wav"

## GUI SFX Definitions
define audio.sfx_click = "audio/sfx/sfx_gui_click.wav"
define audio.sfx_hover = "audio/sfx/sfx_gui_hover.wav"
define audio.sfx_journal_open = "audio/sfx/sfx_journal_open.wav"
define audio.sfx_journal_close = "audio/sfx/sfx_journal_close.wav"
define audio.sfx_clue_select = "audio/sfx/sfx_clue_select.wav"
define audio.sfx_choice = "audio/sfx/sfx_choice.wav"


