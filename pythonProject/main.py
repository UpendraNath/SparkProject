# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def numSplits(str) -> int:
    leftCounter = 0
    rightCounter = len(str)
    res = 0
    for c in str:
        leftCounter[c] += 1
        rightCounter[c] -= 1
        if rightCounter[c] == 0:
           del rightCounter[c]
        if len(leftCounter) == len(rightCounter):
           res += 1
        return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(numSplits('PyCharm'))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
