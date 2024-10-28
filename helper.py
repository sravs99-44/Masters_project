import random

malt_dataset_path = "/Users/sravanimalla/Documents/GitHub/long_tail_kbc/GENRE/MALT/malt_eval.txt"

# Load the MALT dataset
with open(malt_dataset_path, 'r', encoding='utf-8') as f:
    malt_data = f.readlines()


subset_fraction = 0.001  # Use 10% of the dataset for testing
subset_size = int(subset_fraction * len(malt_data))  # Calculate the number of records

# Randomly select a subset of records
malt_subset = random.sample(malt_data, subset_size)

# Optionally write the subset to a new file for future reference
with open("/Users/sravanimalla/Documents/GitHub/long_tail_kbc/GENRE/MALT/malt_subset.txt", 'w', encoding='utf-8') as subset_file:
    subset_file.writelines(malt_subset)

print(f"Subset created with {len(malt_subset)} entries.")
