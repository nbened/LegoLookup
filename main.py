from utilities import *
from models import *
import time

# --------------------------------------------------SETTINGS------------------------------------------------------------

# set program variables
search_for_price = True
verbose = True

# ----------------------------------------------------------------------------------------------------------------------

# set defaults
delay = 45 # requests pause in seconds to skirt rate limiting. higher number for higher requests

# establish broad project params
start_time = time.time()
breakLoop = False
idx = 1
parts,part_ids,colors,quantities = [],[],[],[]
build_name = str(input("\nWhat's the name of the build?\n> ")).title()

# load parts from temp if interrupted last time
parts_path = fr"temp\{build_name}.pkl"

# get piece information
while not breakLoop:
    print(f"\nPiece Entry #{idx}\n(ENTER to quit, 'load' to load cached parts in 'temp' folder)")
    part_id = input(f"Part ID: ")
    if part_id=="":
        print('\nBreaking loop')
        breakLoop=True
    elif part_id == "load":
        print("\nLoading parts file...",end="")
        load_parts_from_temp = True
        try:
            parts = load_pickle(parts_path)

            print("DONE")
            for i in range(len(parts)):
                print(f"[{i}] {parts[i].qty}x {parts[i].color} {parts[i].part_id}")
            if len(parts):
                print(f"{len(parts)} parts loaded. Most recent part was {parts[len(parts)-1].qty} {parts[len(parts)-1].color} {parts[len(parts)-1].part_id} parts.")
        except FileNotFoundError:
            print("\nNo existing temp file found. Moving to dump entries\n")
            load_parts_from_temp = False

    else:
        # colors : white, tan, yellow, orange, red, green, blue, brown, light gray, dark gray, black

        try:
            qty = int(input(f"Qty: "))
            color = str(input(f"Color: ")).lower()

            if len(part_id) and len(color) and qty:
                part_ids.append(part_id)
                colors.append(color)
                quantities.append(qty)
            idx+= 1

        except ValueError:
            print("\nError in value types. Try again.")


# save parts into object
for i in range(len(part_ids)):
    part = Part(part_id=part_ids[i], color=colors[i], qty=quantities[i])
    parts.append(part)

# save parts in case rate limited
dump_pickle(parts_path,parts)
print(f"Parts entered:\n{[part.part_id for part in parts]}")


# source parts for price calculation from piece
if len(parts):
    idx = 0
    build_cost = 0
    for part in parts:
        if part.price == None:
            del parts[idx]
        else:
            if search_for_price and part.price==0:
                part.price = part.get_part_price(part.part_id,part.color)
                # store any modified parts found
                dump_pickle(parts_path, parts)
                print("Updated parts in pickle file.")
                build_cost+=part.total_cost
                print(f"[{idx}]: Sleeping {delay} seconds to evade rate limiting...\n")
                time.sleep(delay)
            elif part.price>0:
                print(f"[{idx}]: Part {part.qty}x {part.color} {part.part_id} already scraped price.\n")


            parts.append(part)
            idx += 1



    # create build object, store it
    build = Build(build_name, parts,build_cost)
    build.count_total_pieces()
    data_path = fr"builds\{build_name}.pkl"
    dump_pickle(data_path,[build])

    # give final message
    run_time = time.time() - start_time
    min_run = int(run_time // 60)
    sec_run = round((run_time % 60), 2)
    print(f"\nBuilt and archived {build.total_parts} parts in build {build.name} in {min_run} minutes and {sec_run} seconds.")
else:
    print("\nNo parts passed to build section. Finishing.")