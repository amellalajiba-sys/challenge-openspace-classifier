# challenge-openspace-classifier
My first project with becode
## 🏢 Description

Your company moved to a new office at CEVI Ghent. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat.

![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)

## 📦 Repo structure

```
.
├── utils/
│   ├── openspace.py
│   ├── table.py
│   └── utils.py
├── main.py
├──.gitignore
├── notebook_guide.ipynb
└── README.md

## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

```
   python main.py
```

3. The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.csv" file in your root directory. 