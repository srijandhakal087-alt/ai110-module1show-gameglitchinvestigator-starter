# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, it looked like a normal number guessing game, but several parts of the logic behaved incorrectly. The hints were sometimes backwards, so a guess below the secret could tell me to go lower instead of higher. The game also accepted invalid guesses such as `-1`, the scoring system gave unexpected negative scores, and the New Game button did not properly restart the game. I also noticed that the attempts display could show outdated information after a guess.

### Bug Reproduction Log

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| `-1` when the secret was `87` | Reject the guess because it is outside the valid 1–100 range | The game accepted `-1`, used an attempt, and displayed an incorrect hint | No console error; incorrect game behavior |
| `24`, then `25` or `26` with a larger secret | All guesses below the secret should say "Go HIGHER!" | Some guesses said "Go HIGHER!" while later guesses incorrectly said "Go LOWER!" | A type mismatch caused the code to enter a `TypeError` fallback |
| Click **New Game** after losing | Reset the game and allow the player to play again | The game remained in the lost state and would not restart correctly | No console error; `status` was never reset to `"playing"` |
| Correct guess on the first attempt | Award 100 points | The game awarded only 80 points | No console error; scoring formula had an off-by-one calculation |
| Wrong guesses | Score should remain predictable | The score sometimes increased or decreased depending on the attempt | No console error; scoring logic changed points inconsistently |

---

## 2. How did you use AI as a teammate?

I used ChatGPT as my AI coding assistant to inspect the code, explain why the bugs were happening, suggest fixes, and help refactor the game logic into `logic_utils.py`. One correct suggestion was to reset `status`, attempts, score, history, and the secret when the New Game button is clicked; I verified this by losing a game, clicking New Game, and successfully starting another round. One suggestion I did not accept as the complete solution was the initial idea to only swap the "Go HIGHER" and "Go LOWER" messages. After more testing, I found that the program was also converting the secret between an integer and a string, so I changed the solution by removing that type conversion and simplifying `check_guess`. This showed why a human-in-the-loop is important because an AI suggestion can look correct at first but still miss the root cause.

---

## 3. Debugging and testing your fixes

I considered a bug fixed only after I could reproduce the original problem and then repeat the same steps without seeing the incorrect behavior. I also used a pytest test set to verify the refactored logic in `logic_utils.py`, including tests for guesses that were too high, too low, correct, and for first-attempt scoring. One test initially failed because `update_score()` still returned `-5` for a wrong guess when the test expected the score to stay unchanged, which helped me catch a remaining scoring bug. After correcting the function, I reran the tests and verified the repaired behavior in both pytest and the live Streamlit game. AI helped generate the tests, but I still used manual verification in the game instead of assuming the generated tests were automatically correct.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the Python script whenever the user interacts with the app instead of running the program once from top to bottom like a normal command-line program. `st.session_state` is how information such as the secret number, attempts, score, history, and game status survives between those reruns. One bug happened because the screen displayed the attempts count before the updated state had been rendered again, so the number looked outdated. I fixed that by saving the updated values in session state and calling `st.rerun()` so the interface would immediately show the current state.

---

## 5. Looking ahead: your developer habits
One habit I want to reuse is reproducing a bug first, writing down the expected and actual behavior, and then creating a test that verifies the repair. Next time I work with AI on a coding task, I would give it all related files earlier and ask it to identify the root cause before accepting a quick fix. I would also review every generated diff carefully because AI can produce a hallucination or a solution that appears reasonable while missing another connected issue. This project changed how I think about AI-generated code because I now see AI as a useful teammate, but not as automatic verification that code is correct.