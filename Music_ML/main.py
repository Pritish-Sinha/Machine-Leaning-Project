# Library Imports
import sys

# File Imports
from model import modeller
from model import model_loader
from csv_import import reader_and_divider

func_to_be_run = input("Make model(0) or load and run model(1): ")

if func_to_be_run == '0':
    modeller()
elif func_to_be_run == '1':
    print("""
If music-recommender.joblib does not exist in current directory, program will crash
""")
    X, y = reader_and_divider()
    model_loader(X, y)
else:
    print("Imma head out...")
    sys.exit(1)
