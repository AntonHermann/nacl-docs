# Secret-key single-message authentication: crypto_onetimeauth

## C++ interface

C++ NaCl provides a `crypto_onetimeauth` function callable as follows:

         #include "crypto_onetimeauth.h"

         std::string k;
         std::string m;
         std::string a;

         a = crypto_onetimeauth(m,k);

The `crypto_onetimeauth` function authenticates a message `m` using a secret key `k`, and returns an authenticator `a`. The authenticator length is always `crypto_onetimeauth_BYTES`. The function raises an exception if `k.size()` is not `crypto_onetimeauth_KEYBYTES`.

C++ NaCl also provides a `crypto_onetimeauth_verify` function callable as follows:

         #include "crypto_onetimeauth.h"

         std::string k;
         std::string m;
         std::string a;

         crypto_onetimeauth_verify(a,m,k);

This function checks that `k.size()` is `crypto_onetimeauth_KEYBYTES`; `a.size()` is `crypto_onetimeauth_BYTES`; and `a` is a correct authenticator of a message `m` under the secret key `k`. If any of these checks fail, the function raises an exception.

## C interface

C NaCl provides a `crypto_onetimeauth` function callable as follows:

         #include "crypto_onetimeauth.h"

         const unsigned char k[crypto_onetimeauth_KEYBYTES];
         const unsigned char m[...]; unsigned long long mlen;
         unsigned char a[crypto_onetimeauth_BYTES];

         crypto_onetimeauth(a,m,mlen,k);

The `crypto_onetimeauth` function authenticates a message `m[0]`, `m[1]`, ..., `m[mlen-1]` using a secret key `k[0]`, `k[1]`, ..., `k[crypto_onetimeauth_KEYBYTES-1]`; puts the authenticator into `a[0]`, `a[1]`, ..., `a[crypto_onetimeauth_BYTES-1]`; and returns 0.

C NaCl also provides a `crypto_onetimeauth_verify` function callable as follows:

         #include "crypto_onetimeauth.h"

         const unsigned char k[crypto_onetimeauth_KEYBYTES];
         const unsigned char m[...]; unsigned long long mlen;
         const unsigned char a[crypto_onetimeauth_BYTES];

         crypto_onetimeauth_verify(a,m,mlen,k);

This function returns `0` if `a[0]`, `a[1]`, ..., `a[crypto_onetimeauth_BYTES-1]` is a correct authenticator of a message `m[0]`, `m[1]`, ..., `m[mlen-1]` under a secret key `k[0]`, `k[1]`, ..., `k[crypto_onetimeauth_KEYBYTES-1]`. Otherwise `crypto_onetimeauth_verify` returns `-1`.

## Security model

The `crypto_onetimeauth` function, viewed as a function of the message for a uniform random key, is designed to meet the standard notion of unforgeability after a single message. After the sender authenticates *one* message, an attacker cannot find authenticators for any other messages.

The sender must not use `crypto_onetimeauth` to authenticate more than one message under the same key. Authenticators for two messages under the same key should be expected to reveal enough information to allow forgeries of authenticators on other messages.

See [Validation](../valid.md) regarding safe message lengths.

## Selected primitive

`crypto_onetimeauth` is `crypto_onetimeauth_poly1305`, an authenticator specified in ["Cryptography in NaCl"](../valid.md), Section 9. This authenticator is *proven* to meet the standard notion of unforgeability after a single message.

## Alternate primitives

NaCl supports the following secret-key single-message authentication functions:

| `crypto_onetimeauth`          | Primitive | `BYTES` | `KEYBYTES` |
|-------------------------------|-----------|---------|------------|
| `crypto_onetimeauth_poly1305` | Poly1305  | 16      | 32         |

For example, a user can replace `crypto_onetimeauth`, `crypto_onetimeauth_BYTES`, etc. with `crypto_onetimeauth_poly1305`, `crypto_onetimeauth_poly1305_BYTES`, etc. Furthermore, users willing to compromise both provability and speed can replace `crypto_onetimeauth` with `crypto_auth` or with any of the `crypto_auth` primitives.

## Version

This is version 2019.03.19 of the onetimeauth.html web page.
