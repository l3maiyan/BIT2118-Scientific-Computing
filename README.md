# BIT 2118 – Scientific Computing

**Individual GitHub repository submission**

This repository contains Python implementations for the scientific-computing topics listed in the supplied BIT 2118 group-work brief. The group discussion may be shared, but each student must maintain and submit an individual repository.

## Repository structure

```text
BIT2118_Scientific_Computing_Submission/
├── README.md
├── requirements.txt
├── .gitignore
├── code/
│   ├── Task_02_numpy_arrays.py
│   ├── Task_03_vectorization.py
│   ├── ...
│   └── Task_20_monte_carlo.py
└── docs/
    └── Scientific_Computing_Documentation.md
```

## Requirements

- Python 3.9 or later
- NumPy
- SciPy
- Matplotlib

Install the libraries using:

```bash
python -m pip install -r requirements.txt
```

## Running a task

Open a terminal in the repository folder and run, for example:

```bash
python code/Task_02_numpy_arrays.py
```

Run the other scripts in the same way. Scripts that produce graphs open a Matplotlib window. Close the graph window to allow the script to finish.

## What each task contains

Each script presents:
1. The original scientific-computing example.
2. A changed input or parameter and its effect.
3. A different but related real-world application.

The accompanying documentation explains the mathematical concept, inputs, operations, output meaning, parameter changes, assumptions and related application.

## Before submitting

1. Replace the student details in the documentation cover section with your own details.
2. Run every Python script on your computer and check that it works.
3. Read the documentation and make sure you can explain the code and results.
4. Create your own GitHub repository named `BIT2118-Scientific-Computing` (or another suitable name).
5. Upload the contents of this folder to your own repository.
6. Copy your repository URL and submit it together with the documentation through VLMS.

**Important:** Do not submit a group member's repository as your own. Do not claim that a script has been tested on your computer until you have run it yourself.
