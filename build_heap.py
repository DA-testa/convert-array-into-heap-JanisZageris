# python3

import os

def build_heap(data): # sift_down funkcija bet dod pareizos rezultātus
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        swaps += sift_down(data, i)

    return swaps

def sift_down(data, i): # build_heap funkcija bet at ačgārni
    swaps = []
    n = len(data)
    while 2*i+1 < n:
        j = 2*i+1
        if j+1 < n and data[j+1] < data[j]:
            j += 1
        if data[i] <= data[j]:
            break
        swaps.append((i, j))
        data[i], data[j] = data[j], data[i]
        i = j

    return swaps

def main():
    input_method = input()

    if 'I' in input_method:
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F' in input_method:
        file_name = input().strip()
        file_path = os.path.join("test", file_name)
        with open(file_path, 'r') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    else:
        print('Invalid input method')
        return

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
