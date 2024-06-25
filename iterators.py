class FlatIterator:
    def __init__(self, list_of_list):
        self.list_ = list_of_list

    def __iter__(self):
        self.cursor = -1
        self.ind = 0
        return self

    def __next__(self):
        self.cursor += 1
        self.ind_list = self.list_[self.ind]

        if self.cursor >= len(self.ind_list):
            self.cursor = 0
            self.ind += 1
            if self.ind == len(self.list_):
                raise StopIteration
            self.ind_list = self.list_[self.ind]

        return self.ind_list[self.cursor]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
