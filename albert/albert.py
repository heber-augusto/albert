# albert.py

from albert.jobcommands.jobcommand import *


def handle_command(args):
    if args.command:
        command_class = globals()[f'{args.command.capitalize()}Command']
        command = command_class(args)
        command.execute()

def main():
    parser = load_and_config_parser()
    args = parser.parse_args()
    handle_command(args)

if __name__ == "__main__":
    main()
