class Project:
    def __init__(
        self,
        id=None,
        name=None,
        description=None,
    ):
        self.id=id
        self.name=name
        self.description=description

    def __repr__(self):
        return f"{self.id}:{self.name}"

    def __eq__(self, other):
        return None in [self.id, other.id] or self.id == other.id

    def __gt__(self, other):
        if self.id is None:
            return True
        if other.id is None:
            return False

        return int(self.id) > int(other.id)