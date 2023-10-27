from pytest import mark, raises
from program import Program


class TestProgram:
    @mark.parametrize("list1, list2, avg1, avg2", [([1, 2, 3], [2, 4, 6], 2, 4),
                                                   ([3, 3, 3], [12, 1, 2], 3, 5),
                                                   ([2.2, 3.5, 3.3], [1.4, 2.6, 2.3],
                                                    3.0, 2.1)])
    def test_avg_lists_equality(self, list1, list2, avg1, avg2):
        res1, res2 = Program.avgs(list1, list2)
        assert res1 == avg1
        assert res2 == avg2

    @mark.parametrize("list1, list2, error", [([1, 2, 3], ["d", "q"], TypeError),
                                              (["d", "q"], [12, 1, 2], TypeError)])
    def test_avg_lists_with_error(self, list1, list2, error):
        with raises(error):
            Program.avgs(list1, list2)

    def test_avr_lists_clear_list(self):
        with raises(ValueError):
            Program.avgs([], [1, 2])

    @mark.parametrize("arg1, arg2, compare", [(4, 2, "Первый список имеет большее среднее значение"),
                                              (1, 3, "Второй список имеет большее среднее значение"),
                                              (6, 6, "Средние значения равны")])
    def test_avg_lists(self, arg1, arg2, compare):
        res = Program.comparison(arg1, arg2)
        assert res == compare
