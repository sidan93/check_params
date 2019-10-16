from unittest import TestCase
from checkparams.checkparams import check_param
from parameterized import parameterized, param


class TestCheckParams(TestCase):
    @parameterized.expand([
        param(True, 4),
        param(False, 'test'),
        param(False, None)
    ])
    def test_base(self, result, args):

        @check_param()
        def my_f(arg: int) -> int:
            return arg

        if result:
            self.assertEqual(my_f(args), 4)
        else:
            with self.assertRaises(Exception):
                my_f(args)
