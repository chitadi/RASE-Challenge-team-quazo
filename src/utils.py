
import yaml

def safe_open_yaml(yaml_file, verbose=False):

    with open(yaml_file, 'r') as file:
        try:
            yaml_data = yaml.safe_load(file)
            if verbose:
                print("YAML content as dictionary:")
                print(yaml_data)
        except yaml.YAMLError as exc:
            print(exc)

    
    return yaml_data


def stringify(input_dict, delimiter):
    output_string = ""
    for key, value in input_dict.items():
        output_string += f"{delimiter}{key}={value}"
    return output_string
