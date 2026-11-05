# Signatures: crypto_sign

**WARNING:** This signature software (both at the C level and at the C++ level) is a prototype. It will be replaced by the final system [Ed25519](https://ed25519.cr.yp.to) in future NaCl releases. A NaCl-compatible Ed25519 implementation is already available as part of [SUPERCOP](https://bench.cr.yp.to/supercop.html).

## C++ interface

C++ NaCl provides a `crypto_sign_keypair` function callable as follows:

         #include "crypto_sign.h"

         std::string pk;
         std::string sk;

         pk = crypto_sign_keypair(&sk);

The `crypto_sign_keypair` function randomly generates a secret key and a corresponding public key. It puts the secret key into `sk` and returns the public key. It guarantees that `sk` has `crypto_sign_SECRETKEYBYTES` bytes and that `pk` has `crypto_sign_PUBLICKEYBYTES` bytes.

C++ NaCl also provides a `crypto_sign` function callable as follows:

         #include "crypto_sign.h"

         std::string sk;
         std::string m;
         std::string sm;

         sm = crypto_sign(m,sk);

The `crypto_sign` function signs a message `m` using the signer's secret key `sk`. The `crypto_sign` function returns the resulting signed message `sm`. The function raises an exception if `sk.size()` is not `crypto_sign_SECRETKEYBYTES`.

C++ NaCl also provides a `crypto_sign_open` function callable as follows:

         #include "crypto_sign.h"

         std::string pk;
         std::string sm;
         std::string m;

         m = crypto_sign_open(sm,pk);

The `crypto_sign_open` function verifies the signature in `sm` using the signer's public key `pk`. The `crypto_sign_open` function returns the message `m`.

If the signature fails verification, `crypto_sign_open` raises an exception. The function also raises an exception if `pk.size()` is not `crypto_sign_PUBLICKEYBYTES`.

## C interface

C NaCl provides a `crypto_sign_keypair` function callable as follows:

         #include "crypto_sign.h"

         unsigned char pk[crypto_sign_PUBLICKEYBYTES];
         unsigned char sk[crypto_sign_SECRETKEYBYTES];

         crypto_sign_keypair(pk,sk);

The `crypto_sign_keypair` function randomly generates a secret key and a corresponding public key. It puts the secret key into `sk[0]`, `sk[1]`, ..., `sk[crypto_sign_SECRETKEYBYTES-1]` and puts the public key into `pk[0]`, `pk[1]`, ..., `pk[crypto_sign_PUBLICKEYBYTES-1]`. It then returns 0.

C NaCl also provides a `crypto_sign` function callable as follows:

         #include "crypto_sign.h"

         const unsigned char sk[crypto_sign_SECRETKEYBYTES];
         const unsigned char m[...]; unsigned long long mlen;
         unsigned char sm[...]; unsigned long long smlen;

         crypto_sign(sm,&smlen,m,mlen,sk);

The `crypto_sign` function signs a message `m[0]`, ..., `m[mlen-1]` using the signer's secret key `sk[0]`, `sk[1]`, ..., `sk[crypto_sign_SECRETKEYBYTES-1]`, puts the length of the signed message into `smlen` and puts the signed message into `sm[0]`, `sm[1]`, ..., `sm[smlen-1]`. It then returns 0.

The maximum possible length `smlen` is `mlen+crypto_sign_BYTES`. The caller must allocate at least `mlen+crypto_sign_BYTES` bytes for `sm`.

C NaCl also provides a `crypto_sign_open` function callable as follows:

         #include "crypto_sign.h"

         const unsigned char pk[crypto_sign_PUBLICKEYBYTES];
         const unsigned char sm[...]; unsigned long long smlen;
         unsigned char m[...]; unsigned long long mlen;

         crypto_sign_open(m,&mlen,sm,smlen,pk);

The `crypto_sign_open` function verifies the signature in `sm[0]`, ..., `sm[smlen-1]` using the signer's public key `pk[0]`, `pk[1]`, ..., `pk[crypto_sign_PUBLICKEYBYTES-1]`. The `crypto_sign_open` function puts the length of the message into `mlen` and puts the message into `m[0]`, `m[1]`, ..., `m[mlen-1]`. It then returns 0.

The maximum possible length `mlen` is `smlen`. The caller must allocate at least `smlen` bytes for `m`.

If the signature fails verification, `crypto_sign_open` instead returns `-1`, possibly after modifying `m[0]`, `m[1]`, etc.

## Security model

The `crypto_sign` function is designed to meet the standard notion of unforgeability for a public-key signature scheme under chosen-message attacks.

See [Validation](../valid.md) regarding safe message lengths.

## Selected primitive

`crypto_sign` is `crypto_sign_edwards25519sha512batch`, a particular combination of Curve25519 in Edwards form and SHA-512 into a signature scheme suitable for high-speed batch verification. This function is conjectured to meet the standard notion of unforgeability under chosen-message attacks.

## Alternate primitives

NaCl supports the following public-key signature functions:

|                                                | `crypto_sign_...` |                  |         |
|------------------------------------------------|-------------------|------------------|---------|
| `crypto_sign`                                  | `PUBLICKEYBYTES`  | `SECRETKEYBYTES` | `BYTES` |
| *\[TO DO:\] `crypto_sign_nistp256sha512ecdsa`* | 64                | 64               | 64      |
| `crypto_sign_edwards25519sha512batch`          | 32                | 64               | 64      |

For example, a user who wants to encrypt and authenticate messages with the NIST P-256 curve using SHA-512 and the ECDSA algorithm can replace `crypto_sign` with `crypto_sign_nistp256sha512ecdsa`.

## Version

This is version 2019.03.19 of the sign.html web page.
