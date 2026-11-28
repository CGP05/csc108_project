"""Analyze health insurance claims data"""

from typing import Any

CSV_FILE = "insurance.csv"


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
            if (
                len(row) == 7
            ):  # ensuring that there is data for each column for each row
                raw_data.append(row)
    return raw_data


def convert_data_types(raw_data: list[list[str]]) -> list[list[Any]]:
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
        smoker = row[4].lower() == "yes"  # True if smoker and False if not a smoker
        region = row[5]
        charges = float(row[6])
        converted_data.append([age, sex, bmi, children, smoker, region, charges])
    return converted_data


def remove_illogical_data(
    converted_data: list[list[Any]],
) -> list[list[Any]]:
    """
    Even though the insurance.csv dataset does not have any illogical data (such as having negative children or a bmi of zero)
    >>> remove_illogical_data([[-29, 'female', 0.0, -1, True, 'southwest', 1000.000]])
    []
    """
    valid_data = []
    for row in converted_data:
        age = row[0]
        bmi = row[2]
        children = row[3]
        charges = row[6]

        if (
            age > 0 and bmi > 0.0 and children >= 0 and charges > 0.0
        ):  # removing irrational data
            valid_data.append(row)
    return valid_data


def percent_high_claims(valid_data: list[list[Any]]) -> float:
    """
    Precondition: len(valid_data) != 0

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


def ols_slope_bmi_and_charges(valid_data: list[list[Any]]) -> float:
    """
    Precondition: len(valid_data) != 0

    Calculate the OLS (ordinary least squares) regression beta 1 (slope) coefficient for "BMI" as the independent variable (x) and "charges" as the dependent variable (y).
    Formula: sum of each individual BMI observation minus the mean BMI times each individual charges observation minues the mean charges, divided by the squared sum of each individual BMI observation minus the mean BMI.
    >>> ols_slope_bmi_and_charges([[30, 'female', 20.0, 1, False, 'southwest', 1000.0],[40, 'male', 30.0, 2, True, 'southeast', 3000.0]])
    200.0
    >>> ols_slope_bmi_and_charges([[30, 'female', 20.0, 1, False, 'southwest', 1000.0]])
    0.0
    >>> ols_slope_bmi_and_charges([[30, 'female', 20.0, 1, False, 'southwest', 1000.0], [40, 'male', 20.0, 2, True, 'southeast', 3000.0]])
    0.0
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


def average_charges_by_region(valid_data: list) -> dict[str, float]:
    """
    Calculate the mean charge for each of the 4 regions.

    >>> average_charges_by_region([[29, "female", 27.9, 0, True, "southwest", 1000.0], [28, 'male', 33.77, 1, False, 'southwest', 3000.0], [40, 'male', 30.0, 2, True, 'southeast', 2000.0]])
    {'southwest': 2000.0, 'southeast': 2000.0}
    """
    charges_by_region = {}

    for row in valid_data:
        region = row[5]
        charges = row[6]

        if region not in charges_by_region:
            charges_by_region[region] = [charges]
        else:
            charges_by_region[region].append(charges)

    mean_charges_by_region = {}

    for region, charges_list in charges_by_region.items():
        total = 0.0

        for charge in charges_list:
            total += charge

        mean = total / len(charges_list)
        mean_charges_by_region[region] = round(mean, 2)

    return mean_charges_by_region


def percent_smoker_by_region(valid_data: list) -> dict[str, float]:
    """
    Calculate the percentage of smokers for each region.

    >>> percent_smoker_by_region([[29, 'female', 27.9, 0, True, 'southwest', 1000.0], [28, 'male', 33.77, 1, False, 'southwest', 3000.0], [40, 'male', 30.0, 2, True, 'southeast', 2000.0]])
    {'southwest': 50.0, 'southeast': 100.0}
    """
    smokers_by_region = {}
    total_by_region = {}

    for row in valid_data:
        region = row[5]
        smoker = row[4]

        if region not in smokers_by_region:
            smokers_by_region[region] = 0
            total_by_region[region] = 0

        total_by_region[region] += 1

        if smoker:
            smokers_by_region[region] += 1

    percent_smoker_by_region = {}

    for region, smoker_count in smokers_by_region.items():
        total = total_by_region[region]
        percentage = (smoker_count / total) * 100
        percent_smoker_by_region[region] = round(percentage, 2)

    return percent_smoker_by_region


