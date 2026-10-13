import json
from pathlib import Path


class Scenario:
    FIELD_NAMES = (
        "DATASET_ID",
        "AS_OF_DATE",
        "SCENARIO",
        "SCN_TAG",
        "STRESS",
        "START_INDEX",
    )

    def __init__(self, customer_name, scenario_input, defaults):
        values = scenario_input.split("~")
        if len(values) != 3:
            raise ValueError(
                f"{customer_name}: scenario_input must contain "
                "DATASET_ID~AS_OF_DATE~SCENARIO"
            )

        values.extend(
            (
                defaults["SCN_TAG"],
                defaults["STRESS"],
                defaults["START_INDEX"],
            )
        )
        self.customer_name = customer_name

        for field_name, value in zip(self.FIELD_NAMES, values):
            setattr(self, field_name, value)


def load_scenarios(config_path):
    with config_path.open(encoding="utf-8") as config_file:
        config = json.load(config_file)

    defaults = config["defaults"]
    return {
        customer["name"]: Scenario(
            customer["name"], customer["scenario_input"], defaults
        )
        for customer in config["customers"]
    }


def main():
    config_path = Path(__file__).resolve().parent / "config" / "scenarios.json"
    customers = load_scenarios(config_path)

    for customer_name, scenario in customers.items():
        values = {
            field_name: getattr(scenario, field_name)
            for field_name in Scenario.FIELD_NAMES
        }
        print(f"{customer_name}: {values}")


if __name__ == "__main__":
    main()
