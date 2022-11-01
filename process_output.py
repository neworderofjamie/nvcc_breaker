import re
from os import path

from csv import writer
from glob import glob
from datetime import timedelta

outputs_filenames = list(glob("synthetic_output/output*.txt"))

name_parser = re.compile(r"output_(\d+)_([A-Z_]+).txt")
with open("summary.csv", "w") as csv_file:
    csv_writer = writer(csv_file, delimiter=",")
    csv_writer.writerow(["Num arrays", "Check CUDA errors implementation", "Runner size [mbyte]", "Wall clock time [s]", "Resident set size [mbyte]"])
    for n in outputs_filenames:
        try:
            with open(n, "r") as f:
                runner_ls = f.readline()
                runner_mbytes = int(runner_ls.split(" ")[4]) / (1024 * 1024)
                
                # Loop through other lines
                wall_clock_sec = None
                resident_set_mbyte = None
                for l in f:
                    # Strip leading whitespace
                    l = l.lstrip()
                    
                    if l.startswith("Elapsed (wall clock) time (h:mm:ss or m:ss):"):
                        components = l[45:].split(":")
                        if len(components) == 3:
                            hours = int(components[0])
                            minutes = int(components[1])
                            seconds = float(components[2])
                        else:
                            hours = 0
                            minutes = int(components[0])
                            seconds = float(components[1])
                        wall_clock_sec = timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()
                    elif l.startswith("Maximum resident set size (kbytes):"):
                        resident_set_mbyte = int(l[36:]) / 1024
                name_fields = name_parser.match(path.basename(n))
                csv_writer.writerow([name_fields.group(1), name_fields.group(2), runner_mbytes, wall_clock_sec, resident_set_mbyte])
        except:
            print(f"Unable to parse {n}")
            
        
