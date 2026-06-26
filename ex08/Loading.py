def ft_tqdm(lst: range) -> None:
    length = len(lst)
    j = 0
    for i in lst:
        max = 91
        percent = int((i + 1) / length * 100)
        j = int(percent / 100 * max)
        bar = "=" * j
        spaces = " " * (max - j)
        print(f"\r{percent}%[{bar}{spaces}] {i + 1}/{length}", end="")
        yield i
