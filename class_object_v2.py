class Scenario:
    def __init__(self, scenario_input):  #create a constructor
        #generate the final value and assign the values in diff variables
        values = scnlist(scenario_input)

        self.DATASET_ID = values[0]
        self.AS_OF_DATE = values[1]
        self.SCENARIO = values[2]
        self.SCN_TAG = values[3]
        self.STRESS = values[4]
        self.START_INDEX = values[5]


def scnlist(scenario_input):
    values = scenario_input.split("~")
    #extend because it adds each item from the tuple to the list or 3 append statement are required to add it
    # values.append("B")
    # values.append(True)
    # values.append(1)
    values.extend(("B", True, 1))
    print(" The scn list after append value:",values)
    return values


def main():
    #input value
    inputvalue1_scnA = "DS109~31-DEC-25~QMMF_202512_IBL"
    #object creation and send the input value
    scnA = Scenario(inputvalue1_scnA)  # Create the object here

    print(
        f"DATASET_ID: {scnA.DATASET_ID}, "
        f"AS_OF_DATE: {scnA.AS_OF_DATE}, "
        f"SCENARIO: {scnA.SCENARIO}, "
        f"STRESS: {scnA.STRESS}, "
        f"START_INDEX: {scnA.START_INDEX}"
    )


if __name__ == "__main__":
    main()