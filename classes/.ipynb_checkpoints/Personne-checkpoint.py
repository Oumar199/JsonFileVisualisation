class Personne:
    def __init__(self, **myDataFrame):
        for index, value in myDataFrame.items():
            setattr(self, index, value)
        
        
        