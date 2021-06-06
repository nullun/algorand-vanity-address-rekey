#!/usr/bin/env python3

from algosdk import account, mnemonic
import time

# Desired prefix for address.
PREFIX = "DODO"

# Store the found Private Key and Public Address
PRIVATE_KEY = ""
ADDRESS = ""

# Keep track of attempts and start time.
ATTEMPT = 0
TIME_START = time.time()

while (not ADDRESS.startswith(PREFIX)):
    TIME_DIFF = time.time() - TIME_START
    print(f" {ATTEMPT} ({ATTEMPT / TIME_DIFF:.2f}/sec) ", end="\r")
    PRIVATE_KEY, ADDRESS = account.generate_account()
    ATTEMPT += 1

print()
print(f"Found after {ATTEMPT} attempts and {TIME_DIFF:.2f} seconds")
print(ADDRESS)
print(PRIVATE_KEY)
print(mnemonic.from_private_key(PRIVATE_KEY))
print()
