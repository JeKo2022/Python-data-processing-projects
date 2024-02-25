# Implements a queue

# create class and set name of class
class Queue:

    # create an object that is internal to our queue objects
    # initializer-methode runt bij het aanmaken van elk object van de klasse Queue
    def __init__(self):
        self._data = [] # elk Queue object begint dus met een lege lijst genaamt data
                        # the underscore (_) to indicate that the variable is private
                        # to the object, and that one should not to write code to
                        # manipulate that variable from anywhere else but the code of the class itself.

    # add element to back of queue
    def enqueue(self, element):
        # use append() to add an item to the “end” of a list
        self._data.append(element)

    # remove and return element from front of queue
    def dequeue(self):
        # TODO
        # set assertion  error when trying to dequeue() when the queue is actually empty.
        assert self.size() > 0

        # use pop to remove  elements from the start of a list.
        # return the element that is popped so it can be used
        return self._data.pop(0)

    def size(self):
        # TODO
        # returns the number of elements “waiting” in the queue
        return len(self._data)

    def peek(self):
        # TODO
        # returns the frontmost element but does not remove it from the queue (yet)
        return self._data[0]

    def empty(self):
        # TODO
        # clear the queue, removing all elements from the list
        return self._data.clear()

# link object "q", to class "Queue"
q = Queue()          # create new queue

# call on function enqueue in class Queue and apply to specific object "q"
q.enqueue(7)         # add number 3 to back of queue
q.enqueue(1)         # add number 1 to back of queue
q.enqueue(5)         # add number 5 to back of queue
q.enqueue(1)         # add number 1 to back of queue
q.enqueue(7)         # add number 7 to back of queue

# calls on function denqueue in class Queue and apply to specific object "q"
print(q.dequeue())   # prints first number "in", so 3, and removes it from list
print(q.peek())
print(q.size())
