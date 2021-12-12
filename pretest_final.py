# Q1 identify the position(s) of the number if the number is in the given list, if the number is not in the given list, return 0
def find_member_positions(number, list_of_number):
    positions = []

    for i in range(len(list_of_number)):
        if number == list_of_number[i]:
            positions.append(i)
    
    if positions == []:
        return 0
    else:
        return positions
    
print(find_member_positions(2, [2,5,3,2,4]))
print(find_member_positions(1, [2,5,3,2,4]))



# Q2
def find_route(node, routes, total_distance = 0):
    nodes = [node]
    
    # d and k has no routes connected
    while node != 'd' and node != 'k':
        node = routes[node] # node = (keys) --> (a-d, i, j, k, distance)
        nodes.append(node[0]) # append a-d, i, j, k to nodes
        total_distance += node[-1] # total += distance
        node = node[0] # node = a-d, i, j, k

    return (nodes, total_distance)

# routes
# a --(3.4)--> b --(4.0)--> c --(5.6)--> d
# i --(4.0)--> j --(6.0)--> k
routes = {"i": ("j", 4.0), "a": ("b", 3.4), "j": ("k", 6.0), "c": ("d",5.6), "b": ("c", 4.0)}    

print(find_route("a", routes))
print(find_route("b", routes))



# Q3 (Q2 but using recursion to find only total disdance instead)
def recur_find_route(node, routes, total_distance = 0):
    
    if node == 'd' or node == 'k':
        return total_distance
    else:
        node = routes[node]
        total_distance += node[-1]
        node = node[0]
        return recur_find_route(node, routes, total_distance)


routes = {"i": ("j", 4.0), "a": ("b", 3.4), "j": ("k", 6.0), "c": ("d",5.6), "b": ("c", 4.0)}    
print(recur_find_route("a",routes))
print(recur_find_route("b",routes))



# Q4 E-wallet
class EWallet:  # super class
    def __init__(self, max_val, owner_name, current_amount):
        self.check = current_amount
        self.name = owner_name
        self.limit = max_val

    def put_in(self, money):
        try:
            if money < 0:
                raise Exception("Please enter positive amount of money.")
            elif (self.check + money) > self.limit:
                raise Exception(f"Sorry, the amount limit is {self.limit} ฿.")
            else:
                self.check += money
                print("Successfully put in money.")
                return True

        except TypeError:
            print("Please enter a number")
        except Exception as e:
            print(e)
            return False

    def take_out(self, money):
        try:
            if (money < 0):
                raise Exception("Please enter positive amount of money")
            elif (money > self.check):
                raise Exception("Not enough balance, please enter the amount of money that is less than your current balance")
            else:
                self.check -= money
                print("Successfully take out money.")
                return True

        except TypeError:
            print("Please enter a number")
        except Exception as e:
            print(e)
            return False

    def current_balance(self):
        print(f"{self.name}'s balance: {self.check} ฿")

# Q5 E-wallet (full version)
class SmartEWallet(EWallet):  # sub class
    def __init__(self, max_val, owner_name, current_amount):
        # super().__init__(things from the super class that we want to use)
        super().__init__(max_val, owner_name, current_amount)
        self.history = []

    def put_in(self, money):  
        if super().put_in(money): # inheritance
            self.history.append(f"Put in: {money} ฿")

    def take_out(self, money):  
        if super().take_out(money): # inheritance
            self.history.append(f"Take out: {money} ฿")

    def show_history(self):  
        for activities in self.history:
            print(activities)

folk = SmartEWallet(5000, "Folk", 1000)
folk.put_in("hi")
folk.put_in(500)
folk.put_in(6000)
folk.take_out(800)
folk.take_out(-500)
print(" ")
folk.current_balance()
folk.show_history()



# Q6 polymorphism
from abc import ABC, abstractmethod


class Phoneservice(ABC):
    def __init__(self, phone_no, customer_name, mm_yyyy):
        self.no = phone_no
        self.name = customer_name
        self.m_y = mm_yyyy

    @abstractmethod
    def find_cost(self):
        pass

