file = open('example.txt','w')
file.write('Hello File Handling')
file.close()

file = open('example.txt','r')
print(file.read())
file.close()


with open('example.txt','a') as f:
    f.write('\nAppending new line')

with open('example.txt','r') as f:
    print(f.readlines())



try:
    num = int(input('Enter a number: '))
    print(10/num)
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError:
    print('Invalid input')
finally:
    print('Execution complete')
