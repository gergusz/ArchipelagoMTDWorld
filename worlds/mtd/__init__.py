from worlds.AutoWorld import World
from .options import MTDOptions
from .items import item_table, MTDItem, create_item_table
from .locations import location_table, create_location_table
from .regions import create_all_regions
from typing import List, ClassVar

start_id = 1_200_000 #20 minutes in milliseconds

class MTDWorld(World):
    """
    20 Minutes Till Dawn is a roguelike shoot 'em up game by flanne.
    The player controls a character who fights against continuous waves of monsters,
    with the goal being to survive the onslaught until dawn.
    """

    game = "20 Minutes Till Dawn"
    options_dataclass = MTDOptions
    options: MTDOptions
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: id for name, id in location_table.items()}
    
    def generate_early(self) -> None:
        create_location_table(self)
    
    def create_item(self, name: str) -> MTDItem:
        data = item_table[name]
        return MTDItem(name, data.item_type, data.code, self.player)
    
    def create_items(self) -> None:
        create_item_table(self)
        itempool: List[str] = []
        for name, _ in item_table.items():
            itempool += [name]
        self.multiworld.itempool += map(self.create_item, itempool)
        
    def create_regions(self) -> None:
        create_all_regions(self)
        
