from BaseClasses import Item, ItemClassification
from typing import NamedTuple, Dict, TYPE_CHECKING
from .options import LocationPerStage

if TYPE_CHECKING:
    from . import MTDWorld

start_id = 1_200_000 #20 minutes in milliseconds

class MTDItem(Item):
    game: str = "20 Minutes Till Dawn"
    
class MTDItemData(NamedTuple):
    code: int
    item_type: ItemClassification = ItemClassification.useful
      
    
item_table: Dict[str, MTDItemData] = {}
    
item_table.update({"Powerup": MTDItemData(start_id),
                   "Experience": MTDItemData(start_id + 1),
                   "Time Trap": MTDItemData(start_id + 2)})