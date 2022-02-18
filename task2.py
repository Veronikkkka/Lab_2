"""Lab 2 Task 2"""
import json

def contents(data):
    """
    Recursive functiom that
    verify type of data, ask user
    what data he want to access
    and return required data
    """
    if type(data) == dict:
        print("The contents in dictionary. Available keys:")
        print(list(data.keys()))
        key_ = input("Enter essential key: ")
        if key_ in data.keys():
            data = data[key_]
        else:
            print("There is no such key. Try again")
            contents(data)
    elif type(data) == list:
        print("List len -", len(data), "Indexes available in range 0,", len(data))
        index_ = int(input("Enter essential index: "))
        if index_ > -1 and index_ < len(data):
            data = data[index_]
        else:
            print("Given index is out of range. Try again")
            contents(data)
    else:
        print(data)
        return None
    contents(data)
    
def main():
    """
    Function take path of file
    and call helping function
    """
    path = input("Enter path to json file: ")
    file = open(path, "r", encoding="utf-8")
    data = json.load(file)    
    print("Data in json file in", str(type(data))[-7:-1])
    if type(data) == dict:
        print("Possible keys to view value", list(data.keys()))
        goal = input("Enter key:")
        if goal in data.keys():
            data = data[goal]
        else:
            return "There is no such key"
    else:
        print("Possible index of value in range (0,", str(len(data))+")")
        goal = input("Enter index:")
        if int(goal) < len(data) and int(goal)>-1:
            data = data[int(goal)]
        else:
            return "Given index is out of range"
    contents(data)
    
main()