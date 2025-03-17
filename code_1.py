import random


def merge_sort(n: int, a: list):
    if n == 1:
        return a
    mid = n // 2
    left = merge_sort(mid, a[:mid])
    right = merge_sort(n - mid, a[mid:])
    return merge(left, right)


def merge(left: list, right: list):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# left = merge_sort(a[:mid])
# right = merge_sort(a[mid:])


def maxVal(n: int, a: list):
    max = a[0]
    for i in range(1, n):
        if a[i] > max:
            max = a[i]
    return max


def maxVal2(a: list, init: int, end: int):
    if (end - init) <= 1:
        return max(a[init], a[end])
    else:
        m = init + (end - init) // 2
        v1 = maxVal2(a, init, m)
        v2 = maxVal2(a, m + 1, end)
        return max(v1, v2)


def main():
    n = list((random.randint(1, 10001)) for _ in range(1000))
    print(merge_sort(1000, n))
    print(maxVal(1000, n))
    print(maxVal2(n, 0, 999))


if __name__ == '__main__':
    main()
