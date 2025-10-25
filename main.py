from enum import StrEnum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ModelName(StrEnum):
    linear = "linear"
    polynomial = "polynomial"


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    match model_name:
        case ModelName.linear:
            return {"model": model_name, "message": f"{model_name} regression"}
        case _:
            return {"model": model_name, "message": f"{model_name} regression"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     if skip < len(fake_items_db):
#         return fake_items_db[skip: skip + limit]
#     return []


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    return item


from fastapi import Query
from typing import Annotated


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50,
                                                    min_length=3,
                                                    pattern="^fixedquery$")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items-list/")
async def read_items_list(q: Annotated[list[str] | None, Query(max_length=50,
                                                               min_length=3,
                                                               description="provide api description",
                                                               )] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    print(q)
    if q:
        results.update({"q": q})
    return results
