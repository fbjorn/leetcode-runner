from pathlib import Path

from typer import Argument, Option, Typer, echo

from leetcode_runner.fetcher import fetch_problem, make_gql_client
from leetcode_runner.generator import create_content

cli = Typer()


@cli.command()
def pull(
    slug: str = Argument(..., help="Problem slug"),
    out: Path = Option(
        None, help="Output filename. Defaults to $id-$slug.py in the current folder"
    ),
):
    client = make_gql_client()
    problem = fetch_problem(client, slug)
    content = create_content(problem)

    if not out:
        out = Path(f"{problem.question.question_id}-{slug}.py")

    out.write_text(content, encoding="utf8")
    echo(f"{out} has been created! Happy solving")


@cli.command(name="help")
def _help():
    pass
