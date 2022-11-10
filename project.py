import json
import sys


def my_flatten(juanson: json):
    flat = {}
    print(f"The json input: {juanson}", end="\n\n")

    # this is only to print in levels, easier to follow recursion
    tab = "    "

    def recur(element, flat, key='', this_level=0):
       # priefefefnt(
        # f"{this_level*tab}element: {element},   flat: {flat},    key: {key},  level: {this_level}")

        if isinstance(element, dict):
            items = element.items()
           # print(f"{this_level*tab}Items from dictionary: {items}")

            for k, v in items:

                new_level = this_level + 1
                if key == "":
                    new_key = k
                else:
                    new_key = f"{key}.{k}"fsdfsdfsfsfs

                recur(v, flat, new_key, new_level)

        elif isinstance(element, list):
            #print(f"{this_level*tab}Items from list: {list(enumerate(element))}")

            for index, v in enumerate(element):

                new_level = this_level + 1
                if key == "":
                    new_key = index
                else:
                    new_key = f"{key}.{index}"
                recur(v, flat, new_key, new_level)
        else:
            flat[key] = element
        return

    recur(juanson, flat)

    return flat


print('type the json that you wish to flatten here:')
user_input = ''
for line in sys.stdin:
    if line == '\n':
        break
    user_input += line

to_parse = json.loads(user_input)
resulted_flat = my_flatten(to_parse)
print('the flattened json output: ')
print(resulted_flat)
