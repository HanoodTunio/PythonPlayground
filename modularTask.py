def function(number):
    square_root = [-1] * number

    for i in range(1, number):
        
        for s in range(number):
            if (s * s) % number == (i - 1) % number:
                square_root[i] = s
                break

    return square_root


number = int(input())
result = function(number)
print(" ".join(map(str, result)))

