from cli import *
from recipes import *


if __name__ == '__main__':
    menu()
    deliver(Margherita())
    print(Margherita('XL').__dict__())
    print(Margherita('XL').__str__())
