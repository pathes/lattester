#!/usr/bin/python3

import sys
import os
import stat

def main():
    # Uncomment following to get a Compile Error
    # exit(1)

    if len(sys.argv) != 2:
        exit(1)
    filepath = os.path.abspath(sys.argv[1])
    root, _ = os.path.splitext(filepath)
    output_filepath = root + '.output'
    # Open the "compiled program"
    with open(root, 'w') as handle:
        handle.write('#!/usr/bin/env bash\n')
        handle.write('cat ' + output_filepath + '\n')
        # Uncomment following to get a Wrong Answer
        # handle.write('echo 123\n')
    # Make it executable
    os.chmod(root, 0o775)

if __name__ == "__main__":
    main()
