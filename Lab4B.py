#Raul Rodriguez
#80549657
#Last Modified - 11/11/2018
#Diego Aguirre - Professor 

class HashTableNode:
    # Constructor with a key parameter creates the Node object.
    def __init__(self, item, next):
        self.item = item
        self.next = next

class HashTable:        
    def __init__(self, table_size):
        self.table = [None] * table_size        
    
    #I converted the letters in the words to integers by 
	#taking the sum of the letters in each word
    def hash(self, k):
        p = 0
        for i in range(len(k)):
            p = p + ord(k[i])
        return p % len(self.table)
    
    #Inserting the item in the table and creating a linked list
    def insert(self, k):
        pos = hash(k)
        self.table[pos] = HashTableNode(k,self.table[pos]) 
        
    #Compute the load factor by dividing the number of elements by the size of the table
    def get_load_factor(self,k):
        num_elements = 0
        pos = hash(k)
        for i in range(len(self.table)):
            temp = self.table[pos]

            while temp is not None:
                num_elements += 1
                temp = temp.next

        return num_elements / len(self.table)
    
    #Find the average number of comparisons
    def get_average_compare(self, k):
        count = 0
        pos =  hash(k)
        for i in self.table:
            temp = self.table[pos]
            while temp != None:
                if temp.item == k:
                    count = count + 1
                temp = temp.next
            return count / len(self.table)
            
    
my_file = open("words.txt")
lines = my_file.readline()
my_file.close()
for i in lines:
    m = HashTable(354984)
    num_list = m.hash(i)
    print(num_list)
    print("Inserting...")
    print(m.insert(num_list))
    print("Average numbers of comparison: ")
    print(m.get_average_compare(num_list))
    print("The load factor is: ")
    print(m.get_load_factor(num_list))
    print()