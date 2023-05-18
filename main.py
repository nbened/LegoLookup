from utilities import *
from models import *
import time

# --------------------------------------------------SETTINGS------------------------------------------------------------

# set program params
search_for_price = True
build_name = "Latest Build" # default name
delay = 5 # delay in s to avoid rate limiting

# ----------------------------------------------------------------------------------------------------------------------

# establish broad project params
start_time = time.time()
breakLoop = False
idx = 1
part_ids,colors,quantities = [],[],[]
if search_for_price:
    build_name = str(input("\nWhat's the name of the build?\n> ")).title()

# get piece information
while not breakLoop:
    print(f"\nPiece Entry #{idx}\n(SPACE+ENTER to quit)")
    part_id = input(f"Part ID: ")
    if part_id=="":
        print('\nBreaking loop')
        breakLoop=True
    else:
        # colors : white, tan, yellow, orange, red, green, blue, brown, light gray, dark gray, black

        try:
            color = str(input(f"Color: ")).lower()
            qty = int(input(f"Qty: "))

            if len(part_id) and len(color) and qty:
                part_ids.append(part_id)
                colors.append(color)
                quantities.append(qty)
            idx+= 1

        except ValueError:
            print("\nError in value types. Try again.")

# source parts for price calculation from piece
idx = 0
parts = []
build_cost = 0
for i in range(len(part_ids)):
    part = Part(part_id=part_ids[i],color=colors[i],qty=quantities[i])
    if search_for_price:
        part.price = part.get_part_price(part.part_id,part.color)
        time.sleep(delay)
        build_cost+=part.total_cost
    parts.append(part)
idx += 1

# create build object, store it
build = Build(build_name, parts,build_cost)
build.count_total_pieces()
data_path = fr"C:\Users\nickb\PycharmProjects\LegoLookup\builds\{build_name}.pkl"
dump_pickle(data_path,[build])

# give final message
run_time = time.time() - start_time
min_run = int(run_time // 60)
sec_run = round((run_time % 60), 2)
print(f"\nBuilt and archived {build.total_parts} parts in build {build.name} in {min_run} minutes and {sec_run} seconds.")