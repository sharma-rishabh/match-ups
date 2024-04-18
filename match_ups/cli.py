import click
from tabulate import tabulate
from .create_match_ups import create_match_ups


@click.command()
@click.argument("participants")
@click.option(
    "--h2h-count",
    required=False,
    help="How many times a pair will go head to head.",
    type=int,
    default=1,
)
@click.option(
    "--phases",
    required=False,
    help="In how many phases would the event take place.",
    type=int,
    default=1,
)
def match_ups(participants: str, h2h_count: int, phases: int):
    """
    Create matchups from a list of participants.

    PARTICIPANTS - Comma separated list of participants. Ex: "Team1,Team2"
    """

    participants = participants.split(",")

    if len(participants) < 2:
        raise click.UsageError("Participant count can not be less than 2")

    if phases == 0:
        raise click.UsageError("Phases can not be less than 1")

    if h2h_count == 0:
        raise click.UsageError("h2h-count can not be less than 1")

    result = create_match_ups(participants, h2h_count, phases)

    for phase, res in enumerate(result):
        click.secho(f"Phase {phase+1}", bold=True)
        click.echo(tabulate(res, tablefmt="grid"))
