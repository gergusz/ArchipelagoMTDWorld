from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING
from BaseClasses import Region, MultiWorld

if TYPE_CHECKING:
    from . import MTDWorld

# Huge thanks to the RoR2 implementation

start_id = 1_200_000 #20 minutes in milliseconds

class MTDRegionData(NamedTuple):
    region_exits: Optional[List[str]]

def create_all_regions(mtdworld: "MTDWorld") -> None:
    player = mtdworld.player
    multiworld = mtdworld.multiworld
    
    region_table: Dict[str, MTDRegionData] = {
    "Menu":                     MTDRegionData(["Forest"]),
    "Forest":                   MTDRegionData(["Temple"]),
    "Temple":                   MTDRegionData(["Pumpkin Patch"]),
    "Pumpkin Patch":            MTDRegionData([])
    }
    
    for name, data in region_table.items():
        multiworld.regions.append(create_region(multiworld, player, name, mtdworld.options.itemsamount.value))
        
    for name, data in region_table.items():
        create_connections_in_region(multiworld, player, name, data)
        
        
def create_region(multiworld: MultiWorld, player: int, name: str, amount: int) -> Region:
    region = Region(name, player, multiworld)
    locations: Dict[str, int] = {}
    if name == "Forest":    
        for i in range(amount):
            locations.update({f"Forest {i + 1}": start_id + i})
    elif name == "Temple":
        for i in range(amount):
            locations.update({f"Temple {i + 1}": start_id + amount*1 + i})
    elif name == "Pumpkin Patch":
        for i in range(amount):
            locations.update({f"Pumpkin Patch {i + 1}": start_id + amount*2 + i})
    if locations: 
        region.add_locations(locations)
    return region

def create_connections_in_region(multiworld: MultiWorld, player: int, name: str, data: MTDRegionData) -> None:
    region = multiworld.get_region(name, player)
    if data.region_exits:
        region.add_exits(data.region_exits)