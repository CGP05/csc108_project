#Utilized Google Gemini for a small amount of help in structuring the functions

csvfile = "insurance.csv"

def load_data(csvfile: str) -> list[list[str]]:
    """Loads the data from the csv file, checks that each row has 7 columns, and returns rows as a list of strings.
    Precondition: csvfile must point to a valid CSV file.
    """
    data = []
    with open(csvfile, "r") as file:
        file.readline() #to skip header
        for line in file:
            for value in line.split(","): #tokenizing
                return data

def convert_data_types(data:str):
    """
    all from string, convert: age to int, bmi to float, children to int, smoker to bool, region to str, and charges to float
    """
    converted_data = []
    for row in data:
        age = int(row[0])
        sex = row[1]
        bmi = float(row[2])
        children = int(row[3])
        smoker = (row[4].lower() == "yes")
        region = row[5]
        charges = float(row[6])

        

def analyze_correlations(data: list[list[str]]):
   """
   Calculate the OLS (ordinary least squares) regression beta 1 (slope) coefficient for "BMI" as the independent variable (x) and "charges" as the dependent variable (y).
   Formula: sum of each individual BMI observation minues the mean BMI times each individual charges observation minues the mean charges, divided by the squared sum of each individual BMI observation minus the mean BMI.
   """
    bmis = ...
    charges = ...

   mean_x = ...
   mean_y = ...
   
def main(data) -> None:
    print(data)

if __name__ == "__main__":
    main()