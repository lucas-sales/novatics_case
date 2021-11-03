from num2words import num2words


class Kudos:
    def __init__(self):
        # Conversão de kudos para pontos
        self.KUDOS_TO_POINTS = [
            {"name": 'OK', "value": 5},
            {"name": 'NICE', "value": 10},
            {"name": 'GOOD', "value": 20},
            {"name": 'GREAT', "value": 50},
            {"name": 'SUPER', "value": 100},
        ]
        # Conversão de kudos para reais
        self.KUDOS_TO_REAL = [
            {"name": 'OK', "value": 2},
            {"name": 'NICE', "value": 5},
            {"name": 'GOOD', "value": 8},
            {"name": 'GREAT', "value": 15},
            {"name": 'SUPER', "value": 25},
        ]
        self.lst_output = []
        self.money = 0
        self.finalMessage = ''

    def convertPoints(self, points):
        current_value = points
        for dic in self.KUDOS_TO_POINTS[::-1]:  # percorre a lista do valor maior para o menor
            if current_value % int(dic["value"]) == 0:  # Verifica se o mesmo elemento do laço se aplica mais de uma vez
                while current_value != 0:
                    current_value -= int(dic["value"])
                    self.lst_output.append(dic["name"])

            if int(dic["value"]) <= current_value:
                current_value -= int(dic["value"])
                self.lst_output.append(dic["name"])

    def convertMoney(self):
        finalValue = 0
        for hating in self.lst_output:
            dic = list(filter(lambda ranking: ranking['name'] == hating, self.KUDOS_TO_REAL))
            finalValue += dic[0]["value"]

        finalValue = num2words(finalValue, lang='pt_BR')
        finalHating = ', '.join(self.lst_output)
        return finalValue, finalHating

    def output(self, points):
        self.convertPoints(points)
        output = self.convertMoney()
        return f'Você recebeu {output[0]} reais em retorno aos kudos {output[1]}!'
