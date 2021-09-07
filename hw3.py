import math
import time
#1
# Sources: https://www.studytonight.com/post/calculate-time-taken-by-a-program-to-execute-in-python
start = time.time()
for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print(f"Time it took to run:  {time.time() - start}")
print("")

#2
radius = 5
volume = (4/3) * math.pi * math.pow(radius,3)
print(f"The volume is: {volume}")
print("")

#3
import csv
dcsv = {'Title': ['1984', 'Animal Farm', 'Brave New World', 'Fahrenheit 451', 'Jane Erye', 'Wuthering Heights'], 'Author': [ 'George Orwell', 'George Orwell', 'Aldous Huxley', 'Ray Bradbury', 'Charlotte Bronte', 'Emily Bronte'], 'ISBN13' : ['987-0451524935°, 978-0451526342', '978-0060929879', '978-0345342966'], 'Pages' : ['268' , '144' , '288' , '208' ]}
csv_columns = {'Title' 'Author' 'ISBN13', 'Pages'}
rcsv = [ '1984', 'Animal Farm', 'Brave New World', 'Fahrenheit 451', 'Jane Erye', 'Wuthering Heights'], [' George Orwell', 'George Orwell', 'Aldous Huxley', 'Ray Bradbury', 'Charlotte Bronte', 'Emily Bronte'], ['987-0451524935', '978-0451526342', '978-0060929879', '978-0345342966'], ['268', '144' , '288', '208']
with open('books.csv', 'w', newline = '') as f:
    w = csv.writer(f);
    w.writerow(["Title", "Author", "ISBN13", "Pages"]);
    for key, items in dcsv.items():
        w.writerow([key,items])

#4
reader = csv.reader (open('data.csv'))
result = {}
for row in reader:
    key = row[0]
    if key in result:
        pass
    result[key] = row[1:]
    print(result)

#5