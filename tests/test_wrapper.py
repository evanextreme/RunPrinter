from runprinter import Printer

printer = Printer(3)
print = printer.print

test_string = "Peter piper picked a peck of pickled peppers"


def test_no_args(capsys):
    print(test_string)
    captured = capsys.readouterr()
    trimmed = captured.out[:len(captured.out)-1]
    assert trimmed == test_string


def test_sep_args(capsys):
    test_args = tuple(test_string.split())
    print(*test_args, sep="/")
    captured = capsys.readouterr()
    with_separators = test_string.replace(" ", "/")
    trimmed = captured.out[:len(captured.out)-1]
    assert trimmed == with_separators
