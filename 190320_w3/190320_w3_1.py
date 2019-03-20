def pyramid(n): 
    layer = 0
    for i in range(1,n): 
        for j in range(i,n): 
            print(' ', end='') 
        while (layer != (2 * i - 1)): 
            if (layer == 0 or layer == 2 * i - 2): 
                print('*', end='') 
            else: 
                print(' ', end ='') 
            layer +=1
        layer = 0; 
        print ('') 
          
   
    for i in range(0,2*n-1):
        
        print ('*', end ='') 
   
n = int(input("Please enter how many levels: "))
pyramid(n)