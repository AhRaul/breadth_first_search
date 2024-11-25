from collections import deque

def person_is_anudj(person):
    """
    Метод возвращает true, если это Анудж.
    Проверяющий не знает заранее, какое имя ищут,
    знает только этот метод.
    """
    if person == 'Анудж':
        return True
    else:
        return False

def breadth_first_search(graph, name):
    """
    Алгоритм поиска в ширину.
    graph - связанный список имен.
    name - имя, начиная с которого вы ищите, если ли в его,
            прямых, или косвенных связях нужный человек.
    """
    search_queue = deque()      #Двусторонняя очередь. (Кто зашел в очередь последним, последним из неё и выйдет.)
    search_queue += graph[name] #Вытаскиваем значение (или список значений) из списка graph по ключу name
    searched = []               #Для предотвращения зацикливания, повторно проверки значения,
                                    # все проверенные значения заносятся в этот массив.
    while search_queue:         #Если есть в списке еще проверяемое значение, продолжать проверку.
        person = search_queue.popleft()     #Извлекаем из начала двусторонней очереди значение.
        if not person in searched:  #Проверка, проверяли ли мы раньше это значение, если нет, то можно проверить.
            if person_is_anudj(person):    #Метод проверки имени. Возвращает True False.
                print(person + " - тот, кто нам нужен!")
                return True                # Нужного нашли, сообщение вывели, возвращаем True, чтобы прервать while.
            else:
                search_queue += graph[person]   #Если это не тот, кого мы ищем,
                                                    # погружаемся на следующий уровень списка,
                                                    # и раскладываем его в конце очереди
                                                    # (если уровня нет, то запишется пустота)
                searched.append(person)         # Записываем значение в список проверенных.
    print("Нет никого нужного в этм списке, так что, сорямба.")
    return False    #Если while закончился, то, значит, значения в списке нет и нужно вернуть False.

graph = {}
graph["вы"] = ["Алиса", "Кролик", "Шляпник"]
graph["Кролик"] = ["Анудж", "Давранбек"]
graph["Алиса"] = ["Давранбек"]
graph["Шляпник"]= ["Чай", "Часы"]
graph["Анудж"] = []
graph["Давранбек"] = []
graph["Чай"] = []
graph["Часы"] = []

breadth_first_search(graph, "вы")