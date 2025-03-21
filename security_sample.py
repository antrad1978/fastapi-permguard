import logging

import uvicorn
from fastapi import FastAPI
from fastapi.security import (
    OAuth2PasswordRequestForm,
)

from permguard_support import get_resource_action_evaluate
from security_support import *

app = FastAPI()


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])]
):
    return [{"item_id": "Foo", "owner": current_user.username}]


@app.get("/status/")
async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
    logging.info(current_user.username)
    return {"status": "ok"}


@app.post("/items/")
async def read_items(result: dict = Depends(get_resource_action_evaluate("platform-editor"))):
    logging.info(result)
    return {"items": ["item1", "item2"]}

if __name__ == "__main__":
    uvicorn.run("security_sample:app", reload=True)