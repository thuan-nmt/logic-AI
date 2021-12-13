import os
import logic
import utils

INPUT_FOLDER = "input/"
OUTPUT_FOLDER = "output/"

for file_name in os.listdir(INPUT_FOLDER):
    alpha, KB = utils.read_input(os.path.join(INPUT_FOLDER, file_name))
    result = logic.pl_resolution(KB, alpha)
    utils.write_output(os.path.join(OUTPUT_FOLDER, file_name), result)