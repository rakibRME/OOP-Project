'''x=int(input())
if(x%2==0): print("Even")
else: print("odd")'''


'''i=1;
x=int(input())
sum=1
for i in range (1,x):
    sum+=sum*i;
print(sum)'''


'''x = input()
print(x[::-1])'''


'''for i in range(2,101):
    for j in range(2, i+1):
        if i == j:
            print(i)
            break;
        if i % j == 0:
            break'''

'''a = int(input())
x = [10, 25, 38, 4, 58, 67, 74, 84, 94, 10]
count = 0
for i in range(len(x)):
    if x[i] == a:
        print("Found")
        print("Position ")
        print(i+1)
        count = count+1;
        break

if count == 0:
    print("Not found")
'''

'''string = input("Enter string: ")
if string.isdigit():
    print("NUMBER")
elif string.isalpha():
    print("WORD")
else:
    print("MIXED")'''


'''string = input("Enter string: ")
string = string.replace("too","excellent")
print(string)'''

'''s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
string=" "
for x in s1:
    if x in s2:
        string=string+x
for x in s2:
    if x in s1:
        string=string+x
print(string)'''

'''upper = 0
lower = 0
s1 = input("Enter string: ")
for x in s1:
    if x.isupper():
        upper += 1
    elif x.islower():
        lower += 1
if lower < upper:
    print(s1.upper())
else:
    print(s1.lower())'''


'''positions = 0
s1 = input("Enter string: ")

for x in range(len(s1)):
    if s1[x].isupper():
        positions =x;
        break;
for y in reversed(range(len(s1))):
    if s1[y].isupper():
        positions =y;
        break;
print(s1[x+1:y])'''

'''upper = 0
lower = 0
digit = 0
special = 0
s1 = input("Enter string: ")
for x in s1:
    if x.isupper():
        upper += 1
    elif x.islower():
        lower += 1
    elif x.isdigit():
        digit += 1
    else:
        special += 1
if upper<1:
    print("Upper case missing")
if lower<1:
    print("Lower case missing")
if digit<1:
    print("Digit missing")
if special<1:
    print("Special character missing")
if upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("OK")'''

'''user_data = {}
key = input("Enter name: ")
value = float(input("Enter CGPA: "))
user_data[key] = value
print("Do you want to Enter another record Press 'y' if yes: ")
print("Do you want to Enter another record Press 'n' if no: ")
ch = input()
while ch == 'y':
    key = input("Enter name: ")
    value = float(input("Enter CGPA: "))
    user_data[key] = value
    print("Do you want to Enter another record Press 'y' if yes: ")
    print("Do you want to Enter another record Press 'n' if no: ")
    ch = input()
    if ch == 'y':
        continue
    else:
        break
print(user_data)

'''
'''count = {}
while True:
    num = input("Enter number (or type 'SHESH' to stop): ")
    if num == "shesh":
        break
    else:
        num = int(num)
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

for num, n in count.items():
    print(f"{num}- {n} times")

'''


'''lst = []
while True:
    count = input("Number of values (or type 'STOP' to stop): ")
    if count == "STOP":
        break
    count = int(count)
    for i in range(count):
        num = input("Enter number: ")
        if num == "STOP":
            break
        else:
            lst.append(int(num))

    if count != 0:
        lst.sort()
        if lst[count - 1] - lst[0] < count:
            print("UB Jumper")
        else:
            print("Not UB Jumper")
    else:
        print("Count cannot be zero.")
'''

'''month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}


usr_input = input("Enter the Month: ")
print("a) Days in the {} is {}".format(usr_input, month_days[usr_input]))

keys_list = list(month_days.keys())
print(sorted(keys_list))

keys_list_31 = []
for k in month_days:
    if month_days[k] == 31:
        keys_list_31.append(k)
print(keys_list_31)

sorted_by_value = sorted(month_days.items(), key=lambda item: item[1])
print(sorted_by_value)
'''

'''def filter_even_numbers(dictionary):
    even_numbers_dict = {}

    for key, value in dictionary.items():
        even_values = [num for num in value if num % 2 == 0]
        even_numbers_dict[key] = even_values

    return even_numbers_dict

# Take user input for the sample input dictionaries
input_dict = {}
num_entries = int(input("Enter the number of entries in the dictionary: "))

for i in range(num_entries):
    key = input("Enter the key: ")
    values = list(map(int, input(f"Enter the values for '{key}' (comma-separated): ").split(',')))
    input_dict[key] = values

# Filter even numbers from the dictionary
output_dict = filter_even_numbers(input_dict)

# Print the filtered dictionary
print("Filter even numbers from given dictionary values:")
print("Sample Output:")
print(output_dict)
'''


