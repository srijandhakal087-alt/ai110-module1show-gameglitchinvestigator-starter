# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

This project is a Streamlit number guessing game that was generated with several bugs. The player must guess a secret number within a limited number of attempts while receiving higher/lower hints. The original version had broken hint logic, inconsistent scoring, state issues, and problems restarting the game.

## 🛠️ Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
python -m streamlit run app.py
```

3. Run the automated tests:

```bash
pytest
```

## 🕵️‍♂️ Bugs Found

While testing the game, I found several problems:

- The higher/lower hints were sometimes backwards.
- The secret value was being converted between an integer and a string, causing inconsistent comparison behavior.
- Invalid guesses such as `-1` were accepted even when the valid range was 1–100.
- The New Game button did not reset the game status, so the player could remain stuck after losing.
- The attempt counter originally started incorrectly and the displayed attempts could become outdated after a guess.
- A first-attempt win gave 80 points instead of 100 because of an off-by-one scoring calculation.
- Wrong guesses could randomly increase or decrease the player's score.

## 🔧 Fixes Applied

I moved the reusable game logic from `app.py` into `logic_utils.py` so that the logic could be tested independently from the Streamlit UI.

The main fixes included:

- Corrected the higher/lower hint logic.
- Removed the integer/string conversion that caused inconsistent comparisons.
- Added input validation so guesses outside the selected difficulty range are rejected.
- Updated New Game so it resets the secret number, attempts, score, status, history, and messages.
- Corrected the scoring formula so a first-attempt win gives 100 points.
- Removed inconsistent score changes for wrong guesses.
- Updated Streamlit session state and rerun behavior so the attempts display stays current.
- Added pytest tests to verify the repaired logic.

## 📸 Demo Walkthrough

1. Start the game by running `python -m streamlit run app.py`.
2. Select a difficulty from the sidebar. The game displays the valid number range and number of allowed attempts.
3. Open **Developer Debug Info** to view the secret number for testing.
4. Enter a number lower than the secret and click **Submit Guess**. The game displays **Go HIGHER!**
5. Enter a number higher than the secret. The game displays **Go LOWER!**
6. Enter the correct secret number. The game displays a winning message and final score.
7. Click **New Game** to reset the secret, attempts, score, game status, and guess history.
8. Try entering a number outside the valid range. The game rejects the input without using an attempt.
9. Run `pytest` in the terminal to verify the game logic automatically.

**Screenshot (optional):**

Add a screenshot here showing the fixed game after a successful guess.

## 🧪 Test Results

The automated test set verifies the hint logic, correct guesses, scoring behavior, and input parsing.

```text
pytest
================================ test session starts ================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0
collected 8 items

tests/test_game_logic.py ........                                      [100%]

================================= 8 passed =================================
```

One scoring test initially failed because the game still subtracted 5 points for a wrong guess. After updating `update_score()` so wrong guesses leave the score unchanged, the test passed.

## 📝 Project Files

The project includes:

- `app.py` — Streamlit user interface and game state management
- `logic_utils.py` — refactored game logic
- `tests/test_game_logic.py` — automated pytest tests
- `reflection.md` — debugging and AI collaboration reflection
- `ai_interactions.md` — AI-assisted test generation documentation
- `README.md` — project overview and demo walkthrough

## 🚀 Stretch Features

- [x] AI-assisted test generation documented in `ai_interactions.md`
- [ didnt do it] Enhanced UI changes