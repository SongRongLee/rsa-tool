#!/usr/bin/env python

# import modules related to cli tool
import sys
import argparse
import logging

# import modules related to main functionality
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

# main function
def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    # generate random rsa key pair
    if args.generate:
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)

        # Save public key
        public_file = open('public_key.pem', 'wb')
        public_file.write(key.publickey().export_key())
        public_file.close()

        # Save private key
        private_file = open('private_key.pem', 'wb')
        private_file.write(key.export_key())
        private_file.close()
        print('Key pair generated successfully.')

    # decrypt message_file with private_file
    elif args.decrypt:
        # decrypt
        message_file = open(args.decrypt[0], 'rb')        
        private_key = RSA.import_key(open(args.decrypt[1], 'rb').read())
        decryptor = PKCS1_OAEP.new(private_key)
        decrypted = decryptor.decrypt(message_file.read())
        print('Message decrypted as follow:')
        print(decrypted.decode('utf-8'))

    # encrypt message_file with public_file
    elif args.encrypt:
        # encrypt
        message_file = open(args.encrypt[0], 'rb')        
        public_key = RSA.import_key(open(args.encrypt[1], 'rb').read())
        encryptor = PKCS1_OAEP.new(public_key)
        encrypted = encryptor.encrypt(message_file.read())

        # Save encrypted message
        encrypted_file = open('encrypted', 'wb')
        encrypted_file.write(encrypted)
        encrypted_file.close()
        print('Message encrypted successfully.')

# Program begin point
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Simple tool provides rsa key generation, message encryption and decription.")
    # Parameters
    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-g",
        "--generate",
        help="generate a random rsa key pair",
        action="store_true")
    group.add_argument(
        "-d",
        "--decrypt",
        help="decrypt a message file using a specific private key file",
        nargs=2,
        metavar=('message_file', 'private_key'))
    group.add_argument(
        "-e",
        "--encrypt",
        help="encrypt a message file using a specific public key file",
        nargs=2,
        metavar=('message_file', 'public_key'))

    args = parser.parse_args()

    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO

    main(args, loglevel)
