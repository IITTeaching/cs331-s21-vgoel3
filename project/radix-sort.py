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
    
    # max-idx is a negative value. I will iterate strings from back to front using negative 
    # indexes starting from -1 in a process analogous to traversing over ints from their 
    # units place to their thousands place (LSD)
    max_len *= -1

    # LSD ITERATION - RADIX SORT LOOP
    for i in range(-1, max_len -1, -1):
        byte_lst = count_sort(byte_lst, i)
    return byte_lst

def count_sort(arr, idx):
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]
 
    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(128)]
 
    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]
 
    # Store count of each character
    # i is a word in arr, which is a list of byte-string words
    for i in arr:
        if -idx <= len(i):
            count[i[idx]] += 1
        else:
            count[0] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(128):
        count[i] += count[i-1]
 
    # Build the output character array
    for i in range(len(arr) -1, -1, -1):
        if -idx <= len(arr[i]):
            output[count[arr[i][idx]] - 1] = arr[i]
            count[arr[i][idx]] -= 1            
        else:
            output[count[0] - 1] = arr[i]
            count[0] -= 1            
    
    # Copy the output array to arr, so that arr now
    # contains sorted characters

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

def test_book(link='https://www.gutenberg.org/files/84/84-0.txt'):
    r_sort_lst = radix_a_book(link)
    print(r_sort_lst[:20], r_sort_lst[1000:1020], r_sort_lst[10000:10020], r_sort_lst[70000:70020], r_sort_lst[-20:], sep='\n')    

def main():
    
    test_book() # frankenstein
    test_book('https://www.gutenberg.org/files/2701/2701-0.txt') # moby dick
    test_book('https://www.gutenberg.org/files/4300/4300-0.txt') # ulysses (last words are pretty funny)
    test_book('https://www.gutenberg.org/files/345/345-0.txt') # dracula

    ## \/\/\/ SMALL TEST CASE OF RADIX-SORT VIA LOOPING OF COUNT_SORT() \/\/\/
    
    test_list_1 = [b'Act', b'Bear', b'Cat', b'125', b'Dog', b'it', b'the']
    for i in range(-1, -len('bear') -1, -1):
        test_list_1 = count_sort(test_list_1, i)
        print(test_list_1) 


main()