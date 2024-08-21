"""Embed audio in a batch of files using ffmpeg.

Video and sub files are expected to have same names
"""

from pathlib import Path
import subprocess


video_ext = ".mkv"
audio_ext = ".mka"
video_dir = Path("/Users/user/Main/Content/Video")
audio_dir = Path("/Users/user/Main/Content/Video/Dub")
output_dir = Path("/Users/user/Main/Content/Video/Embedded dub")


def main(  # noqa: D103
    video_dir: Path,
    video_ext: str,
    audio_dir: Path,
    audio_ext: str,
    output_dir: Path,
) -> None:
    output_dir.mkdir(exist_ok=True)

    for video_path in video_dir.glob(f"*{video_ext}"):
        audio_path = audio_dir / video_path.with_suffix(audio_ext).name
        output_path = output_dir / video_path.name

        subprocess.call(
            f"""ffmpeg -i '{video_path}' -i '{audio_path}' -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 '{output_path}'""",
            shell=True,
        )


if __name__ == "__main__":
    main(
        video_dir=video_dir,
        video_ext=video_ext,
        audio_dir=audio_dir,
        audio_ext=audio_ext,
        output_dir=output_dir,
    )
