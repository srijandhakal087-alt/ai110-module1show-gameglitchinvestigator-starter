import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from logic_utils import (
    check_guess,
    parse_guess,
    update_score,
    validate_guess_range,
)


def test_guess_too_high():
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_correct_guess():
    outcome, message = check_guess(50, 50)

    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_first_try_score():
    score = update_score(0, "Win", 1)

    assert score == 100


def test_second_try_score():
    score = update_score(0, "Win", 2)

    assert score == 90


def test_wrong_guess_does_not_change_score():
    score = update_score(0, "Too High", 1)

    assert score == 0


def test_parse_valid_guess():
    ok, guess, error = parse_guess("42")

    assert ok is True
    assert guess == 42
    assert error is None


def test_parse_non_numeric_guess():
    ok, guess, error = parse_guess("hello")

    assert ok is False
    assert guess is None
    assert error == "That is not a number."


# Edge case 1: empty input
def test_empty_guess_is_rejected():
    ok, guess, error = parse_guess("")

    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


# Edge case 2: negative number
def test_negative_guess_is_out_of_range():
    ok, guess, error = parse_guess("-1")

    assert ok is True
    assert guess == -1
    assert error is None

    range_ok, range_error = validate_guess_range(
        guess,
        1,
        100,
    )

    assert range_ok is False
    assert range_error == "Enter a number between 1 and 100."


# Edge case 3: number above maximum
def test_guess_above_maximum_is_out_of_range():
    ok, guess, error = parse_guess("101")

    assert ok is True
    assert guess == 101
    assert error is None

    range_ok, range_error = validate_guess_range(
        guess,
        1,
        100,
    )

    assert range_ok is False
    assert range_error == "Enter a number between 1 and 100."