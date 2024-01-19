class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.back = None  # could be called .rear

    def enqueue(self, value):
        """
        Adds a new node to the end of the queue, with the provided value.
        """
        new_node = Node(value)

        # if the Queue is empty
        if self.back is None:
            self.front = new_node
            self.back = new_node

        # Queue isn't empty
        else:
            self.back.next = new_node
            # point the queue's self.back to our new node. Update the pointer!
            self.back = new_node

    def dequeue(self):
        """
        Removes the front node from the queue and returns its value.
        """
        # if the Queue is empty
        if self.front is None:
            # TODO: raise an error
            return None

        # get the value
        dequeue_value = self.front.value

        # move the front pointer to its next
        self.front = self.front.next

        # the Queue has become empty
        if self.front is None:
            # also need to update self.back
            self.back = None

        return dequeue_value
