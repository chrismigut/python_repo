from pylab import plot, show

x_number = [1,2,3]
y_number = [2,4,6]

def basic_graph():
    plot(x_number, y_number)
    show()

def marker_graph():
    plot(x_number, y_number, marker='o')
    show()

def marker_noline_graph():
    plot(x_number, y_number, 'o')
    show()

if __name__ == '__main__':
    op = int(input('''Select grapth type: \n 1) basic \n 2) marker \n 3) marker (no-line) \n: '''))

    if op == 1:
        basic_graph()
    
    if op == 2:
        marker_graph()
    
    if op == 3:
        marker_noline_graph()