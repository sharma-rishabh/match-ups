import pytest
from unittest.mock import patch
from match_ups.cli import match_ups
from click.testing import CliRunner


@patch("match_ups.cli.create_match_ups")
def test_arguments_parsing(create_matchups):
    create_matchups.return_value = []
    runner = CliRunner()
    runner.invoke(match_ups, ["A,B,C", "--h2h-count", "3", "--phases", "4"])
    create_matchups.assert_called_once_with(["A", "B", "C"], 3, 4)


def test_output():
    runner = CliRunner()
    result = runner.invoke(match_ups, ["A,B,C", "--h2h-count", "3", "--phases", "2"])
    expected = """Phase 1
+---+---+
| A | B |
+---+---+
| A | C |
+---+---+
| B | C |
+---+---+
| B | A |
+---+---+
| C | A |
+---+---+
Phase 2
+---+---+
| C | B |
+---+---+
| A | B |
+---+---+
| A | C |
+---+---+
| B | C |
+---+---+
"""
    assert result.exit_code == 0

    assert result.output == expected


def test_single_participant_validation():
    runner = CliRunner()
    result = runner.invoke(match_ups, ["A"])
    expected="Participant count can not be less than 2"
    assert result.exit_code != 0
    assert expected in result.output


def test_phase_validation():
    runner = CliRunner()
    result = runner.invoke(match_ups, ["A,B", "--phases", "0"])
    expected = "Phases can not be less than 1"
    assert result.exit_code != 0
    assert expected in result.output


def test_h2h_count_validation():
    runner = CliRunner()
    result = runner.invoke(match_ups, ["A,B", "--h2h-count", "0"])
    expected = "h2h-count can not be less than 1"
    assert result.exit_code != 0
    assert expected in result.output
