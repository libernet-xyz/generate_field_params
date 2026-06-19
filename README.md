This Python script is used to derive all parameters of a finite field (eg. multiplicative generator,
root of unity, etc.) given its prime order. The derived parameters are printed in both natural and
Montgomery form.

The script currently support [BlueSky](https://crates.io/crates/starkom-bluesky) (order
`0x7ffffffffffffffffffffffffffffffe0673ddf29e9b5547c000000000000001`) and the scalar field of
BLS12-381 (order `0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001`).

The following is the output for BlueSky:

```
p bit length: 255
p:           0x7ffffffffffffffffffffffffffffffe0673ddf29e9b5547c000000000000001
k:           256
num limbs:   4
g:           5  (verified)

prime factors of p-1: [2, 3, 31, 47491, 117579359, 20313611, 880985987837994013]

R          = 0x10000000000000000000000000000000000000000000000000000000000000000
gcd(R, p)  = 1  (must be 1)
R mod p    = 0x00000000000000000000000000000003f318441ac2c955707ffffffffffffffe, 0x1968ac3835a4f8ddb296e2afc92ce69dab970f33c00b568dbfffffffffffffe5
R^2 mod p  = 0x1968ac3835a4f8ddb296e2afc92ce69dab970f33c00b568dbfffffffffffffe5, 0x47d59d40e87e7a4d4393385da60db4e3a322c6f674c8858b4333760f1eed1fbe

p-1        = 0x7ffffffffffffffffffffffffffffffe0673ddf29e9b5547c000000000000000, 0x7ffffffffffffffffffffffffffffffa135b99d7dbd1ffd74000000000000003

P0         = 0x000000000000000000000000000000000000000000000000c000000000000001
P^-1       = 0x000000000000000000000000000000000000000000000000bfffffffffffffff

2^-1       = 0x3fffffffffffffffffffffffffffffff0339eef94f4daaa3e000000000000001, 0x00000000000000000000000000000001f98c220d6164aab83fffffffffffffff

S:           62
w          = 0x2772569d549e1249ca6891eceba43568f6e0a747a2afe898b3977ca1a5bbfc9c, 0x771ec3ece255e5ff539332d8030750aa9668eae30ea674fd1c21299e7a6bf02c
w^-1       = 0x76def406f046ef5ee7eeecd2c4e6ecd7cdedc4e2bcf6b19f1420121cd00b4cdb, 0x093d94fd0d3cc2799ed9b5f1d9a9a30f3eb41e848f20b29e9d664a1b2af8b848
delta      = 0x232680e97f4b6251c95edefd145053d6dea23905b503a1002987caddeb54cdce, 0x0e26e41e50befeed1690cf9f051915cadaab9f0d961bebc70f81667ad386a65e
```
