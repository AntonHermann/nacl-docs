# Public-key authenticated encryption: crypto_box

## C++ interface

C++ NaCl provides a `crypto_box_keypair` function callable as follows:

         #include "crypto_box.h"
         
         std::string pk;
         std::string sk;
         
         pk = crypto_box_keypair(&sk);

The `crypto_box_keypair` function randomly generates a secret key and a corresponding public key. It puts the secret key into `sk` and returns the public key. It guarantees that `sk` has `crypto_box_SECRETKEYBYTES` bytes and that `pk` has `crypto_box_PUBLICKEYBYTES` bytes.

C++ NaCl also provides a `crypto_box` function callable as follows:

         #include "crypto_box.h"
         
         std::string pk;
         std::string sk;
         std::string n;
         std::string m;
         std::string c;

         c = crypto_box(m,n,pk,sk);

The `crypto_box` function encrypts and authenticates a message `m` using the sender's secret key `sk`, the receiver's public key `pk`, and a nonce `n`. The `crypto_box` function returns the resulting ciphertext `c`. The function raises an exception if `sk.size()` is not `crypto_box_SECRETKEYBYTES` or if `pk.size()` is not `crypto_box_PUBLICKEYBYTES` or if `n.size()` is not `crypto_box_NONCEBYTES`.

C++ NaCl also provides a `crypto_box_open` function callable as follows:

         #include "crypto_box.h"
         
         std::string pk;
         std::string sk;
         std::string n;
         std::string c;
         std::string m;

         m = crypto_box_open(c,n,pk,sk);

The `crypto_box_open` function verifies and decrypts a ciphertext `c` using the receiver's secret key `sk`, the sender's public key `pk`, and a nonce `n`. The `crypto_box_open` function returns the resulting plaintext `m`.

If the ciphertext fails verification, `crypto_box_open` raises an exception. The function also raises an exception if `sk.size()` is not `crypto_box_SECRETKEYBYTES` or if `pk.size()` is not `crypto_box_PUBLICKEYBYTES` or if `n.size()` is not `crypto_box_NONCEBYTES`.

## C interface

C NaCl provides a `crypto_box_keypair` function callable as follows:

         #include "crypto_box.h"
         
         unsigned char pk[crypto_box_PUBLICKEYBYTES];
         unsigned char sk[crypto_box_SECRETKEYBYTES];
         
         crypto_box_keypair(pk,sk);

The `crypto_box_keypair` function randomly generates a secret key and a corresponding public key. It puts the secret key into `sk[0]`, `sk[1]`, ..., `sk[crypto_box_SECRETKEYBYTES-1]` and puts the public key into `pk[0]`, `pk[1]`, ..., `pk[crypto_box_PUBLICKEYBYTES-1]`. It then returns 0.

C NaCl also provides a `crypto_box` function callable as follows:

         #include "crypto_box.h"
         
         const unsigned char pk[crypto_box_PUBLICKEYBYTES];
         const unsigned char sk[crypto_box_SECRETKEYBYTES];
         const unsigned char n[crypto_box_NONCEBYTES];
         const unsigned char m[...]; unsigned long long mlen;
         unsigned char c[...];
         
         crypto_box(c,m,mlen,n,pk,sk);

The `crypto_box` function encrypts and authenticates a message `m[0]`, ..., `m[mlen-1]` using the sender's secret key `sk[0]`, `sk[1]`, ..., `sk[crypto_box_SECRETKEYBYTES-1]`, the receiver's public key `pk[0]`, `pk[1]`, ..., `pk[crypto_box_PUBLICKEYBYTES-1]`, and a nonce `n[0]`, `n[1]`, ..., `n[crypto_box_NONCEBYTES-1]`. The `crypto_box` function puts the ciphertext into `c[0]`, `c[1]`, ..., `c[mlen-1]`. It then returns 0.

**WARNING:** Messages in the C NaCl API are 0-padded versions of messages in the C++ NaCl API. Specifically: The caller must ensure, before calling the C NaCl `crypto_box` function, that the first `crypto_box_ZEROBYTES` bytes of the message `m` are all 0. Typical higher-level applications will work with the remaining bytes of the message; note, however, that `mlen` counts all of the bytes, including the bytes required to be 0.

Similarly, ciphertexts in the C NaCl API are 0-padded versions of messages in the C++ NaCl API. Specifically: The `crypto_box` function ensures that the first `crypto_box_BOXZEROBYTES` bytes of the ciphertext `c` are all 0.

C NaCl also provides a `crypto_box_open` function callable as follows:

         #include "crypto_box.h"
         
         const unsigned char pk[crypto_box_PUBLICKEYBYTES];
         const unsigned char sk[crypto_box_SECRETKEYBYTES];
         const unsigned char n[crypto_box_NONCEBYTES];
         const unsigned char c[...]; unsigned long long clen;
         unsigned char m[...];
         
         crypto_box_open(m,c,clen,n,pk,sk);

