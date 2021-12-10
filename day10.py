def get_data(filename):
    mapxy = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

lines = get_data("day10.txt")
scores = []

points = {")": 1, "]": 2, "}": 3, ">":4}
op = {"(": ")", "[": "]", "{": "}", "<": ">"}

for line in lines:
    stack = []
    for ch in line:
        if ch in "([{<":
            stack.append(ch)
        else:
            last = stack.pop()
            if (last == "(" and ch == ")") or (last == "{" and ch == "}") or (last == "[" and ch == "]") or (last == "<" and ch == ">"):
                continue
            else:
                score += points[ch]
                break
    else:
        if len(stack) != 0:
            score = 0
            stackr = reversed(stack)
            print(list(reversed(stack)))
            for ch in stackr:
                print("@@@@", points[op[ch]])
                score = score * 5 + points[op[ch]]
                print(score)
            scores.append(score)
            
            

print(scores)

print(sorted(scores)[round(len(scores)/2)])