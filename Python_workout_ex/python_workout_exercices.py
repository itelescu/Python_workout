'''Guessing number game'''

import random
def guessing_game():
    number = random.randint(0,101)
    count = 0
    while count < 100:
        guess = int(input('Guess the number chosen by computer: '))
        if guess > number:
            print('Too high')
        elif guess < number:
            print('Too low')
        else:
            print('Just right')
            break
        count+=1
    print('Time succeed, I\'m sorry ')

guessing_game()

'''Write the result of guessing game into a file''' 
import random
def guessing_game():
    number = random.randint(0,101)
    count = 0
    lst = []
    while count < 100:
        guess = int(input('Guess the number chosen by computer: '))
        lst.append(str(guess))
        if guess > number:
            print('Too high')
        elif guess < number:
            print('Too low')
        else:
            print('Just right')
            break
        count+=1
    joined_lst = ','.join(lst)
    return (f'Choosed number is {str(number)}\nUser guessed numbers are {joined_lst}')

def save_file():
    name = input('What is your name?: ')
    guessed_num = f'User name is {name}\n{guessing_game()}'
    
    with open('C:\\Users\\itelescu\\OneDrive - ENDAVA\\Documents\\Python Test\\Python Test\\computer.txt','w') as filed:
        comp_file = filed.write(guessed_num)
    # return name, guessed_num

save_file()

'''Calculate the average of *args in a list'''
def my_sum(*par):
    count = 0
    for i in par:
        count+=i
    return count/len(par)

print(my_sum(*[10, 20, 30, 40]))

'''Calculate the sum of *args'''
def my_sum(*args):
    count = 0
    for num in args:
        count+= num
    return count

print(my_sum(10, 20, 30, 40))

'''Write a function that takes a list of words (strings). It should return a tuple con-
taining three integers, representing the length of the shortest word, the length
of the longest word, and the average word length.'''

def lenght(par):
    from statistics import mean
    lst_lenght = []
    for i in par:
        lst_lenght.append(len(i))
    mi_ma_av = [min(lst_lenght), max(lst_lenght), mean(lst_lenght)]
    return tuple(mi_ma_av)

print(lenght(['The','version','of','takes','an','optional second argument']))

'''Write a function that takes a list of Python objects. Sum the objects that either
are integers or can be turned into integers, ignoring the others.'''

def count_integers(par):
    int_sum = []
    for i in par:
        if i is int:
            int_sum+= i
        elif i is not int:
            try:
                int_numb = int(i)
            except (TypeError, ValueError):
                continue
            else:
                int_sum.append(int_numb)
       
    return sum(int_sum)

print(count_integers(['because',1, 2,'+','3', 6,'which']))

'''Run timing'''

def run_time():
    from statistics import mean
    count= 0
    run_km = []
    while True:
        select_time = input('Enter 10 km run time: ')
        if select_time !='':
            run_km.append(float(select_time))
            count+=1
        else:
            break
    return print(f'Average of {mean(run_km)}, over {count}')

run_time()

'''Before and After integers will show the numbers before and after point'''

def floating_point(num1, int1, int2):
    splited_num = str(num1).split('.')
    empty_lst= []
    part1 = splited_num[0]
    part2 = splited_num[1]
    slice_part1 = str(part1)[-int1:]
    slice_part2 = str(part2)[:int2]
    empty_lst.append(slice_part1)
    empty_lst.append(slice_part2)
    return '.'.join(empty_lst)


print(floating_point(120043.209932,2,3))


'''Transfer string into decimal numbers and show the sum of them'''

def str_to_float(*param):
    from decimal import Decimal
    lst = []
    for num in param:
        lst.append(Decimal(num.strip(' "')))
    return sum(lst)

print(str_to_float("0.1","0.2"))

'''Output hexadecimal from int'''
def hexadec(num):
    hexas = (f'{num:#x}')
    return hex(hexas)

print(hexadec(10))

'''Above problem is not solved, solution is below !!!'''

def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

hex_output()

'''Write a program that asks the user for their name and then produces a “name
triangle”: the first letter of their name, then the first two letters, then the first
three, and so forth'''

def triangle_name(name):
    for i,k in enumerate(name):
        print(name[:int(i)+1])

triangle_name('Telescu')

''''Pig Latin'''

