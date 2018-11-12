#Raul Rodriguez
#80549657
#Last Modified - 11/11/2018
#Diego Aguirre - Professor 

# HashTable class 
class HashTable:
    def __init__(self, initial_size=26):
        # Hash Table is initialized with 26 indices
        self.table = []
        for i in range(initial_size):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, word):
        #get index where the word will go.
        index = (ord(word[:1].lower())-97) % len(self.table)
        list = self.table[index]
        # The word is inserted at the end of the list.
        list.append(word.lower())

    # Searches for an item with matching key in the hash table.
    def find(self, word):
        # get the list at index where the word would be.
        index = (ord(word[:1].lower())-97) % len(self.table)
        list = self.table[index]
        try:
            item_index = list.index(word)
        except ValueError as e:
            return None
        return list[item_index]

    def average_number_strings(self):
        sum = 0
        for i in range(len(self.table)):
            sum += len(self.table[i])
        return str(sum/len(self.table))

def hash_list(file_name):
    hashTable = HashTable()
    with open(file_name, 'r') as file:
        for line in file:
            hashTable.insert(line.split()[0])
    return hashTable

def max_in_list(list):
    max = list[0] 
    for i in range(1, len(list)):
        if int(list[i].split()[0]) > int(max.split()[0]):
            max = list[i]
    return max

def print_anagrams(dict, count, word, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        #If in tree, print string, and append to counter
        if dict.find(str.lower()) != None:
            print(str)
            count.append(str)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            if cur not in before:
                print_anagrams(dict, count, before + after, prefix + cur)

def read_file(file_name, dict):
        most_anagrams = []
        with open(file_name, 'r') as file:
            for line in file:
                count = [] # Stores word and count of angrams
                word = line.split()[0]
                print("---Anagrams for " + word.upper() + "---")
                print_anagrams(dict, count, word)
                most_anagrams.append(str(len(count)) + " " + word) # Appends words, and amount of anagrams
                print("Total Anagrams: " + str(len(count)) +"\n")
            max = max_in_list(most_anagrams) # Which word contains the most anagrams
            print("The word with the most anagrams:" + max.split()[1])
            return

def main():
        words = ("words.txt")
        file_name = ("list.txt")
        hashTable = hash_list(words)
        print("The average number of strings in the hash table is: " + hashTable.average_number_strings())
        read_file(file_name, hashTable)

main()    
