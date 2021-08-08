from random import randint as rand

def random_name(vaule=False):
    Soglasn = {1:"q", 2:"w", 3:"r", 4:"t", 5:"p", 6:"s", 7:"d", 8:"f", 9:"g", 10:"h", 11:"j", 12:"k", 13:"l", 14:"z", 15:"x", 16:"c", 17:"v", 18:"b", 19:"n", 20:"m"}
    Glasn = {1:"e", 2:"y", 3:"u", 4:"i", 5:"o", 6:"a"}
    #Готовые имена
    Names = ["Ibraghim", "Vitalya", "Ridle", "Willy", "Grisha", "Billy", "Kenny", "Lisa", "Mihaile", "Nikalas", "Alexandr", "Alex", "Sasha", "Rotackovsky", "Nike", "Yuppi", "Richard", "Adolf", "Tengu", "Itachi", "Saske", "Maxim", "Fridrich", "Vinne"]

    #"Пространство" для генерации имени
    Name = ""
    #Количество символов в ранд. имени
    max = rand(2, 8)

    #Рандомное имя
    if vaule:
        #Определяем начальную букву
        SoglStyle = random_bool()
        #Генерация
        for i in range(max):
            if SoglStyle:
                Name += (Soglasn[rand(1, len(Soglasn))])
                SoglStyle = False
            elif not SoglStyle:
                Name += (Glasn[rand(1, len(Glasn))])
                SoglStyle = True
        return Name.title()
    #Имя из списка
    elif random_bool() and not vaule: return Names[rand(0, len(Names)-1)]

#Рандомное четырёх-значное число, либо строка
def random_id(vaule=True):
    if vaule:
        return (str(rand(0,9)) + str(rand(0,9)) + str(rand(0,9)) + str(rand(0,9)))
    elif not vaule:
        return (rand(0,9)) + str(rand(0,9)) + str(rand(0,9)) + str(rand(0,9))

def random_bool():
    if rand(0, 1) == 1:
        return True
    else:
        return False

def remove_wich_list(object, list, vaule=False):
    if not vaule:
        for i in range(len(list)):
            if object in list[i]:
                list.remove(list[i])
                break
    elif vaule:
        if object in list:
            list.remove(object)
            return True
    return False

def found_in_list(object, list, vaule=None):
    for i in range(len(list)):
        if object in list[i]:
            if vaule == "i":
                return i
            else:
                return True
            break
    return False

def skip_itiration(num_skip, i):
    if i == num_skip: return False
    else: return True
