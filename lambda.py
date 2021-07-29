import gc

x = 10

add_one = lambda x: x**3

print(f"cube of number is {add_one(3)}")

full_name = lambda fir, sec: print(f"Full name is {fir} {sec}")

full_name("kiran", "krishnan")

import pandas as pd
dfj =pd.read_json(r"C:\Users\kiran\OneDrive\Desktop\haha.json")
print(dfj.info())

iterable_value = 'Geeks'
iterable_obj = iter(iterable_value)
collected = gc.collect()
while True:
    try:
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:

        # exception will happen when iteration will over
        break


print(collected)
print(gc.get_threshold())