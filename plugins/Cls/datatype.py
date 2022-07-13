class Gamers:
    def __init__(self) -> None:
        self.__Gamers = dict()
    
    async def Add(
        self,
        key,
        value
        )-> None:

        "Add Game"

        self.__Gamers[key] = value
    
    async def Remove(
        self,
        key
        )-> None:

        "Remove Value With Key"

        del self.__Gamers[key]

    async def Get(
        self,
        key
        )-> None:
        
        "Get Value With Key"

        value = self.__Gamers.get(key)
        return value
    
    def __str__(self) -> str:
        return f"{self.__Gamers}"
_Gamers = Gamers()