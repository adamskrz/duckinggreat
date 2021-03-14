from collections import Counter


def ordered_unique(sequence):
    # Tracks elements and removes using list comprehension
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def solution(data, n):
    id_count = Counter(data)
    new_shifts = []

    for shift_id in ordered_unique(data):
        if(id_count[shift_id] <= n):
            new_shifts.append(shift_id)

    return new_shifts


print(solution([1, 2, 7, 2, 3, 3, 7, 3, 4, 5, 5], 2))
