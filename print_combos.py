from itertools import product
from argparse import ArgumentParser


def get_solutions(string, chars_remaining=None):
    if chars_remaining is None:
        chars_remaining = 'abcdefghijklmnopqrstuvwxyz'
    solutions = []
    spaces_to_fill = len(list(filter(lambda x: x == '_', string)))
    filler_chars = product(chars_remaining, repeat=spaces_to_fill)
    for char_set in filler_chars:
        cur_word = string
        for i in range(spaces_to_fill):
            cur_word = cur_word.replace('_', char_set[i], 1)
        solutions.append(cur_word)

    return solutions


def print_combos():
    parser = ArgumentParser()
    parser.add_argument(
        '-s',
        '--string',
        type=str,
        required=True,
        help='a 5-char string with letters and underscores only, representing '
             'correctly placed letters and unknown positions'
    )
    parser.add_argument(
        '-r',
        '--remaining',
        type=str,
        required=False,
        help='a string containing letters only, which may fill the empty, '
             'unknown spaces'
    )
    remaining, string = parse_and_validate_options(parser)

    solutions = get_solutions(string, chars_remaining=remaining)
    print(f"There are {len(solutions)} possible solutions:")
    for solution in solutions:
        print(solution)


def parse_and_validate_options(parser):
    args = parser.parse_args()
    string = args.string
    remaining = args.remaining
    if len(string) != 5:
        raise Exception(f"The string should be exactly 5 characters long.")
    for char in string:
        if not char.isalpha() and not char == '_':
            raise Exception(f"The string passed for validation contains "
                            f"invalid characters. It should only contain "
                            f"letters and underscores.")
    if remaining is not None:
        for char in remaining:
            if not char.isalpha():
                raise Exception("The option --remaining should contain letters only.")
    return remaining, string


if __name__ == "__main__":
    print_combos()