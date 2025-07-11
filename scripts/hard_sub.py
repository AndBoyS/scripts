"""Hard-sub a batch of files using ffmpeg."""

import subprocess
from pathlib import Path


def main(
    video_dir: Path,
    video_ext: str,
    output_dir: Path | None = None,
    sub_stream: int | None = None,
    sub_dir: Path | None = None,
    sub_ext: str | None = None,
    dry_run: bool = False,
) -> None:
    """Hard-sub videos using FFmpeg.

    Arguments:
        video_dir -- Path to the directory containing input videos
        video_ext -- File extension of the input videos
        output_dir -- Path to the directory where output videos will be saved
        sub_stream -- Index of the subtitle stream in the videos to use, sub_dir and sub_ext must not be set (default: {None})
        sub_dir -- Path to the directory containing subtitle files, with the same names as videos, sub_stream must not be set (default: {None})
        sub_ext -- File extension of the subtitle files, sub_stream must not be set (default: {None})
        dry_run -- don't execute commands, just print them

    Raises:
        ValueError: If neither sub_stream nor both sub_dir and sub_ext are provided,
        or if all three parameters are provided simultaneously
    """
    if output_dir is None:
        output_dir = video_dir
    output_dir.mkdir(exist_ok=True)

    sub_file_params_set = sub_dir is not None and sub_ext is not None

    if sub_stream is None and not sub_file_params_set:
        raise ValueError("sub_dir and sub_ext or sub_stream must be set")
    if sub_stream is not None and sub_file_params_set:
        raise ValueError(
            "sub_dir and sub_ext and sub_stream are all set, you must either set sub_dir and sub_ext or sub_stream"
        )

    for video_path in video_dir.glob(f"*{video_ext}"):
        output_path = output_dir / video_path.name
        if output_dir == video_dir:
            output_path = output_path.with_stem(f"{output_path.stem} (Hardsubbed)")

        if sub_file_params_set:
            assert sub_dir is not None
            assert sub_ext is not None
            cur_sub_path = sub_dir / video_path.with_suffix(sub_ext).name
            cmd = f"""ffmpeg -i \"{video_path}\" -filter_complex subtitles='{cur_sub_path}' -crf 18 -c:v libx265 -c:a copy -shortest \"{output_path}\""""

        else:
            cmd = f"""ffmpeg -i \"{video_path}\" -filter_complex "[0:v][0:s]overlay[v]" -map "[v]" -map 0:a -c:a copy -shortest \"{output_path}\""""

        if dry_run:
            print(cmd)
        else:
            subprocess.call(cmd, shell=True, text=True)


if __name__ == "__main__":
    # Use subs embedded in videos
    main(
        sub_stream=0,
        video_dir=Path("/Users/user/Main/aboba/Active/t"),
        output_dir=Path("/Users/user/Main/aboba/Active/t"),
        video_ext=".mkv",
        dry_run=False,
    )
    # Use subs from directory
    # main(
    #     video_dir=Path("/Users/user/Main/aboba/Active/t"),
    #     sub_dir=Path("/Users/user/Main/aboba/Archive/untitled folder"),
    #     sub_ext=".ass",
    #     video_ext=".mkv",
    #     dry_run=False,
    # )