class Pre_paid(Phoneservice):
    def __init__(self, phone_no, customer_name, mm_yyyy, call_duration, monthly_allowance, fixed_cost):
        super().__init__(phone_no, customer_name, mm_yyyy)
        self.cd = call_duration
        self.ma = monthly_allowance
        self.fc = fixed_cost

    def find_cost(self):
        if  self.cd > self.ma:
            return self.fc + (self.cd - self.ma)
        else:
            return self.fc

class Post_paid(Phoneservice):
    def __init__(self, phone_no, customer_name, mm_yyyy, call_duration):
        super().__init__(phone_no, customer_name, mm_yyyy)
        self.cd = call_duration

    def find_cost(self):
        return self.cd * 2

class Fixed_line(Phoneservice):
    def __init__(self, phone_no, customer_name, mm_yyyy, call_duration):
        super().__init__(phone_no, customer_name, mm_yyyy)
        self.local_calls = call_duration

    def find_cost(self):
        return self.local_calls * 3

print(Pre_paid("0926703260", "FOlk", "05/2020", 1250, 1000, 800).find_cost())
print(Post_paid("0926703260", "FOlk", "05/2020", 800).find_cost())
print(Fixed_line("0926703260", "FOlk", "05/2020", 300).find_cost())



# Q6 upgraded version (with describing polymorphism)
from abc import ABC, abstractmethod


class Phoneservice(ABC):
    def __init__(self, phone_no, customer_name, mm_yyyy, call_duration):
        self.no = phone_no
        self.name = customer_name
        self.m_y = mm_yyyy
        self.cd = call_duration # # definetion 1
        # polymorphism
        # call_duration in Pre-paid and Post-paid (Concrete class) means actual call durations
        # but in Fixed-line(class) call_duration does not means  actual call durations , it means local calls instead,
        # so this is called polymorphsm(same word, different meaning)

    @abstractmethod
    def find_cost(self): # find_cost has a different meaning in each class (poly)
        pass

class Pre_paid(Phoneservice):
    def __init__(self, phone_no, customer_name, mm_yyyy, call_duration, monthly_allowance, fixed_cost):
        super().__init__(phone_no, customer_name, mm_yyyy, call_duration)
        self.ma = monthly_allowance
        self.fc = fixed_cost

    def find_cost(self): # definetion 1
        if  self.cd > self.ma:
            return self.fc + (self.cd - self.ma)
        else:
            return self.fc

class Post_paid(Phoneservice):
    def __init__(self, phone_no, customer_name, mm_yyyy, call_duration):
        super().__init__(phone_no, customer_name, mm_yyyy, call_duration)

    def find_cost(self): # definetion 2
        return self.cd * 2

class Fixed_line(Phoneservice):
    def __init__(self, phone_no, customer_name, mm_yyyy, call_duration):
        super().__init__(phone_no, customer_name, mm_yyyy, call_duration)
        self.local_calls = call_duration # # definetion 2

    def find_cost(self): # definetion 3
        return self.local_calls * 3

print(Pre_paid("0926703260", "FOlk", "05/2020", 1250, 1000, 800).find_cost())
print(Post_paid("0926703260", "FOlk", "05/2020", 800).find_cost())
print(Fixed_line("0926703260", "FOlk", "05/2020", 300).find_cost())



# keep grade and score of each subject in Dict
subject_dict = dict({})
try:
    while True:
        print("Example format: Science:(3.00, A)")
        print("To exit enter -1")
        usin = input("Enter here: ").split(':')
        if usin == ['-1']:
            raise Exception(subject_dict)
        else:
            subject = usin[0]
            usin = usin[-1].replace('(', '')
            usin = usin.replace(')', '')
            credit, grade = usin.split(',') # ---> credit = 3.0, grade = 'A'
            credit = float(credit)
            subject_dict[subject] = (credit, grade) # {'subject': (credit, grade)}

except IndexError:
    print("Please enter -1 to exit")

except Exception as e:
    print(e)
