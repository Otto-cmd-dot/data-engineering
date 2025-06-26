from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/")
def read_items(q: str = None):    
    if q: return {"items": ["Item 1", "Item 2", "Item 3"], "query": q}    
    return {"items": ["Item 1", "Item 2", "Item 3"]}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):    
    return {"item_id": item_id, "query": q}