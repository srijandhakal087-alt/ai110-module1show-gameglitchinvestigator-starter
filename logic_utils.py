def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for the selected difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50

    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an integer guess.

    Returns:
        tuple: (ok, guess_int, error_message)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    return True, value, None


def validate_guess_range(guess: int, low: int, high: int):
    """
    Check whether a parsed guess is inside the allowed game range.

    Returns:
        tuple: (is_valid, error_message)
    """
    if guess < low or guess > high:
        return False, f"Enter a number between {low} and {high}."

    return True, None


# FIXME: Logic breaks here because the high/low hint logic was incorrect.
# FIX: Refactored from app.py and corrected the hint direction with AI assistance.
def check_guess(guess: int, secret: int):
    """
    Compare a guess with the secret number.

    Returns:
        tuple: (outcome, message)
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


# FIXME: Logic breaks here because the scoring calculation was off.
# FIX: Corrected first-attempt scoring and removed inconsistent score
# changes for incorrect guesses with AI assistance.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Return the updated score for the current guess outcome."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)

        if points < 10:
            points = 10

        return current_score + points

    return current_score