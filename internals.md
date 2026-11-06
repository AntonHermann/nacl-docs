# Internals

Are you contributing code to NaCl? Here's some advice on how to write your code.

## Language choice

All NaCl functions are *distributed* as C implementations, often with assembly-language implementations as extra options. C++ and Python are handled as wrappers around the C implementations.

There are an increasing number of cases where the C implementations and assembly-language implementations are automatically generated from code that was actually written in another language, such as CAO or qhasm. This automatic generation takes place as part of creating the NaCl distribution, not as part of installing NaCl.

## Naming conventions: an example

The reference SHA-512 implementation in NaCl is `crypto_hash/sha512/ref/hash.c`, which defines a `crypto_hash` function as follows:

```c
#include "crypto_hash.h"

int crypto_hash(unsigned char *out,const unsigned char *in,unsigned long long inlen)
{
  ...
}
```

An accompanying file `crypto_hash/sha512/ref/api.h` says

```c
#define CRYPTO_BYTES 64
```

to indicate that this function produces a 64-byte hash.

The NaCl compilation scripts automatically create `crypto_hash.h` with various macros, including the following:

```c
#define crypto_hash crypto_hash_sha512
#define crypto_hash_sha512 crypto_hash_sha512_ref
#define crypto_hash_BYTES crypto_hash_sha512_BYTES
#define crypto_hash_sha512_BYTES crypto_hash_sha512_ref_BYTES
#define crypto_hash_sha512_ref_BYTES 64
#define crypto_hash_PRIMITIVE "sha512"
#define crypto_hash_IMPLEMENTATION crypto_hash_sha512_IMPLEMENTATION
#define crypto_hash_sha512_IMPLEMENTATION "crypto_hash/sha512/ref"
```

This means that `hash.c` actually defines a `crypto_hash_sha512_ref` function. Normally, as an implementor, you don't have to think about this; but if you avoid including `crypto_hash.h` (for example, because you're actually writing `hash.s` instead of `hash.c`) then you should make sure to define `crypto_hash_sha512_ref`.

## Multiple implementations of the same primitive

To add another SHA-512 implementation, create another subdirectory of `crypto_hash/sha512`. For example, you might choose `crypto_hash/sha512/core2` for an implementation optimized for the Core 2. Inside that subdirectory, create an `api.h` file that defines `CRYPTO_BYTES`, and a `.c` file that defines `crypto_hash`.

You can use names other than `hash.c`. You can split your code across several files `*.c` defining various auxiliary functions; the files will be automatically compiled together. You can use external names prefixed by the implementation name: for example, `crypto_hash/sha512/core2` can define `crypto_hash_sha512_core2_iv`, `crypto_hash_sha512_core2_expand`, etc.

## Branches

Do not use secret data to control a branch. In particular, do not use the `memcmp` function to compare secrets. Instead use `crypto_verify_16`, `crypto_verify_32`, etc., which perform constant-time string comparisons.

Even on architectures that support fast constant-time conditional-move instructions, always assume that a comparison in C is compiled into a branch, not a conditional move. Compilers can be remarkably stupid.

## Array lookups

Do not use secret data as an array index.

Early plans for NaCl would have allowed exceptions to this rule inside primitives specifically labelled `vulnerable`, in particular to allow fast `crypto_stream_aes128vulnerable`, but subsequent research showed that this compromise was unnecessary.

## Dynamic memory allocation

Do not use heap allocators (`malloc`, `calloc`, `sbrk`, etc.) or variable-size stack allocators (`alloca`, `int `*`x`*`[`*`n`*`]`, etc.) in C NaCl.

## Thread safety

Do not use global variables (i.e., static variables or variables defined outside functions) in C NaCl.

## Alignment

Do not assume that the input arrays or output arrays have any particular alignment. If you want to use, e.g., an aligned 16-byte load instruction for speed, check at the top of your function that the input array is properly aligned, and have a (slower) fallback in case the input array is not properly aligned.

## Specific integer sizes

If you want a 32-bit integer in C NaCl, use `crypto_int32` after `#include <crypto_int32.h>`. This is more portable than `int32_t` from `inttypes.h`, and more portable than `int32_t` from `stdint.h`. Similar comments apply to `crypto_int8`, `crypto_int16`, `crypto_int32`, `crypto_int64`, `crypto_uint8`, `crypto_uint16`, `crypto_uint32`, `crypto_uint64`.

## Variable definitions

Define stack variables at the beginning of each function in C NaCl. Some C compilers will accept variable definitions after statements, but some won't.

## Comments

Do not use C++-style comments (double slashes) in C NaCl. Some C compilers will accept these comments, but some won't.

## Version

This is version 2011.06.26 of the internals.html web page.
