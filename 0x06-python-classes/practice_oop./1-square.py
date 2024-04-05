class square:
    """show size of a sqaure"""

    def __init__(self, size=0):
        

        if not isinstance(size, int):
            raise typerror('must be an integer')
        elif size < 0:
            raise valueError('size must be >=0')
        
        self.__size = size