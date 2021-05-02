# ---------------------------------------- #
# Bounded Queue
# - Not using linked list
# Shaishav Shah
# 2021-05-02
# ---------------------------------------- #


class BoundedQueue: 
    def __init__(self, capacity): 
        '''
        Constructor, which creates a new empty queue
        '''        
        assert isinstance(capacity, int), ('Error: Type error: {}'.format(type(capacity)))
        assert capacity >= 0, ('Error: Illegal capacity: {}'.format(capacity))
        self.__items = []
        self.__capacity = capacity
        self.__size = 0
 
    
    def enqueue(self, item): 
        ''' 
        Adds a new item to the back of the queue, and returns nothing
        '''
        if len(self.__items) >= self.__capacity:     
            raise Exception('Error: Queue is full')       
        self.__items.append(item)
        self.__size += 1
        
  
    def dequeue(self):
        '''
        Removes and returns the front-most item in the queue.      
        Returns nothing if the queue is empty.  
        '''
        if len(self.__items) <= 0:            
            raise Exception('Error: Queue is empty')                
        self.__size -= 1
        return self.__items.pop(0)  
   
          
    def peek(self):   
        '''
        Returns the front-most item in the queue, and DOES NOT change the queue.
        '''
        if len(self.__items) <= 0:            
            raise Exception('Error: Queue is empty')        
        return self.__items[0]
        
      
    def isEmpty(self):
        '''
        Returns True if the queue is empty, and False otherwise.  
        '''
        return self.__size == 0    
    
        
    def isFull(self):  
        '''
        Returns True if the queue is full, and False otherwise.
        '''
        return self.__size == self.__capacity
    
        
    def size(self):   
        '''
        Returns the number of items in the queue
        '''
        return self.__size       
    
       
    def capacity(self):
        '''
        Returns the capacity of the queue.
        '''
        return self.__capacity
    
  
    def clear(self):
        '''
        Removes all items from the queue, and sets the size to 0.    
        '''
        self.__items = []
        self.__size = 0

    
    def __str__(self):   
        '''
        Returns a string representation of the queue. 
        '''
        str_msg = "Front -> Back | "        
        for item in self.__items:            
            str_msg += (str(item) + " ")                    
        return str_msg
        
    
    def __repr__(self):    
        '''
        Returns a formal string representation of the object BoundedQueue.
        '''
        return  str(self) + " | Size = {}/{}".format(self.__size, self.__capacity)      



