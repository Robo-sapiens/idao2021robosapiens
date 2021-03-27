import re

def parse_class_from_filename(filename):
    match = re.search(r'(E|N)+R_\d+', filename)
    return match[0]

def parse_angle_from_filename(filename):
    match = re.search(r'-*[\d.]+', filename)
    return match[0]
