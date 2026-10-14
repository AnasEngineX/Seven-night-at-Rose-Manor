# tools/translate_game.py
# Script to translate Ren'Py dialogue and string blocks into natural, fluent English

import os
import re
import json
import urllib.request
import urllib.parse
import time

CACHE_FILE = r"e:\Seven Nights at Rose Manor\tools\tl_cache.json"
os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)

cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)
    except Exception as e:
        print("Warning loading cache:", e)

def save_cache():
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Warning saving cache:", e)

# Gothic Victorian refinement glossary for natural literary translation
GLOSSARY_REPLACEMENTS = [
    (r"\bRose Manor's\b", "Rose Manor's"),
    (r"\bthe Rose Manor residence\b", "Rose Manor"),
    (r"\bthe manor\b", "the manor"),
    (r"\bhead of the servant\b", "head maid"),
    (r"\bhead servant\b", "head maid"),
    (r"\bthe waitress\b", "the maid"),
    (r"\bthe tavern keeper\b", "the innkeeper"),
    (r"\bMr\. \[mc_name\]\b", "[mc_name]"),
    (r"\bMr\. Guest\b", "Guest"),
    (r"\bMiss Seraphina\b", "Lady Seraphina"),
    (r"\bMiss Victoria\b", "Lady Victoria"),
    (r"\bMiss Lilith\b", "Lady Lilith"),
    (r"\bLady Eleanor\b", "Lady Eleanor"),
    (r"\bseventh seal\b", "Seventh Seal"),
    (r"\bSeventh seal\b", "Seventh Seal"),
    (r"\bRosewood clan\b", "House of Rosewood"),
    (r"\bRosewood dynasty\b", "House of Rosewood"),
    (r"\bblood oath\b", "blood oath"),
    (r"\bunderground chapel\b", "underground chapel"),
    (r"\bsilver locket\b", "silver locket"),
    (r"\bsilver key\b", "silver key"),
    (r"\bblack rose\b", "black rose"),
    (r"\brose brooch\b", "rose brooch"),
]

def refine_english(text):
    for pattern, repl in GLOSSARY_REPLACEMENTS:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    return text

def translate_str(text):
    text = text.strip()
    if not text:
        return text
    if text in cache:
        return cache[text]

    tag_map = {}
    counter = [0]
    def repl(m):
        key = f"___TAG{counter[0]}___"
        tag_map[key] = m.group(0)
        counter[0] += 1
        return key

    # Mask Ren'Py tags like [mc_name], {i}, {/i}, {b}, {/b}
    masked = re.sub(r"(\[[a-zA-Z0-9_!]+\]|\{[a-zA-Z0-9_=/]+\}|\{/[a-zA-Z0-9_]+\})", repl, text)

    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=id&tl=en&dt=t&q=" + urllib.parse.quote(masked)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                res = "".join([item[0] for item in data[0] if item[0]])
                for k, v in tag_map.items():
                    res = res.replace(k, v).replace(k.lower(), v)
                res = refine_english(res)
                cache[text] = res
                time.sleep(0.04)
                return res
        except Exception as e:
            time.sleep(1.2 * (attempt + 1))

    cache[text] = text
    return text

def extract_quote_content(line):
    # Find first unescaped " and last "
    first_q = line.find('"')
    last_q = line.rfind('"')
    if first_q != -1 and last_q != -1 and first_q < last_q:
        prefix = line[:first_q]
        content = line[first_q + 1:last_q]
        suffix = line[last_q + 1:]
        return prefix, content, suffix
    return None, None, None

def process_file(filepath):
    print(f"Processing: {os.path.basename(filepath)}")
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    n = len(lines)
    changed_count = 0

    while i < n:
        line = lines[i]

        # Case 1: Dialogue translation block
        # Line i is: '    # speaker "Indonesian text"' or '    # "Indonesian text"'
        # Line i + 1 is: '    speaker "..."' or '    "..."'
        stripped = line.lstrip()
        if stripped.startswith("#") and ('"' in stripped):
            content_after_hash = stripped[1:].strip()
            # Check if this commented line looks like Ren'Py dialogue (ends with quote)
            if content_after_hash.endswith('"') and (i + 1 < n):
                next_line = lines[i + 1]
                next_stripped = next_line.lstrip()
                if not next_stripped.startswith("#") and ('"' in next_stripped) and next_stripped.endswith('"\n'):
                    # We have a dialogue pair!
                    # Extract original Indonesian text from commented line
                    p_orig, orig_text, s_orig = extract_quote_content(content_after_hash)
                    p_curr, curr_text, s_curr = extract_quote_content(next_line)

                    if orig_text is not None and curr_text is not None:
                        # Translate orig_text
                        trans_text = translate_str(orig_text)
                        # Escape unescaped double quotes inside the translation
                        trans_text = trans_text.replace('\\"', '"').replace('"', '\\"')
                        new_line = f'{p_curr}"{trans_text}"{s_curr}'
                        new_lines.append(line)
                        new_lines.append(new_line)
                        changed_count += 1
                        i += 2
                        continue

        # Case 2: String translation block (old / new)
        if stripped.startswith('old "') and stripped.endswith('"\n') and (i + 1 < n):
            next_line = lines[i + 1]
            next_stripped = next_line.lstrip()
            if next_stripped.startswith('new "') and next_stripped.endswith('"\n'):
                p_old, orig_text, s_old = extract_quote_content(line)
                p_new, curr_text, s_new = extract_quote_content(next_line)
                if orig_text is not None and curr_text is not None:
                    trans_text = translate_str(orig_text)
                    trans_text = trans_text.replace('\\"', '"').replace('"', '\\"')
                    new_line = f'{p_new}"{trans_text}"{s_new}'
                    new_lines.append(line)
                    new_lines.append(new_line)
                    changed_count += 1
                    i += 2
                    continue

        new_lines.append(line)
        i += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    save_cache()
    print(f"  Finished {os.path.basename(filepath)}: translated {changed_count} lines")

if __name__ == "__main__":
    import sys
    tl_dir = r"e:\Seven Nights at Rose Manor\game\tl\english"
    if len(sys.argv) > 1:
        target_files = [os.path.join(tl_dir, sys.argv[1])]
    else:
        files = [
            "story_prologue.rpy",
            "story_night1.rpy",
            "story_day2.rpy",
            "story_night2.rpy",
            "story_day3.rpy",
            "story_night3.rpy",
            "story_day4.rpy",
            "story_night4.rpy",
            "story_day5.rpy",
            "story_night5.rpy",
            "story_day6.rpy",
            "story_night6.rpy",
            "story_day7.rpy",
            "story_night7.rpy",
            "endings.rpy",
            "story_epilogues.rpy",
        ]
        target_files = [os.path.join(tl_dir, f) for f in files if os.path.exists(os.path.join(tl_dir, f))]

    for fpath in target_files:
        process_file(fpath)

    print("All translation processing complete!")
