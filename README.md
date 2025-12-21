# Git Assignment - HeroVired

## Project Description
This repository contains the solution for the Git Assignment, including the CalculatorPlus app, Git LFS implementation, and Geometry Calculator.

## Steps Performed
Detailed steps are listed in the assignment submission.

# My Git Project - HeroVired

**Name:** Krish Makwana

**Project:** Calculator and Geometry Tools

This is my project for the Git assignment. I have made a calculator and a geometry tool. I used different branches and fixed bugs to show how Git works.

---

## 1. CalculatorPlus App

I built a simple calculator that can add, subtract, multiply, and divide.

**What I did:**

* **Branches:** I used a `dev` branch for my daily work and a `main` branch for the final version.
* **New Feature:** I added a way to find the square root of a number in a special branch called `feature/sqrt`.
* **Fixing a Bug:** I found out that the calculator crashed if someone tried to divide by zero. I went back to the `dev` branch, fixed the code to show an error instead of crashing, and then updated my other branches.
* **Review:** I asked a classmate to check my code before I merged it into the final version.

---

## 2. Handling Big Files (LFS)

I learned how to handle large files that are over 200MB.

* I used **Git LFS** (Large File Storage).
* This keeps the repository fast because big files are stored separately.
* I tracked `.bin` files to make sure they are handled correctly.

---

## 3. Geometry Calculator (Using Stash)

I made a tool to calculate the area of circles and rectangles.

**What I did:**

* I started working on the circle area, but I wasn't finished yet.
* I used `git stash` to "hide" my unfinished work so I could switch to the rectangle area task.
* Later, I "popped" the stash to bring my circle work back and finish it.
* This helped me work on two things at the same time without making a mess.

---

## How to use this

* Open `calculator.py` to see the math functions.
* Open `geometry.py` to see the area functions.
* You can run these in any Python environment.

---

"Note: I set up the .gitattributes file to track .bin files with LFS. Due to GitHub's web upload limits, I uploaded a smaller placeholder file to show the tracking is working."

---

