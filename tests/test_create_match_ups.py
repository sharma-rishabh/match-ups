import pytest
from match_ups.create_match_ups import create_match_ups

def test_only_two_participants():
    participants=["A","B"]
    assert create_match_ups(participants) == [[("A","B")]]

def test_more_than_two_participants():
    participants=["A","B","C"]
    expected= [
        [
            ("A","B"),
            ("A","C"),
            ("B","C")
        ]
    ]
    assert create_match_ups(participants) == expected


def test_union_count():
    participants = ["A", "B", "C"]
    expected = [
        [("A", "B"), ("A", "C"), ("B", "C"), ("B", "A"), ("C", "A"), ("C", "B")]
    ]
    assert create_match_ups(participants,union_count=2) == expected


def test_phases():
    participants = ["A", "B", "C"]
    expected = [[("A", "B"), ("A", "C")], [("B", "C"), ("B", "A")], [("C", "A"), ("C", "B")]]
    assert create_match_ups(participants, union_count=2, phases=3) == expected


def test_uneven_phases():
    participants = ["A", "B", "C"]
    expected = [
        [("A", "B"), ("A", "C")],
        [("B", "C")], [("B", "A")],
        [("C", "A")], [("C", "B")],
    ]
    assert create_match_ups(participants, union_count=2, phases=5) == expected
