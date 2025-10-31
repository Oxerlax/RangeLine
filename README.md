# RangeLine – Golf Distance Tracker 🏌️‍♂️⛳

------

## Overview 📝

RangeLine is a Python project that tracks and analyzes golf club distances. Users can record distances for various clubs, update past data, and view summary statistics.  

  - Works on Windows, macOS, and Linux  
  - Tested with Python’s Pytest  
  - Automatically stores golf statistics in JSON format  

------

## Features ✨

  - Track distances for all standard golf clubs (driver, irons, wedges, putter, etc.)  
  - Automatically stores golf statistics in JSON (`JSON/golf_clubs_statistics.json`)  
  - Update and analyze historical performance    

------

## Prerequisites 🐍⚡

  Python 3.11 or newer (https://www.python.org/downloads/)  
  `matplotlib` library  

------

## Setup Instructions (Cross-Platform) ⚙️

------

### 1. Clone the repository

  git clone https://github.com/<YOUR_GITHUB_USERNAME>/RangeLine.git
  cd RangeLine

------

### 2. Create a virtual environment (Command Prompt only)

**Windows**

  python -m venv .venv
  .venv\Scripts\activate.bat

**macOS / Linux**

  python3 -m venv .venv
  source .venv/bin/activate

  You should now have a (.venv) next to your file path. 
  
  Example:
  (.venv) C: Users/Me/RangeLine>

------

### 3. Install dependencies

  pip install matplotlib

------

## Run the Main Program ▶️

  Make sure you are in the project root (the folder containing `Main/`, `Logic/`, `JSON/`, etc.)

  ---
  
  To check this, enter the correct command:

  **Windows**

  dir

  **macOS / Linux**

  ls

  ---

  Once you have verified you have the folders, simply run:

  python -m Main.rangeline

  Now you can simply follow the program's instructions! 🎉
  
  Note: Exiting out of the program at any point could result in unsaved data, so be sure to confirm all inputs before exiting!

------

## Run Unit Tests (optional) 🧪

  Install pytest if not already installed:

  pip install pytest

  Then run tests:

  pytest

  All tests should pass if the setup is correct.

------

## View the JSON golf statistics file 📂

  The program automatically stores golf club statistics in your storage in:

  C:Users/[YOUR USERNAME]/RangeLine/JSON/golf_clubs_statistics.json

  You can find this file in your File Explorer and view it with any app you prefer.

------

## Project Structure

  RangeLine/
  
  ├── Main/
  
  │ ├── __init__.py
  
  │ └── rangeline.py
  
  ├── Logic/
  
  │ ├── __init__.py
  
  │ └── update.py
  
  ├── JSON/
  
  │ ├── __init__.py
  
  │ └── golf_clubs_statistics.json # generated automatically if it doesn't exist when running the program
  
  ├── Tests/
  
  │ └── __init__.py
  
  │ └── test_rangeline.py
  
  ├── .venv/ # virtual environment
  
  └── README.md

------

## Contact 🤝

  If you would like to let me know of any improvements I can make, send me an email and I'll see what I can do!
  Email: [kob20800@gmail.com]

------
