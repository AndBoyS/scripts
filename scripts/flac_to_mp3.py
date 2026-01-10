import subprocess
from pathlib import Path

from src.utils import tqdm


def main() -> None:
    MUSIC_DIR = Path.home() / "Main/Music"
    SOURCE_DIR = MUSIC_DIR / "[Discographies]"
    TRASH_DIR = MUSIC_DIR / "[Flac backup]"
    for p in tqdm(list(SOURCE_DIR.rglob("*.flac"))):
        new_p = p.with_suffix(".mp3")
        if new_p.exists():
            continue
        subprocess.call(f'ffmpeg -i "{p}" -ab 320k "{new_p}"', shell=True)
        backup_p = TRASH_DIR / p.relative_to(SOURCE_DIR)
        backup_p.parent.mkdir(exist_ok=True, parents=True)
        p.rename(backup_p)


if __name__ == "__main__":
    main()
