csvfile = "insurance.csv"

def load_data(csvfile: str) -> list[list[str]]:
    """Loads the data from the csv file, checks that each row has 7 columns, and returns rows as a list of strings.
    Precondition: csvfile must point to a valid CSV file.
    >>> data = load_data("insurance.csv")
    >>> data[0]
    ['29', 'female', '27.9', '0', 'yes', 'southwest', '16884.924']
    """
    raw_data = []
    with open(csvfile, "r") as file:
        file.readline()  # to skip header
        for line in file:
            row = line.strip().split(",")  # tokenizing
            if len(row) == 7: #ensuring that there is data for each column for each row
                raw_data.append(row)
    return raw_data


def convert_data_types(raw_data: list[list[str]]) -> list[list[str]]:
    """
    All from string, convert: age to int, bmi to float, children to int, smoker to bool, region to str, and charges to float
    >>> convert_data_types([['29', 'female', '27.9', '0', 'yes', 'southwest', '16884.924']])
    [[29, 'female', 27.9, 0, True, 'southwest', 16884.924]]
    """
    converted_data = []
    for row in raw_data:
        age = int(row[0])
        sex = row[1]
        bmi = float(row[2])
        children = int(row[3])
        smoker = row[4].lower() == "yes" #True if smoker and False if not a smoker
        region = row[5]
        charges = float(row[6])
        converted_data.append([age, sex, bmi, children, smoker, region, charges])
    return converted_data


def remove_outliers_and_illogical_data(converted_data: list[list[str]]) -> list[list[str]]:
    """
    Even though the insurance.csv dataset does not have any illogical data (such as having negative children or a bmi of zero)
    >>> remove_outliers_and_illogical_data([[-29, 'female', 0.0, -1, True, 'southwest', 1000.000]])
    []
    """
    valid_data = []
    for row in converted_data:
        age = row[0]
        bmi = row[2]
        children = row[3]
        charges = row[6]

        if age > 0 and bmi > 0.0 and children >= 0 and charges > 0.0: #removing irrational data
            valid_data.append(row)
    return valid_data


def total_charges(valid_data: list[list[str]]) -> float:
    """
    Calculate the total sum of all the charges recorded in the CSV file.
    >>> total_charges([[29, 'female', 27.9, 0, True, 'southwest', 16884.924], [28, 'male', 33.77, 1, False, 'southeast', 1725.5523]])
    18610.48
    """
    total = 0.0
    for row in valid_data:
        charges = float(row[6])
        total += charges
    return round(total, 2)


def percent_high_claims(valid_data: list) -> float:
    """
    Calculate the percentage of claims that exceed $50,000.
    >>> percent_high_claims([[29, 'female', 27.9, 0, True, 'southwest', 16884.924], [28, 'male', 33.77, 1, False, 'southeast', 99999.999]])
    50.0
    """
    high_count = 0
    for row in valid_data:
        charges = row[6]
        if charges > 50000.0000:
            high_count += 1
            
    percentage = (high_count / len(valid_data)) * 100
    return round(percentage, 2)


def mean_number_of_children(valid_data: list[list[str]]) -> float:
    """
    Calculate the mean number of children recorded in the CSV file.
    >>> mean_number_of_children([[29, 'female', 27.9, 0, True, 'southwest', 16884.924], [28, 'male', 33.77, 1, False, 'southeast', 99999.999]])
    0.5
    """
    total_children = 0
    for row in valid_data:
        children = int(row[3])
        total_children += children
    mean_children = total_children / len(valid_data)
    return mean_children


def ols_slope_bmi_and_charges(valid_data: list[list[str]]):
    """
    Calculate the OLS (ordinary least squares) regression beta 1 (slope) coefficient for "BMI" as the independent variable (x) and "charges" as the dependent variable (y).
    Formula: sum of each individual BMI observation minus the mean BMI times each individual charges observation minues the mean charges, divided by the squared sum of each individual BMI observation minus the mean BMI.
    >>> ols_slope_bmi_and_charges([[30, 'female', 20.0, 1, False, 'southwest', 1000.0],[40, 'male', 30.0, 2, True, 'southeast', 3000.0]])
    200.0
    """
    n = len(valid_data)

    total_x = 0.0
    total_y = 0.0
    for row in valid_data:
        total_x += row[2]
        total_y += row[6]

    mean_x = total_x / n
    mean_y = total_y / n

    numerator = 0.0
    denominator = 0.0
    for row in valid_data:
        bmi = row[2]
        charges = row[6]
        numerator += (bmi - mean_x) * (charges - mean_y)
        denominator += (bmi - mean_x) ** 2

    slope = numerator / denominator if denominator != 0 else 0.0
    return round(slope, 2)


def main(total, mean_children, slope, percentage) -> None:
    print(f"The total amount of claim charges is ${total}")
    print(f"The percentage of claims greater than $50,000 is {percentage}%")
    print(f"The mean number of children is {mean_children}.")
    print(f"For every one unit increase in BMI, charges are expected to increase by ${slope}.")

if __name__ == "__main__":    
    raw_data = load_data(csvfile)
    cleaned_data = convert_data_types(raw_data)
    valid_data = remove_outliers_and_illogical_data(cleaned_data)
    
    total = total_charges(valid_data)
    mean_children = mean_number_of_children(valid_data)
    slope = ols_slope_bmi_and_charges(valid_data)
    percentage = percent_high_claims(valid_data)

    main(total, mean_children, slope, percentage)