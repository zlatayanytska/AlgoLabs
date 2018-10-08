import math 

def algorithm(piles, H):
    piles = sorted(piles)
    k = 1
    count = 0
    boolean = True
    while boolean == True:
      for i in range(0, len(piles)):
        count += math.ceil(piles[i]/k)
      if count <= H:
        boolean = False
      else:
        k += 1
        count = 0
        boolean = True
      
    return k

if __name__ == '__main__':
    piles = [30,11,23,4,20]
    H = 6
    result = algorithm(piles, H)
    print(result)

