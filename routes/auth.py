from fastapi import APIRouter  # type: ignore
import boto3  # type: ignore
from pydantic_model.auth_model import SingupRequest  # type: ignore
from secret_keys import SecretKeys

router = APIRouter()

congnito_client = boto3.client("cognito-idp", region_name="ap-south-1")


@router.post("/singup")
def singup_user(data: SingupRequest):
    congnito_client.sing_up(
        ClientID=secret_key.COGINTO_CLINET_ID,
    )
