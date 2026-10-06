# AI Interactions Log

## Test Generation (SF7)

I used ChatGPT to help generate pytest cases for the refactored game logic in `logic_utils.py`. I reviewed the suggested tests, ran them with `pytest`, and used the results to find one remaining scoring bug.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Guess is higher than the secret | "Generate a pytest test for the high/low hint bug after moving `check_guess` into `logic_utils.py`." | `check_guess(60, 50)` should return `"Too High"` and `"📉 Go LOWER!"` | Yes | A guess of 60 is above the secret 50, so the game should tell the player to go lower. |
| Guess is lower than the secret | "Generate a pytest test for the high/low hint bug after moving `check_guess` into `logic_utils.py`." | `check_guess(40, 50)` should return `"Too Low"` and `"📈 Go HIGHER!"` | Yes | A guess of 40 is below the secret 50, so the correct hint is to go higher. |
| Wrong guess should not change score | "Generate a pytest case to verify the repaired scoring logic." | `update_score(0, "Too High", 1)` should return `0` | No at first, then Yes after the fix | The first run returned `-5`, which showed that part of the old scoring logic was still present. I changed `update_score()` so incorrect guesses leave the score unchanged, then reran pytest and verified the test passed. |
| Correct guess on first attempt | "Generate a test for the first-attempt scoring bug." | `update_score(0, "Win", 1)` should return `100` | Yes | The original game incorrectly gave 80 points on the first try. The repaired formula should award 100 points. |

---

## Agent Workflow (SF8)

Not attempted.

---

## Linting & Style (SF9)

Not attempted.

---

## Model Comparison (SF11)

Not attempted.