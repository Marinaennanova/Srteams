import threading
import time

# объявление функции wite_words,word_count-кол-во записываемых слов,file_name-имя файла
def wite_words(word_count,file_name):

    with open (file_name,"a",encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i+1}\n")
            time.sleep(0.01)
        print(f"Завершилась запись в фаил {file_name}")
# Взятие текущего времени

start = time.time()
# Запук функции 4 ре раза с аргументами
wite_words(3,"example1.txt")
wite_words(5,"example2.txt")
wite_words(10,"example3.txt")
wite_words(20,"example4.txt")
# завершение времени
fin = time.time()
finish =fin - start
print(f"Затрачено времени:  {finish}")

# После вызовов функций создаем 4 потока для вызова этой функции
# Взятие текущего времени на момент создания потоков
start_2 = time.time()
thread_1 = threading.Thread(target=wite_words, args= (3, 'example5.txt'))
thread_2 = threading.Thread(target=wite_words, args= (5, 'example6.txt'))
thread_3 = threading.Thread(target=wite_words, args= (10, 'example7.txt'))
thread_4 = threading.Thread(target=wite_words, args= (20, 'example8.txt'))
# Запуск потоков
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
# приостановка потоков программы
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
# финальное время после того,как потоки отработали
fin_2 = time.time()
finish_2 = fin_2 - start_2
print(f"Затрачено времени:  {finish_2}")
# Вывод разницы начала и конца работы потоков
print(f'Использование Потоков быстрее функций на {finish-finish_2} секунд')




