''' Importing pythonProject class from Excel file'''
from excel import PythonProject
# creating the object of pythonProject
obj = PythonProject()

# PS Number to searched
PS = "40019032"

# Test case 1
def test_index1():
    ''' T1 '''
    # Requesting Marks
    data = obj.employee_marks(PS)

    #Checking
    assert obj.employee_marks(PS) == data

# Test case 2
def test_index2():
    ''' T2 '''
    # Requesting Hobbies
    data = obj.employee_hobbies(PS)

    # checking
    assert obj.employee_hobbies(PS) == data

# Test case 3
def test_index3():
    ''' T3 '''
    # Requesting Citis Travelled
    data = obj.employee_cities_travelled(PS)

    # Checking
    assert obj.employee_cities_travelled(PS) == data

# Test case 4
def test_index4():
    ''' T4'''
    # Requesting Programming Languages
    data = obj.employee_programming(PS)

    # checking
    assert obj.employee_programming(PS) == data

# Test case 5
def test_index5():
    ''' T5 '''
    # Requesting Domain
    data = obj.employee_domain(PS)

    # Checking
    assert obj.employee_domain(PS) == data

# Test case 6
def test_index6():
    ''' T6 '''
    # Requesting Marks
    marks = obj.employee_marks(PS)
    print(marks)

    # Requesting Hobbies
    hobbies = obj.employee_hobbies(PS)
    print(hobbies)

    # Requesting Cities
    cities = obj.employee_cities_travelled(PS)
    print(cities)

    # requesting Programming Languages
    programming = obj.employee_programming(PS)
    print(programming)

    # Requesting Domain
    domain = obj.employee_domain(PS)
    print(domain)

    # Passing all info to get new excel file
    assert obj.employee_new_excel(PS,marks,hobbies,cities,programming,domain) == 0
