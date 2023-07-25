import argparse
from pathlib import Path

args = None

def parse_args():
    global args
    if args is not None:
        return args
    """Parse comand-line options"""

    parser = argparse.ArgumentParser(
        description="Sort files by extension. Can unpack supported archives.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog = "Usage examples:\n\
            sorter.py -v -o /usr/home/root/downloads /usr/home/root/must_be_sorted -s settings.json\n\
        or  sorter.py -v -o /usr/home/root/downloads /usr/home/root/must_be_sorted -d images -e jpg bmp jpeg -f move"
    )  # ,exit_on_error=False
    parser.add_argument(
        "directories",
        help    = "Directories list to process, if not specified used current directory.",
        type    = Path,
        default = Path().cwd(),
        action  = "store",
        required= False,
        nargs   = '*'
    )
    parser.add_argument(
        "-k", "--keep-empty-dir",
        help        = "Don't remove empty directories.",
        action      = "store_true",
        default     = False,
        required    = False
    )
    parser.add_argument(
        "-n", "--normalize",
        help        = "Normalize file and directory(for unpacking archives) names.",
        action      = "store_true",
        default     = False,
        required    = False
    )
    parser.add_argument(
        "-o", "--overwrite",
        help        = "Overwrite existing files and directories.",
        action      = "store_true",
        default     = False,
        required    = False
    )
    parser.add_argument(
        "-x", "--executor",
        type        = str.lower,
        help        = "Main executor.",
        choices     =   [
                            "mainthread",
                            "thread",
                            "process",
                            "threads",
                            "processes",
                            "threadpool",
                            "processpool"
                        ],
        metavar     = "executor",
        action      = "store",
        default     = "mainthread",
        required    = False,
        nargs='?'
    )
    parser.add_argument(
        "-u", "--use",
        type        = str.lower,
        help        = "Individual executor.",
        choices     =   [
                            "mainthread",
                            "thread",
                            "process",
                            "threads",
                            "processes",
                            "threadpool",
                            "processpool"
                        ],
        metavar     = "ext_executor",
        dest        = "ext_executor",
        action      = "store",
        default     = "mainthread",
        require     = False,
        nargs='?'
    )

    parser.add_argument(
        "-v", "--verbose",
        help        = ("increase output verbosity.\n\
    0 - Only errors printout\n\
    1 - Add warnings\n\
    2 - Add destination directory creation\n\
    3 - Add all filesystem modification\n\
    4 - Add internal script structures"),
        choices     =   [
                            "critical",
                            "error",
                            "warning",
                            "info",
                            "debug",
                            "notset"
                        ],
        # action="count",
        action      = "store",
        required    = False,
        default     = "notset",
        nargs       = '*'
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-s", "--settings",
        help        = "Specify path to settings(JSON) file. Ex: settings.json",
        type        = Path,
        action      = "store",
        metavar     = "settings",
        default     = "settings.json",
        required    = False
    )
    group.add_argument(
        "-d", "--destination",
        help        = "Destination directory.",
        type        = Path,
        metavar     = "destination",
        action      = "store",
        default     = None,
        required    = False
    )
    parser.add_argument(
        "-e", "--extensions",
        help        = "File's extensions. Ex: 'jpg jpeg png bmp'",
        metavar     = "extensions",
        action      = "store",
        default     = "*",
        required    = False,
        nargs       = '*'
    )
    parser.add_argument(
        "-f", "--functions",
        help        = "Functions' list(order sensitive).\n\
    A list of next functions:\n\
    copy, move, unpack, delete(check if archive already unpacked), remove.\n\
    Ex: 'unpack move' - will unpack archive file to destination directory\n\
    and move it to same path.",
        metavar     = "functions",
        action      = "store",
        default     = "move",
        required    = False,
        choices     =    [
                            "copy",
                            "move",
                            "unpack",
                            "remove",
                            "removechecked"
                        ],
        nargs       = '*'
    )
    args = parser.parse_args()
    return args