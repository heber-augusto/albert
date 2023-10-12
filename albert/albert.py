# albert.py

from jobcommands.jobcommand import *

def main():
    parser = argparse.ArgumentParser(description="Comandos para gerenciamento de job types.")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis.")

    commands = [
        CreateCommand,
        CheckCommand,
        RunCommand,
        DeployCommand,
        TestCommand
    ]

    for command_class in commands:
        command = command_class(None)
        command.add_parser(subparsers)

    args = parser.parse_args()

    if args.command:
        command_class = globals()[f'{args.command.capitalize()}Command']
        command = command_class(args)
        command.execute()

if __name__ == "__main__":
    main()
