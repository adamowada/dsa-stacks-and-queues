class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Pushes a new value onto the top of the stack.
        """
        # create a new node
        new_node = Node(value)

        # point the new node to the current top
        new_node.next = self.top

        # reassign the self.top in the stack
        self.top = new_node

    def pop(self):
        """
        Pops the top value from the stack and returns it.
        """
        # popping from an empty list
        if self.top is None:
            # TODO: change this to raise an error
            return None

        # get the return value
        pop_value = self.top.value

        # move the pointer which "removes" the node from the Stack
        self.top = self.top.next

        return pop_value


