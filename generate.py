#!/usr/bin/env python3

# Copyright 2026 The Libernet Team
# SPDX-License-Identifier: Apache-2.0

"""Compute Montgomery constants for a given prime modulus."""

import math

from sympy import factorint

# BLS12-381
# p = 0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001
# g = 7

# BlueSky
p = 0x7ffffffffffffffffffffffffffffffe0673ddf29e9b5547c000000000000001
g = 5

prime_factors = list(factorint(p - 1).keys())


def is_generator(g):
    return all(pow(g, (p - 1) // q, p) != 1 for q in prime_factors)


assert g == next(g for g in range(2, p) if is_generator(g))

bits = p.bit_length()
print(f"p bit length: {bits}")

word_size = 64
num_limbs = math.ceil(bits / word_size)
k = word_size * num_limbs

R = (1 << k) % p
R2 = (R * R) % p

# P_INV = -p^{-1} mod 2^64
# Used in CIOS Montgomery reduction: m = t0.wrapping_mul(P_INV)
# Only the lowest 64-bit limb of p matters for the mod-2^64 inverse.
word = 1 << word_size
p0 = p % word  # lowest 64-bit limb
p_inv = (-pow(p0, -1, word)) % word

two_inv = pow(2, p - 2, p)

s = 0
t = p - 1
while t % 2 == 0:
    t //= 2
    s += 1

omega = pow(g, t, p)
omega_inv = pow(omega, p - 2, p)

assert (pow(omega, 1 << i, p) != 1 for i in range(0, s))
assert pow(omega, 1 << s, p) == 1

delta = pow(g, 1 << s, p)


def hex(n):
    return f"{n:#0{66}x}"


def mont(v):
    return hex((v * R) % p)


print(f"p:           {hex(p)}")
print(f"k:           {k}")
print(f"num limbs:   {num_limbs}")
print(f"g:           {g}  (verified)")
print()

print(f"prime factors of p-1: {prime_factors}")
print()

print(f"R          = {hex(1 << k)}")
print(f"gcd(R, p)  = {math.gcd((1 << k), p)}  (must be 1)")
print(f"R mod p    = {hex(R)}")
print(f"R^2 mod p  = {hex(R2)}")
print()

print(f"p-1        = {hex(p - 1)}, {mont(p - 1)}")
print(f"p-2        = {hex(p - 2)}, {mont(p - 2)}")
print(f"g          = {hex(g)}, {mont(g)}")
print()

print(f"P0         = {hex(p0)}")
print(f"P^-1       = {hex(p_inv)}")
print()

print(f"2^-1       = {hex(two_inv)}, {mont(two_inv)}")
print()

print(f"S:           {s}")
print(f"w          = {hex(omega)}, {mont(omega)}")
print(f"w^-1       = {hex(omega_inv)}, {mont(omega_inv)}")
print(f"delta      = {hex(delta)}, {mont(delta)}")
print()
