# String comparison: crypto_verify

C NaCl provides a `crypto_verify_16` function callable as follows:

```c
#include "crypto_verify_16.h"

const unsigned char x[16];
const unsigned char y[16];

crypto_verify_16(x,y);
```

The `crypto_verify_16` function returns `0` if `x[0]`, `x[1]`, ..., `x[15]` are the same as `y[0]`, `y[1]`, ..., `y[15]`. Otherwise it returns `-1`.

This function is safe to use for secrets `x[0]`, `x[1]`, ..., `x[15]`, `y[0]`, `y[1]`, ..., `y[15]`. The time taken by `crypto_verify_16` is independent of the contents of `x[0]`, `x[1]`, ..., `x[15]`, `y[0]`, `y[1]`, ..., `y[15]`. In contrast, the standard C comparison function `memcmp(x,y,16)` takes time that depends on the longest matching prefix of `x` and `y`, often allowing easy timing attacks.

C NaCl also provides a similar `crypto_verify_32` function.

## Version

This is version 2010.03.09 of the verify.html web page.
