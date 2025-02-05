## Questions:

1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>
2.  What is the difference between the continue and break statements in Python?
3. Can you explain the difference between for loop and while loop?
4. How would you implement a nested for loop system? Provide an example.

## Homeworks:

**1.** Return uncommon elements of lists. Order of elements does not matter.
```
input:
    list1 = [1, 1, 2]
    list2 = [2, 3, 4]
output: [1, 1, 3, 4]
```

```
input:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
output: [1, 2, 3, 4, 5, 6]
```

```
input:
    list1 = [1, 1, 2, 3, 4, 2]
    list2 = [1, 3, 4, 5]
output: [2, 2, 5]
```

**2.** Print the square of each number which is less than `n` on a separate line.

```
input: n = 5
output:
    1
    4
    9
    16
```

**3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

```
input: hello
output: hel_lo
```

```
input: assalom
output: ass_alom
```

```
input: abcabcdabcdeabcdefabcdefg
output: abc_abcd_abcdeab_cdef_abcdefg
```


**4. Number Guessing Game**
Create a simple number guessing game.
- The computer randomly selects a number between 1 and 100. 
- If the guess is high, print "Too high!". 
- If the guess is low, print "Too low!". 
- If they guess correctly, print "You guessed it right!" and exit the loop.
- The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
- If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.


> Hint: Use Python’s `random.randint()` to generate the number.

**5. Password Checker**
Task: Create a simple password checker.
- Ask the user to enter a password. 
- If the password is shorter than 8 characters, print "Password is too short." 
- If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
- If the password meets both criteria, print "Password is strong."

**6. Prime Numbers**
Task: Write a Python program that prints all prime numbers between 1 and 100.

> A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.

---

### Bonus Challenge
Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
- The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
- The player enters their choice.
- Display the winner and keep track of scores for the player and the computer.
- First to 5 points wins the match.
