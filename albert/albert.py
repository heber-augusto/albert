# albert.py

from albert.jobcommands.jobcommand import *

def main():
    parser = load_and_config_parser()

    args = parser.parse_args()

    if args.command:
        command_class = globals()[f'{args.command.capitalize()}Command']
        command = command_class(args)
        command.execute()

if __name__ == "__main__":
    main()
