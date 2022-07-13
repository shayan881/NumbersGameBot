class Gamers:
    def __init__(self) -> None:
        self.__Gamers = dict()
    
    async def Add(
        self,
        key,
        value
        )-> None:

        """Add game with user id"""

        self.__Gamers[key] = value
    
    async def Remove(
        self,
        key
        )-> None:

        """Remove game with user id"""

        del self.__Gamers[key]

    async def Get(
        self,
        key
        )-> None:
        
        """Get game with user id"""

        value = self.__Gamers.get(key)
        return value
    
    def __str__(self) -> str:
        return f"{self.__Gamers}"
    
_Gamers = Gamers()
