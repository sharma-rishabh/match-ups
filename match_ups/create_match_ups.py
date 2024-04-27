import math
from typing import List, Tuple
from itertools import combinations
from functools import reduce
from match_ups.pair import Pair


def is_even(num):
    return num % 2 == 0


def current_union_combinations(
    combinations: List[Pair], curr_union_count: int
) -> List[Pair]:
    if not is_even(curr_union_count):
        return [combo.reverse() for combo in combinations]

    return combinations


def partition(input_array, partition_size):
    min_element_count = len(input_array) // partition_size
    remaining_element_count = len(input_array) % partition_size

    def create_partition(partitions, new_ele):
        if len(partitions[-1]) < min_element_count:
            partitions[-1].append(new_ele)
            return partitions

        partitions.append([new_ele])
        return partitions

    return reduce(
        create_partition,
        input_array[min_element_count + remaining_element_count :],
        [input_array[: min_element_count + remaining_element_count]],
    )


def can_add(shuffled: List[Pair], pair: Pair, unique_pair_count: int) -> bool:
    if len(shuffled) % unique_pair_count == 0:
        return True
    
    for p in shuffled[-(unique_pair_count - 1):]:
        if pair.does_intersect(p):
            return False

    return True

def get_remaining(remaining: List[Pair], shuffled: List[Pair]) -> List[Pair]:
    return [rem for rem in remaining if rem not in shuffled]

def get_pair_recency(curr_pair: Pair, window: List[Pair], max_recency: int):
    recency = max_recency * 2

    for i, pair in enumerate(reversed(window),1):
        intersections = pair.intersection_count(curr_pair)
        recency -=((max_recency * intersections) - ( i * intersections))
    return recency

def update_recency(window: List[Pair], pairs: List[Pair], max_recency: int)->List[Pair]:
    for pair in pairs:
        pair.recency = get_pair_recency(pair, window, max_recency)

    return pairs

def get_next_pair(pairs:List[Pair]) -> Pair:
    return reduce(lambda x, y: x if x.recency >= y.recency else y, pairs)

def organized_shuffle(pairs: List[Pair], max_recency:int) -> List[Pair]:
    shuffled = []
    remaining = pairs[:]

    max_window_size=max_recency-1


    while len(remaining) != 0:

        window = shuffled[-max_window_size:]
        remaining = update_recency(window, remaining, max_recency)
        shuffled.append(get_next_pair(remaining))

        remaining = get_remaining(remaining, shuffled)


    return shuffled


def create_match_ups(
    participants: List[str], h2h_count: int = 1, phases: int = 1
) -> List[List[Tuple[str]]]:
    all_combinations = list(combinations(participants, 2))

    max_recency=math.ceil(len(participants) / 2)
    all_combinations = [Pair(combo, max_recency) for combo in all_combinations]

    all_combinations=organized_shuffle(all_combinations, max_recency)

    match_ups = []
    for i in range(h2h_count):
        match_ups += current_union_combinations(all_combinations, i)

    return partition(match_ups, phases)
