#Utilized Google Gemini for a small amount of help in structuring the functions

def load_data(filename: str) -> list[list[str]]:
    """Loads the data from the csv file, checks that each row has 7 columns, and returns rows as a list of strings.
    Precondition: csvfile must point to a valid CSV file.
    """
    csvfile = "insurance.csv"
    data = []
    with open(csvfile, "r") as file_obj:
        file_obj.readline()
        for line in file_obj:
            parts = line.strip().split(",")
            if len(parts) == 7:
                data.append(parts)
        return data

def convert_data_types(data:str):
    """
    all from string, convert: age to int, bmi to float, children to int, smoker to bool, region to str, and charges to float
    """

def analyze_correlations(data: list[list[str]]):
   """
   Calculate the ordinary least squares regression beta 1 (slope) coefficient for "BMI" as the independent variable (x) and "charges" as the dependent variable (y).
   Formula: sum of each individual BMI observation minues the mean BMI times each individual charges observation minues the mean charges, divided by the squared sum of each individual BMI observation minus the mean BMI.
   """
   mean_x = ...
   mean_y = ...
   

