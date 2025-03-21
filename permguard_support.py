import json
import logging
import os
import uuid

from fastapi import Depends, HTTPException, Request
from permguard.az.azreq.builder_principal import PrincipalBuilder
from permguard.az.azreq.builder_request_atomic import AZAtomicRequestBuilder
from permguard.az_client import AZClient
from permguard.az_config import with_endpoint
from typing_extensions import Annotated

from security_support import User, get_current_user


async def resource_action_evaluate(request: Request, current_user: User, input_string: str):
    try:
        az_client = AZClient(with_endpoint(os.environ.get("host", "127.0.0.1"), os.environ.get("port", 9094)))
        body = await request.body()
        body_json = json.loads(body)
        principal = PrincipalBuilder(current_user.username).build()
        req = (
            AZAtomicRequestBuilder(
                os.environ.get("zone", 197102289968),
                os.environ.get("ledger", "359f7ed82fac42f0a438f4f80174c52a"),
                input_string,
                body_json.get("resource_type"),
                body_json.get("action"),
            )
            .with_request_id(str(uuid.uuid4()))
            .with_principal(principal)
            .with_entities_items("cedar", [])
            .with_subject_role_actor_type()
            .with_subject_source("fastapi")
            .with_subject_property("groups", current_user.groups)
            .with_resource_id(body_json.get("resource_id"))
            .build()
        )

        ok, response = az_client.check(req)
        logging.info(f"Permguard check: {response}")
        if not ok:
            raise HTTPException(status_code=403, detail="Permguard check failed: " + str(response))
        return True
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_resource_action_evaluate(input_string: str):
    async def wrapper(request: Request, current_user: Annotated[User, Depends(get_current_user)]):
        return await resource_action_evaluate(request, current_user, input_string)
    return wrapper
