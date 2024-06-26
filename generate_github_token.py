from jwt import PyJWT
from pathlib import Path
import time
import requests
import sys

def create_jwt(
    application_id: int, private_key: bytes, expiration_seconds: int = 600
) -> str:
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + expiration_seconds,
        "iss": application_id,
    }
    jwt_instance = PyJWT()
    encoded_jwt = jwt_instance.encode(
        payload=payload, key=private_key, algorithm="RS256"
    )
    return encoded_jwt

def get_private_key_bytes(private_key_file: Path) -> bytes:
    return private_key_file.read_bytes()

def get_token(
    application_id: int, installation_id: int, private_key_file: Path
) -> str:
    private_key_bytes = get_private_key_bytes(private_key_file=private_key_file)
    signing_jwt = create_jwt(application_id=application_id, private_key=private_key_bytes)
    headers = {"Authorization": f"Bearer {signing_jwt}"}
    response = requests.post(
        url=f"https://api.github.com/app/installations/{installation_id}/access_tokens",
        headers=headers,
    )
    return response.json()["token"]

def usage():
    print("""GitHub Application Authentication Tester
Usage: python3 generate_github_token.py <application_id> <installation_id> <private_key_file>""")

def main(application_id: int, installation_id: int, private_key_file: Path):
    token = get_token(application_id=application_id, installation_id=installation_id, private_key_file=private_key_file)
    print(f"Generated GitHub Token: {token}")

if __name__ == "__main__":
    if not len(sys.argv) == 4:
        usage()
        sys.exit(1)
    main(application_id=int(sys.argv[1]), installation_id=int(sys.argv[2]), private_key_file=Path(sys.argv[3]))
