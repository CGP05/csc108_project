#Utilized Google Gemini for a small amount of help in structuring the functions
def load_data():
    data = []
    with open("insurance.csv", "r") as csv_file:
        csv_file.readline()
        for line in csv_file:
            if len(line) == 7 and "" not in line:
                data.append(line)
            for value in line.strip().split(","):
                print(value)

#all from string, convert: age to int, bmi to float, children to int, smoker to bool, region to str, and charges to float
