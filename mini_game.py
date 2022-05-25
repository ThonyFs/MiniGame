class MiniGame:
    def __init__(self, powerOn, selectGame, volume):
        self._powerOn = powerOn
        self._selectGame = selectGame
        self._volume = volume
    
    def ligar(self):
        self._powerOn =True
        print("MiniGame LIGADO")
    
    def desligar(self):
        self._powerOn = False
        print("MiniGame DESLIGADO")

    def selecionarGame(self, selectGame):
        self._selectGame = input("Informe o nome do game:")
        return self._selectGame 

    def volumeUp(self):
        self._volume += 1
        if self._volume > 0 and self._volume < 5:
            print(f"Seu volume esta baixo: volume {self._volume}")
        elif self._volume >= 5 and self._volume < 10:
            print(f"Seu volume esta na faixa ideal: volume {self._volume}")
        else: 
            print(f"Seu volume esta muito alto: volume {self._volume}")

    def volumeDown(self):
        self._volume -= 1
        if self._volume > 0 and self._volume < 5:
            print(f"Seu volume esta baixo: volume {self._volume}")
        elif self._volume >= 5 and self._volume < 8:
            print(f"Seu volume esta na faixa ideal: volume {self._volume}")
        else: 
            print(f"Seu volume esta muito alto: volume {self._volume}")
        
    @property
    def get_selectGame(self):
        return self._selectGame

    @property
    def get_volume(self):
        return self._volume




