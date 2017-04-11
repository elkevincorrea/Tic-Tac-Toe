from abc import ABCMeta, abstractmethod

class Minimax_State(object):
    __metaclass__ = ABCMeta
    PLAYER_1 = 1
    PLAYER_2 = 2
    @abstractmethod
    def sucessors(self):
        pass
    @abstractmethod
    def is_finished(self):
        pass
    @abstractmethod
    def utility(self):
        pass
    @abstractmethod
    def get_player(self):
        pass

def get_next_step(state):
    if state.get_player() == Minimax_State.PLAYER_1:
        return max_value(state)
    else:
        return min_value(state)

def max_value(state):
    utility = state.utility()
    if utility != None:
        return utility, state
    max_v = -999
    max_res = None
    succesors = state.sucessors()
    for succesor in succesors:
        min_v, min_res = min_value(succesor)
        if min_v > max_v:
            max_v = min_v
            max_res = succesor
    return max_v, max_res

def min_value(state):
    utility = state.utility()
    if utility != None:
        return utility, state
    min_v = 999
    min_res = None
    succesors = state.sucessors()
    for succesor in succesors:
        max_v, max_res = max_value(succesor)
        if max_v < min_v:
            min_v = max_v
            min_res = succesor
    return min_v, min_res
