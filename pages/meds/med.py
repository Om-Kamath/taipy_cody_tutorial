
class Medicine():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def render(self):
        return f"""
# <|{self.name}|text|>

<|{self.description}|text|>

"""
    
