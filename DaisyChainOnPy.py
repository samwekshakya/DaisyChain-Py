import random

class DaisyChain(): 
    a = [0] * 5 
    pc1=pc2=pc3=pc4=pc5=0
    
    for x in range(20): 
        a[1]= random.random()
        a[0]= random.random()
        a[2]= random.random()
        a[3]= random.random()
        a[4]= random.random()  
          
        if a[0]>a[1] and a[0]>a[2] and a[0]>a[3] and a[0]>a[4]:
            pc1+=1
        elif a[1]>a[0] and a[1]>a[2] and a[1]>a[3] and a[1]>a[4]:
             pc2+=1
        elif a[2]>a[0] and a[2]>a[1] and a[2]>a[3] and a[2]>a[4]:
            pc3+=1    
        elif a[3]>a[0] and a[3]>a[1] and a[3]>a[2] and a[1]>a[4]:
            pc4+=1
        else:
            pc5+=1
        
    print("Device 1 interrupted: " +str(pc1)+  " times")
    print("Device 2 interrupted: " +str(pc2)+  " times")
    print("Device 3 interrupted: " +str(pc3)+  " times")
    print("Device 5 interrupted: " +str(pc5)+  " times")
    print("Device 4 interrupted: " +str(pc4)+  " times")
       
    print()
    
    if pc1>pc2 and pc1>pc3 and pc1>pc4 and pc1>pc5:
        print("Device 1 is prioritized")
    elif pc2>pc1 and pc2>pc3 and pc2>pc4 and pc2>pc5:
        print("Device 2 is prioritized")
    elif pc3>pc1 and pc3>pc2 and pc3>pc4 and pc3>pc5:
        print("Device 3 is prioritized")
    elif pc4>pc1 and pc4>pc3 and pc4>pc2 and pc4>pc5:
        print("Device 4 is prioritized")
    else: 
        print("Device 5 is prioritized")
       
        