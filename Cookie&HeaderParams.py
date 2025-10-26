from typing import Annotated

from fastapi import Cookie, FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None,
                     user_agent: Annotated[str | None, Header()] = None):
    return {"ads_id": ads_id, "User-Agent": user_agent}


class Cookies(BaseModel):
    model_config = {"extra": "forbid"} # Not common but can forbid extra cookies
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers


