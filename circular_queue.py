# ---------------------------------------- #
# Circlular Queue
# - Not using linked list, but has O(n) time efficiency for all operations
# Shaishav Shah
# 2021-05-02
# ---------------------------------------- #

class CircularQueue:
    def __init__(self, max_size): 
        if type(max_size) != int or max_size<=0:
            raise Exception('max_size Error')                

        self.__items = []
        self.__max_size = max_size
        self.__head=0
        self.__tail=0
        
    def enqueue(self, item): 
        '''
        Adds a new item to the back of the queue
        '''
        if self.__count == self.__max_size:     
            raise Exception('Error: Queue is full')       
        elif self.__count < self.__max_size:
            self.__items.append(item)
        else:
            self.__items[self.__tail] = item
            
        self.__count +=1
        self.__tail= (self.__tail +1) % self.__max_size
        
       
    def dequeue(self):
        '''
        Removes and returns the front-most item in the queue.      
        '''
        if self.__count == 0:            
            raise Exception('Error: Queue is empty') 
        
        item_to_return = self.__items[self.__head]     
        self.__items[self.__head] = None     
        self.__count -= 1                    
        self.__head = (self.__head+1) % self.__max_size             
        return item_to_return         
    
         
    def peek(self): 
        if self.__count == 0:            
            raise Exception('Error: Queue is empty')        
        
        return self.__items[self.__head]
    
       
    def isEmpty(self):
        return self.__count == 0        
    
        
    def isFull(self):   
        return self.__count == self.__max_size

       
    def max_size(self): 
        return self.__max_size
    
       
    def clear(self):
        self.__items = []
        self.__count = 0
        self.__head = 0
        self.__tail = 0
    
    
    def __str__(self):
        str_exp = "]"        
        i = self.__head
        for j in range(self.__count):            
            str_exp += str(self.__items[i]) + " "
            i = (i+1) % self.__max_size
        return str_exp + "]"
        
       
    def __repr__(self):  
        '''
        Returns a formal string representation of the object CircularQueue 
        '''
        return str(self.__items) + " H= {} T= {} ({}/{})".format(str(self.__head), str(self.__tail), str(self.__count), str(self.max_size))  
