# Problem-Solving
This repo contains problem solving practice. In this README file there will be notes about each algorithm beside the problems that will be solved in separate files.

## Recursion Problem Set

### 1. The Classic Staircase

*Problem:* You are standing at the bottom of a staircase with  steps. You want to reach the top. In a single move, you are only allowed to climb either *1 step* or *2 steps*.

* *Task:* Write a function count_ways(n) that returns the total number of distinct combinations of moves that lead to the top.
* *Constraint:* Consider what happens if  (you are already at the top).

---

### 2. The Abstract Sum Architect

*Problem:* You are given two "building blocks": the digit *1* and the digit *3*. Your goal is to construct a string of these digits (in any order) such that the sum of all digits in the string equals exactly .

* *Example:* If , the possible strings are:
* "1111" ()
* "13" ()
* "31" ()
* *Total ways:* 3


* *Task:* Write a function count_sum_strings(n) that returns the number of unique strings that satisfy the sum .
* *The Challenge:* Unlike the staircase problem, there is no "physical" top or bottom. You must figure out how choosing a digit "reduces" the remaining problem.

### 3. The 2D Dungeon Crawler

*Problem:* You are a character in a 2D grid-based game starting at the top-left corner . Your goal is to reach the treasure at the bottom-right corner .

* *Allowed Moves:* You can move exactly one unit *Right, one unit **Down, or one unit **Diagonally* (down and right simultaneously).
* *Task:* Create a function count_paths_2d(m, n) to calculate all possible paths to the treasure.

---

### 4. The 3D Space Architect

*Problem:* You are designing a path for a drone inside a 3D structural frame of size . The drone starts at  and must navigate to .

* *Allowed Moves:* The drone can move one unit at a time, but only in directions parallel to the axes: *Positive X, **Positive Y, or **Positive Z*.
* *Task:* Write a function count_paths_3d(x, y, z) to determine how many unique flight paths exist.

---

### 5. Advanced: The Restricted Path

*Problem:* You are back to the -step staircase (moving 1 or 2 steps), but with a "stamina" constraint and obstacles.

* *The Obstacles:* You are given a list of integers broken_steps. If a step number is in this list, you cannot land on it.
* *The Stamina Rule:* Taking a 2-step jump is exhausting. You are *not allowed* to take two 2-step jumps in a row.
* *Task:* Write a function count_advanced_ways(n, broken_steps).
* *Hint:* You may need to track more than just your current step number in your function arguments to keep track of your "history."

