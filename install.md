# Installation

NaCl works on a wide variety of UNIX-like systems, including Linux, BSD, Solaris, etc. Here is how to download and compile NaCl:

         wget https://hyperelliptic.org/nacl/nacl-20110221.tar.bz2
         bunzip2 < nacl-20110221.tar.bz2 | tar -xf -
         cd nacl-20110221
         ./do

Several machines sharing the same filesystem can compile NaCl simultaneously in the same shared directory. All compilation takes place in a host-specific subdirectory: for example, `build/atlas` on a machine named `atlas`, and `build/katana` on a machine named `katana`.

Some machines support multiple application binary interfaces (ABIs). For example, the machine `katana` can run 32-bit x86 programs and 64-bit amd64 programs; both types of programs are supported by the CPU (an Intel Core 2 Duo), the operating system (64-bit Ubuntu), and the compiler (gcc). NaCl automatically compiles itself for each ABI: inside `build/katana`, NaCl creates both

- a 64-bit `lib/amd64/libnacl.a` accompanied by header files `include/amd64/crypto_auth.h`, `include/amd64/crypto_stream.h`, etc., and
- a 32-bit `lib/x86/libnacl.a` accompanied by `include/x86/crypto_auth.h`, `include/x86/crypto_stream.h`, etc.

The NaCl header files are created dynamically as part of the compilation process, reflecting machine-specific optimizations, and can vary from one ABI to another.

NaCl creates an ABI-independent program `bin/okabi` that prints the list of supported ABIs: for example, `amd64` and `x86`. NaCl also creates `bin/okc-amd64` to print the list of C compilers supporting the `amd64` ABI, `bin/okc-x86` to print the list of C compilers supporting the `x86` ABI, etc.

*\[TO DO:\] NaCl's header files and compiled code can be installed in appropriate system locations so that applications can include `<crypto_auth.h>`, link with `-lnacl`, etc.* Beware that current operating systems have many incompatible, and generally deficient, mechanisms of handling multiple ABIs, making multiple-ABI support rather difficult for libraries and for applications.

Rather than relying on the system to have an installation of NaCl, applications can include the NaCl source code as part of the application source code. The applications can then use `okabi`, `okc-amd64`, etc. to automatically try all ABIs and compilers and to select the fastest option.

## Version

This is version 2016.03.15 of the install.html web page.