def pig_latin(par):
    x = 'aeiou'
    if par[0] in x:
        print(par[:]+'way')
    elif par[0] in x.capitalize():
        print(par[1:].capitalize()+'way')
    else:
        print(par[1:]+par[0]+'ay')

pig_latin('Aay')

'''Pig Latin sentence'''

def pig_sent(par):
    x = 'aeiou'
    final_lst = []
    for i in par.split():
        if i[0] in x:
            final_lst.append(i[:]+'way')
        else:
            final_lst.append(i[1:]+par[0]+'ay')
    return ' '.join(final_lst)


print(pig_sent('this is a test translation'))

'''List modification'''

def ubi_dubbi(par):
    lst = []
    x = 'aeiou'
    for i in par:
        if i in x:
            lst.append(f'ub{i}')
        else:
            lst.append(i)
    return ''.join(lst)

print(ubi_dubbi('program'))

'''Sorted string'''
def sorte(par):
    return ''.join(sorted(par))

print(sorte('gbc'))

def sorts(par):
    return ','.join(sorted(par.split()))

print(sorts('Tom Dick Harry'))

'''First-last'''

from operator import itemgetter

def firstlast(par):
    return list(itemgetter(0,-1)(par))

print(firstlast('abc'))

'''Personal zip function'''

def myzip(par1,par2):
    for i in range(len(par1)):
        print(par1[i],par2[i])

myzip([10, 20,30], 'abc')

'''Summing anything'''

def mysum(par1,par2):
    if type(par1)==type(par1):
        print(par1+par2)
    else:
        print('Sorry, but the items have different type')

mysum('abc', 'def')

'''Numeric sum'''
def sum_numeric(*par):
    total = 0
    for i in par:
        try:
            total+=int(i)
        except ValueError:
            continue
    return total

print(sum_numeric(10, 20, 'a', '30', 'bcd'))

'''Given a sequence of positive and negative numbers,
sort them by absolute value'''

def sort_num(par):
    final_lst = []
    for i in par:
        if i <0:
            final_lst.append(-i)
        else:
            final_lst.append(i)
    return sorted(final_lst)

print(sort_num([10,60, -20, -30, 40, 50]))


'''Given a list of strings, sort them according to how many vowels they contain. Unsolved problem'''

def vowels_sort(lst):
    ls = []
    for i in lst:
        count=0
        for k in i:
            if k in 'aeiou':
                count+=1
        ls.append(count)
    zipped = list(zip(ls,lst))
    return sorted(zipped,reverse=True)

string = ['according','else','vintage','oculele']

print(vowels_sort(string))

'''Given a list of lists, with each list containing zero or more numbers, sort by the
sum of each inner list’s numbers.'''

def lst_of_lst(lst):
    emptu_lst = []
    for i in lst:
        emptu_lst.append(sum(i))
    return sorted(emptu_lst)

t = [[1, 2], [3], [4, 5, 6]]

print(lst_of_lst(t))

'''Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
evaluates it using eval , and prints the result. After 'done' it should return last expresion'''

def eval_loop():

    empty = []
    
    while True:
        string = input('Select what needs to be evalueted: ')
        if string != 'done':
            empty.append(eval(string))
            print(empty[-1])
        else:
            print(empty[-1])
            break
        
eval_loop()
        
'''Write a function which removes all punctuation from the string, breaks the string into a list of words, and counts
the number of words in your text that contain the letter “e”.'''

x = '''One of the challenges of getting started with Python is that you might have to install
Python and related software on your computer. If you are familiar with your operating
system, and especially if you are comfortable with the command-line interface, you will
have no trouble installing Python. But for beginners, it can be painful to learn about sys-
tem administration and programming at the same time.
To avoid that problem, I recommend that you start out running Python in a browser. Later,
when you are comfortable with Python, Ill make suggestions for installing Python on your
computer.'''

def analyss(docs):
    lst_words = []
    punctuation_sign = ':;!,-.[]()'
    for i in docs:
        if i not in punctuation_sign:
            lst_words.append(i)
            continue
    joined = ''.join(lst_words)
    count =0
    for i in joined:
        if 'e'in i:
            count+=1
    print(f'Your text contains {len(docs)} words, of which {count} ({count*100/len(docs):0.2f}%) contain an ''e''')

analyss(x)
'''Return the revers pair.'''

def rev_lst(lst):
    emoty = []  
    for i in lst:
        emoty.append(i[::-1])
    return emoty

