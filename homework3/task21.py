class CyclicIterator:
    """
    A cyclic iterator. When the last element is reached, it starts over.
    """

    def __init__(self, iterable_obj):
        self.iterable_obj = iterable_obj
        self.inner_iterator = iter(self.iterable_obj)

    def __next__(self):
        try:
            val = next(self.inner_iterator)
        except StopIteration:
            self.inner_iterator = iter(self.iterable_obj)
            val = next(self.inner_iterator)
        return val

    def __iter__(self):
        return self


if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
