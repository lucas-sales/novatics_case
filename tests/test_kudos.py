#  python -m unittest discover
from app.kudos import Kudos
from unittest import TestCase


class TestKudos(TestCase):
    def setUp(self):
        self.kudos = Kudos()

    def test_convertPoints(self):
        self.kudos.convertPoints(30)
        if self.kudos.lst_output[0] == "GOOD" and self.kudos.lst_output[-1] == "NICE":
            self.assertTrue(True)

    def test_output(self):
        output = self.kudos.output(40)
        if output == "Você recebeu dezesseis reais em retorno aos kudos GOOD, GOOD!":
            self.assertTrue(True)