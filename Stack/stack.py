class Stack(object):

    def __init__(self):
        self.item = []

    def push(self, value):
        """
        add the value into self.item
        :param value: value that to be added into self.item
        :return:
        """
        self.item.append(value)
        pass

    def pop(self):
        """
        remove the last value from the self.item
        :return:
        """
        self.item.pop()
        pass

    def peek(self):
        """
        peek the last value from self.item
        :return: last value from self.item
        """
        if self.item:
            return self.item[-1]
        else:
            return None

    def size(self):
        """
        show the total values size into self.item
        :return: total values size into self.item
        """
        if self.item:
            return len(self.item)
        else:
            return None

    def is_empty(self):
        """
        show the self.item is empty or not
        :return: self.item is empty or not
        """
        if not self.item:
            return True
        else:
            return False


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2323)
    # print(stack.size())
    stack.push(2323)
    # print(stack.size())
    # stack.pop()
    # print(stack.size())
    # print(stack.is_empty())
    # stack.pop()
    # stack.pop()
    # print(stack.is_empty())
    stack.push('abcd')
    print(stack.peek())
    stack.pop()
    print(stack.peek())
