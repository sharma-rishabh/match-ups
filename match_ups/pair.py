from typing import Tuple


class Pair:

    def __init__(self, value: Tuple[str, str], recency:int) -> None:
        self.value = set(value)
        self.recency=recency

    def does_intersect(self, pair: 'Pair') -> bool:
        return len(self.value.intersection(pair.value)) > 0

    def intersection_count(self, pair: 'Pair') -> int:
        return len(self.value.intersection(pair.value))
    
    def reverse(self):
        return Pair(tuple(reversed(tuple(self.value))),self.recency)

    def __eq__(self, pair: 'Pair') -> bool:
        if not isinstance(pair, Pair):
            return False

        return len(self.value.union(pair.value)) == 2

    def __str__(self) -> str:
        return f"Pair({self.value}, {self.recency})"

    def __hash__(self):
        return hash(tuple(self.value))
