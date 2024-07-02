from typing import Dict, TYPE_CHECKING
from BaseClasses import Location

if TYPE_CHECKING:
    from . import MTDWorld

start_id = 1_200_000 #20 minutes in milliseconds

class MTDLocation(Location):
    game: str = "20 Minutes Till Dawn"

location_table: Dict[str, int] = {}

def create_location_table(mtdworld: "MTDWorld") -> None:
    options = mtdworld.options
    for i in range(options.itemsamount.value):
        location_table.update({f"Forest {i + 1}": start_id + i})
    for i in range(options.itemsamount.value):
        location_table.update({f"Temple {i + 1}": start_id + options.itemsamount.value*1 + i})
    for i in range(options.itemsamount.value):
        location_table.update({f"Pumpkin Patch {i + 1}": start_id + options.itemsamount.value*2 + i})


