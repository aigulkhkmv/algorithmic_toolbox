def fib(n):
    fib_nums = [0, 1]
    if n == 0:
        return fib_nums[0]
    elif n == 1:
        return fib_nums[1]
    else:
        for i in range(2, n + 1):
            fib_nums.append(fib_nums[-1] + fib_nums[-2])
        return fib_nums[-1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
