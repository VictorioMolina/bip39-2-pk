#!/usr/bin/env python3
"""
Interactively derive an Ethereum private key and address from a BIP-39 mnemonic.
"""

import getpass
from bip_utils import (
  Bip39SeedGenerator,
  Bip44,
  Bip44Coins,
  Bip44Changes
)

# Ask the user for the mnemonic and (optionally) the index
mnemonic = getpass.getpass(
    prompt="Enter your BIP-39 mnemonic (words separated by spaces): "
).strip()

if not mnemonic:
    print("Mnemonic cannot be empty. Aborting.")
    exit(1)

index_input = input("Address index [default: 0]: ").strip()
try:
    index = int(index_input) if index_input else 0
    if index < 0:
        raise ValueError
except ValueError:
    print("Index must be a non-negative integer. Aborting.")
    exit(1)

# Derivation: m/44'/60'/0'/0/{index}
seed_bytes   = Bip39SeedGenerator(mnemonic).Generate()
bip44_master = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)

account = (
    bip44_master
    .Purpose()                       # 44'
    .Coin()                          # 60'
    .Account(0)                      # account 0
    .Change(Bip44Changes.CHAIN_EXT)  # external chain
    .AddressIndex(index)             # desired address index
)

# Output
print("\nDerived account")
print(f"  Index    : {index}")
print(f"  Address  : {account.PublicKey().ToAddress()}")
print(f"  PrivKey  : {account.PrivateKey().Raw().ToHex()}")
print()
