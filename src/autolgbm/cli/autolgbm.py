import argparse

from .. import __version__
from .predict import PredictAutoLGBMCommand
from .serve import ServeAutoLGBMCommand
from .train import TrainAutoLGBMCommand


def main():
    parser = argparse.ArgumentParser(
        "AutoLGBM CLI",
        usage="autolgbm <command> [<args>]",
        epilog="For more information about a command, run: `autolgbm <command> --help`",
    )
    parser.add_argument("--version", "-v", help="Display AutoLGBM version", action="store_true")

    commands_parser = parser.add_subparsers(help="commands")
    TrainAutoLGBMCommand.register_subcommand(commands_parser)
    PredictAutoLGBMCommand.register_subcommand(commands_parser)
    ServeAutoLGBMCommand.register_subcommand(commands_parser)

    args = parser.parse_args()

    if args.version:
        print(__version__)
        exit(0)

    if not hasattr(args, "func"):
        parser.print_help()
        exit(1)

    command = args.func(args)
    command.execute()


if __name__ == "__main__":
    main()
