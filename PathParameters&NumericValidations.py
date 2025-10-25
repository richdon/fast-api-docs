from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title="The ID of the item to get, must be >= 1", ge=1)],
                     q: Annotated[str | None, Query(alias="item-query")] = None):

    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title="The ID of the item to get, must be > 0, less than 1000",
                                                  gt=0, lt=1000)],
                     q: Annotated[str | None, Query(alias="item-query")] = None):

    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
