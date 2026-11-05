# Secret-key authenticated encryption: crypto_secretbox

## C++ interface

C++ NaCl provides a `crypto_secretbox` function callable as follows:

         #include "crypto_secretbox.h"

         std::string k;
         std::string n;
         std::string m;
         std::string c;

         c = crypto_secretbox(m,n,k);

The `crypto_secretbox` function encrypts and authenticates a message `m` using a secret key `k` and a nonce `n`. The `crypto_secretbox` function returns the resulting ciphertext `c`. The function raises an exception if `k.size()` is not `crypto_secretbox_KEYBYTES`. The function also raises an exception if `n.size()` is not `crypto_secretbox_NONCEBYTES`.

C++ NaCl also provides a `crypto_secretbox_open` function callable as follows:

         #include "crypto_secretbox.h"

         std::string k;
         std::string n;
         std::string c;
         std::string m;

         m = crypto_secretbox_open(c,n,k);

The `crypto_secretbox_open` function verifies and decrypts a ciphertext `c` using a secret key `k` and a nonce `n`. The `crypto_secretbox_open` function returns the resulting plaintext `m`.

If the ciphertext fails verification, `crypto_secretbox_open` raises an exception. The function also raises an exception if `k.size()` is not `crypto_secretbox_KEYBYTES`, or if `n.size()` is not `crypto_secretbox_NONCEBYTES`.

## C interface

C NaCl provides a `crypto_secretbox` function callable as follows:

         #include "crypto_secretbox.h"

         const unsigned char k[crypto_secretbox_KEYBYTES];
         const unsigned char n[crypto_secretbox_NONCEBYTES];
         const unsigned char m[...]; unsigned long long mlen;
         unsigned char c[...]; unsigned long long clen;

         crypto_secretbox(c,m,mlen,n,k);

The `crypto_secretbox` function encrypts and authenticates a message `m[0]`, `m[1]`, ..., `m[mlen-1]` using a secret key `k[0]`, ..., `k[crypto_secretbox_KEYBYTES-1]` and a nonce `n[0]`, `n[1]`, ..., `n[crypto_secretbox_NONCEBYTES-1]`. The `crypto_secretbox` function puts the ciphertext into `c[0]`, `c[1]`, ..., `c[mlen-1]`. It then returns 0.

**WARNING:** Messages in the C NaCl API are 0-padded versions of messages in the C++ NaCl API. Specifically: The caller must ensure, before calling the C NaCl `crypto_secretbox` function, that the first `crypto_secretbox_ZEROBYTES` bytes of the message `m` are all 0. Typical higher-level applications will work with the remaining bytes of the message; note, however, that `mlen` counts all of the bytes, including the bytes required to be 0.

Similarly, ciphertexts in the C NaCl API are 0-padded versions of messages in the C++ NaCl API. Specifically: The `crypto_secretbox` function ensures that the first `crypto_secretbox_BOXZEROBYTES` bytes of the ciphertext `c` are all 0.

C NaCl also provides a `crypto_secretbox_open` function callable as follows:

         #include "crypto_secretbox.h"

         const unsigned char k[crypto_secretbox_KEYBYTES];
         const unsigned char n[crypto_secretbox_NONCEBYTES];
         const unsigned char c[...]; unsigned long long clen;
         unsigned char m[...];

         crypto_secretbox_open(m,c,clen,n,k);

The `crypto_secretbox_open` function verifies and decrypts a ciphertext `c[0]`, `c[1]`, ..., `c[clen-1]` using a secret key `k[0]`, `k[1]`, ..., `k[crypto_secretbox_KEYBYTES-1]` and a nonce `n[0]`, ..., `n[crypto_secretbox_NONCEBYTES-1]`. The `crypto_secretbox_open` function puts the plaintext into `m[0]`, `m[1]`, ..., `m[clen-1]`. It then returns 0.

If the ciphertext fails verification, `crypto_secretbox_open` instead returns `-1`, possibly after modifying `m[0]`, `m[1]`, etc.

The caller must ensure, before calling the `crypto_secretbox_open` function, that the first `crypto_secretbox_BOXZEROBYTES` bytes of the ciphertext `c` are all 0. The `crypto_secretbox_open` function ensures (in case of success) that the first `crypto_secretbox_ZEROBYTES` bytes of the plaintext `m` are all 0.

## Security model

The `crypto_secretbox` function is designed to meet the standard notions of privacy and authenticity for a secret-key authenticated-encryption scheme using nonces. For formal definitions see, e.g., Bellare and Namprempre, "Authenticated encryption: relations among notions and analysis of the generic composition paradigm," Lecture Notes in Computer Science **1976** (2000), 531–545, <http://www-cse.ucsd.edu/~mihir/papers/oem.html>.

Note that the length is not hidden. Note also that it is the caller's responsibility to ensure the uniqueness of nonces—for example, by using nonce 1 for the first message, nonce 2 for the second message, etc. Nonces are long enough that randomly generated nonces have negligible risk of collision.

See [Validation](../valid.md) regarding safe message lengths.

## Selected primitive

`crypto_secretbox` is `crypto_secretbox_xsalsa20poly1305`, a particular combination of Salsa20 and Poly1305 specified in ["Cryptography in NaCl"](../valid.md). This function is conjectured to meet the standard notions of privacy and authenticity.

## Alternate primitives

NaCl supports the following secret-key message-protection functions:

| `crypto_secretbox`                        | `KEYBYTES` | `NONCEBYTES` | `ZEROBYTES` | `BOXZEROBYTES` |
|-------------------------------------------|------------|--------------|-------------|----------------|
| *\[TO DO:\] `crypto_secretbox_aes256gcm`* | 32         | 8            | 32          | 0              |
| `crypto_secretbox_xsalsa20poly1305`       | 32         | 24           | 32          | 16             |

For example, a user who wants to encrypt and authenticate messages with AES-256-GCM can replace `crypto_secretbox` with `crypto_secretbox_aes256gcm`, `crypto_secretbox_KEYBYTES` with `crypto_secretbox_aes256gcm_KEYBYTES`, etc.

Beware that some of these primitives have 8-byte nonces. For those primitives it is no longer true that randomly generated nonces have negligible risk of collision. Callers who are unable to count 1,2,3,..., and who insist on using these primitives, are advised to use a randomly derived key for each message.

## Version

This is version 2019.03.19 of the secretbox.html web page.
