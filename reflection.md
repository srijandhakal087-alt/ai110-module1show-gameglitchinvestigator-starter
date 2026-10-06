# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, it looked like a normal number guessing game, but several parts of the logic behaved incorrectly. The hints could be backwards, the game accepted guesses outside the allowed range, and the scoring system produced unexpected values such as negative scores. I also found that the New Game button did not fully reset the state after a loss. Another hidden problem was that the secret value was intentionally converted between an integer and a string on alternating attempts, which caused inconsistent comparisons.

### Bug Reproduction Log

| Input / Trigger | Expected Behavior | Actual Behavior | Console Output / Error |
|---|---|---|---|
| Secret `87`, guess `-1` | Reject the guess because it is outside 1–100 | Game accepted the guess, used an attempt, and displayed an incorrect hint | No uncaught console error |
| Guess below the secret on alternating attempts | Every guess below the secret should return `Go HIGHER!` | Some guesses returned `Go LOWER!` because the secret changed between `int` and `str` | A `TypeError` occurred internally and was caught by the fallback logic |
| Click **New Game** after losing | Reset the game and allow another round | Game remained in the lost state | No console error; `status` was not reset to `"playing"` |
| Correct answer on attempt 1 | Award 100 points | Game awarded 80 points | No console error; scoring formula had an off-by-one calculation |
| Wrong guesses | Score should behave consistently | Score could increase or decrease depending on the attempt number | No console error; scoring rules were inconsistent |

### Reproduction Evidence

```text
Example 1
Secret: 87
Input: -1
Expected: Reject the guess because it is outside 1-100.
Actual: Guess was accepted and the game displayed "Go LOWER!"
Observed score after losing: -35

Example 2
Input: correct secret on first attempt
Expected score: 100
Actual original score: 80

Example 3
Trigger: lose game, then click New Game
Expected: new playable round
Actual: game remained in the finished/lost state
```

---

## 2. How did you use AI as a teammate?

I used ChatGPT as my AI coding assistant to investigate bugs, explain their causes, refactor logic, and generate pytest tests. One correct suggestion was to reset `status`, attempts, score, history, and the secret when New Game was clicked; I verified this by losing a game, starting a new game, and successfully playing another round. One suggestion I did not accept as the complete fix was initially swapping only the `Go HIGHER` and `Go LOWER` messages. Further testing showed that the secret was also alternating between an integer and a string, so I changed the solution by removing the type conversion and simplifying `check_guess`. This was an example of keeping a human-in-the-loop instead of assuming the first AI-generated fix was complete.

---

## 3. Debugging and testing your fixes

I considered a bug fixed only after reproducing the original behavior and then repeating the same steps after the change. I used a pytest test set for `check_guess`, scoring, input parsing, and range validation, and I also manually tested the Streamlit application. One generated scoring test initially failed because `update_score()` still subtracted five points for a wrong guess, which showed that the scoring repair had not been completely applied. I corrected the function and reran pytest to verify the result. AI helped generate the tests, but I reviewed their expectations and used both automated and manual verification before accepting the fixes.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the Python script when a user interacts with a widget instead of keeping execution paused like a normal command-line program. `st.session_state` allows values such as the secret number, score, history, attempts, and game status to survive those reruns. I also learned that the interface can display stale values if state changes happen after a component was already rendered during that run. Calling `st.rerun()` after updating the game state allowed the attempts display and final results to immediately reflect the newest values.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is reproducing a bug first, recording the expected and actual behavior, and then creating a test that proves the repair works. Next time I work with AI on code, I would give it all related files earlier and ask it to identify the root cause before applying a quick fix. I would also review generated changes instead of assuming an AI response is correct, because a hallucination or incomplete suggestion can still look convincing. This project changed how I think about AI-generated code because I now see AI as a useful teammate whose work still requires human verification.