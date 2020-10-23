import math

def classify_rug(pattern):
    
    isV = not False in [x[:len(x)//2] == x[math.ceil(len(x)/2):][::-1] for i, x in enumerate(pattern)]
    isH = pattern[:len(pattern)//2] == pattern[math.ceil(len(pattern)/2):]

    if isV and isH: return 'perfect'

    if isV: return 'vertically symmetric'
    
    if isH: return 'horizontally symmetric'

    return 'imperfect'


# print(classify_rug([
#   ["a", "b", "b", "a"],
#   ["b", "b", "b", "b"],
#   ["a", "b", "b", "a"]
# ]))

def isWordChain(arr):
    def validate(x, i):
        prev = arr[i]
        am = len(list(filter(lambda x: not x, [l in x for l in prev])))
        # +1 one
        if am == 0 and len(x) == (len(prev) + 1): return True
        #  -1 one
        if am == 1 and len(x) == (len(prev) - 1): return True
        #  Changed one
        if am == 1 and len(x) == len(prev): return True

        return False

    return not False in [validate(x, i) for i, x in enumerate(arr[1:])]


# print(isWordChain(["run", "runny", "bunny"]))

def smallest(n):
	iteration, a = 1, 1;
	while iteration <= n:
		i = 1
		while a % iteration != 0:
			if a * i % iteration == 0: 
				a *= i
			else:
				i += 1
		iteration += 1
	return a


# print(smallest(10));

def cycle_length(arr, item):
	sorted_list = sorted(arr)
	pos = arr.index(item)
	cycles = 0

	while arr[pos] != sorted_list[pos]:
		cycles += 1
		b = sorted_list.index(arr[pos])
		arr[pos], arr[b] = arr[b], arr[pos]

	return cycles
	
	
# print(cycle_length([1, 5, 4, 3, 2, 6], 4))