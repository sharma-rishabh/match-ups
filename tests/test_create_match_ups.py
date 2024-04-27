import pytest
from match_ups.create_match_ups import create_match_ups
from match_ups.pair import Pair


def test_only_two_participants():
    participants = ["A", "B"]
    assert create_match_ups(participants) == [[Pair(("A", "B"),2)]]


def test_more_than_two_participants():
    participants = ["A", "B", "C"]
    expected = [[Pair(("A", "B"),2), Pair(("A", "C"),2), Pair(("B", "C"),2)]]
    assert create_match_ups(participants) == expected


def test_union_count():
    participants = ["A", "B", "C"]
    expected = [
        [Pair(("A", "B"),6), Pair(("A", "C"),6), Pair(("B", "C"),6), Pair(("B", "A"),6), Pair(("C", "A"),6), Pair(("C", "B"),6)]
    ]
    assert create_match_ups(participants, h2h_count=2) == expected


def test_phases():
    participants = ["A", "B", "C"]
    expected = [
        [Pair(("A", "B"),6), Pair(("A", "C"),6)],
        [Pair(("B", "C"),6), Pair(("B", "A"),6)],
        [Pair(("C", "A"),6), Pair(("C", "B"),6)],
    ]
    assert create_match_ups(participants, h2h_count=2, phases=3) == expected


def test_uneven_phases():
    participants = ["A", "B", "C"]
    expected = [
        [Pair(("A", "B"),6), Pair(("A", "C"),6)],
        [Pair(("B", "C"),6)],
        [Pair(("B", "A"),6)],
        [Pair(("C", "A"),6)],
        [Pair(("C", "B"),6)],
    ]
    assert create_match_ups(participants, h2h_count=2, phases=5) == expected

def test_shuffle():
    participants = ["A", "B", "C", "D"]
    expected = [
        [
            Pair(("B", "A"),6),
            Pair(("D", "C"),6),
            Pair(("C", "A"),6),
            Pair(("D", "B"),6),
            Pair(("D", "A"),6),
            Pair(("B", "C"),6),
        ]
    ]
    actual = create_match_ups(participants)
    assert actual == expected


def test_odd_shuffle():
    participants = ["A", "B", "C", "D", "E"]
    expected = [
        [
            Pair(('B', 'A'), 6),
            Pair(('C', 'D'), 6),
            Pair(('E', 'A'), 5),
            Pair(('B', 'C'), 5),
            Pair(('A', 'D'), 5),
            Pair(('B', 'E'), 5),
            Pair(('A', 'C'), 5),
            Pair(('B', 'D'), 5),
            Pair(('E', 'C'), 5),
            Pair(('E', 'D'), 3)
        ]
    ]
    actual = create_match_ups(participants)
    assert actual == expected
