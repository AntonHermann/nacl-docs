# Secret-key encryption: crypto_stream

## C++ interface

C++ NaCl provides a `crypto_stream` function callable as follows:

         #include "crypto_stream.h"

         std::string k;
         std::string n;
         std::string c;
         size_t clen;

         c = crypto_stream(clen,n,k);

The `crypto_stream` function produces a `clen`-byte stream `c` as a function of a secret key `k` and a nonce `n`. The function raises an exception if `k.size()` is not `crypto_stream_KEYBYTES`. It also raises an exception if `n.size()` is not `crypto_stream_NONCEBYTES`.

C++ NaCl also provides a `crypto_stream_xor` function callable as follows:

         #include "crypto_stream.h"

         std::string k;
         std::string n;
         std::string m;
         std::string c;

         c = crypto_stream_xor(m,n,k);

The `crypto_stream_xor` function encrypts a message `m` using a secret key `k` and a nonce `n`. The `crypto_stream_xor` function returns the ciphertext `c`. The function raises an exception if `k.size()` is not `crypto_stream_KEYBYTES`. It also raises an exception if `n.size()` is not `crypto_stream_NONCEBYTES`.

The `crypto_stream_xor` function guarantees that the ciphertext has the same length as the plaintext, and is the plaintext xor the output of `crypto_stream`. Consequently `crypto_stream_xor` can also be used to decrypt.

## C interface

C NaCl provides a `crypto_stream` function callable as follows:

         #include "crypto_stream.h"

         const unsigned char k[crypto_stream_KEYBYTES];
         const unsigned char n[crypto_stream_NONCEBYTES];
         unsigned char c[...]; unsigned long long clen;

         crypto_stream(c,clen,n,k);

The `crypto_stream` function produces a stream `c[0]`, `c[1]`, ..., `c[clen-1]` as a function of a secret key `k[0]`, `k[1]`, ..., `k[crypto_stream_KEYBYTES-1]` and a nonce `n[0]`, `n[1]`, ..., `n[crypto_stream_NONCEBYTES-1]`. The `crypto_stream` function then returns 0.

C NaCl also provides a `crypto_stream_xor` function callable as follows:

         #include "crypto_stream.h"

         const unsigned char k[crypto_stream_KEYBYTES];
         const unsigned char n[crypto_stream_NONCEBYTES];
         unsigned char m[...]; unsigned long long mlen;
         unsigned char c[...];

         crypto_stream_xor(c,m,mlen,n,k);

The `crypto_stream_xor` function encrypts a message `m[0]`, `m[1]`, ..., `m[mlen-1]` using a secret key `k[0]`, `k[1]`, ..., `k[crypto_stream_KEYBYTES-1]` and a nonce `n[0]`, `n[1]`, ..., `n[crypto_stream_NONCEBYTES-1]`. The `crypto_stream_xor` function puts the ciphertext into `c[0]`, `c[1]`, ..., `c[mlen-1]`. It then returns 0.

The `crypto_stream_xor` function guarantees that the ciphertext is the plaintext xor the output of `crypto_stream`. Consequently `crypto_stream_xor` can also be used to decrypt.

## Security model

The `crypto_stream` function, viewed as a function of the nonce for a uniform random key, is designed to meet the standard notion of unpredictability ("PRF"). For a formal definition see, e.g., Section 2.3 of Bellare, Kilian, and Rogaway, "The security of the cipher block chaining message authentication code," Journal of Computer and System Sciences **61** (2000), 362–399; <http://www-cse.ucsd.edu/~mihir/papers/cbc.html>.

This means that an attacker cannot distinguish this function from a uniform random function. Consequently, if a series of messages is encrypted by `crypto_stream_xor` *with a different nonce for each message*, the ciphertexts are indistinguishable from uniform random strings of the same length.

Note that the length is not hidden. Note also that it is the caller's responsibility to ensure the uniqueness of nonces—for example, by using nonce 1 for the first message, nonce 2 for the second message, etc. Nonces are long enough that randomly generated nonces have negligible risk of collision.

NaCl does not make any promises regarding the resistance of `crypto_stream` to "related-key attacks." It is the caller's responsibility to use proper key-derivation functions.

See [Validation](valid.md) regarding safe message lengths.

## Selected primitive

`crypto_stream` is `crypto_stream_xsalsa20`, a particular cipher specified in ["Cryptography in NaCl"](valid.md), Section 7. This cipher is conjectured to meet the standard notion of unpredictability.

## Alternate primitives

NaCl supports the following secret-key encryption functions:

| `crypto_stream`                        | Primitive   | `KEYBYTES` | `NONCEBYTES` |
|----------------------------------------|-------------|------------|--------------|
| `crypto_stream_aes128ctr`              | AES-128-CTR | 16         | 16           |
| *\[TO DO:\] `crypto_stream_aes256ctr`* | AES-256-CTR | 32         | 16           |
| `crypto_stream_salsa208`               | Salsa20/8   | 32         | 8            |
| `crypto_stream_salsa2012`              | Salsa20/12  | 32         | 8            |
| `crypto_stream_salsa20`                | Salsa20/20  | 32         | 8            |
| `crypto_stream_xsalsa20`               | XSalsa20/20 | 32         | 24           |

For example, a user who wants to encrypt with AES-128 can replace `crypto_stream`, `crypto_stream_KEYBYTES`, etc. with `crypto_stream_aes128ctr`, `crypto_stream_aes128ctr_KEYBYTES`, etc.

Beware that several of these primitives have 8-byte nonces. For those primitives it is no longer true that randomly generated nonces have negligible risk of collision. Callers who are unable to count 1,2,3,..., and who insist on using these primitives, are advised to use a randomly derived key for each message.

Beware that the `aes` (AES-CTR) functions put extra requirements on the nonce: each message actually uses a range of nonces (counting upwards for each 16-byte block), and these nonces must not be reused for other messages. Randomly generated nonces are safe.

## Version

This is version 2019.03.19 of the stream.html web page.
