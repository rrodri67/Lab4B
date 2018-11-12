#Raul Rodriguez
#80549657
#Last Modified - 11/11/2018
#Diego Aguirre - Professor 

#hash table node
class HashTableNode:
    def __init__(self, item, next):
        self.item = item
        self.next = next  
        
class HashTable:

    def __init__(self, table_size):
        self.table = [None] * table_size     
        
    # 3 diffrent hash functions and take the integer value of each character in the word and muplity it using pow function
    def hash_1(self, word):
        hash = 0
        for i in range(len(word)):
            k = ord(word[i])
            k = k * (pow(4, i))
            hash += k
        return hash % len(self.table)


    def hash_2(self, word):
        hash = 0
        for i in range(len(word)):
            k = ord(word[i])
            k = k * (pow(8, i))
            hash += k
        return hash % len(self.table)


    def hash_3(self, word):
        hash = 0
        for i in range(len(word)):
            k = ord(word[i])
            k = k * (pow(14, i))
            hash += k
        return hash % len(self.table)
           
    #count all the elements in the table and divide that number by the size of the table
    def get_load_factor(self):
        num_elements = 0
        for i in range(len(self.table)):
            temp = self.table[i]

            while temp is not None:
                num_elements += 1
                temp = temp.next
        return num_elements / len(self.table)        
    #insert new word at the beginning of the list
    def insert(self, k, hash):
        if hash == 1:
            loc = self.hash_1(k)
            self.table[loc] = HashTableNode(k, self.table[loc])
        if hash == 2:
            loc = self.hash_2(k)
            self.table[loc] = HashTableNode(k, self.table[loc])
        if hash == 3:
            loc = self.hash_3(k)
            self.table[loc] = HashTableNode(k, self.table[loc])  
            
print("Loading...")            
table1 = HashTable(250000)
table2 = HashTable(300000) 
table3 = HashTable(354984) 
my_file = open("words.txt", "r")
my_list = my_file.readlines()
count = 0
while(count != len(my_list)):
    k = my_list[count]
    words = k.split()
    table1.insert(words[0], 1)
    table2.insert(words[0], 2)
    table3.insert(words[0], 3)
    count = count + 1

print("Load factor for first table is: "+str(table1.get_load_factor()))
print("Load factor for second table is: "+str(table2.get_load_factor()))
print("Load factor for third table is: "+str(table3.get_load_factor()))
    