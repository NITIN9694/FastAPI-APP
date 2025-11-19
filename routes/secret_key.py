from pydantic import BaseSetting


class SecretKeys(BaseSetting):
    COGINTO_CLINET_ID: str = ""
    COGINTO_CLINET_SECRET: str = ""
