#!/usr/bin/python3

import sys
import os
import stat

def main():
    if len(sys.argv) != 2:
        exit(1)
    filepath = os.path.abspath(sys.argv[1])

    # Induce compiler error
    if 'bad' in filepath:
        exit(1)

    root, _ = os.path.splitext(filepath)
    output_filepath = root + '.output'
    # Open the "compiled program"
    with open(root, 'w') as handle:
        handle.write('#!/usr/bin/env bash\n')
        handle.write('cat ' + output_filepath + '\n')
    # Make it executable
    os.chmod(root, 0o775)

if __name__ == "__main__":
    main()
