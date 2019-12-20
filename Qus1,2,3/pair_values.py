MAVAL = 1000000000

def printClosest(arr, n, x): 

    res_l, res_r = 0, 0
    l, r, diff = 0, n-1, MAVAL 
    while r > l: 

        if abs(arr[l] + arr[r] - x) < diff: 
            res_l = l 
            res_r = r 
            diff = abs(arr[l] + arr[r] - x) 
      
        if arr[l] + arr[r] > x: 
            r -= 1
        else: 

            l += 1
          
    print('The closest pair ',arr[res_l], arr[res_r]) 


arr = [11, 25, 29, 30, 35, 50] 
n = len(arr) 
x=50
printClosest(arr, n, x) 

