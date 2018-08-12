# rsa-tool
Simple tool provides rsa key generation, message encryption and decription. Useful when sending  secret messages to others. This program is more like a practice for command line tool, you can treat it as an template as well.

**usage:**  
rsa-tool.py [-h] [-v]  
                   [-g | -d message_file private_key | -e message_file public_key]  

**optional arguments:**  

  -h, --help            show this help message and exit  
  -v, --verbose         increase output verbosity  
  -g, --generate        generate a random rsa key pair  
  -d message_file private_key, --decrypt message_file private_key  
                        decrypt a message file using a specific private key file  
  -e message_file public_key, --encrypt message_file public_key
                        encrypt a message file using a specific public key file