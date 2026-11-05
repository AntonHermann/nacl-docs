# Validation and verification

It is essential for cryptographic libraries to compute exactly the functions that they are meant to compute, and for those functions to be secure. A signature-checking library is a security disaster if it has a bug that accepts invalid signatures, for example, or if the signature system that it implements is 512-bit RSA.

The following report specifies NaCl's default mechanism for public-key authenticated encryption, and along the way specifies NaCl's default mechanisms for scalar multiplication (Curve25519), secret-key authenticated encryption, secret-key encryption (Salsa20), and one-time authentication (Poly1305): [(PDF)](https://cr.yp.to/highspeed/naclcrypto-20090310.pdf) Daniel J. Bernstein, "Cryptography in NaCl", 45pp.

The same report includes a complete step-by-step example of authenticated encryption, independent implementations testing each step, detailed security notes, and references to the relevant literature.

The NaCl compilation scripts test known outputs of each primitive for many different message lengths, test consistency of different functions supported by the same primitive (for example, `crypto_stream_xor` matches `crypto_stream`), and test memory safety in several ways.

Tests are currently limited to 4096-byte messages. This is one of [several reasons](https://groups.google.com/forum/#!original/boring-crypto/BpUmNMXKMYQ/EEwAIeQdjacJ) that callers should (1) split all data into packets sent through the network; (2) put a small global limit on packet length; and (3) separately encrypt and authenticate each packet.

## Version

This is version 2016.06.17 of the valid.html web page.
