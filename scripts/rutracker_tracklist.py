"""Specify path to a folder with music files and get formatted list of songs to use in rutracker post."""

import math
from mutagen.mp3 import MP3
from pathlib import Path
from natsort import natsorted

SONGS_PTRN = "*.mp3"

album_dir = Path(
    "/Users/user/Main/Music/[Discographies]/[Torrenting]/Clarence Clarity - Collection (2013-2015)/2020 - Dead Screen Scrolls"
)


def main(album_dir: Path) -> None:
    """Print formatted text with album tracklist.

    Arguments:
        album_dir -- Path to the album
    """
    track_paths = natsorted(path for path in album_dir.glob(SONGS_PTRN))

    for i, path in enumerate(track_paths, start=1):
        name = path.name
        name = " ".join(name.split()[1:])
        name = name.split(".")[0]

        audio_len = MP3(path).info.length
        len_min = int(audio_len // 60)
        len_sec = int(math.ceil(audio_len % 60))
        print(f"[b]{i:0>2}.[/b] {name} [color=gray]({len_min:0>2}:{len_sec:0>2})[/color]")


if __name__ == "__main__":
    main(album_dir)
