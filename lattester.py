#!/usr/bin/python3

from glob import glob
import os
import subprocess
import filecmp
import sys

NORMAL = '\x1b[0m'
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'


LATTESTS_PATH = 'lattests/'


def run_good(LATC_PATH):
    for rel_filepath in sorted(glob(LATTESTS_PATH + 'good/*.lat')):
        abs_filepath = os.path.abspath(rel_filepath)

        root, _ = os.path.splitext(abs_filepath)
        rel_root, _ = os.path.splitext(rel_filepath)

        # Compile
        compile_retcode = subprocess.call([LATC_PATH, abs_filepath])

        if compile_retcode > 0:
            print('{} {}'.format(rel_root, RED + 'CE' + NORMAL))
            continue

        # Open input if it exists
        proc_stdin = open(root + '.input') if os.path.isfile(root + '.input') else None
        # Open tmp output
        with open(root + '.proc.output', 'w') as proc_output:
            proc = subprocess.Popen(
                [root],
                stdin=proc_stdin,
                stdout=proc_output,
                stderr=proc_output
            )
            proc.communicate()
        # Close input
        if proc_stdin is not None:
            proc_stdin.close()
        # Compare outputs
        same = filecmp.cmp(root + '.output', root + '.proc.output')
        print('{} {}'.format(rel_root,
            GREEN + 'OK' + NORMAL if same
            else YELLOW + 'WA' + NORMAL)
        )
        # Remove tmp output
        os.remove(root + '.proc.output')


def run_bad(LATC_PATH):
    for rel_filepath in sorted(glob(LATTESTS_PATH + 'bad/*.lat')):
        abs_filepath = os.path.abspath(rel_filepath)

        root, _ = os.path.splitext(abs_filepath)
        rel_root, _ = os.path.splitext(rel_filepath)

        # Compile
        compile_retcode = subprocess.call([LATC_PATH, abs_filepath])

        print('{} {}'.format(rel_root,
            RED + 'no CE' + NORMAL if compile_retcode == 0
            else GREEN + 'CE' + NORMAL)
        )


def main():
    # Following can be changed by passing an argument to lattests.py
    LATC_PATH = './latc_llvm'
    if len(sys.argv) > 1:
        LATC_PATH = sys.argv[1]
    run_good(LATC_PATH)
    run_bad(LATC_PATH)

if __name__ == "__main__":
    main()
