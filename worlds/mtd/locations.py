from typing import Dict, TYPE_CHECKING
from BaseClasses import Location
from .options import LocationPerStage

if TYPE_CHECKING:
    from . import MTDWorld

start_id = 1_200_000 #20 minutes in milliseconds

class MTDLocation(Location):
    game: str = "20 Minutes Till Dawn"

location_table: Dict[str, int] = {}

for i in range(LocationPerStage.range_end):
    location_table.update({f"Forest {i + 1}": start_id + i})
for i in range(LocationPerStage.range_end):
    location_table.update({f"Temple {i + 1}": start_id + LocationPerStage.range_end*1 + i})
for i in range(LocationPerStage.range_end):
    location_table.update({f"Pumpkin Patch {i + 1}": start_id + LocationPerStage.range_end*2 + i})


