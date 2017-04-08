from abc import ABCMeta, abstractmethod

class Minimax_State(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def sucessors(self):
        pass
    @abstractmethod
    def is_finished(self):
        pass
    @abstractmethod
    def utility(self):
        pass

def get_next_step(state):
    #Return max...
    pass
def max(state):
    pass
def min(state):
    pass