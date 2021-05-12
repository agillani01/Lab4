import driver

def letter(row, col):
    if row>1 and row<5 and col>2 and col<7:
        return 'M'
    else:
        return 'S'

if __name__ == '__main__':
   driver.comparePatterns(letter)
