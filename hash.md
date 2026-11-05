# Hashing: crypto_hash

## C++ interface

C++ NaCl provides a `crypto_hash` function callable as follows:

         #include "crypto_hash.h"

         std::string m;
         std::string h;

         h = crypto_hash(m);

The `crypto_hash` function hashes a message `m`. It returns a hash `h`. The output length `h.size()` is always `crypto_hash_BYTES`.

## C interface

C NaCl provides a `crypto_hash` function callable as follows:

         #include "crypto_hash.h"

         const unsigned char m[...]; unsigned long long mlen;
         unsigned char h[crypto_hash_BYTES];

         crypto_hash(h,m,mlen);

The `crypto_hash` function hashes a message `m[0]`, `m[1]`, ..., `m[mlen-1]`. It puts the hash into `h[0]`, `h[1]`, ..., `h[crypto_hash_BYTES-1]`. It then returns 0.

## Security model

The `crypto_hash` function is designed to be usable as a strong component of DSA, RSA-PSS, key derivation, hash-based message-authentication codes, hash-based ciphers, and various other common applications. "Strong" means that the security of these applications, when instantiated with `crypto_hash`, is the same as the security of the applications against generic attacks. In particular, the `crypto_hash` function is designed to make finding collisions difficult.

See [Validation](valid.md) regarding safe message lengths.

## Selected primitive

`crypto_hash` is currently an implementation of SHA-512.

There has been considerable degradation of public confidence in the security conjectures for many hash functions, including SHA-512. However, for the moment, there do not appear to be alternatives that inspire satisfactory levels of confidence. One can hope that NIST's SHA-3 competition will improve the situation.

## Alternate primitives

NaCl supports the following hash functions:

| `crypto_hash`        | Primitive | `BYTES` |
|----------------------|-----------|---------|
| `crypto_hash_sha256` | SHA-256   | 32      |
| `crypto_hash_sha512` | SHA-512   | 64      |

For example, a user who wants to hash with SHA-256 can simply replace `crypto_hash`, `crypto_hash_BYTES`, etc. with `crypto_hash_sha256`, `crypto_hash_sha256_BYTES`, etc.

## Version

This is version 2019.03.19 of the hash.html web page.
