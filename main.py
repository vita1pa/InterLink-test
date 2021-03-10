from datetime import datetime as dt

def convert_inp_type(el):
    idx, val = el
    if idx==0:
        return val
    elif idx==1:
        return dt.strptime(val, "%b %d %Y") # convert string: Jun 29 2020 -> datetime
    elif idx==2:
        return float(val)
    else:
        return None

# Step 1. Read input data from file
lst_inp = []
with open("acme_worksheet.csv", "r") as f:
    _ = f.readline()
    for line in f:
        lst_inp.append(tuple(map(convert_inp_type, enumerate(line.strip().split(",")))))

# Step 2. Form uniques commons dates and sort it
#  Form all present dates
dates = [el[1] for el in lst_inp]
#  Form unique present dates
dates = list(set(dates))
#  Sort unique present dates
dates = sorted(dates)

# Step 4. Form uniques sorted names workers
workers = [el[0] for el in lst_inp]
workers = list(set(workers))
workers = sorted(workers)

# Step 4. Form output empty dict for form result table
out_dict ={worker: {dt.strftime(dat,"%Y-%m-%d"):0 for dat in dates} for worker in workers} 

# Step 5. Fill output dict
for el in lst_inp:
    out_dict[el[0]][dt.strftime(el[1],"%Y-%m-%d")] = el[2]

# Step 6. Form result list
lst_result = []
lst_result.append(",".join(["Name / Date"] + list(out_dict[workers[0]].keys())))
for key, val in out_dict.items():
    lst_result.append(key + "," + ",".join(map(lambda el: f"{el:g}", val.values())))

# Step 7. Out result to file result.csv
with open("result.csv", "w") as f:
    f.write("\n".join(lst_result))

