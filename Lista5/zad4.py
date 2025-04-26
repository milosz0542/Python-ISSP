from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    def take_break(self):
        pass

class HumanWorker(Worker):
    def work(self):
        return "Working hard!"

    def take_break(self):
        return "Taking a break!"

class RobotWorker(Worker):
    def work(self):
        return "Working efficiently!"

human_worker = HumanWorker()
robot_worker = RobotWorker()

print(human_worker.work())
print(robot_worker.work())
print(human_worker.take_break())