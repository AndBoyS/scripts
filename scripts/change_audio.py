"""Change audio in mkv from one format to another"""

import subprocess
from pathlib import Path

FILE_EXT = ".mkv"

TEMP = "temp"


def main(
    input_dir: Path,
    output_dir: Path | None = None,
    audio_in: str = ".ogg",
    audio_out: str = ".mp3",
    copy_suffix: str = " (Mp3 Audio)",
) -> None:
    if output_dir is not None:
        output_dir.mkdir(exist_ok=True)

    for video_path in input_dir.glob(f"*{FILE_EXT}"):
        out_path = (
            output_dir / video_path.name if output_dir else video_path.with_stem(f"{video_path.stem}{copy_suffix}")
        )
        audio_in_path = out_path.parent / f"{TEMP}{audio_in}"
        audio_out_path = out_path.parent / f"{TEMP}{audio_out}"

        extract_audio_cmd = f"""ffmpeg -i '{video_path}' -q:a 0 -map a -c copy '{audio_in_path}'"""
        subprocess.run(extract_audio_cmd, shell=True, text=True, check=True)

        convert_audio_cmd = f"""ffmpeg -i '{audio_in_path}' '{audio_out_path}'"""
        subprocess.run(convert_audio_cmd, shell=True, text=True, check=True)

        create_video_cmd = f"""ffmpeg -y -i '{video_path}' -i '{audio_out_path}' -c copy -map 0 -map -0:a -map 1:a -shortest '{out_path}'"""
        subprocess.run(create_video_cmd, shell=True, text=True, check=True)

        audio_in_path.unlink()
        audio_out_path.unlink()


if __name__ == "__main__":
    main(
        input_dir=Path("/Users/user/Main/aboba/Active/t"),
        # output_dir=Path("/Users/user/Main/aboba/Active/temp/out"),
    )
