#Part B

def test_ed_append():
    test_name = 'test_append'
    test_fn = 'test.txt'
    if os.path.isfile(test_fn):
        os.remove(test_fn)
        
    initial_text = 'ABCD'
    with open(test_fn, 'w') as test_f:
        test_f.write(initial_text)
        
    try:
        new_text = '01234'
        ret = ed_append(test_fn, new_text)
        expected_text = initial_text + new_text
        current_text = open(test_fn, 'r').read()
        
        cond = (ret == len(new_text)) and (current_text == expected_text)
        
        return testif(cond, test_name)
    except Exception as exc:
        print('test {} failed due to exception: {}\n'.format(test_name, str(exc)))
        return False

def testif(b, testname, msgOK= "" , msgFailed= "" ):
    """Function used for testing."""
    if b:
        print ( "Success: " + testname + "; " + msgOK)
    else :
        print ( "Failed: " + testname + "; " + msgFailed)
    return b


#Part A

def ed_read(file, start, end):
    """Will Read the file starting from the give starting index and 
        ending at the given end index
       """
    try:
        str_read = ""
        str_file = open(file, "r", encoding='utf8')
        for start, c in str_file:
            if start == end:
                break
            else:
                str_read = str_read + c

    except IOError:
        print('{} is a bad file name'.format(file))
        break

    except FileNotFoundError:
        print('file {}: cannot be found'.format(file))
        break

    except ValueError:
        print('one or more variables exceed file length')
        break

def ed_find(file, search_str):
    """This function will retun the first index a word is found and can return
        multiple values. will return [] if nothing is found
    """
    try:
        temp = list()       #for variables
        str_file = open(file, "r", encoding='utf8')

        for i, c in str_file:           #start searching the file
            if c == search_str[0]:          #if the character in the file is equal to the first letter in the search string then...         
                temp.append(i)                  #append it to list then..
                for j in search_str:                    #incrementing through the search word
                    if str_file[i+j] != search_str[j]:      #if it doesnt match the part of the file then.... 
                        temp.remove(i)                          #Remove the value from the list and end the loop
                        break
        return temp    
        
    except IOError:
        print('{} is a bad file name'.format(file))
        break

    except FileNotFoundError:
        print('file {}: cannot be found'.format(file))
        break


def ed_replace(file, search_str, replace_with, occurence):
    """Similar to ed_find .. can probably call it...
        This function takes a search string and a astring to replace with..
        if occurence >= 0 it replaces the search string with the replace word only at that index
        if occurence == -1 then it replaces all of them
    """

    try:
        str_file = open(file, "w", encoding='utf8')

        if occurence == -1:
            temp_ls = ed_find(file, search_str)

            for i in temp_ls:
                #temp_str = ""
                #for j in search_str:
                    #temp_str = str_file[temp_ls + j]
                str_file[i].replace(search_str, replace_with)           #hoping that this works like a string 
        
        else:
            str_file[occurence].replace(search_str, replace_with)

    except IOError:
        print('{} is a bad file name'.format(file))
        break

    except FileNotFoundError:
        print('file {}: cannot be found'.format(file))
        break

def ed_append(file, str_a):
    """Appends a string to the end of the file. If the file does not exist a new one is created
        The function returns the number of characters written to the file
    """

    try:
        str_file = open(file, "a", encoding='utf8')

        str_file.write(str_a)

        return len(str_a)


    except IOError:
        print('{} is a bad file name'.format(file))
        break

    except FileNotFoundError:
        print('file {}: cannot be found'.format(file))
        break


def ed_write(file, pos_str_col):
    """pos_str_col is a list has (position, s)
        
    """

    try:
        str_file = open(file, "r+", encoding='utf8')
        count = 0
        for i in pos_str_col:
            if i < 0 or i > len(str_file):
                raise ValueError('position parameter is less than 0 or greater than the file length')
            
        return count

    except IOError:
        print('{} is a bad file name'.format(file))
        break

    except FileNotFoundError:
        print('file {}: cannot be found'.format(file))
        break


def ed_insert(file, pos_str_col):
    """
    """

    try: 
        str_file = open(file, "r+", encoding='utf8')
        count = 0

        for i in pos_str_col:
            if i < 0 or i > len(str_file):
                raise ValueError('position parameter is less than 0 or greater than the file length')
                     
        return count

    except IOError:
        print('{} is a bad file name'.format(file))
        break

    except FileNotFoundError:
        print('file {}: cannot be found'.format(file))
        break
        
#Part C

def main():
    fn = "file1.txt"         # assume this file does not exist yet.
    ed_append(fn, "0123456789")    # this will create a new file
    ed_append(fn, "0123456789")    # the file content is: 01234567890123456789
    print(ed_read(fn, 3, 9))    # prints 345678. Notice that the interval excludes index to (9)
    print(ed_read(fn, 3))       # prints from 3 to the end of the file: 34567890123456789
    lst = ed_find(fn, "345")
    print(lst)             # prints [3, 13]
    print(ed_find(fn, "356"))                       # prints []
    ed_replace(fn, "345", "ABCDE", 1)  # changes the file to 0123456789012ABCDE6789
    # assume we reset the file content to 01234567890123456789  (not shown
    ed_replace(fn, "345", "ABCDE")  # changes the file to 012ABCDE6789012ABCDE6789
    # assume we reset the file content to 01234567890123456789 (not shown)
    # # this function overwrites original content:
    ed_write(fn, ((2, "ABC"), (10, "DEFG")))   # changes file to: 01ABC56789DEFG456789# this should work with lists as well: [(2, "ABC"), (10, "DEFG")]
   
    ed_write(fn, ((2, "ABC"), (30, "DEFG")))   
    ed_insert(fn, ((2, "ABC"), (10, "DEFG"))) # changed file to: 01ABC23456789DEFG0123456789

main()