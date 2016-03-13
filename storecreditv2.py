import sys

with open(sys.argv[1].replace('.in', '.out'), 'w') as out_file:
    with open(sys.argv[1]) as input_file:
        for case_idx in range(int(next(input_file))):
            credit = int(next(input_file))
            num_items = next(input_file)
            items = [int(item) for item in next(input_file).split()]
            for item_idx, item in enumerate(items):
                if credit - item in items[item_idx + 1:]:
                    out_file.write('Case #{}: {} {}\n'.format(case_idx + 1, item_idx + 1, item_idx + 1 + items[item_idx + 1:].index(credit - item) + 1))
                    break
