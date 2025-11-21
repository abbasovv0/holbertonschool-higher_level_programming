#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a0 + b0, a1 + b1)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ((1, 2), (1, 2)),
        ((1, 2), (1, 2, 3)),
        ((1, 2, 3), (1, 2)),
        ((1, 2, 3), (1, 2, 3)),
        ((1,), (1, 2)),
        ((), (1, 2)),
        ((1, 2), (1,)),
        ((1, 2), ()),
        ((1,), (1,)),
        ((), ()),
    ]

    for t_a, t_b in test_cases:
        print(f"{t_a} + {t_b} = {add_tuple(t_a, t_b)}")

