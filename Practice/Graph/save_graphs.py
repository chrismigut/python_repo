from pathlib import Path
import matplotlib.pyplot as plt

def create_graph(path):
    x_number = [1,2,3]
    y_number = [4,6,8]
    plt.plot(x_number, y_number)
    plt.savefig(path + '\\mygraph.png')

if __name__ == '__main__':
    savePath = str(Path.home()) + "\\Pictures"
    print (savePath)
    create_graph(savePath)

# recommended why to navigate around with paths: https://docs.python.org/3/library/pathlib.html
