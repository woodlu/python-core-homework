class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(self, type(other))

    def __hash__(self):
        return hash(self.name)

    def __gt__(self, other):
        if self.name == 'Rock':
            if other.name == 'Paper':
                return False
            else:
                return True
        elif self.name == 'Paper':
            if other.name == 'Scissors':
                return False
            else:
                return True
        else:
            if other.name == 'Rock':
                return False
            else:
                return True


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')