def highest_charge_region(
    mean_charges_by_region: dict,
    index: int,
    regions: list[str] | None = None,
) -> int:
    """
    Find the region with the highest mean claim charges and return its index.

    >>> highest_charge_region({'southwest': 2000.0, 'southeast': 3000.0, 'northwest': 1000.0}, 0)
    1
    """
    if regions is None:
        regions = list(mean_charges_by_region.keys())

    index_of_highest_region = index

    for region_index in range(index, len(regions)):
        if (
            mean_charges_by_region[regions[index_of_highest_region]]
            < mean_charges_by_region[regions[region_index]]
        ):
            index_of_highest_region = region_index

    return index_of_highest_region


def charges_ranked_by_region(mean_regional_charges: dict[str, float]) -> list[str]:
    """
    Use selection sort to rank the 4 regions from highest to lowest average charge.

    >>> charges_ranked_by_region({'southwest': 2000.0, 'southeast': 3000.0, 'northwest': 1000.0})
    ['southeast', 'southwest', 'northwest']
    >>> charges_ranked_by_region({'southwest': 2000.0, 'southeast': 3000.0, 'northwest': 2500.0})
    ['southeast', 'northwest', 'southwest']
    """
    regions = list(mean_regional_charges.keys())

    for region_index in range(len(regions) - 1):
        swap_index = highest_charge_region(
            mean_regional_charges, region_index, regions
        )
        regions[region_index], regions[swap_index] = (
            regions[swap_index],
            regions[region_index],
        )

    return regions


def main(slope: float, percentage: float, mean_charges_by_region: dict, percent_smoker_by_region: dict,) -> None:
    """Print the summary statistics for the insurance claims dataset.
    >>> main(393.87, 0.52,
    ...      {'southeast': 14735.41, 'southwest': 12346.94,
    ...       'northeast': 13406.38, 'northwest': 12417.58},
    ...      {'southeast': 25.0, 'southwest': 17.85,
    ...       'northeast': 20.68, 'northwest': 17.85})
    The percentage of claims greater than $50,000 is approximately 0.52%
    For every one unit increase in BMI, charges are expected to increase by $393.87.
    The average insurance claim charges and percent smokers by region are: $14735.41 mean claim charges, and 25.0% smokers for southeast, $12346.94 mean claim charges, and 17.85% smokers for southwest, $13406.38 mean claim charges, and 20.68% smokers for northeast, and $12417.58 mean claim charges, and 17.85% smokers for northwest.
    The three regions ranked from highest to lowest average charge are: southeast, northeast, northwest
    The index of the highest region is 0
    
    """
    index_of_highest_region = highest_charge_region(mean_charges_by_region, 0)
    ranked_regions = charges_ranked_by_region(mean_charges_by_region)
    print(f"The percentage of claims greater than $50,000 is approximately {percentage}%")
    print(f"For every one unit increase in BMI, charges are expected to increase by ${slope}.")
    print(
        f"The average insurance claim charges and percent smokers by region are: "
        f"${mean_charges_by_region['southeast']} mean claim charges, and "
        f"{percent_smoker_by_region['southeast']}% smokers for southeast, "
        f"${mean_charges_by_region['southwest']} mean claim charges, and "
        f"{percent_smoker_by_region['southwest']}% smokers for southwest, "
        f"${mean_charges_by_region['northeast']} mean claim charges, and "
        f"{percent_smoker_by_region['northeast']}% smokers for northeast, and "
        f"${mean_charges_by_region['northwest']} mean claim charges, and "
        f"{percent_smoker_by_region['northwest']}% smokers for northwest."
    )
    print(
        "The three regions ranked from highest to lowest average charge are: "
        + ", ".join(ranked_regions[:3])
    )
    print(f"The index of the highest region is {index_of_highest_region}")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    raw_data = load_data(CSV_FILE)
    cleaned_data = convert_data_types(raw_data)
    valid_data = remove_illogical_data(cleaned_data)

    slope_val = ols_slope_bmi_and_charges(valid_data)
    percentage_val = percent_high_claims(valid_data)

    mean_charges_by_region = average_charges_by_region(valid_data)
    percent_smoker_region = percent_smoker_by_region(valid_data)

    main(slope_val, percentage_val, mean_charges_by_region, percent_smoker_region)
