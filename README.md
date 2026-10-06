# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

Game Glitch Investigator is a Streamlit number guessing game. The player guesses a secret number within a limited number of attempts while receiving higher/lower hints.

The starter version contained several logic and state bugs that made the game behave unpredictably. This project investigates those bugs, repairs them, refactors reusable logic into `logic_utils.py`, and verifies the fixes with pytest.

## 🛠️ Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

Run the automated tests:

```bash
pytest
```

## 🐛 Bugs Found

During manual testing, I found several reproducible issues:

- Higher/lower hints could point in the wrong direction.
- The secret value alternated between an integer and a string, causing inconsistent comparisons.
- Invalid guesses such as `-1` were accepted even though the valid range started at 1.
- New Game did not reset the game status after a loss.
- The initial attempt counter was incorrect.
- A first-attempt win awarded 80 points instead of 100.
- Wrong guesses could inconsistently add or subtract score.
- The displayed attempts remaining could become stale after a guess.

## 🔧 Fixes Applied

The repaired version:

- Refactors game logic into `logic_utils.py`.
- Keeps the secret number as an integer.
- Corrects the higher/lower hints.
- Validates guesses against the selected difficulty range.
- Prevents invalid guesses from using an attempt.
- Correctly resets state when starting a new game.
- Starts the attempt counter at zero.
- Awards 100 points for a first-attempt win and reduces the reward for later wins.
- Prevents wrong guesses from randomly changing score.
- Uses Streamlit session state and reruns so displayed values stay synchronized with the game state.

## 🧪 Edge-Case Testing

The automated test suite includes normal game behavior and several invalid-input edge cases.

Examples include:

- Empty input
- Non-numeric input such as `"hello"`
- Negative input such as `-1`
- Input above the maximum such as `101`
- High and low hint behavior
- Correct-guess behavior
- First- and second-attempt scoring
- Incorrect-guess scoring behavior

These tests are implemented in `tests/test_game_logic.py`.

## 📸 Demo Walkthrough

1. Run `python -m streamlit run app.py`.
2. Select Easy, Normal, or Hard difficulty.
3. The game displays the selected number range and available attempts.
4. Open **Developer Debug Info** to view the secret for testing.
5. Enter a number below the secret. The game displays **Go HIGHER!**
6. Enter a number above the secret. The game displays **Go LOWER!**
7. Enter an invalid number such as `-1`. The game rejects it without consuming an attempt.
8. Enter the correct number. The game displays a successful result and final score.
9. Click **New Game** and verify that attempts, score, history, secret, and game status reset.
10. Run `pytest` to verify the game logic automatically.

## 🧪 Test Results

Example final test run:

```text
pytest
================================ test session starts ================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0
collected 11 items

tests/test_game_logic.py ...........                                  [100%]

================================ 11 passed ================================
```

The test suite helped catch a remaining scoring bug during development. A test originally expected an incorrect guess to leave the score unchanged but received `-5`, which showed that part of the old scoring logic was still active. After repairing `update_score()`, the test passed.

## 📁 Project Files

- `app.py` — Streamlit interface and session-state management
- `logic_utils.py` — reusable and testable game logic
- `tests/test_game_logic.py` — pytest test suite
- `reflection.md` — bug reproduction evidence and AI collaboration reflection
- `ai_interactions.md` — AI-assisted edge-case test-generation log
- `README.md` — project documentation

## 🚀 Stretch Features

- [x] Advanced edge-case testing with AI-assisted pytest generation
- [ ] Feature expansion via Agent Mode
- [ ] Professional linting/style stretch challenge
- [ ] Enhanced UI stretch challenge
- [ ] Two-model comparison