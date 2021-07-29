import gc
import tracemalloc
i = 0

# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
	x = { }
	x[i+1] = x
	print(x)

print(f"Garbage collector threshold: {gc.get_threshold()}")
# lists are cleared whenever a full collection or
# collection of the highest generation (2) is run
collected = gc.collect() # or gc.collect(2)
print(f"Garbage collector: collected {collected} objects.")

print("Creating cycles...")
for i in range(10):
	create_cycle()

print(f"Garbage collector threshold: {gc.get_threshold()}")
collected = gc.collect()

print(f"Garbage collector: collected {collected} objects.")


