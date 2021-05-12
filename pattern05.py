import driver

def letter(row, col):
    if col - row > -1:
        return 'W'
    else:
        return 'T'

if __name__ == '__main__':
   driver.comparePatterns(letter)