def read_files(name): 
        if name == 'newsfr.txt' or name == 'newsafr.txt':
                code = 'koi8_r'
        else:
                code = 'cp1251'
        with open(name, 'r', encoding=code) as f:
                return f.read()

def count_word(original_text): 
	to_list = original_text.split(' ') 
	to_set = set() 
	for i in to_list:
                if len(i) > 6:
                        to_set.add(i) 
	word_value = {}  
	for i in to_set: 
		count = 0 
		for j in to_list: 
			if i == j: 
				count += 1 
			word_value[i] = count 
	return word_value  

def sort_top(word_value): 
	register = list() 
	l_dict = str(len(word_value)) 
	for i in word_value.items(): 
		l_word = str(i[1]) 
		register.append((len(l_dict)-len(l_word))*'0' + str(i[1]) + ' ' + i[0])  
	register.sort(reverse = True) 
	top_10_list = list() 
	top_10 = {} 
	count = 1 
	for j in register: 
		top_10[count] = j.split(' ') 
		top_10[count][0] = int(top_10[count][0]) 
		if count == 10: 
			break 
		count += 1 
	return top_10  
 
def main(): 
        while True: 
                name = input('Введите имя файла: newsfr.txt, newsit.txt, newsafr.txt, newscy.txt. Выход - exit: ') 
                if name == 'newsfr.txt' or name == 'newsit.txt' or name == 'newsafr.txt' or name == 'newscy.txt': 
                        print('Идет обработка файла ...') 
                        top_10 = sort_top(count_word(read_files(name))) 
                        for k in top_10.values(): 
                                print (k[0], ': ', k[1]) 
                elif name == 'exit': 
                        break 
                else: 
                        print('Некорректный ввод, повторите.') 

main()
