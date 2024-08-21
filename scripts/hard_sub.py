"""Hard-sub a batch of files using ffmpeg."""

from pathlib import Path
import subprocess


video_ext = ".mkv"
video_dir = Path("/Users/user/Main/aboba/Videos/Original")
output_dir = Path("/Users/user/Main/aboba/Videos/Hardsubbed")

sub_stream = 0
# sub_stream = None

# sub_dir = Path("/Users/user/Main/aboba/Videos/Subs")
# sub_ext = ".ass"
sub_dir = None
sub_ext = None


def main(
    video_dir: Path,
    video_ext: str,
    output_dir: Path,
    sub_stream: int | None = None,
    sub_dir: Path | None = None,
    sub_ext: str | None = None,
) -> None:
    """Hard-sub videos using FFmpeg.

    Arguments:
        video_dir -- Path to the directory containing input videos
        video_ext -- File extension of the input videos
        output_dir -- Path to the directory where output videos will be saved
        sub_stream -- Index of the subtitle stream in the videos to use, sub_dir and sub_ext must not be set (default: {None})
        sub_dir -- Path to the directory containing subtitle files, with the same names as videos, sub_stream must not be set (default: {None})
        sub_ext -- File extension of the subtitle files, sub_stream must not be set (default: {None})

    Raises:
        ValueError: If neither sub_stream nor both sub_dir and sub_ext are provided,
        or if all three parameters are provided simultaneously
    """
    output_dir.mkdir(exist_ok=True)

    sub_file_params_set = sub_dir is not None and sub_ext is not None

    if sub_stream is None and not sub_file_params_set:
        raise ValueError("sub_dir and sub_ext or sub_stream must be set")
    if sub_stream is not None and sub_file_params_set:
        raise ValueError(
            "sub_dir and sub_ext and sub_stream are all set, you must either set sub_dir and sub_ext or sub_stream"
        )

    for video_path in video_dir.glob(f"*{video_ext}"):
        if sub_file_params_set:
            assert sub_dir is not None
            assert sub_ext is not None
            sub_str = f"""subtitles='{sub_dir / video_path.with_suffix(sub_ext).name}'"""
        else:
            sub_str = f"""\"[0:v:0]subtitles=\'{video_path}\':si={sub_stream}[v]\" -map \"[v]\" -map 0:a:0 -c:a copy"""

        output_path = output_dir / video_path.name

        subprocess.call(
            f"""ffmpeg -i '{video_path}' -filter_complex {sub_str} -crf 18 -c:v libx265 '{output_path}'""",
            shell=True,
        )


if __name__ == "__main__":
    main(
        video_dir=video_dir,
        video_ext=video_ext,
        output_dir=output_dir,
        sub_stream=sub_stream,
        sub_dir=sub_dir,
        sub_ext=sub_ext,
    )
