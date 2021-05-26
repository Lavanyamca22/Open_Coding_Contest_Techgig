def main(Virus,Bi):
      string = []
      for i in Bi:
            if(Virus.find(i) != -1):
                  Virus = Virus[Virus.find(i):len(Virus)]
                  string.append(Virus)
      if(len(string) == len(Bi)):
            return "POSITIVE"
      else:
            return "NEGATIVE"
        
V = input()
N = int(input())
B = [input() for i in range(0,N)]
for i in range(0,len(B)):
    result = main(V, B[i])
    print(result)
