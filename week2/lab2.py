KB = 1024
MB = 1048576
GB = 1073741824

num_entries = int(input("Please enter the number of entries per second: "))
entry_size = int(input("Please enter the average number of bytes per entry: "))

kb_size = (num_entries * entry_size * 60) / KB
print()
print("Storage Estimates:")
print(f"Per minute: {kb_size}KB")