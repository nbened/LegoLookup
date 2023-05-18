from utilities import *

# define what build to retrive
build_name = "submarine"
list_out_parts = True

def retrieve_build(build_name,list_out_parts):

    """

    This function allows you to retrieve any build name in 'builds', and list out its parts, their prices, and links.

    :param build_name:
    :param list_out_parts:
    :return:
    """

    try:
        # load saved build path
        data_path = fr"C:\Users\nickb\PycharmProjects\LegoLookup\builds\{build_name}.pkl"
        build = load_pickle(data_path)[0]

        print(f"\nRetrieved build '{build.name}' with {len(build.parts)} part types, {build.total_parts} pieces for ${round(build.build_cost,2)}.\n")

        if list_out_parts:
            count = 1
            for part in list(build.parts):
                print(f"Part [{count}]: {part.qty} {part.color} brick of id {part.part_id} for ${part.total_cost/part.qty} each, ${part.total_cost} total.")
                print(f"Bricklink url: {part.url}")
                count += 1

    except FileNotFoundError:
        print(f"No existing pickle file with name {build_name} found.")

retrieve_build(build_name=build_name.title(),list_out_parts=list_out_parts)