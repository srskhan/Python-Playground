inp = input().split()

count = 0
for word in inp:
    if word == "ai" or word == "data" or word == "model" or word == "learn" or word == "train" or word == "neural":
        count+=1

if count>=2:
    print("AI Detected")
else:
    print("Not AI Related")