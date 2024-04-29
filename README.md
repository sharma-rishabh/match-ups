# Match Ups

A CLI tool to help you organize the next event. It can help you pair up a group of participants with each other without the fear of missing anyone out.

## How it works 

```sh
❯ match-ups "jason,roy,william,ben" --h2h-count 2 --phases 3

Phase 1
+---------+---------+
| roy     | jason   |
+---------+---------+
| ben     | william |
+---------+---------+
| william | jason   |
+---------+---------+
| ben     | roy     |
+---------+---------+
Phase 2
+-----+---------+
| ben | jason   |
+-----+---------+
| roy | william |
+-----+---------+
| roy | jason   |
+-----+---------+
| ben | william |
+-----+---------+
Phase 3
+---------+---------+
| william | jason   |
+---------+---------+
| ben     | roy     |
+---------+---------+
| ben     | jason   |
+---------+---------+
| roy     | william |
+---------+---------+

❯ match-ups --help
Usage: match-ups [OPTIONS] PARTICIPANTS

  Create matchups from a list of participants.

  PARTICIPANTS - Comma separated list of participants. Ex: "Team1,Team2"

Options:
  --h2h-count INTEGER  How many times a pair will go head to head.
  --phases INTEGER     In how many phases would the event take place.
  --help               Show this message and exit.

```

## How to install

### Prerequisite

- Python [download-python](https://www.python.org/downloads/)
- Pipx [installation-guide](https://pipx.pypa.io/stable/installation/)


```shell
❯ pipx install  git+https://github.com/sh'''arma-rishabh/match-ups.git
```
