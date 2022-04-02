for row in range(7):
    for col in range(4):
        if row == 0 and col in {1,2}:
          print('0',end = ' ')
        elif row in {1,2,4,5,6} and col in {0,3}:
            print('0',end = ' ')
        elif row == 3:
            print('0',end = ' ')
        else:
            print(' ',end = ' ')
    print() # this is meant for next line




for row in range(7):
    for col in range(5):
          if row in {0,6} and col in {1,2,3}:
              print('0',end = ' ')
          elif row in {1,4,5} and col in {0,4}:
              print('0',end =' ') 
          elif row == 2 and col == 0:
              print('0',end = ' ')
          elif row == 3 and col in {0,2,3,4}:
              print ('0', end = ' ')  
          else:
              print(' ', end = ' ')
    print() 