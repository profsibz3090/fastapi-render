from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

inventory = {}

class Item(BaseModel):
    name: str
    price: int
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    brand: Optional[str] = None

@app.get('/')
def hello():
    return {'data': 'tirimo'}

@app.get('/get-item/{item_id}')
def get_item(item_id: int):
    return inventory[item_id]

@app.post('/create/{item_id}')
def create_item(item_id: int, item: Item):
    inventory[item_id] = item
    return inventory[item_id]

@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {'Error': 'item does not exist'}
    
    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price
    
    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]

@app.delete('/delete/{item_id}')
def delete_item(item_id: int):
    if item_id not in inventory:
        return {'Error': 'item doesnot exist'}
    
    del inventory[item_id]
    return {'success': ' item deleted successfully'}