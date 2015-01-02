lattester
=========

Automated test runner for Latte compilers.

Usage
-----

Assuming that `lattester.py` is in the same directory as `lattests` directory and `latc_llvm` binary:

```
./lattester.py
```

If you want to specify binary:

```
./lattester.py path_to_binary
```

In order to test the `lattester.py`, you can run with mocked compiler:

```
../lattester.py './mock_latc.py'
```

