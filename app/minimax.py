from abc import ABCMeta, abstractmethod

class Minimax_State(metaclass=ABCMeta):
    @abstractmethod
    def sucessors(self):
        pass
    
    def is_finished(self):
        pass

class Minimax:
    def get_next_step(state):
        pass
    def max(state):
        pass
    def min(state):
        pass