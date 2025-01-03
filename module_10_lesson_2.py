# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
import threading
import time

class Knight(threading.Thread):
# Атрибуты класса :
# -Атрибут name - имя рыцаря. (str)
# -Атрибут power - сила рыцаря. (int)
     def __init__(self,name,power):
         threading.Thread.__init__(self)
         self.name = name
         self.power = power
         self.day = 0
         self.knigts = 100

# Создаем метод run, в котором рыцарь будет сражаться с врагами
     def run (self):

         print(f"{self.name}, на нас напали!")
         while self.knigts > 0:
             print(f"Рыцарь {self.name} сражается уже  {self.day} день(дней), осталось {self.knigts} воинов\n")

             self.knigts -= self.power
             self.day += 1
             time.sleep(0.01)
             print(f'{self.name} одержал победу спустя {self.day} дней(дня)!\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
third_knight = Knight("King Arthur", 50)

first_knight.start()
second_knight.start()
third_knight.start()
first_knight.join()
second_knight.join()
third_knight.join()
print('Все битвы закончились!')