def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
       
def get_user_input():
    user_input=input()
    mylist=user_input.split(",")

    for i in range(len(mylist)):
        mylist.append(float(mylist[0]))
        mylist.pop(0)
        
    print(mylist)
    return mylist 

def calc_average():
    print("calc_average")

def find_min_max():
    print("find_min_max")

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")
       
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__":
 main()

