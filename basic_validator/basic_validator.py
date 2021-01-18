import jsonschema
import json
import sys


def run(path_to_schema, path_to_json_file):
    """
    Very basic example of how to validate a FunPDBe/PDBe-KB JSON file against the data exchange schema
    :param path_to_schema: String; the path to the data schema
    :param path_to_json_file: String; the path to a single JSON file that needs to be validated
    :return: Boolean; True if the JSON file is valid, False if invalid
    """

    with open(path_to_schema) as schema_file:
        funpdbe_schema = json.load(schema_file)

    with open(path_to_json_file) as funpdbe_json_file:
        funpdbe_annotations = json.load(funpdbe_json_file)

    try:
        if not (jsonschema.validate(funpdbe_annotations, funpdbe_schema)):
            print("\nJSON validated - has all the required fields and with the expected data types")
            return True
    except jsonschema.ValidationError as valerr:
        print(valerr)
        return False


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
