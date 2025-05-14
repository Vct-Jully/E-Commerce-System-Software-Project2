class Subject:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observer):
        self._observers.append(observer)

    def notificar(self, mensagem):
        for observer in self._observers:
            observer.update(mensagem)

class Observer(ABC):
    @abstractmethod
    def update(self, mensagem):
        pass

# Observer (notifica por e-mail)
class EmailNotifier(Observer):
    def update(self, mensagem):
        print(f"Email enviado: {mensagem}")
