from typing import List, Tuple
from itertools import combinations
from functools import reduce


def is_even(num):
    return num % 2 == 0


def current_union_combinations(
    combinations: List[str], curr_union_count: int
) -> List[str]:
    if not is_even(curr_union_count):
        return [tuple(reversed(combo)) for combo in combinations]

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


def create_match_ups(
    participants: List[str], h2h_count: int = 1, phases: int = 1
) -> List[List[Tuple[str]]]:
    all_combinations = list(combinations(participants, 2))

    match_ups = []
    for i in range(h2h_count):
        match_ups += current_union_combinations(all_combinations, i)

    return partition(match_ups, phases)
