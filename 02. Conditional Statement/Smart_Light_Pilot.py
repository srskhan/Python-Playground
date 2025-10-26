inp = input().split()
brightness = float(inp[0])
threshold = float(inp[1])

if brightness>= threshold:
    print("ON")
else:
    print("OFF")