The `crypto_box_open` function verifies and decrypts a ciphertext `c[0]`, ..., `c[clen-1]` using the receiver's secret key `sk[0]`, `sk[1]`, ..., `sk[crypto_box_SECRETKEYBYTES-1]`, the sender's public key `pk[0]`, `pk[1]`, ..., `pk[crypto_box_PUBLICKEYBYTES-1]`, and a nonce `n[0]`, ..., `n[crypto_box_NONCEBYTES-1]`. The `crypto_box_open` function puts the plaintext into `m[0]`, `m[1]`, ..., `m[clen-1]`. It then returns 0.

If the ciphertext fails verification, `crypto_box_open` instead returns `-1`, possibly after modifying `m[0]`, `m[1]`, etc.

The caller must ensure, before calling the `crypto_box_open` function, that the first `crypto_box_BOXZEROBYTES` bytes of the ciphertext `c` are all 0. The `crypto_box_open` function ensures (in case of success) that the first `crypto_box_ZEROBYTES` bytes of the plaintext `m` are all 0.

## C precomputation interface

Applications that send several messages to the same receiver can gain speed by splitting `crypto_box` into two steps, `crypto_box_beforenm` and `crypto_box_afternm`. Similarly, applications that receive several messages from the same sender can gain speed by splitting `crypto_box_open` into two steps, `crypto_box_beforenm` and `crypto_box_open_afternm`.

The `crypto_box_beforenm` function is callable as follows:

         #include "crypto_box.h"
         
         unsigned char k[crypto_box_BEFORENMBYTES];
         const unsigned char pk[crypto_box_PUBLICKEYBYTES];
         const unsigned char sk[crypto_box_SECRETKEYBYTES];
         
         crypto_box_beforenm(k,pk,sk);

The `crypto_box_afternm` function is callable as follows:

         #include "crypto_box.h"
         
         const unsigned char k[crypto_box_BEFORENMBYTES];
         const unsigned char n[crypto_box_NONCEBYTES];
         const unsigned char m[...]; unsigned long long mlen;
         unsigned char c[...];
         
         crypto_box_afternm(c,m,mlen,n,k);

The `crypto_box_open_afternm` function is callable as follows:

         #include "crypto_box.h"
         
         const unsigned char k[crypto_box_BEFORENMBYTES];
         const unsigned char n[crypto_box_NONCEBYTES];
         const unsigned char c[...]; unsigned long long clen;
         unsigned char m[...];
         
         crypto_box_open_afternm(m,c,clen,n,k);

The intermediate data computed by `crypto_box_beforenm` is suitable for both `crypto_box_afternm` and `crypto_box_open_afternm`, and can be reused for any number of messages.

## Security model

The `crypto_box` function is designed to meet the standard notions of privacy and third-party unforgeability for a public-key authenticated-encryption scheme using nonces. For formal definitions see, e.g., Jee Hea An, "Authenticated encryption in the public-key setting: security notions and analyses," <https://eprint.iacr.org/2001/079>.

Distinct messages between the same {sender, receiver} set are required to have distinct nonces. For example, the lexicographically smaller public key can use nonce 1 for its first message to the other key, nonce 3 for its second message, nonce 5 for its third message, etc., while the lexicographically larger public key uses nonce 2 for its first message to the other key, nonce 4 for its second message, nonce 6 for its third message, etc. Nonces are long enough that randomly generated nonces have negligible risk of collision.

There is no harm in having the same nonce for different messages if the {sender, receiver} sets are different. This is true even if the sets overlap. For example, a sender can use the same nonce for two different messages if the messages are sent to two different public keys.

The `crypto_box` function is not meant to provide non-repudiation. On the contrary: the `crypto_box` function *guarantees* repudiability. A receiver can freely modify a boxed message, and therefore cannot convince third parties that this particular message came from the sender. The sender and receiver are nevertheless protected against forgeries by other parties. In the terminology of <https://groups.google.com/group/sci.crypt/msg/ec5c18b23b11d82c>, `crypto_box` uses "public-key authenticators" rather than "public-key signatures."

Users who want public verifiability (or receiver-assisted public verifiability) should instead use signatures (or signcryption). Signature support is a high priority for NaCl; a signature API will be described in subsequent NaCl documentation.

See [Validation](../valid.md) regarding safe message lengths.

## Selected primitive

`crypto_box` is `curve25519xsalsa20poly1305`, a particular combination of Curve25519, Salsa20, and Poly1305 specified in ["Cryptography in NaCl"](../valid.md). This function is conjectured to meet the standard notions of privacy and third-party unforgeability.

## Alternate primitives

NaCl supports the following public-key message-protection functions:

|                                             | `crypto_box_...BYTES` |             |         |        |           |            |
|---------------------------------------------|-----------------------|-------------|---------|--------|-----------|------------|
| `crypto_box`                                | `PUBLICKEY`           | `SECRETKEY` | `NONCE` | `ZERO` | `BOXZERO` | `BEFORENM` |
| *\[TO DO:\] `crypto_box_nistp256aes256gcm`* | 64                    | 32          | 8       | 32     | 0         | 32         |
| `crypto_box_curve25519xsalsa20poly1305`     | 32                    | 32          | 24      | 32     | 16        | 32         |

For example, a user can replace `crypto_box` etc. with `crypto_box_curve25519xsalsa20poly1305` etc.

## Version

This is version 2019.03.19 of the box.html web page.
