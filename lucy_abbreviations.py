def Myabbrev(text_file):
    """MyAbbrev was created to read text files that contain names and 
    came out with abbrevs with three letter words.
    Some functions were also created to achieve the result.
    """
    # Import random and set seed to 1
    import random
    random.seed(1)

    """discard_puncs  was created to remove all punctuations from each of the names in the list 
    and prepare the names for further processing 
    """
    # List of non-letter characters that are likely used for compound words
    more_puncs = ["-", "_"]
    def discard_puncs(myfile):
        with open(myfile, 'r', encoding='utf-8') as lucy_file:
            mynames = lucy_file.read().split('\n')
            # dictionary of non-letter characters that are likely to exist in names
        puncs = {
            "'":"",
            "+":"",
            "!":"",
            "’":"",
            "`":""
        }
        puncs_discarded = []
        # Looping through each word and removing non-letter characters defined in the dictionary
        for n in mynames:
            remv_punc = n.translate(str.maketrans(puncs)).upper()
            puncs_discarded.append(remv_punc)
        puncs_discarded
        return puncs_discarded

    """Detach_compoundnames was created to identify any compound word that does not have letter with them, 
    like the once explained in (more-puncs) variable  
    """
    def detach_compoundnames(cleaned_names):
        nd = []
        nd1 = []
        if len(cleaned_names.split()) > 1:
            # Loops through the cleaned names and separate by space first 
            for n in cleaned_names.split():
                for puncs in more_puncs:
                    # Checking if the charaters in more_puncs is in any of the splitted words 
                    if puncs in n:
                        # Split the word by that charater found in the word
                        d=n.split(puncs)
                        # Add the splitted word to the list defined above
                        nd  += d
                    else:
                        pass
            # Add word that did not fall in the if statement above to the list.
            nd.append(n)
        elif len(cleaned_names.split()) == 1:
            for n in cleaned_names.split():
                for puncs in more_puncs:
                    if puncs in n:
                        d=n.split(puncs)
                nd+=d
        return nd
    
    numbers_dictionary = {
        'A':25, 'B':8, 'C':8, 'D': 9, 'E':35,
        'F':7, 'G':9, 'H':7, 'I':25, 'J':3,
        'K':6, 'L':15, 'M':8, 'N':15, 'O':20,
        'P':8, 'Q':1, 'R':15, 'S':15, 'T':15, 
        'U':20, 'V':7, 'W':7, 'X':3, 'Y':7, 'Z':1
    }

    def small_figures_picker(string):
        separate = [*string]
        new_dictionary = {}
        for n,m in numbers_dictionary.items():
            if n in separate:
                new_dictionary[n] = m
                
        alphabet = list(new_dictionary.keys())
        numerical_list = list(new_dictionary.values())
        numbers_list = []
        for n in separate[1:]:
            numbers_list.append(new_dictionary[n])
        numbers_list.sort()

        first = numbers_list[0]
        second = numbers_list[1]
        number1 = numerical_list.index(first)
        number2 = numerical_list.index(second)
        both = alphabet[number1] + alphabet[number2]
        
        sorted = []
        split1 = [*string]
        split2 = [*both]
        sorted.append(split1.index(split2[0]))
        sorted.append(split1.index(split2[1]))
        sorted.sort()
        return split1[sorted[0]]+split1[sorted[1]]
    
    def small_figure_picker2(string):
        separate = [*string]
        new_dictionary = {}
        for n,m in numbers_dictionary.items():
            if n in separate:
                new_dictionary[n] = m
                
        alphabet = list(new_dictionary.keys())
        numerical_list = list(new_dictionary.values())
        numbers_list = []
        for n in separate[1:]:
            numbers_list.append(new_dictionary[n])
        numbers_list.sort()

        first = numbers_list[0]
        number1 = numerical_list.index(first)
        one = alphabet[number1]
        return one

    """Here, all functions created above are put to use to perform the task. 
    """
    # Remove apostrophes and non-letter character
    renamed = discard_puncs(text_file)
    # Empty list to hold the new results, words followed by its abbreviation.
    abbreviations = []
    section = []
    # loop through the clean names, seperate any joined words, and extract letters.
    # Add results to the empty list above.
    for word in renamed:
        string = ''
        if any(n in word for n in more_puncs):
            sep = detach_compoundnames(cleaned_names=word)
            abbreviations.append(sep)
            if len(sep) > 2:
                string += sep[0][0] + sep[1][0] + sep[2][0]
                section.append(word)
                section.append(string)
            elif len(sep) == 2:
                string += sep[0][0] + sep[1][0] + sep[1][1]
                section.append(word)
                section.append(string)
        else:
            each = word.split() 
            if len(each) > 2: 
                string += each[0][0] + each[1][0] + each[2][0]
                section.append(word)
                section.append(string)
            elif len(each) == 2:
                string += each[0][0] + each[1][0] + small_figure_picker2(each[1])
                section.append(word)
                section.append(string)
            elif len(each) == 1:
                chars = each[0]
                string += each[0][0] + small_figures_picker(chars)
                section.append(word)
                section.append(string)
    print(section)

    # Creating file output name as per requirements
    myfile_name = text_file.split('.')[0]
    sur_name = 'awah-ubah'
    outcome_name = (f'{sur_name.lower()}_{myfile_name.lower()}_abbrevs.txt')
    
    # writing the results to the created file above
    with open(outcome_name, 'w') as file:
        file.write('\n'.join(section)) 

# Script based condition to run if script is in main scope 
if __name__ == '__main__':
    nameofFile = input('Enter file name: ')
    Myabbrev(text_file=nameofFile)
