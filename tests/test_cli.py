import pytest
from unittest.mock import patch
from match_ups.cli import match_ups
from click.testing import CliRunner


@patch("match_ups.cli.create_match_ups")
def test_arguments_parsing(create_matchups):
    create_matchups.return_value=[]
    runner = CliRunner()
    runner.invoke(match_ups, ["A,B,C", "--h2h-count", "3", "--phases", "4"])
    create_matchups.assert_called_once_with(["A", "B", "C"], 3, 4)

def test_output():
    runner = CliRunner()
    result = runner.invoke(match_ups, ["A,B,C", "--h2h-count", "3", "--phases", "2"])
    excepted = """Phase 1
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

    assert result.output == excepted
