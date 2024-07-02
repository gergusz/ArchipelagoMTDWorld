from BaseClasses import Item, ItemClassification
from typing import NamedTuple, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import MTDWorld

start_id = 1_200_000 #20 minutes in milliseconds

class MTDItem(Item):
    game: str = "20 Minutes Till Dawn"
    
class MTDItemData(NamedTuple):
    code: int
    item_type: ItemClassification = ItemClassification.progression
      
    
item_table: Dict[str, MTDItemData] = {}
    
def create_item_table(mtdworld: "MTDWorld") -> None:
    options = mtdworld.options
    for i in range(options.itemsamount.value):
        item_table.update({f"Forest: Item {i + 1}": MTDItemData(start_id + i)})
    for i in range(options.itemsamount.value):
        item_table.update({f"Temple: Item {i + 1}": MTDItemData(start_id + options.itemsamount.value*1 + i)})
    for i in range(options.itemsamount.value):
        item_table.update({f"Pumpkin Patch: Item {i + 1}": MTDItemData(start_id + options.itemsamount.value*2 + i)})