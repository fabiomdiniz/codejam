import sys

def parse_input(input_file_path):
    '''
    Receives path for input file and returns a list of dicts for each case containing a key for credit
    and a key for items
    '''
    with open(input_file_path) as input_file:
        lines = input_file.read().splitlines()
        num_cases = int(lines[0])
        cases = [{'credit': int(lines[1 + 3 * case_idx]),
                  'items': [int(item) for item in lines[3 + 3 * case_idx].split()]} for case_idx in range(num_cases)]
    return cases

def find_solution(case):
    ''' For a specific case with credit and items returns the sorted indexes for the items to be bought '''
    for idx_item, item in enumerate(case['items']):
        for idx_other_item, other_item in enumerate(case['items']):
            if idx_item == idx_other_item:
                continue
            if item + other_item == case['credit']:
                return sorted([idx_item + 1, idx_other_item + 1])

if __name__ == '__main__':
    with open(sys.argv[1].replace('.in', 'out'), 'w') as out_file:
        out_file.write('\n'.join('Case #{}: {} {}'.format(idx_case + 1, *find_solution(case))
                                 for idx_case, case in enumerate(parse_input(sys.argv[1]))))
