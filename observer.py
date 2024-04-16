class Subject(object):
    def __init__(self):
        self.observers=[]
    def notify(self):
        for obs in self.observers:
            obs.update(self)
    def attach(self,obs):
        if not hasattr(obs,"update"):
            raise ValueError("Observer must have  an update() method")
        
        self.observers.append(obs)
    def detach(self,obs):
        if obs in self.observers :
            self.observers.remove(obs)

class Observer:
    def update(self,subject):
        raise NotImplementedError
        
class ConcreteObserver :
    def __init__(self):
        Observer.__init__(self) 
    # def update(self,subject):
    #     pass

if __name__ =="__main__" :
    subject=Subject()
    observer=ConcreteObserver()
    subject.attach(observer)

    