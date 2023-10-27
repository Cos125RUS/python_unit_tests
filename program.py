class Program:
    @staticmethod
    def avgs(list1, list2):
        args = [list1, list2]
        if len(list1) == 0 or len(list2) == 0:
            raise ValueError
        res = []
        for arg in args:
            sum = 0
            for i in arg:
                if not (isinstance(i, int) or isinstance(i, float)):
                    raise TypeError
                sum += i
            res.append(sum / len(arg))
        return res

    @staticmethod
    def comparison(avg1, avg2):
        for i in [avg1, avg2]:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError
        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
