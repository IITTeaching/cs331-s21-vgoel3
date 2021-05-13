import time
from unittest import TestCase   
import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    byte_lst = book_to_words(book_url)
    ### \/\/\/ USEFUL TO ME FOR UNDERSTANDING WHAT EXACTLY IS GOING ON WITH CHAR-VALS \/\/\/ 
    # 
    # byte_words = byte_lst[49:99]
    # ascii_vals = [[]]
    # for i in byte_words:
    #     for j in range(len(i)):
    #         ascii_vals[-1].append(i[j])
    #     ascii_vals.append([])
    # for i in range(len(byte_words)):
    #     print('{}, {}'.format(byte_words[i], ascii_vals[i]))
    # 
    ### /\/\/\ USEFUL TO ME FOR UNDERSTANDING WHAT EXACTLY IS GOING ON WITH CHAR-VALS /\/\/\ 
    
    # finding highest length of word in byte_lst to determine how far the sort must iterate
    # to ensure a complete sort
    

    max_len = 0
    for i in byte_lst:
        if max_len < len(i):
            max_len = len(i)

    # LSD ITERATION - RADIX SORT LOOP - INDEX ADJUSTMENTS PERFORMED FOR EACH BYTE-STRING WITHIN COUNT_SORT()
    for i in range(max_len):
        byte_lst = count_sort(byte_lst, i, max_len - 1)
    return byte_lst

def count_sort(arr, curr_i, max_idx):
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]
 
    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(128)]
  
    # Store count of each character
    # i is a word in arr, and arr is a list of byte-strings
    for i in arr:

        # max_len - curr_i is how to 'pad' the strings at the back so that alphabetical order takes precedence
        # over length of strings. Originally, length took precedence over alphabetical order in my algorithm, 
        # which wasn't correct as a result of padding at the front of the strings.
        if max_idx - curr_i < len(i):
            count[i[max_idx - curr_i]] += 1
        else:
            count[0] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(128):
        count[i] += count[i-1]
 
    # Build the output character array
    for i in range(len(arr) -1, -1, -1):
        if max_idx - curr_i < len(arr[i]):
            output[count[arr[i][max_idx - curr_i]] - 1] = arr[i]
            count[arr[i][max_idx - curr_i]] -= 1            
        else:
            output[count[0] - 1] = arr[i]
            count[0] -= 1            
    
    return output

def test_book(link='https://www.gutenberg.org/files/84/84-0.txt', title = 'FRANKENSTEIN'):
    tc = TestCase()
    print(80 * '#', 'BEGIN SORTING *{}*'.format(title), 80 * '#', sep='\n')
    print()
    copy_lst = book_to_words(link)

    ### lines of code which could be used to help compare the runtimes of PythonSort and RadixSort (noted with <<<<)
    # py_start = time.time() <<<<
    copy_lst = sorted(copy_lst)
    # py_end = time.time()   <<<<
    
    ### RadixSort runtime <<<<
    # start = time.time() <<<<
    r_sort_lst = radix_a_book(link)
    # end = time.time() <<<<

    ### random sampling of the sorted list - enables rough visual checking of a correct sort
    # print(r_sort_lst[:20], r_sort_lst[1000:1020], r_sort_lst[10000:10020], r_sort_lst[70000:70020], r_sort_lst[-20:], sep='\n\n')    
    
    # success report and statistics
    tc.assertEqual(r_sort_lst, copy_lst)
    # print('RadixSort runtime: {} seconds.'.format(end - start))
    # print('PythonSort runtime: {} seconds.'.format(py_end - py_start))
    print(80 * '#', 'END SORTING *{}*: CORRECTLY SORTED'.format(title), 80 * '#', '\n\n', sep='\n')

def main():
    
    test_book() # frankenstein
    test_book('https://www.gutenberg.org/files/2701/2701-0.txt', 'MOBY DICK') # moby dick
    test_book('https://www.gutenberg.org/files/345/345-0.txt', 'DRACULA') # dracula
    test_book('https://www.gutenberg.org/files/4300/4300-0.txt', 'ULYSSES') # ulysses 

    ### \/\/\/ SMALL TEST CASE OF RADIX-SORT VIA LOOPING OF COUNT_SORT() \/\/\/
    # test_list_1 = [b'Act', b'Bear', b'Cat', b'125', b'Dog', b'it', b'the']
    # for i in range(0, len('bear')):
    #     test_list_1 = count_sort(test_list_1, i, len('bear') - 1)
    #     print(test_list_1) 


main()