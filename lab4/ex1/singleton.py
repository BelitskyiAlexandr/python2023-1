class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance



try:
    a = Singleton()
    b = Singleton()
except Exception:
    print("Signleton exception")