import os
import argparse
import yaml
import zipfile

parser = argparse.ArgumentParser(description='Save for submission')

parser.add_argument('-c', "--config", type=str, required=True, help='The config file for submission with contents to be saved in zip.')

args = parser.parse_args()

yaml_path = args.config
folder, _file = os.path.split(yaml_path)
output_zip = os.path.join(folder, "model_submission.zip")

with open(yaml_path, "r") as f:
    data = yaml.safe_load(f)

# Extract paths
best_model_path = data.get("best_model_path")
config_path = data.get("config")
source_folder_path = "/src/models/"
# Collect files/folders to zip
files_to_zip = [best_model_path, config_path, source_folder_path]
def arcname_from_abs(abs_path: str) -> str:
    """
    Produce an archive name that mirrors the absolute path but without the leading '/'.
    Example: '/src/a/b.txt' -> 'src/a/b.txt'
    """
    # Relativize against POSIX root so we keep the whole tree structure after '/'
    # On POSIX: relpath('/src/a', '/') -> 'src/a'
    # On Windows paths this would differ, but you’re using POSIX-like paths.
    rel = os.path.relpath(abs_path, start=os.path.sep)
    # Normalize backslashes just in case and strip leading separators
    return rel.lstrip("/\\")
    
with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for item in files_to_zip:
        if not os.path.exists(item):
            print(f"Warning: {item} not found, skipping.")
            continue

        if os.path.isdir(item):
            # Add folder recursively, preserving '/...' structure (minus the leading '/')
            for root, _, files in os.walk(item):
                for fn in files:
                    abs_path = os.path.join(root, fn)
                    zf.write(abs_path, arcname_from_abs(abs_path))
        else:
            # Single file
            zf.write(item, arcname_from_abs(os.path.abspath(item)))

print(f"Created {output_zip}")
  

# print(config)