def final_lst(emoty, lst):
    lis = []
    for k in emoty:
        for i in lst:
            if k==i:
                pair = (k, i[::-1])
                lis.append(pair)
    return lis

lst = ['ioi','dima','ror']

print(final_lst(rev_lst(lst),lst))

'''Alphabetical listing of all the words, and the number of times each occurs'''

def alice():
    with open('word.txt') as alice:
        alice_file = alice.read()
    ordered = sorted(alice_file.split())
    dicts ={}
    print('Word'+' '*36 + 'Count')
    print('='*45)
    for i in ordered:    
        dicts[i] = dicts.get(i, 0) + 1
    for k,v in dicts.items():
        print(f'{k:20} {v:20}')
    
alice()

'''Find anamgram(words with the same letters but different meaning) words in a file and print them'''

def read_word():
    with open('word.txt') as word_file:
        opened_word = word_file.read()
    emp_dicts = {}
    emp_lst = []
    for i in opened_word.split():
        sorted_string = str(sorted(i))
        if sorted_string in emp_dicts:
            emp_dicts[sorted_string].append(i)
        else:
            emp_dicts[sorted_string] = [i]
        
    anagram = list(emp_dicts.values())
    for i in anagram:
        if len(i)>0:
            emp_lst.append(i)
    comp = [k for k in [set(i) for i in emp_lst]if len(k)>1]
    return comp

print(read_word())

'''Program that reads a file break each line into words, strip punctuation and convert in lowercase.
count total number of words and number of time each word was used. Print 20 mose frequently used words.'''

def single_word():
    import string
    with open('word.txt') as word_file:
        opened_word = word_file.read()
    strin = ''
    punctuation = string.punctuation
    
    for i in opened_word:
        if i in punctuation:
            continue
        else:
            strin+=i.lower()
    emp_dic = {}
    for i in strin.split():
        if i not in emp_dic:
            emp_dic[i] = 0
        emp_dic[i]+=1
    return emp_dic #len(emp_dic)
    
def count():
    sort_orders = sorted(single_word().items(), key=lambda x: x[1], reverse=True)
    lst = []
    for i in sort_orders:
        lst.append((i[0],i[1]))
    return lst[0:21]

print(single_word())
print(count())

'''Select random word from the text and show it's frequency'''
import random

def histogram(s):
    d = dict()
    for c in s.split():
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

x ='''One of the challenges of getting started with Python is that you might have to install
# Python and related software on your computer. If you are familiar with your operating
# system, and especially if you are comfortable with the command-line interface, you will
# have no trouble installing Python. But for beginners, it can be painful to learn about sys-
# tem administration and programming at the same time.
# To avoid that problem, I recommend that you start out running Python in a browser. Later,
# when you are comfortable with Python, Ill make suggestions for installing Python on your
# computer.'''

histogram(x)

def probability():
    count = 0
    for v in histogram(x).values():
        count+=v
    lst = []
    for k,i in histogram(x).items(): 
        lst.append((k,f'{(i*100)/count:2.3}'))
    u = random.choice(lst)
    print(f'you\'ve got \'{u[0]}\' with probability of {u[1]}')

'''Ask user to introduce username and password and verify it with minidatabase if they match and get the output'''

def password(choose):
    while True:
        # asks user for input username
        enter_user = input('Username: ')

        if enter_user not in choose:
            print('You are not in our database, sorry!')
        if enter_user in choose:
        # if username is in database then choose it as a key for dictionary
            password = choose[enter_user]
            # asks user to input password
            enter_pass = input(f'Hello {enter_user}, please select the password: ')
            if enter_pass == password:
                print(f'Congrats, You are succesfully logged in as {enter_user}')
            else:
                print('Sorry, but the password is wrong')
        return 
           
pass_wor = {'Ion': '122112aa', 'Dima': '079637816', 'Andrei': '011235813aa', 'Maria': '024326089'}

password(pass_wor)

'''Read through a text file on disk. Use a dict to track how many words of each
length are in the file—that is, how many three-letter words, four-letter words,
five-letter words, and so on. Display your results.'''

def word_num():
    import sys
    # checking if the name of the file was introduced in powershell
    if len(sys.argv)<2:
        print('Select the file please!')
    empt_dict = {}
    #check first argument which will be the path of the file
    path = sys.argv[1]
    with open(path,'r') as filed:
        read_file = filed.read()
        for i in read_file.split():
            if len(i) not in empt_dict:
                empt_dict[len(i)] = 1
            else:
                empt_dict[len(i)] += 1
    for k,v in empt_dict.items():
        print(f'There is {v} words with {k} letters')
            
