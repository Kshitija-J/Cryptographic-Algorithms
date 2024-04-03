import os
import base64
from cryptography.fernet import Fernet
import hashlib
import json


class DiffieHellman:
    def __init__(self, p, g):
        self.p = p
        self.g = g
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key(self.private_key)

    def generate_private_key(self):
        return os.urandom(16)  # In real use, this should be a large random number

    def generate_public_key(self, private_key):
        return pow(self.g, int.from_bytes(private_key, byteorder='big'), self.p)

    def generate_shared_secret(self, private_key, public_key):
        return pow(public_key, int.from_bytes(private_key, byteorder='big'), self.p)


class C_ABAC_System:
    def __init__(self, dh_instance):
        self.dh = dh_instance
        self.policies = {
            "confidential": {"min_clearance": 2, "department": "finance"},
            "restricted": {"min_clearance": 1, "department": "hr"}
        }

    def generate_nonce(self):
        return os.urandom(16)

    def encrypt_policy_with_dh(self, policy_name, nonce, public_key_other):
        shared_secret = self.dh.generate_shared_secret(self.dh.private_key, public_key_other)
        cipher_suite = Fernet(base64.urlsafe_b64encode(shared_secret.to_bytes(32, byteorder='big')))

        policy = self.policies[policy_name]
        policy_str = json.dumps(policy).encode() + nonce
        encrypted_policy = cipher_suite.encrypt(policy_str)

        print("PGU - Plain Policy:", policy_str)
        print("PGU - Encrypted Policy:", encrypted_policy)

        return encrypted_policy, shared_secret

    def generate_token(self, user_attributes, nonce):
        token_input = json.dumps(user_attributes).encode() + nonce
        attribute_token = hashlib.sha256(token_input).hexdigest()

        print("TGU - Token Input:", token_input)
        print("TGU - Attribute Token:", attribute_token)

        return attribute_token

    def access_decision(self, encrypted_policy, attribute_token, nonce, public_key_other, shared_secret):
        try:
            cipher_suite = Fernet(base64.urlsafe_b64encode(shared_secret.to_bytes(32, byteorder='big')))
            decrypted_policy_bytes = cipher_suite.decrypt(encrypted_policy)
            decrypted_policy = decrypted_policy_bytes[:-len(nonce)].decode()  # Removing nonce before decoding

            print("PDU - Decrypted Policy:", decrypted_policy)

            expected_token = hashlib.sha256(decrypted_policy_bytes).hexdigest()
            return attribute_token == expected_token
        except Exception as e:
            print("Error during decryption:", e)
            return False


p = 23 
g = 5  

dh = DiffieHellman(p, g)
c_abac_system = C_ABAC_System(dh)


public_key_other = dh.generate_public_key(dh.generate_private_key())

nonce = c_abac_system.generate_nonce()
user_attributes = {"clearance": 2, "department": "finance"}

encrypted_policy, shared_secret = c_abac_system.encrypt_policy_with_dh("confidential", nonce, public_key_other)
attribute_token = c_abac_system.generate_token(user_attributes, nonce)

decision = c_abac_system.access_decision(encrypted_policy, attribute_token, nonce, public_key_other, shared_secret)
print("Access Granted:", decision)
