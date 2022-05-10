infile = ''
women_preferrence = dict()
men_preferrence = dict()
matched_couples = list()
single_men = list()
m = int()
n = int()
match_check_result = list()

# Function to format and clean data
def format_preferrence(data_lst):
    # Clean the data
    blacklist = ['', ' ']
    for data in data_lst:
        if data in blacklist:
            index = data_lst.index(data)
            while data == data_lst[index]:
                data_lst.pop(index)

    key = data_lst[0]
    data_lst = data_lst[1:]

    return key,data_lst

# Function to match one man to a woman
def match(man):
	for woman in men_preferrence[man]:
		taken = [pair for pair in matched_couples if woman in pair]

		if not taken:
			matched_couples.append([man, woman])
			single_men.remove(man)
			break

		else:
			current_partner_rank = women_preferrence[woman].index(taken[0][0])
			potential_partner_rank = women_preferrence[woman].index(man)

			if potential_partner_rank < current_partner_rank:
				single_men.remove(man)
				single_men.append(taken[0][0])

				taken[0][0] = man
				break

# Function to create a stable match
def stable_match():
	while len(single_men) > 0:
		for man in single_men:
			match(man)

# Function to check if a given match is stable
def check_stability(canditate_matches, stable_matches):
    matching_pairs = 0
    max_loop = len(canditate_matches)-1
    match_stable = 1

    for i in range(max_loop):
        canditate_couple = canditate_matches[i]
        canditate_couple.sort()

        for couple in stable_matches:
            couple.sort()
            if (not couple==canditate_couple) and (couple[0] == canditate_couple[0]):
                return [matching_pairs, match_stable]
        
        matching_pairs += 1

    if(matching_pairs == max_loop):
        match_stable = 0

    return [matching_pairs, match_stable]
    
def save_output(result):
    outfile = infile.replace('Input', 'Output')
    f2 = open(outfile, 'w')

    for data in result:
        data = [str(item) for item in data]
        output = ' '.join(data)
        output += '\n'
        if f2.writable():
            f2.write(output)
        else:
            print('ERROR!! Unable to write to file.')
    print(f'SUCCESS!! Saved the result to {outfile}')

# Obtain data
infile = input('Enter file name: ')

try:
    f = open(infile, 'r')
except FileNotFoundError:
    print('ERROR!!! The file ile specified does not exist.')
    exit()

if not f.readable():
    print('EPRROR!! The file specified is unreadable.')

n = int(f.readline())
m = int(f.readline())

for i in range(n*2):
    tmp_lst = f.readline().replace('\n', '').split(' ')
    key, value = format_preferrence(tmp_lst)
    
    if i<n:
        women_preferrence[key] = value
    else:
        men_preferrence[key] = value

single_men = [man for man in men_preferrence]
stable_match()

j=0
tmp = list()
tmp_lst.clear()
for i in range(m):
    for j in range(n):
        tmp.append(f.readline().replace('\n', '').split(' '))

    tmp_lst = check_stability(tmp, matched_couples)
    num_of_pairs = tmp_lst[0]
    stability = tmp_lst[1]
    match_check_result.append([num_of_pairs, n*2, stability])

    tmp.clear()
    tmp_lst.clear()

f.close()

save_output(match_check_result)