word_num()

'I/O'

'''Write a program that reads a file and prints only those lines that contain the substring snake'''

def snake():
    with open('myfile.txt','r') as filer:
        snake_holder = filer.readlines()
        for i in snake_holder:
            if 'snake' in i:
                print(i)
snake()

'''Copy content of a file in another file and replace pattern string with replacement string in the second file'''

def repl_str(pat_str,repl_str,file_a,file_b):
    with open(file_a,'r') as input_file, open (file_b,'w') as output_file:
        lines = input_file.readlines()
        for i in lines:
            output_file.write(i)
    with open (file_b,'r') as output_file:
        rep = output_file.read().replace(pat_str,repl_str)
    with open (file_b,'w') as output_file:
        output_file.write(rep)

pattern = 'snake'
replacement = 'buffallo'
a = 'myfile.txt'
b = 'computer.txt'

repl_str(pattern, replacement,a,b)

'''Create a file called remove_newlines.py that will be able to read all the lines of a given file
into a list and remove trailing newlines.'''

def remove_newlines():
    import sys
#should be at list one argument beside current working file in order to process the rest of the code
    if len(sys.argv)<2:
        print('File was not selected, please choose one')
#assige the first command line argument (which will be a path to the file) to a variable
    file_name = sys.argv[1]
    rmv_string = []
    with open(file_name) as filed:
#readlines method will return a list of all the lines, that's what we need 
        lines = filed.readlines()
        for i in lines:
            rmv_string.append(i.strip('\n'))
    return rmv_string

'''Get the final line of a text file'''

import pathlib

def get_final_line(f):
    with open(f,'r') as filed:
        f_file = filed.readlines()
    return f_file[-1]

path = pathlib.Path.home()/'OneDrive - ENDAVA'/'Documents'/'Python Test'/'Python Test'/'word.txt'

print(get_final_line(path))

'''Read through a text file, line by line. Use a dict to keep track of how many times
each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation.'''

import pathlib

def vowel_count(f):
    
    dic = {}
    with open(f,'r') as filed:
        f_file = filed.read()

        for i in f_file.lower():
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

    return {f'{k}:{v}' for k,v in dic.items() if k in 'aeiou'}

path = pathlib.Path.home()/'OneDrive - ENDAVA'/'Documents'/'Python Test'/'Python Test'/'word.txt'

print(vowel_count(path))

'''Get the number of Characters, words, lines and unique words'''

import pathlib

def word_count(f_file):
    #Create a dictionary and initialize the key
    result = {'Characters':0,
            'Words':0,
            'Lines':0}
    uniq_words = set()
    with open(f_file) as filed:
        f = filed.read()

        for char in f:
            result['Characters'] +=1

        for char in f.split():
            result['Words'] += 1
            uniq_words.add(char.lower())

    with open(f_file) as f:
        f_line = f.readlines()

        for line in f_line:
            result['Lines'] += 1
    return f'1.Number of characters is:{result["Characters"]}\n2.Number of words is:{result["Words"]}\n\
3.Number of lines is :{result["Lines"]}\n4.Number of unique words is:{len(uniq_words)}'


path = pathlib.Path.home()/'OneDrive - ENDAVA'/'Documents'/'Python Test'/'Python Test'/'myfile.txt'

print(word_count(path))

# '''Ask the user to enter the name of a text file and then (on one line, separated by
# spaces) words whose frequencies should be counted in that file. Count how
# many times those words appear in a dict, using the user-entered words as the
# keys and the counts as the values. Unsolved problem '''

'''Create a dict in which the keys are the names of files on your system and the val-
ues are the sizes of those files. To calculate the size, you can use os.stat.'''

def file_size():

    import os
    from pathlib import Path

    path = r'C:\Users\itelescu\OneDrive - ENDAVA\Desktop\Python info'

    lst = []
    
    for (root,dirs, files) in os.walk(path): # walk through directories and specify root, dirname and filename
        for item in files:
            lst.append(os.path.join(root,item)) # merge the root and file name into one path 
            
    backslash = "\\"    # create variavle that will contatin backslash character for spliting the path
    for entry in lst:
        print (f'{(entry.split(backslash)[-1])} - {Path(entry).stat().st_size} bytes')

print(file_size())

