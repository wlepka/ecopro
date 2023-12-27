import os

def update_class_index(label_path, old_index, new_index):
    with open(label_path, 'r') as file:
        lines = file.readlines()

    updated_lines = [line.replace(f"{old_index} ", f"{new_index} ") for line in lines]

    with open(label_path, 'w') as file:
        file.writelines(updated_lines)

def update_class_indices_in_directory(directory, old_index, new_index):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            label_path = os.path.join(directory, filename)
            update_class_index(label_path, old_index, new_index)

# Example usage:
directory_path = r"E:\dataset\new_plastic_dataset\valid\labels"
old_class_index = 0
new_class_index = 2

update_class_indices_in_directory(directory_path, old_class_index, new_class_index)
