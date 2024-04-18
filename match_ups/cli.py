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
    participants=participants.split(",")
    result = create_match_ups(participants, h2h_count, phases)

    for phase,res in enumerate(result):
        click.secho(f"Phase {phase+1}", bold=True)
        click.echo(
            tabulate(
                res,
                tablefmt="grid"
            )
        )
