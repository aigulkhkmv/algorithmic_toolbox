def count(n):
    i = 1
    k = []
    while n > 0:
        n_test = n - i
        if n_test < 0:
            return [n+i-1]
        if n_test not in k and n_test != i:
            n -= i
            k.append(i)
            i += 1
        elif n_test == i:
            i+=1
        else:
            i += 1
    return k


def count_2(n):
    if n == 1:
        return [1]
    else:
        n_test = n
        k = []
        for i in range(1, n):
            if n_test > 2*i:
                k.append(i)
                n_test -= i
            else:
                k.append(n_test)
                return k
    return k


if __name__ == "__main__":
    n = int(input())
    answer = count_2(n)
    print(len(answer))
    print(*answer)
