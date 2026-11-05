# Introduction

NaCl (pronounced "salt") is a new easy-to-use high-speed software library for network communication, encryption, decryption, signatures, etc. NaCl's goal is to provide all of the core operations needed to build higher-level cryptographic tools.

Of course, other libraries already exist for these core operations. NaCl advances the state of the art by improving security, by improving usability, and by improving speed.

The following report contrasts NaCl with other libraries from a security perspective: [(PDF)](https://cr.yp.to/highspeed/coolnacl-20120725.pdf) Daniel J. Bernstein, Tanja Lange, Peter Schwabe, "The security impact of a new cryptographic library". Pages 159–176 in Proceedings of LatinCrypt 2012, edited by Alejandro Hevia and Gregory Neven, Lecture Notes in Computer Science 7533, Springer, 2012. ISBN 978-3-642-33480-1.

The following report was created for Research Plaza and gives an introduction to NaCl for a wider audience: [(PDF)](securing-communication.pdf)

## Upcoming features

Major features in the next release of NaCl: full PIC support, for easy integration into other languages; Ed25519 signatures (currently available in SUPERCOP); NEON optimizations.

## Contributors

The core NaCl development team consists of Daniel J. Bernstein (University of Illinois at Chicago and Technische Universiteit Eindhoven), Tanja Lange (Technische Universiteit Eindhoven), and Peter Schwabe (Radboud Universiteit Nijmegen).

NaCl was initiated under the CACE (Computer Aided Cryptography Engineering) project funded by the European Commission's Seventh Framework Programme (FP7), contract number ICT-2008-216499, running from 2008 through 2010. CACE activities were organized into several Work Packages (WPs); NaCl was the main task of WP2, "Accelerating Secure Networking". Work on NaCl at Technische Universiteit Eindhoven between 2008 and 2010 was sponsored by CACE.

NaCl benefits from close collaboration with two other projects. The NaCl API is based on, and has influenced, the SUPERCOP (System for Unified Performance Evaluation Related to Cryptographic Operations and Primitives) API developed for the [eBACS (ECRYPT Benchmarking of Cryptographic Systems)](https://bench.cr.yp.to) project. Many of the algorithms and implementations used in NaCl were developed as part of Daniel J. Bernstein's High-Speed Cryptography project funded by the U.S. National Science Foundation, grant number 0716498, and the followup Higher-Speed Cryptography project funded by the U.S. National Science Foundation, grant number 1018836. Work on NaCl at the University of Illinois at Chicago was sponsored by these grants. "Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation."

Several of the implementations in NaCl are partially or entirely from third parties. The portability of NaCl relies on the `ref` implementation of Curve25519 written by Matthew Dempsky (Mochi Media, now Google). From 2009 until 2011 the speed of NaCl on common Intel/AMD CPUs relied on the `donna` and `donna_c64` implementations of Curve25519 written by Adam Langley (Google). The newest implementations of Curve25519 and Ed25519 were joint work with Niels Duif (Technische Universiteit Eindhoven) and Bo-Yin Yang (Academia Sinica). The `core2` implementation of AES was joint work with Emilia Käsper (Katholieke Universiteit Leuven, now Google).

Prototype Python wrappers around C NaCl have been posted by Langley; by Jan Mojzis; and by Sean Lynch (Facebook). Dempsky wrote reference implementations of many functions in Python NaCl.

## Version

This is version 2016.03.15 of the index.html web page.
