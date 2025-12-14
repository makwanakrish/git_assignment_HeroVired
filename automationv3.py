import os
import subprocess
import shutil
import stat
import time

# Configuration
REPO_NAME = "git_assignment_HeroVired"
BRANCH_DEV = "dev"
BRANCH_MAIN = "main"

# --- HELPER FUNCTIONS ---

def run_cmd(command, cwd=None):
    """Runs a shell command and prints output."""
    try:
        print(f"Executing: {command}")
        subprocess.run(command, check=True, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")
        exit(1)

def write_file(filepath, content):
    """Creates or overwrites a file with content."""
    with open(filepath, "w") as f:
        f.write(content)
    print(f"Updated file: {filepath}")

def on_rm_error(func, path, exc_info):
    """Error handler for shutil.rmtree to fix Windows permission issues."""
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

# --- CODE CONTENT STRINGS ---

CALC_V1 = """import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    # TODO: Implement the following function to calculate the square root of a number.
    # def square_root(self, x):
    #    return math.sqrt(x)

if __name__ == "__main__":
    calculator = Calculator()
    num1 = 16
    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
    
    # TODO: Uncomment and test the square root feature.
    # num3 = 25
    # print(f"The square root of {num3} = {calculator.square_root(num3)}")
"""

CALC_BUGFIX = CALC_V1.replace(
    "return a / b", 
    'if b == 0:\n            raise ValueError("Cannot divide by zero.")\n        return a / b'
)

CALC_FINAL = CALC_BUGFIX.replace(
    "# def square_root(self, x):", "def square_root(self, x):"
).replace(
    "#    return math.sqrt(x)", "    return math.sqrt(x)"
).replace(
    "# TODO: Uncomment and test the square root feature.", "# Testing Square Root"
).replace(
    "# num3 = 25", "num3 = 25"
).replace(
    "# print", "print"
)

GEO_V1 = """import math

class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()
    
    # TODO: Implement the feature to calculate the area of a circle
    # radius = 5
    # print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius)}")

    # TODO: Implement the feature to calculate the area of a rectangle
    # length = 10
    # width = 6
    # print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")
"""

GEO_CIRCLE_DONE = GEO_V1.replace(
    "# radius = 5", "radius = 5"
).replace(
    "# print(f\"The area of the circle", "print(f\"The area of the circle"
)

GEO_RECT_DONE = GEO_V1.replace(
    "# length = 10", "length = 10"
).replace(
    "# width = 6", "width = 6"
).replace(
    "# print(f\"The area of the rectangle", "print(f\"The area of the rectangle"
)

README_CONTENT = """# Git Assignment - HeroVired

## Project Description
This repository contains the solution for the Git Assignment, including the CalculatorPlus app, Git LFS implementation, and Geometry Calculator.

## Steps Performed
Detailed steps are listed in the assignment submission.
"""

# --- EXECUTION ---

print("=== STARTING HEROVIRED GIT ASSIGNMENT AUTOMATION (V3) ===")

# 1. CLEANUP & INIT
if os.path.exists(REPO_NAME):
    print(f"WARNING: Folder '{REPO_NAME}' exists. Deleting it to start fresh...")
    shutil.rmtree(REPO_NAME, onerror=on_rm_error)
    time.sleep(1) 

os.makedirs(REPO_NAME)
cwd = os.path.abspath(REPO_NAME)
run_cmd("git init", cwd)

# FIX: Create a commit IMMEDIATELY to establish the main branch
write_file(os.path.join(cwd, "README.md"), README_CONTENT)
run_cmd("git add README.md", cwd)
run_cmd('git commit -m "Initial commit"', cwd)
run_cmd(f"git branch -M {BRANCH_MAIN}", cwd) # Force branch name to main

# 2. Q1: Calculator Setup
print("\n--- Q1: Setting up CalculatorPlus ---")
run_cmd(f"git checkout -b {BRANCH_DEV}", cwd)
write_file(os.path.join(cwd, "calculator.py"), CALC_V1)
run_cmd("git add calculator.py", cwd)
run_cmd('git commit -m "feat: Initial CalculatorPlus code"', cwd)

# Merge to main and Release V1
run_cmd(f"git checkout {BRANCH_MAIN}", cwd)
run_cmd(f"git merge {BRANCH_DEV}", cwd)
run_cmd('git tag -a v1.0 -m "Release version 1"', cwd)
run_cmd(f"git checkout {BRANCH_DEV}", cwd)

# Feature Branch and Bugfix Simulation
print("\n--- Q1: Feature Branch & Bugfix Simulation ---")
run_cmd("git checkout -b feature/sqrt", cwd)
# (Imagine we started working here... now switching back to dev for bugfix)
print(">>> SIMULATING CRITICAL BUG REPORT <<<")
run_cmd(f"git checkout {BRANCH_DEV}", cwd)
write_file(os.path.join(cwd, "calculator.py"), CALC_BUGFIX)
run_cmd("git add calculator.py", cwd)
run_cmd('git commit -m "fix: Divide by zero error"', cwd)

# Update feature branch
run_cmd("git checkout feature/sqrt", cwd)
run_cmd(f"git merge {BRANCH_DEV}", cwd) 

# Finish Feature
write_file(os.path.join(cwd, "calculator.py"), CALC_FINAL)
run_cmd("git add calculator.py", cwd)
run_cmd('git commit -m "feat: Implement square root function"', cwd)

# 3. Q2: Git LFS
print("\n--- Q2: Git LFS Large File ---")
run_cmd("git checkout -b lfs", cwd)
run_cmd("git lfs install", cwd)
run_cmd('git lfs track "*.bin"', cwd)
run_cmd("git add .gitattributes", cwd)

# Generate 200MB file
large_file_path = os.path.join(cwd, "large_data.bin")
print("Generating 200MB binary file... (this may take a second)")
with open(large_file_path, "wb") as f:
    f.seek(200 * 1024 * 1024 - 1)
    f.write(b"\0")

run_cmd("git add large_data.bin", cwd)
run_cmd('git commit -m "feat: Add large binary file via LFS"', cwd)

# 4. Q3: Geometry Calculator and Stashing
print("\n--- Q3: Geometry Calculator & Stashing ---")
run_cmd(f"git checkout {BRANCH_MAIN}", cwd)
run_cmd(f"git checkout {BRANCH_DEV}", cwd)
run_cmd("git checkout -b geometry-calculator", cwd)
write_file(os.path.join(cwd, "geometry.py"), GEO_V1)
run_cmd("git add geometry.py", cwd)
run_cmd('git commit -m "feat: Initial Geometry Calculator"', cwd)

# Circle Feature + Stash
run_cmd("git checkout -b feature/circle-area", cwd)
write_file(os.path.join(cwd, "geometry.py"), GEO_CIRCLE_DONE) 
run_cmd("git stash", cwd)
print(">>> Stashed Circle changes")

# Rectangle Feature + Stash
run_cmd("git checkout -b feature/rectangle-area", cwd)
write_file(os.path.join(cwd, "geometry.py"), GEO_RECT_DONE) 
run_cmd("git stash", cwd)
print(">>> Stashed Rectangle changes")

# Finish Circle
run_cmd("git checkout feature/circle-area", cwd)
run_cmd("git stash apply stash@{1}", cwd) 
run_cmd("git add geometry.py", cwd)
run_cmd('git commit -m "feat: Implement Circle Area"', cwd)

# Finish Rectangle
run_cmd("git checkout feature/rectangle-area", cwd)
run_cmd("git stash apply stash@{0}", cwd) 
run_cmd("git add geometry.py", cwd)
run_cmd('git commit -m "feat: Implement Rectangle Area"', cwd)

print("\n\n=======================================================")
print("   AUTOMATION COMPLETE - READY TO PUSH   ")
print("=======================================================")
print(f"Project created at: {cwd}")