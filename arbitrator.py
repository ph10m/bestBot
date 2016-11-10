from random import uniform

class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon  # En pointer til bbcon-objektet
        recommendations = []

    def choose_action(self):
        # hent ut en tilfeldig aksjon fra lista med en vektet sannsynlighet
        recommendations = self.bbcon.recommendations
        r_sum = 0
        for recommendation in recommendations:
            if recommendation[1] == 1:  # Returnerer recommendationen dersom den har prioritet 1
                return recommendation
            else:
                r_sum += recommendation[1]
        rand_num = uniform(0, r_sum)
        for recommendation in recommendations:
            if rand_num <= recommendation[1]:
                return recommendation
            else:
                rand_num -= recommendation[1]



# class Bbcon:
#     def __init__(self):
#         self.recommendations = [["a", 0.5], ["b", 0.7], ["c", 0.9], ["d", 1]]
#         arb = Arbitrator(self)
#         print(arb.choose_action())

# if __name__ == "__main__":
#     bbcon = Bbcon()
