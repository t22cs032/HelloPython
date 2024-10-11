import random

class Player:
    def init_(self,name):
        self_name = name
        self_wincount = 0

    def show_hand(self):
        return random.randrange(3)

    def notify_result(self,result):
        if True == result:
            self_wincount += 1

    def get_wincount(self):
        return self_wincount

    def get_name(self):
        return self_name



class Judge:
    def print_hand(self,hand):
        if hand == 0:
            return 'グー'
        elif hand == 1:
            return 'ちょき'
        elif hand == 2:
            return 'パー'
                                                