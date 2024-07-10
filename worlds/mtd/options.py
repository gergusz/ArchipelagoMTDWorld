from dataclasses import dataclass
from Options import Range, PerGameCommonOptions

class LocationPerStage(Range):
    """
    Amount of items to give to *each* of the maps
    """
    display_name = "Item Amount"
    range_start = 5
    range_end = 50
    default = 20


@dataclass
class MTDOptions(PerGameCommonOptions):
    locationperstage: LocationPerStage