'''Given a directory, read through each file and count the frequency of each let-
ter. (Force letters to be lowercase, and ignore nonletter characters.) Use a dict
to keep track of the letter frequencies. What are the five most common letters
across all of these files? Unsolved problem.'''

'''Write two functions. find_longest_word takes a filename as an
argument and returns the longest word found in the file. The second function, find-
_all_longest_words, takes a directory name and returns a dict in which the keys are
filenames and the values are the longest words from each file.'''

import os

def find_longest_word(f):
    
    with open(f) as filed:
        longest_word = ''
        fh = filed.read()

        stripped = fh.rstrip()
        
        for item in (".", ",", "!", "?",'"','(',')','_',';',':','[',']',):
            stripped = stripped.replace(item,'')

        for item in stripped.split():
            if len(item) > len(longest_word):
                longest_word = item # creating the word with highes number of letters
    return longest_word

def find_all_longest_word(path):
    
    lst = []

    for (root,dirs,files) in os.walk(path): 
        for item in files:
            lst.append(os.path.join(root,item)) # creating a list with filename path. Combining root and filesname

    backslash = "\\" # specify the separator for split

    for entry in lst:
        if (entry.split(backslash)[-1]).endswith('.txt'): # select only txt files for printing the largest word
            print(f'{entry.split(backslash)[-1]} - {find_longest_word(entry)}')


path =r'C:\Users\itelescu\OneDrive - ENDAVA\Documents\Python Test' # the sourch where we should search for txt files

print(find_all_longest_word(path))

'''The function takes two arguments: the names of the input file (to be read from) and 
the output file (which will be created). Invers the words in first file and write them down in second one '''

def reverse_line(f1,f2):

    with open(f1) as filed, open(f2,'w') as filed2: # open both files for reading and writing
        f_holder = filed.readlines()

        for line in f_holder:
            file_holder = filed2.write(line[::-1]) # revers the words

    return file_holder


path = r'myfile.txt' #file are created in current working firectory, so we will not specify full path
path2 = r'myfile2.txt'

'Functions'

'''XML generator format. Based on the arguments provided return the final format of XML.'''

def myxml(tag,tags='', **kargs):

    dic = ''.join(f'{key}="{value}"'for key,value in kargs.items())

    return f'<{tag}>{dic}>{tags}</{tag}>'


print(myxml('foo','bar',a=1,b=2,c=3))

'''Write a copyfile function that takes one mandatory argument—the name of
an input file—and any number of additional arguments: the names of files to
which the input should be copied. Calling copyfile('myfile.txt', 'copy1
.txt', 'copy2.txt', 'copy3.txt') will create three copies of myfile.txt:
one each in copy1.txt, copy2.txt, and copy3.txt.'''

def copyfile(myfile, *copied_files):
    with open(myfile,'r') as filed:
        read_file = filed.read()
    for item in copied_files:
        with open(item,'w') as copied:
            write_file = copied.write(read_file)

origin = r'C:\Users\itelescu\OneDrive - ENDAVA\Documents\Python Test\Python Test\myfile.txt'

file1 = r'C:\Users\itelescu\OneDrive - ENDAVA\Documents\Python Test\Test files folder\numbers.txt'
file2 = r'C:\Users\itelescu\OneDrive - ENDAVA\Documents\Python Test\Test files folder\numbers2.txt'

copyfile(origin, file1, file2)

'''Write a function that works like map function'''

def func(a):
    return a*2

def apply_to_each(function,string):
    lst = []
    for item in string:
        lst.append(function(item))
    return lst

print(apply_to_each(func,'hello'))

'''Generate a passowrd based on the characters and lenght required'''

def create_password(string):
    from random import choice

    def passowrd(num): 
        f_str =''

        for item in range(num): # Based on numbers selected we will generate the password length 

            f_str += choice(string) # Append each generated character to the final password
        
        return f'{f_str}' 
    return passowrd

generate_pass = create_password('abcdef') 

print(generate_pass(10)) # Calling a function with inner function



def join_numbers(num):
    return ','.join([str(item) for item in range(num)])

print(join_numbers(10))


def sum_of_hex(lst):
    return sum([int(item,16) for item in lst])

lst_hex =['0x9a', '0x14', '0x28', '0x14', '0xb']

str_numb = '10 abc 20 de44 30 55fg 40'

x =sum([int(number) for number in str_numb.split() if number.isdigit()])
