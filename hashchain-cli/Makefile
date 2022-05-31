# /* +----------------------------------+ */
# /* | InERGitance - Hashchain CLI tool | */
# /* |             Makefile             | */
# /* |   (c)copyright nitram147 2022    | */
# /* +----------------------------------+ */
all: test_hashchain

test_hashchain: holiday_protector_hashchain.py
	python3 ./holiday_protector_hashchain.py generate "test" 10000
	python3 ./holiday_protector_hashchain.py preimage "test" "e9c7a6286aeb03820f55d3d65cc3fbf80807de327ac7f5530901b915431f7233"

.PHONY: all test_hashchain
