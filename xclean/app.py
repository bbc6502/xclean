import os
from argparse import ArgumentParser
from xclean.scanner import Scanner


def main():
    parser = ArgumentParser(description='File de-duplication utility')
    parser.add_argument('-m', '--main', help='Directory where main files reside')
    parser.add_argument('-t', '--target', help='Directory where duplicate files may reside')
    parser.add_argument('-a', '--archive-to', help='Archive duplicates to directory')
    parser.add_argument('-i', '--include', nargs='*', help='Include Extensions')
    parser.add_argument('-x', '--exclude', nargs='*', help='Exclude Extensions')
    parser.add_argument('--unprotect', default=False, action='store_true', help='Unprotect main files')
    parser.add_argument('--remove', default=False, action='store_true', help='Remove duplicate files')
    parser.add_argument('--trash', default=False, action='store_true', help='Trash duplicate files')
    parser.add_argument('--clean', default=False, action='store_true', help='Clean database')
    parser.add_argument('--xmp', default=False, action='store_true', help='Include xmp files when checking for duplicates')
    parser.add_argument('--aae', default=False, action='store_true', help='Include aae files when checking for duplicates')
    args = parser.parse_args()
    home_dir = os.environ.get('HOME')
    if home_dir is None:
        db_path = 'xclean.sqlite'
    else:
        db_path = os.path.join(home_dir, 'xclean.sqlite')
    xclean = Scanner(db_path=db_path, clean=args.clean)
    if args.main is not None:
        xclean.scan(
            dir_path=args.main,
            include=args.include,
            exclude=args.exclude,
        )
    if args.target is not None:
        xclean.clean(
            dir_path=args.target,
            include=args.include,
            exclude=args.exclude,
            remove_dups=args.remove,
            trash_dups=args.trash,
            check_xmp=args.xmp,
            check_aae=args.aae,
            archive_to=args.archive_to,
            unprotect=args.unprotect,
        )
