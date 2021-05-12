import driver
def letter(row, col):
    if col - row == 0 or row + col == 6:
        return 'X'
    else:
        return 'O'

if __name__ == '__main__':
   driver.comparePatterns(letter)