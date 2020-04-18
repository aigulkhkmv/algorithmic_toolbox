from operator import itemgetter


def find(sorted_segments):
    dots = []
    i = 0
    n = len(sorted_segments)
    while i < n:
        r = sorted_segments[i][1]
        i += 1
        while i < n and sorted_segments[i][0] <= r:
            i += 1
        dots.append(r)
    return dots


def main():
    nums = input()
    segments = []
    for i in range(int(nums)):
        segments.append([int(j) for j in input().split()])
    sorted_segments = sorted(segments, key=itemgetter(1))
    return sorted_segments


if __name__ == "__main__":
    sorted_segments = main()
    dots = find(sorted_segments)
    print(len(dots))
    print(*dots)
