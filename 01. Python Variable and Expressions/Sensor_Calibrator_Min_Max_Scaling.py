inp = input().split()

x = float(inp[0])
min_v = float(inp[1])
max_v = float(inp[2])

norm = (x-min_v)/(max_v-min_v)
print(f"{norm:.2f}")