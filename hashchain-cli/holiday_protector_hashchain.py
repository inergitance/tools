# /* +----------------------------------+ */
# /* | InERGitance - Hashchain CLI tool | */
# /* |  holiday_protector_hashchain.py  | */
# /* |   (c)copyright nitram147 2022    | */
# /* +----------------------------------+ */
import hashlib
import binascii
import sys

def blake2b256(data):
    blake2b256 = hashlib.blake2b(digest_size=32)
    blake2b256.update(data)
    return bytes(blake2b256.digest())

def print_help():
	print("Usage:")
	print("\tGenerate last hash in chain")
	print("\tpython3 " + sys.argv[0] + " generate password chain_length")
	print("\n")
	print("\tFind hash preimage in chain")
	print("\tpython3 " + sys.argv[0] + " preimage password hash_value")

if len(sys.argv) != 4:
	print("Invalid count of arguments!", file=sys.stderr)
	print_help()
	sys.exit(1)

do_generate = True if sys.argv[1] == "generate" else False
do_preimage = True if sys.argv[1] == "preimage" else False

prev_hash = sys.argv[2].encode("utf-8")

if do_generate:
	
	chain_length = int(sys.argv[3])
	if chain_length < 1:
		print("Invalid chain_length value!", file=sys.stderr)
		print_help()
		sys.exit(2)
	
	for i in range(0, chain_length):
		prev_hash = blake2b256(prev_hash)

	print(binascii.hexlify(prev_hash).decode("utf-8"))
	sys.exit(0)

elif do_preimage:

	hash_value = sys.argv[3]
	if(
		len(hash_value) != 64
	):
		print("Invalid length of hash_value!", file=sys.stderr)
		print_help()
		sys.exit(3)

	try:
		hash_value = bytes.fromhex(hash_value)
	except Exception as e:
		print("Invalid hash_value - hash_value should be in hex fromat!", file=sys.stderr)
		print_help()
		sys.exit(4)

	while True:
		new_hash = blake2b256(prev_hash)
		if new_hash == hash_value:
			print(binascii.hexlify(prev_hash).decode("utf-8"))
			break
		prev_hash = new_hash

	sys.exit(0)

else:
	print("Invalid action!", file=sys.stderr)
	print_help()
	sys.exit(100)