'''def invert_dictionary(input_dict):
    inverted_dict = {}

    for key, value in input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)

    return inverted_dict


input_dict = {}
num_entries = int(input("Enter the number of entries in the dictionary: "))
for _ in range(num_entries):
    key = input("Enter a key: ")
    value = input("Enter its value: ")
    input_dict[key] = value

inverted_dict = invert_dictionary(input_dict)'''

'''def lcm(a, b):
  maxi = max(a, b)
  while True:
    if maxi % a == 0 and maxi % b == 0:
      return maxi
    maxi += 1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = lcm(num1, num2)
print("The GCD is ")
print(num1*num2/result)'''


'''def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y

print("Press 1 for Addition")
print("Press 2 Subtraction")
print("Press 3 Multiplication")
print("Press 4 Division")
x = int(input(""))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if x == 1:
    print(add(num1, num2))
elif x == 2:
    print(sub(num1, num2))
elif x == 3:
    print(mul(num1, num2))
elif x == 4:
    print(div(num1, num2))'''

'''def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fib(n - 1)
        series.append(series[-1] + series[-2])
        return series

x = int(input("Enter the number: "))
if x > 0:
    series = fib(x)
    print(series)'''

'''
def extra_char(str1, str2):
    extra_char =""

    for j in str2:

        if j not in str1:
            extra_char += j

    return extra_char
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(extra_char(str1,str2))
'''
'''
def diff(n):
    s1 = n
    s1 = ''.join(sorted(s1))
    s2 = s1[::-1]
    r = int(s2)-int(s1)
    return r

n = input("Enter a number: ")
print(diff(n))
'''
'''
class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Invalid amount or insufficient balance.")

    def bankFees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        print("Bank fees applied.")

    def display(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)
        print("\n")

account = BankAccount(11223344, "Sakib", 100000)
account.display()
account.deposit(10000)
account.display()
account.withdrawal(2000)
account.display()
account.bankFees()
account.display()

'''
'''
text = {
    '.':'1',
    ',':'11',
    '?':'111',
    '!':'1111',
    'A':'2',
    'B':'22',
    'C':'222',
    'D':'3',
    'E':'33',
    'F':'333',
    'G':'4',
    'H':'44',
    'I':'444',
    'J':'5',
    'K':'55',
    'L':'555',
    'M':'6',
    'N':'66',
    'O':'666',
    'P':'7',
    'Q':'77',
    'R':'777',
    'S':'7777',
    'T':'8',
    'U':'88',
    'V':'888',
    'W':'9',
    'X':'99',
    'Y':'999',
    'Z':'9999',
    ' ':'0'
}
def convert_to_text(st1):
    st1 = st1.upper()
    value = ""
    for c in st1:
        value = value + str(text[str(c)])
    return value
print(convert_to_text(input("Enter the text: ")))

'''
'''
class Restaurant:
    def __init__(self):
        self.menu_items = {"A": 100,"B": 200, "C": 300,"C":400, "D":500,"E":600}
        self.booked_tables = set()
        self.customer_orders = []

    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price

    def book_table(self, table_number):
        self.booked_tables.add(table_number)

    def customer_order(self, table_number, items):
        order = {"Table Number": table_number, "Items Ordered": items}
        self.customer_orders.append(order)

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: {price:.2f} TK")

    def print_table_reservations(self):
        print("Reserved Tables:")
        for table_number in self.booked_tables:
            print(f"Table {table_number}")

    def print_customer_orders(self):
        print("Customer orders:")
        for order in self.customer_orders:
            table_number = order["Table Number"]
            items_ordered = ", ".join(order["Items Ordered"])
            print(f"Table {table_number}: {items_ordered}")

restaurant = Restaurant()

restaurant.print_menu()
restaurant.add_item_to_menu(input("Add item "),int(input("Item price ")))
x = int(input("Add book_table number "))
restaurant.book_table(x)
restaurant.customer_order(x, [input("Item 1 "),input("Item 2 ")])
restaurant.print_table_reservations()
restaurant.print_customer_orders()
'''
























