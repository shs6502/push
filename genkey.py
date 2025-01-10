from py_vapid import Vapid
import base64
from cryptography.hazmat.primitives import serialization

vapid = Vapid()
vapid.generate_keys()

# 공개키를 raw 형식으로 변환
public_key = vapid.public_key.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
)

# 개인키는 DER 형식 유지
private_key = vapid.private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

print("Public key:", base64.urlsafe_b64encode(public_key).decode('utf-8'))
print("Private key:", base64.urlsafe_b64encode(private_key).decode('utf-8'))