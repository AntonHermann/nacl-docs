# Secret-key message authentication: crypto_auth

## C++ interface

C++ NaCl provides a `crypto_auth` function callable as follows:

```cpp
#include "crypto_auth.h"

std::string k;
std::string m;
std::string a;

a = crypto_auth(m,k);
```

The `crypto_auth` function authenticates a message `m` using a secret key `k`. The function returns an authenticator `a`. The authenticator length is always `crypto_auth_BYTES`. The function raises an exception if `k.size()` is not `crypto_auth_KEYBYTES`.

C++ NaCl also provides a `crypto_auth_verify` function callable as follows:

```cpp
#include "crypto_auth.h"

std::string k;
std::string m;
std::string a;

crypto_auth_verify(a,m,k);
```

The `crypto_auth_verify` function checks that `k.size()` is `crypto_auth_KEYBYTES`; `a.size()` is `crypto_auth_BYTES`; and `a` is a correct authenticator of a message `m` under the secret key `k`. If any of these checks fail, the function raises an exception.

## C interface

C NaCl provides a `crypto_auth` function callable as follows:

```c
#include "crypto_auth.h"

const unsigned char k[crypto_auth_KEYBYTES];
const unsigned char m[...]; unsigned long long mlen;
unsigned char a[crypto_auth_BYTES];

crypto_auth(a,m,mlen,k);
```

The `crypto_auth` function authenticates a message `m[0]`, `m[1]`, ..., `m[mlen-1]` using a secret key `k[0]`, `k[1]`, ..., `k[crypto_auth_KEYBYTES-1]`. The `crypto_auth` function puts the authenticator into `a[0]`, `a[1]`, ..., `a[crypto_auth_BYTES-1]`. It then returns 0.

C NaCl also provides a `crypto_auth_verify` function callable as follows:

```c
#include "crypto_auth.h"

const unsigned char k[crypto_auth_KEYBYTES];
const unsigned char m[...]; unsigned long long mlen;
const unsigned char a[crypto_auth_BYTES];

crypto_auth_verify(a,m,mlen,k);
```

The `crypto_auth_verify` function returns `0` if `a[0]`, ..., `a[crypto_auth_BYTES-1]` is a correct authenticator of a message `m[0]`, `m[1]`, ..., `m[mlen-1]` under a secret key `k[0]`, `k[1]`, ..., `k[crypto_auth_KEYBYTES-1]`. Otherwise `crypto_auth_verify` returns `-1`.

## Security model

The `crypto_auth` function, viewed as a function of the message for a uniform random key, is designed to meet the standard notion of unforgeability. This means that an attacker cannot find authenticators for any messages not authenticated by the sender, even if the attacker has adaptively influenced the messages authenticated by the sender. For a formal definition see, e.g., Section 2.4 of Bellare, Kilian, and Rogaway, "The security of the cipher block chaining message authentication code," Journal of Computer and System Sciences **61** (2000), 362–399; <http://www-cse.ucsd.edu/~mihir/papers/cbc.html>.

NaCl does not make any promises regarding "strong" unforgeability; perhaps one valid authenticator can be converted into another valid authenticator for the same message. NaCl also does not make any promises regarding "truncated unforgeability."

See [Validation](../valid.md) regarding safe message lengths.

## Selected primitive

`crypto_auth` is currently an implementation of HMAC-SHA-512-256, i.e., the first 256 bits of HMAC-SHA-512. HMAC-SHA-512-256 is conjectured to meet the standard notion of unforgeability.

## Alternate primitives

NaCl supports the following secret-key authentication functions:

| `crypto_auth`               | Primitive        | `BYTES` | `KEYBYTES` |
|-----------------------------|------------------|---------|------------|
| `crypto_auth_hmacsha256`    | HMAC_SHA-256     | 32      | 32         |
| `crypto_auth_hmacsha512256` | HMAC_SHA-512-256 | 32      | 32         |

For example, a user can replace `crypto_auth`, `crypto_auth_KEYBYTES`, etc. with `crypto_auth_hmacsha256`, `crypto_auth_hmacsha256_KEYBYTES`, etc.

## Version

This is version 2019.03.19 of the auth.html web page.
