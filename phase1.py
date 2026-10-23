# Utilized Google Gemini for a small amount of assisstance in structuring the functions

csvfile = "insurance.csv"


def load_data(csvfile: str) -> list[list[str]]:
    """Loads the data from the csv file, checks that each row has 7 columns, and returns rows as a list of strings.
    Precondition: csvfile must point to a valid CSV file.
    """
    raw_data = []
    with open(csvfile, "r") as file:
        file.readline()  # to skip header
        for line in file:
            row = line.strip().split(",")  # tokenizing
            if len(row) == 7: #ensuring that there is data for each column for each row
                raw_data.append(row)
    return data


def convert_data_types(data: str):
    """
    All from string, convert: age to int, bmi to float, children to int, smoker to bool, region to str, and charges to float
    """
    converted_data = []
    for row in data:
        age = int(row[0])
        sex = row[1]
        bmi = float(row[2])
        children = int(row[3])
        smoker = row[4].lower() == "yes"
        region = row[5]
        charges = float(row[6])
        return converted_data


def remove_outliers_and_illogical_data(converted_data: list[list[str]],
) -> list[list[str]]:
    """
    Even though the insurance.csv dataset does not have any illogical data (such as having negative children or a bmi of 0)
    """
    valid_data = []
    for row in converted_data:
        age = row[0]
        bmi = row[2]
        children = row[3]
        charges = row[6]

        if age > 0 and bmi > 0.0 and children >= 0 and charges > 0.0:
            valid_data.append(row)
    return valid_data


def total_charges(valid_data: list[list[str]]) -> float:
    """
    Calculate the total sum of all the charges recorded in the CSV file.
    """
    total = 0.0
    for row in data:
        charges = float(row[6])
        total += charges
    return round(total, 2)


def mean_number_of_children(data: list[list[str]]) -> float:
    """
    Calculate the mean number of children recorded in the CSV file.
    """
    total_children = 0
    for row in data:
        children = int(row[3])
        total_children += children
    mean_children = total_children / len(data)
    return mean_children


def analyze_correlation(data: list[list[str]]):
    """
    Calculate the OLS (ordinary least squares) regression beta 1 (slope) coefficient for "BMI" as the independent variable (x) and "charges" as the dependent variable (y).
    Formula: sum of each individual BMI observation minues the mean BMI times each individual charges observation minues the mean charges, divided by the squared sum of each individual BMI observation minus the mean BMI.
    """
    bmis = 0.0
    charges = 0.0

    mean_x = ...
    mean_y = ...  # reusing the


def main(data, total) -> None:
    print(f"The total amount of claim charges is ${total}")
    print(
        "The mean number of children is ... and the standard deviation for number of children is ..."
    )
    print("For every one unit increase in BMI, ")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    data = load_data(csvfile)
    total = total_charges(data)
    main(data, total)
